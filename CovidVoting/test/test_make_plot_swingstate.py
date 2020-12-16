"""
This module contains a series of test cases to confirm the validity
of the implementation of the make_plot_swingstate.py module.
"""
# Importing libraries
import unittest
import sys
import pandas as pd
import numpy as np
import geopandas as gpd
from CovidVoting.make_plot_swingstate import (make_plot_map,
                                              make_plot_scatter,
                                              make_plot_bar,
                                              make_plot_time_series)
sys.path.append("..")

# define swing states
swing_states = ["Arizona", "Colorado", "Florida",
                "Georgia", "Iowa", "Michigan",
                "Minnesota", "Nevada", "New Hampshire",
                "North Carolina", "Ohio",
                "Pennsylvania", "Texas", "Wisconsin"]

# Read files
contiguous_usa = gpd.read_file("./data/shapefiles/cb_2018_us_state_20m.shp")
df_covid = pd.read_csv("./data/raw_2_covid_latest.csv")
df_covid_daily = pd.read_csv("./data/raw_1_covid_daily.csv")
df_election = pd.read_csv("./data/use_election.csv")
df_state = pd.read_csv("./data/raw_0_states.csv")

# Keep states which are in the shapefile contiguous_usa
df_covid = df_covid.loc[df_covid[
  "State/Territory"].isin(contiguous_usa["NAME"])]
df_election = df_election.loc[
  df_election["state"].isin(contiguous_usa["NAME"])]

# process election and covid data
df_covid_election = pd.merge(left=df_covid, right=df_election, how='right',
                             left_on='State/Territory', right_on='state')
df_covid_election["swing_state_2020"] = np.where(
  df_covid_election["state"].isin(swing_states),
  df_covid_election['color_2020'], np.nan)
df_covid_election["swing_state_2016"] = np.where(
  df_covid_election["state"].isin(swing_states),
  df_covid_election['color_2016'],
  np.nan)
# process daily covid data
df_covid_daily = pd.merge(left=df_covid_daily,
                          right=df_state[["state_code", "state"]],
                          left_on='state_code', right_on='state_code')
df_covid_daily['date'] = pd.to_datetime(df_covid_daily['date'],
                                        format='%m/%d/%Y')

# data for swing states
df_covid_daily_swing = df_covid_daily[
  df_covid_daily["state"].isin(swing_states)]
df_covid_daily_swing = pd.merge(left=df_covid_daily_swing,
                                right=df_election[["state",
                                                   "win_2016", "win_2020"]],
                                left_on='state', right_on='state')


class UnitTestsMakePlotSwing(unittest.TestCase):
    """the class is for unit test of the making plot module"""
    def test_make_map(self):
        """
        This is a test that proves our code works. With the given
        inputs, make_plot_map function should return a bokeh plot.
        """
        hover_list = [('State', '@NAME')]
        plot = make_plot_map(df_covid_election,
                             contiguous_usa, 'swing_state_2020',
                             'color_2020', hover_list,
                             '2020 Election Result of Swing States')
        self.assertEqual(str(type(plot)),
                         "<class 'bokeh.plotting.figure.Figure'>")

    def test_make_scatter(self):
        """
        This is a test that proves our code works. With the given
        inputs, make_plot_scatter function should return a bokeh plot.
        """
        category_list = ['Democratic', 'Republican']
        source_df = df_covid_election[
          df_covid_election['state'].isin(swing_states)]
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
        plot = make_plot_scatter(source_df, category_list,
                                 color_col, color_palette,
                                 x_col, y_col, hover_list, x_label,
                                 y_label, title, subtitle)
        self.assertEqual(str(type(plot)),
                         "<class 'bokeh.plotting.figure.Figure'>")

    def test_make_bar(self):
        """
        This is a test that proves our code works. With the given
        inputs, make_plot_bar function should return a bokeh plot.
        """
        source_df = df_covid_election[["state", "percent_turnout_mail_2016",
                                       "percent_turnout_mail_2020",
                                       "Total Cases",
                                       "Total Deaths", 'win_2020', 'win_2016']]
        x_axis_list = swing_states
        title = "the percentage of turnout by mail in 2016 and 2020 election"
        y_1 = "percent_turnout_mail_2016"
        y_2 = "percent_turnout_mail_2020"
        y1_label = "2016"
        y2_label = "2020"
        hover_list = [("win", "@$name"),
                      ('Total Cases', '@{Total Cases}'),
                      ('Total Deaths', '@{Total Deaths}')]
        plot = make_plot_bar(source_df, x_axis_list,
                             title, y_1, y_2, y1_label, y2_label, hover_list)
        self.assertEqual(str(type(plot)),
                         "<class 'bokeh.plotting.figure.Figure'>")

    def test_make_line(self):
        """
        This is a test that proves our code works. With the given
        inputs, make_plot_time_series function should return a bokeh plot.
        """
        source_df = df_covid_daily_swing
        group_col = 'win_2020'
        use_col = 'tot_cases'
        y_label = 'total cases (thousands)'
        title = 'total cumulative cases for states each party won in 2020'
        hover_list = [('Date', '@date{%F}'),
                      ('Total Cases (thousands)', '@{tot_cases}{int}')]
        plot = make_plot_time_series(source_df, group_col,
                                     use_col, y_label, title, hover_list)
        self.assertEqual(str(type(plot)),
                         "<class 'bokeh.plotting.figure.Figure'>")

    def test_edge(self):
        '''
        This is an edge test that proves our code catches a type error when
        the take in parameter is invalid.
        '''
        source_df = df_covid_daily_swing
        group_col = 'win_2020'
        use_col = 'tot_cases'
        y_label = ['total cases (thousands)']
        title = 'total cumulative cases for states each party won in 2020'
        hover_list = [('Date', '@date{%F}'),
                      ('Total Cases (thousands)', '@{tot_cases}{int}')]
        with self.assertRaises(Exception):
            make_plot_time_series(
                source_df, group_col,
                use_col, y_label, title, hover_list)


if __name__ == '__main__':
    unittest.main()
