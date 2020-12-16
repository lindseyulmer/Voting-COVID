"""
This module contains a series of test cases to confirm the validity
of the implementation of the make_plot_2020_and_2016.py module.
Tests include smoke tests and edge tests.
"""
import unittest
import geopandas as gpd
import pandas as pd
from CovidVoting.make_plot_2020_and_2016 import (make_plot)

contiguous_usa = gpd.read_file("data/shapefiles/cb_2018_us_state_20m.shp")
covid = pd.read_csv("data/raw_2_covid_latest.csv")
df_election = pd.read_csv("data/use_election.csv")
df_covid = covid.loc[covid["State/Territory"].
                     isin(contiguous_usa["NAME"])]
df_merge = pd.merge(left=df_covid, right=df_election,
                    left_on='State/Territory', right_on='state')


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
        plot = make_plot(df_merge, contiguous_usa)
        self.assertEqual(str(type(plot)),
                         "<class 'bokeh.models.layouts.Tabs'>")

    def test_edge(self):
        '''
        This is an edge test that proves our code catches a type error when
        the take in parameter is invalid.
        '''
        with self.assertRaises(TypeError):
            make_plot(1, contiguous_usa)


if __name__ == '__main__':
    unittest.main()
