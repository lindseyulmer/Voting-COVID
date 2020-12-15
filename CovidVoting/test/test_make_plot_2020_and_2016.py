"""
This module contains a series of test cases to confirm the validity
of the implementation of the make_plot_2020_and_2016.py module.
Tests include smoke tests and edge tests.
"""
import os
import unittest
import geopandas as gpd
import pandas as pd
from CovidVoting.add_data import (add_data)
from CovidVoting.make_plot_2020_and_2016 import (make_plot)

current_location = os.getcwd()
os.chdir(current_location)
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
# use add_data to create covid_election.csv
add_data('data/basedata.csv', "data/use_election.csv", 'NAME',
         "state", allstates, "data/covid_election.csv")
covid = pd.read_csv("data/covid_election.csv")
contiguous_usa = gpd.read_file("data/shapefiles/cb_2018_us_state_20m.shp")


class UnitTests(unittest.TestCase):
    """
    This is a class that inherits from unittest.TestCase, in which each
    method executes a test to catch potential errors.
    """
    def test_smoke(self):
        """
        This is a smoke test that proves our code works. With the given
        inputs, make_plot function should return a plot with tabs.
        """
        p = make_plot(covid, contiguous_usa)
        self.assertEqual(str(type(p)), "<class 'bokeh.models.layouts.Tabs'>")

    def test_edge(self):
        '''
        This is an edge test that proves our code catches a type error when
        the take in parameter is invalid.
        '''
        with self.assertRaises(TypeError):
            make_plot(1, contiguous_usa)

    if __name__ == '__main__':
        unittest.main()
