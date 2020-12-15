'''
In this module, the below functions use the package Bokeh, and geopandas to help users create
interactive plots to provide more information of voting and COVID in the swing states.
make_plot_map(source_df, shapefile, field, range_col, hover_list, title)
make_plot_scatter(source_df, category_list, color_col, color_palette,
                      x_col, y_col, hover_list,
                      x_label, y_label, title, subtitle)
make_plot_bar(source_df, x_axis_list, title, y_1,
                  y_2, y1_label, y2_label, hover_list)
make_plot_time_series(source_df, group_col, use_col,
                          y_label, title, hover_list)
'''

# Importing libraries
from bokeh.models import (ColorBar, ColumnDataSource,
                          GeoJSONDataSource, HoverTool,
                          LinearColorMapper,
                          Title)
from bokeh.plotting import figure
from bokeh.transform import dodge, factor_cmap

# define swing states
swing_states = ["Arizona", "Florida", "Georgia", "Michigan",
                "Minnesota", "North Carolina", "Ohio",
                "Pennsylvania", "Texas", "Wisconsin"]


def make_plot_map(source_df, shapefile, field, range_col, hover_list, title):
    '''
    This function provide a map to show the election results in swing states.

    Args:
    - source_df: (pandas.dataframe) the data used to make a plot
    - shapefile: (shp) shape data of the U.S. to make a map
    - field: (a column of source_df contains integers) the variable used to fill colors
    - range_col: (a column of source_df contains integers) the variable used to map numbers
                 in a range into a sequence of colors (the condition of results)
    - hover_list: (list) a list of tuples shown in the hover
    - title: (string) the title of the plot

    Returns:
    - plots: one bokeh plot
    '''

    # Merge shapefile with covid data
    map_info = shapefile.merge(source_df, left_on="NAME", right_on="state")
    # Drop Alaska and Hawaii
    map_info = map_info.loc[~map_info['NAME'].isin(['Alaska', 'Hawaii'])]
    # Input GeoJSON source that contains features for plotting
    geosource = GeoJSONDataSource(geojson=map_info.to_json())

    base_colors = ["#cb181d", "#fb6a4a", "#fcae91", "#fee5d9",
                   "#eff3ff", "#bdd7e7", "#6baed6", "#2171b5"]

    color_mapper = LinearColorMapper(palette=base_colors,
                                     low=source_df[range_col].min(),
                                     high=source_df[range_col].max())

    # Define custom tick labels for color bar.
    tick_labels = {'-8': 'Trump wins',
                   '-6': '',
                   '-4': '',
                   '-2': '',
                   '2': '',
                   '4': '',
                   '6': '',
                   '8': 'Biden wins'}

    # Create color bar.
    color_bar = ColorBar(color_mapper=color_mapper,
                         label_standoff=5,
                         width=200, height=10,
                         border_line_color=None,
                         location=(0, 0),
                         orientation='horizontal',
                         major_label_overrides=tick_labels)

    # Create figure object
    plot = figure(title=title,
               plot_height=400,
               plot_width=600,
               toolbar_location=None)
    plot.xgrid.grid_line_color = None
    plot.ygrid.grid_line_color = None

    # Add patch renderer to figure
    states = plot.patches('xs', 'ys', source=geosource,
                          fill_color={'field': field,
                                      'transform': color_mapper},
                          line_color="gray",
                          line_width=0.25,
                          fill_alpha=1)
    # Create hover tool
    plot.add_tools(HoverTool(renderers=[states], tooltips=hover_list))

    # Specify layout
    plot.add_layout(color_bar, 'below')
    # plot.title.text_color = "#7D3C98"
    plot.title.text_font_size = "15px"
    # plot.border_fill_color = "whitesmoke"
    plot.background_fill_color = "beige"
    sub_text = Title(text="", align='left',
                     text_font_size='12px', text_color="#A6ACAF")
    plot.add_layout(sub_text, 'below')

    return plot


