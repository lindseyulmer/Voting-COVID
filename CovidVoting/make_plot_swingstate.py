'''
module_text
'''

# Importing libraries
import pandas as pd
import numpy as np
import geopandas as gpd
import json
from bokeh.io import output_notebook, show, reset_output
from bokeh.models import (CDSView, ColorBar, ColumnDataSource,
                          CustomJS, CustomJSFilter, Div,
                          GeoJSONDataSource, HoverTool,
                          LinearColorMapper, Slider,
                          LogColorMapper, Legend, Title)
from bokeh.layouts import column, row, widgetbox
from bokeh.palettes import brewer
from bokeh.plotting import figure
from bokeh.transform import dodge, factor_cmap
from bokeh.plotting import figure
from bokeh.embed import file_html
from bokeh.models import Div, Paragraph, Row, Column
from bokeh.resources import CDN
from bokeh.util.browser import view
from jinja2 import Template

# define swing states
swing_states = ["Arizona", "Colorado", "Florida", "Georgia", "Iowa", "Michigan",
                "Minnesota", "Nevada", "New Hampshire", "North Carolina", "Ohio",
                "Pennsylvania", "Texas", "Wisconsin"]


def make_plot_map(source_df, shapefile, field, range_col, hover_list, title):
    '''
    function: make a map to show the swing states

    source_df: (df)the data to show in the map
    shapefile: (shp)to make a map
    field: (df's col -> int) the variable used to fill colors
    range_col: (df's col -> int) the variable used to map numbers in a range, into a sequence of colors (the condition of results)
    hover_list: (list) 
    title: (string)the title of the map
    '''

    # Merge shapefile with covid data
    map_info = shapefile.merge(source_df, left_on = "NAME", right_on = "state")
    # Drop Alaska and Hawaii
    map_info = map_info.loc[~map_info['NAME'].isin(['Alaska', 'Hawaii'])]
    # Input GeoJSON source that contains features for plotting
    geosource = GeoJSONDataSource(geojson = map_info.to_json())

    base_colors = ["#cb181d","#fb6a4a","#fcae91","#fee5d9","#eff3ff","#bdd7e7","#6baed6","#2171b5"]
    # Instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
    color_mapper = LinearColorMapper(palette = base_colors,
                                     low = source_df[range_col].min(),
                                     high = source_df[range_col].max())

    # Define custom tick labels for color bar.
    tick_labels = {'-8': 'Trump wins',
                   '-6':'',
                   '-4':'',
                   '-2':'', 
                   '2':'',
                   '4':'',
                   '6':'',
                   '8':'Biden wins'}

    # Create color bar.
    color_bar = ColorBar(color_mapper = color_mapper, 
                         label_standoff = 5,
                         width = 200, height = 10,
                         border_line_color = None,
                         location = (0,0), 
                         orientation = 'horizontal',
                         major_label_overrides = tick_labels
                        )

    # Create figure object
    p = figure(title = title, 
                      plot_height = 400,
                      plot_width = 600,
                      toolbar_location=None
                      #toolbar_location = 'below',
                      #tools = "pan, wheel_zoom, box_zoom, reset"
                      )
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    # Add patch renderer to figure
    states = p.patches('xs','ys', source = geosource,
                               fill_color = {'field' :field,
                                             'transform' : color_mapper},
                               line_color = "gray", 
                               line_width = 0.25, 
                               fill_alpha = 1)
    # Create hover tool
    p.add_tools(HoverTool(renderers = [states], tooltips = hover_list))

    # Specify layout
    p.add_layout(color_bar, 'below')
    #p.title.text_color = "#7D3C98"
    p.title.text_font_size = "15px"
    #p.border_fill_color = "whitesmoke"
    p.background_fill_color = "beige"
    sub_text = Title(text="", align='left', text_font_size='12px', text_color = "#A6ACAF")
    p.add_layout(sub_text, 'below')
    
    return p


