'''
# Importing libraries
import os
import pandas as pd
import numpy as np
import geopandas as gpd
from bokeh.embed import file_html
from bokeh.models import Row, Column
from bokeh.resources import CDN
from bokeh.util.browser import view
from jinja2 import Template
from add_data import (add_data)
from make_plot_2020_and_2016 import (make_plot)
from make_plot_swingstate import (make_plot_map, make_plot_scatter,
                                  make_plot_bar, make_plot_time_series)
current_location = os.getcwd()
os.chdir(current_location)

# define swing states
# Define all states
allstates = ["Maryland", "Iowa", "Delaware", "Ohio",
             "Pennsylvania", "Nebraska", "Washington",
             "Alabama", "Arkansas", "New Mexico", "Texas",
             "California", "Kentucky", "Georgia", "Wisconsin",
             "Oregon", "Missouri", "Virginia", "Tennessee",
             "Louisiana", "New York", "Michigan", "Idaho",
             "Florida", "Illinois", "Montana", "Minnesota",
             "Indiana", "Massachusetts", "Kansas", "Nevada", "Vermont",
             "Connecticut", "New Jersey", "District of Columbia",
             "North Carolina", "Utah", "North Dakota", "South Carolina",
             "Mississippi", "Colorado", "South Dakota", "Oklahoma", "Wyoming",
             "West Virginia", "Maine", "New Hampshire", "Arizona",
             "Rhode Island"]
# Define key states
key = ["Arizona", "Florida", "Georgia", "Michigan",
       "Minnesota", "North Carolina", "Ohio",
       "Pennsylvania", "Texas", "Wisconsin"]

swing_states = ["Arizona", "Colorado", "Florida",
                "Georgia", "Iowa", "Michigan",
                "Minnesota", "Nevada", "New Hampshire",
                "North Carolina", "Ohio",
                "Pennsylvania", "Texas", "Wisconsin"]
# print(current_location)
# Read files
contiguous_usa = gpd.read_file("data/shapefiles/cb_2018_us_state_20m.shp")

df_covid = pd.read_csv("data/raw_2_covid_latest.csv")
df_covid_daily = pd.read_csv("data/raw_1_covid_daily.csv")
df_election = pd.read_csv("data/use_election.csv")
df_state = pd.read_csv("data/raw_0_states.csv")

# Keep states which are in the shapefile contiguous_usa
df_covid = df_covid.loc[df_covid[
                                 "State/Territory"].isin(contiguous_usa["NAME"])]
df_election = df_election.loc[df_election[
                                          "state"].isin(contiguous_usa["NAME"])]

# process election and covid data
df_covid_election = pd.merge(left=df_covid, right=df_election, how='right',
                             left_on='State/Territory', right_on='state')
df_covid_election["swing_state_2020"]= np.where(df_covid_election[
                                                "state"].isin(swing_states),
                                                df_covid_election[
                                                'color_2020'], np.nan)
df_covid_election["swing_state_2016"]= np.where(df_covid_election[
                                                "state"].isin(swing_states),
                                                df_covid_election['color_2016'],
                                                np.nan)
# process daily covid data
df_covid_daily = pd.merge(left=df_covid_daily, right=df_state[["state_code",
           "state"]], left_on='state_code', right_on='state_code')
df_covid_daily['date'] = pd.to_datetime(df_covid_daily['date'],
                                        format='%m/%d/%Y')

# data for swing states
df_covid_daily_swing = df_covid_daily[
                                      df_covid_daily["state"].isin(swing_states)]
df_covid_daily_swing = pd.merge(left=df_covid_daily_swing,
                                right=df_election[["state",
                                "win_2016", "win_2020"]],
                                left_on='state', right_on='state')
print(df_covid_daily_swing.head())
"""
# use add_data to create covid_election.csv
add_data('data/basedata.csv', "data/use_election.csv", 'NAME',
         "state", allstates, "data/covid_election.csv")
# use add_data to create covid_daily_swing.csv
add_data('data/basedata.csv', "data/raw_1_covid_daily.csv", "NAME",
         "state_code", key, "data/covid_daily_swing.csv")
# read add_data results as a csv
df_covid_election = pd.read_csv("data/covid_election.csv")
df_covid_daily_swing = pd.read_csv("data/covid_daily_swing.csv")
"""
# all states plot for 2016 and 2020 election
plot_0 = make_plot(df_covid_election, contiguous_usa)

# map 1
hover_list = [('State', '@NAME')]
plot_1 = make_plot_map(df_covid_election, contiguous_usa,
                       'swing_state_2020', 'color_2020', hover_list,
                       '2020 Election Result of Swing States')
# map 2
hover_list = [('State', '@NAME')]
plot_2 = make_plot_map(df_covid_election, contiguous_usa,
                       'swing_state_2016', 'color_2016', hover_list,
                       '2016 Election Result of Swing States')
                       
# scatter plot 1
category_list = ['Democratic', 'Republican']
source_df = df_covid_election[df_covid_election['state'].isin(key)]
x_col = 'Total Cases'
y_col = 'Total Deaths'
hover_list = [('State', '@state'),
              ('Total Cases', '@{Total Cases}'),
              ('Total Deaths', '@{Total Deaths}')]
color_col = 'win_2020'
color_palette = ["#5DADE2", "#EC7063"]
title = 'Total cases and total deaths in swing states'
subtitle = "colors from 2020 election results"
x_label = 'the number of total cases'
y_label = 'the number of total deaths'
plot_3 = make_plot_scatter(source_df, category_list, color_col, color_palette,
                           x_col, y_col, hover_list,
                           x_label, y_label, title, subtitle)
# scatter plot 2
category_list = ['Democratic', 'Republican']
source_df = df_covid_election[df_covid_election['state'].isin(key)]
x_col = 'Total Cases'
y_col = 'Total Deaths'
hover_list = [('State', '@state'),
              ('Total Cases', '@{Total Cases}'),
              ('Total Deaths', '@{Total Deaths}')]
color_col = 'win_2016'
color_palette = ["#5DADE2", "#EC7063"]
title = 'Total cases and total deaths in swing states'
subtitle = "colors from 2016 election results"
x_label = 'the number of total cases'
y_label = 'the number of total deaths'
plot_4 = make_plot_scatter(source_df, category_list, color_col, color_palette,
                           x_col, y_col, hover_list,
                           x_label, y_label, title, subtitle)
# bar chart 1
source_df = df_covid_election[["state", "percent_turnout_mail_2016",
                               "percent_turnout_mail_2020", "Total Cases",
                               "Total Deaths", 'win_2020',
                               'win_2016']][df_covid_election
                                            ["swing_state_2020"].notnull()]
x_axis_list = key
title = "the percentage of turnout by mail in 2016 and 2020 election"
y1 = "percent_turnout_mail_2016"
y2 = "percent_turnout_mail_2020"
y1_label = "2016"
y2_label = "2020"
hover_list = [("win", "@$name"),
              ('Total Cases', '@{Total Cases}'),
              ('Total Deaths', '@{Total Deaths}')]
plot_5 = make_plot_bar(source_df, x_axis_list, title,
                       y1, y2, y1_label, y2_label, hover_list)
# daily 1
source_df = df_covid_daily_swing
group_col = 'win_2020'
use_col = 'tot_cases'
y_label = 'total cases (thousands)'
title = 'total cumulative cases for states where each party won in 2020'
hover_list = [('Date', '@date{%F}'),
              ('Total Cases (thousands)', '@{tot_cases}{int}')]
plot_6 = make_plot_time_series(source_df, group_col, use_col,
                               y_label, title, hover_list)
# daily 2
source_df = df_covid_daily_swing
group_col = 'win_2016'
use_col = 'tot_cases'
y_label = 'total cases (thousands)'
title = 'total cumulative cases for states where each party won in 2016'
hover_list = [('Date', '@date{%F}'),
              ('Total Cases (thousands)', '@{tot_cases}{int}')]
plot_7 = make_plot_time_series(source_df, group_col, use_col, y_label,
                               title, hover_list)
# show in the html file
template = Template(
    """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>{{ title if title else "Bokeh Plot" }}</title>
            {{ bokeh_css | safe }}
            {{ bokeh_js | safe }}
        </head>
        <body>
            {{ plot_div | safe }}
            {{ plot_script | safe }}
        </body>
    </html>
    """)
html = file_html(Column(Row(plot_1, plot_2),
                        Row(plot_3, plot_4),
                        Row(plot_5),
                        Row(plot_6, plot_7)),
                 template=template, resources=CDN)
output_file = './example/plot_swingstate.html'
with open(output_file, 'w') as f:
    f.write(html)
view(output_file)

html2 = file_html(plot_0, CDN, "plot all states")
output_file2 = './example/plot_all_states.html'
with open(output_file2, 'w') as f:
    f.write(html2)
view(output_file2)
'''