def make_plot_scatter(source_df, category_list, color_col, color_palette,
                      x_col, y_col, hover_list,
                      x_label, y_label, title, subtitle):
    """
    This function provide a scatter plot to show the relationship
    among COVID-19 positive cases,
    deaths and election results in the swing states

    Args:
    - source_df: (pandas.dataframe) the data used to make a plot
    - category_list: (list)
    - color_col, x_col, y_col: (string) names of columns used for color,
                               x axis and y axis
    - color_palette: (list) a list of color codes
    - hover_list: (list) a list of tuples shown in the hover
    - x_label, y_label: (string) names of x axis and y axis
    - title: (string) the title of the plot
    - subtitle: (string) the subtitle of the plot

    Returns:
    - plots: one bokeh plot
    """

    plot = figure(plot_height=400, toolbar_location=None)
    plot.scatter(x=x_col, y=y_col,
              source=source_df,
              color=factor_cmap(color_col,
                                palette=color_palette, factors=category_list),
              size=10, legend=color_col)

    plot.title.text = title
    plot.xaxis.axis_label = x_label
    plot.yaxis.axis_label = y_label

    hover = HoverTool()
    hover.tooltips = hover_list
    plot.background_fill_color = "beige"

    plot.add_tools(hover)
    plot.legend.location = "top_left"
    # plot.border_fill_color = "whitesmoke"
    plot.title.text_font_size = "15px"

    sub_text = Title(text=subtitle, align='left',
                     text_font_size='12px', text_color="#A6ACAF")
    plot.add_layout(sub_text, 'above')
    sub_text = Title(text="", align='left',
                     text_font_size='12px', text_color="#A6ACAF")
    plot.add_layout(sub_text, 'below')

    return plot

def make_plot_bar(source_df, x_axis_list, title, y_1,
                  y_2, y1_label, y2_label, hover_list):
    '''
    This function provide a bar chart to compare the
    percentage of turnout by mail in 2016 and 2020 election

    Args:
    - source_df: (pandas.dataframe) the data used to make a plot
    - x_axis_list: (list)
    - title: (string) the title of the plot
    - y_1, y_2: (string) names of columns used for comparison
    - hover_list: (list) a list of tuples shown in the hover
    - y1_label, y2_label: (string) names of 2 variables

    Returns:
    - plots: one bokeh plot
    '''

    # change dataframe to ColumnDataSource for Bokeh
    source = ColumnDataSource(data=source_df)

    plot = figure(x_range=x_axis_list, y_range=(0, 1),
               plot_height=400, plot_width=1200, title=title,
               toolbar_location=None, tools="hover", tooltips=hover_list)

    plot.vbar(x=dodge("state", -0.15, range=plot.x_range),
           top=y_1, width=0.2, source=source,
           color="#CAAD8D", legend_label=y1_label, name='win_2016')

    plot.vbar(x=dodge("state",  0.15,  range=plot.x_range),
           top=y_2, width=0.2, source=source,
           color="#F4D03F", legend_label=y2_label, name='win_2020')

    hover = HoverTool()
    hover.tooltips = hover_list
    plot.add_tools(hover)

    # plot.x_range.range_padding = 0.2
    plot.xgrid.grid_line_color = None
    plot.legend.location = "top_right"
    plot.legend.orientation = "horizontal"

    # plot.border_fill_color = "whitesmoke"
    plot.title.text_font_size = "15px"
    plot.background_fill_color = "beige"
    sub_text = Title(text="", align='left',
                     text_font_size='12px', text_color="#A6ACAF")
    plot.add_layout(sub_text, 'below')
    return plot


def make_plot_time_series(source_df, group_col, use_col,
                          y_label, title, hover_list):
    '''
    This function provide a time series chart to show the total
    cumulative cases for states where each party won in the election.

    Args:
    - source_df: (pandas.dataframe) the data used to make a plot
    - group_col: (string) choose the variable to use groupby function
    - use_col: (string) names of a column used in the plot
    - y_label: (string) names of a variable
    - title: (string) the title of the plot
    - hover_list: (list) a list of tuples shown in the hover

    Returns:
    - plots: one bokeh plot
    '''

    # make groups
    grouped = source_df.groupby(['date',
                                 group_col])[use_col].sum().reset_index()
    grouped[use_col] = grouped[use_col]/1000
    r_group = grouped[grouped[group_col] == "Republican"]
    d_group = grouped[grouped[group_col] == "Democratic"]

    # Create a ColumnDataSource object for each group
    r_cds = ColumnDataSource(r_group)
    d_cds = ColumnDataSource(d_group)
    # Create and configure the figure
    plot = figure(x_axis_type='datetime',
                  plot_height=400, plot_width=600,
                  title=title,
                  x_axis_label='Date', y_axis_label=y_label,
                  toolbar_location=None)

    # Render the race as step lines
    plot.line('date', use_col, line_width=3,
              color="#5DADE2", legend_label='Democratic',
              source=d_cds)
    plot.line('date', use_col, line_width=3,
              color="#EC7063", legend_label='Republican',
              source=r_cds)
    hover = HoverTool(tooltips=hover_list,
                      formatters={'@date': 'datetime'})

    plot.add_tools(hover)

    # Move the legend to the upper left corner

    plot.legend.location = 'top_left'
    # plot.border_fill_color = "whitesmoke"
    plot.title.text_font_size = "15px"
    plot.background_fill_color = "beige"
    # Show the plot
    return plot