def make_plot_scatter(source_df, category_list, color_col, color_palette,
                      x_col, y_col, hover_list, x_label, y_label, title, subtitle):
    """
    function: make a scatter plot to show the relationship among COVID-19 positive cases,
              deaths and election results in the swing states
              
    source_df: (dataframe)
    category_list: (list)
    color_col, x_col, y_col:
    color_palette
    hover_list:
    x_label, y_label:
    title
    subtitle
    """
    p = figure(plot_height = 400, toolbar_location=None)
    p.scatter(x=x_col, y=y_col,
              source=source_df,
              color=factor_cmap(color_col, palette = color_palette, factors = category_list),
              size=10, legend=color_col)

    p.title.text = title
    p.xaxis.axis_label = x_label
    p.yaxis.axis_label = y_label

    hover = HoverTool()
    hover.tooltips = hover_list
    p.background_fill_color = "beige"
    
    p.add_tools(hover)
    p.legend.location = "top_left"
    #p.border_fill_color = "whitesmoke"
    p.title.text_font_size = "15px"
    
    sub_text = Title(text=subtitle, align='left', text_font_size='12px', text_color = "#A6ACAF")
    p.add_layout(sub_text, 'above')
    sub_text = Title(text="", align='left', text_font_size='12px', text_color = "#A6ACAF")
    p.add_layout(sub_text, 'below')

    return p


def make_plot_bar(source_df, x_axis_list, title, y1, y2, y1_label, y2_label, hover_list):
    '''
    function: make a bar chart to compare the percentage of turnout by mail in 2016 and 2020 election

    source_df: (df)
    x_axis_list: (list)
    y1, y2: (string)
    y1_label, y2_label: (string)
    hover_list: (list) 
    title: (string)the title of the bar chart

    '''

    # change dataframe to ColumnDataSource for Bokeh
    source = ColumnDataSource(data=source_df)

    p = figure(x_range=x_axis_list, y_range=(0, 1), plot_height=400, plot_width=1200, title=title,
               toolbar_location=None, tools="hover", tooltips=hover_list)

    p.vbar(x=dodge("state", -0.15, range=p.x_range), top=y1, width=0.2, source=source,
           color="#CAAD8D", legend_label=y1_label, name='win_2016')

    p.vbar(x=dodge("state",  0.15,  range=p.x_range), top=y2, width=0.2, source=source,
           color="#F4D03F", legend_label=y2_label, name='win_2020')

    hover = HoverTool()
    hover.tooltips = hover_list
    p.add_tools(hover)

    #p.x_range.range_padding = 0.2
    p.xgrid.grid_line_color = None
    p.legend.location = "top_right"
    p.legend.orientation = "horizontal"

    #p.border_fill_color = "whitesmoke"
    p.title.text_font_size = "15px"
    p.background_fill_color = "beige"
    sub_text = Title(text="", align='left', text_font_size='12px', text_color = "#A6ACAF")
    p.add_layout(sub_text, 'below')
    return p


def make_plot_time_series(source_df, group_col, use_col, y_label, title, hover_list):
    '''
    function: make a time series chart to show the total cumulative cases for states where 
              each party won in the election

    source_df: (df)
    group_col: (string) group by date and what 
    use_col: (string) the variables to show in the plot
    y_label: (string)
    title: (string)the title of the bar chart
    hover_list: (list)
    '''

    # make groups
    grouped = source_df.groupby(['date', group_col])[use_col].sum().reset_index()
    grouped[use_col] = grouped[use_col]/1000
    r_group = grouped[grouped[group_col]=="Republican"]
    d_group = grouped[grouped[group_col]=="Democratic"]

    # Create a ColumnDataSource object for each group
    r_cds = ColumnDataSource(r_group)
    d_cds = ColumnDataSource(d_group)


    # Create and configure the figure
    p = figure(x_axis_type='datetime',
                 plot_height=400, plot_width=600,
                 title=title,
                 x_axis_label='Date', y_axis_label=y_label,
                 toolbar_location=None)

    # Render the race as step lines
    p.line('date', use_col, line_width=3,
             color="#5DADE2", legend_label='Democratic', 
             source=d_cds)
    p.line('date', use_col, line_width=3,
             color="#EC7063", legend_label='Republican', 
             source=r_cds)


    hover = HoverTool(tooltips=hover_list,
                      formatters={'@date': 'datetime'})

    p.add_tools(hover)

    # Move the legend to the upper left corner

    p.legend.location = 'top_left'
    #p.border_fill_color = "whitesmoke"
    p.title.text_font_size = "15px"
    p.background_fill_color = "beige"
    # Show the plot
    return p