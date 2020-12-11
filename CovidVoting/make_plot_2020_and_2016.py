"""
In this module, the function make_plot uses the package Bokeh to help creating
interactive plots to show voting and Covid data. 
"""
import pandas as pd
from bokeh.models import ColorBar, GeoJSONDataSource, HoverTool, LinearColorMapper
from bokeh.models.widgets import Panel, Tabs
from bokeh.plotting import figure

def make_plot(covid, contiguous_usa, df_election):
    '''
    This function makes maps to show 2020 or 2016 election results
    and Covid data together. Users can choose to see which year's election
    result they want to see by clicking on the tabs provided.
    
    Args:
    - covid: (csv) Covid data in a csv file
    - contiguous_usa: (shp) to make a map
    - df_election: (csv) election results data of 2020 and 2016 in a csv file
    
    Returns:
    - plots: contains two plots and tabs on top
    '''
    # Keep states which are in the shapefile contiguous_usa
    df_covid = covid.loc[covid["State/Territory"].isin(contiguous_usa["NAME"])]
    df_merge = pd.merge(left=df_covid, right=df_election, left_on='State/Territory', right_on='state')
    # Merge shapefile with covid data
    map_info = contiguous_usa.merge(df_merge, left_on = "NAME", right_on = "State/Territory")
    # Drop Alaska and Hawaii
    map_info = map_info.loc[~map_info['NAME'].isin(['Alaska', 'Hawaii'])]
    # Input GeoJSON source that contains features for plotting
    geosource = GeoJSONDataSource(geojson = map_info.to_json())
    base_colors = ["#cb181d", "#fb6a4a", "#fcae91", "#fee5d9", "#eff3ff", "#bdd7e7", "#6baed6", "#2171b5"]
    # Instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
    color_mapper_2020 = LinearColorMapper(palette = base_colors,
                                     low = df_election["color_2020"].min(),
                                     high = df_election["color_2020"].max())
    color_mapper_2016 = LinearColorMapper(palette = base_colors,
                                 low = df_election["color_2016"].min(),
                                 high = df_election["color_2016"].max())
    tick_labels_2020 = {'-8': 'Trump wins', '-6': '', '-4': '', '-2': '',
                        '2': '', '4': '', '6': '', '8': 'Biden wins'}
    tick_labels_2016 = {'-8': 'Trump wins', '-6': '', '-4': '',
                        '-2': '', '2': '', '4': '', '6': '', '8': 'Clinton wins'}
    
    # Create color bar.
    color_bar_2020 = ColorBar(color_mapper = color_mapper_2020, 
                         label_standoff = 10,
                         width = 500, height = 20,
                         border_line_color = None,
                         location = (0,0), 
                         orientation = 'horizontal',
                         major_label_overrides = tick_labels_2020)
    color_bar_2016 = ColorBar(color_mapper = color_mapper_2016, 
                         label_standoff = 10,
                         width = 500, height = 20,
                         border_line_color = None,
                         location = (0,0), 
                         orientation = 'horizontal',
                         major_label_overrides = tick_labels_2016)

    # Create figure object
    p2020 = figure(title = 'COVID-19 cases & 2020 election', 
                   plot_height = 600 ,
                   plot_width = 950, 
                   toolbar_location = 'below',
                   tools = "pan, wheel_zoom, box_zoom, reset")
    p2020.xgrid.grid_line_color = None
    p2020.ygrid.grid_line_color = None
    p2016 = figure(title = 'COVID-19 cases & 2016 election', 
                   plot_height = 600 ,
                   plot_width = 950, 
                   toolbar_location = 'below',
                   tools = "pan, wheel_zoom, box_zoom, reset")
    p2016.xgrid.grid_line_color = None
    p2016.ygrid.grid_line_color = None

    # Add patch renderer to figure
    states_2020 = p2020.patches('xs','ys', source = geosource,
                           fill_color = {'field' :'color_2020',
                                         'transform' : color_mapper_2020},
                           line_color = "gray", 
                           line_width = 0.25, 
                           fill_alpha = 1)
    states_2016 = p2016.patches('xs','ys', source = geosource,
                           fill_color = {'field' :'color_2016',
                                         'transform' : color_mapper_2016},
                           line_color = "gray", 
                           line_width = 0.25, 
                           fill_alpha = 1)
    # Create hover tool
    p2020.add_tools(HoverTool(renderers = [states_2020],
                          tooltips = [('State', '@NAME'),
                                      ('Case Rate per 100000', '@{Case Rate per 100000}'),
                                      ('Confirmed cases', '@{Total Cases}'),
                                      ('Total deaths', '@{Total Deaths}')]))
    p2016.add_tools(HoverTool(renderers = [states_2016],
                          tooltips = [('State', '@NAME'),
                                      ('Case Rate per 100000', '@{Case Rate per 100000}'),
                                      ('Confirmed cases', '@{Total Cases}'),
                                      ('Total deaths', '@{Total Deaths}')]))
    # Specify layout
    p2020.add_layout(color_bar_2020, 'below')
    p2016.add_layout(color_bar_2016, 'below')
    panel_2020 = Panel(child=p2020, title='COVID-19 cases & 2020 election')
    panel_2016 = Panel(child=p2016, title='COVID-19 cases & 2016 election')
    plots = Tabs(tabs=[panel_2020, panel_2016])
    return plots



