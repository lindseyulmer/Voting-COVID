"""This module creates a base data set that add_data() build on.
add_data(startdata,newdatafile,startdatastate, newdatastate, states,
newfilename)
The purpose of this module is to prepare data for visualization
"""
# Import Packages
import pandas as pd
import geopandas as gpd
# Read the coviddata from a csv into a dataframe
coviddata = pd.read_csv('data/raw_2_covid_latest.csv',
                        index_col=0)
# Read in shapefile and examine data
contiguous_usa = gpd.read_file('data/shapefiles/cb_2018_us_state_20m.shp')
# Merge shapefile with population data
case_states = contiguous_usa.merge(coviddata, left_on='NAME',
                                   right_on='State/Territory')
# Drop Alaska and Hawaii
case_states = case_states.loc[~case_states['NAME'].isin(['Alaska', "Hawaii",
                                                         "Puerto Rico"])]
case_states.to_csv('basedata.csv')
case_states.head()
# Define allstates
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


def add_data(start_data, new_data_file, start_data_state, new_data_state,
             states, new_file_name):
    """
    Args:
        start_data (str):filename with path of starting dataframe that
        includes geopandas
        shape information, recommended use basedata.csv from github repo
        new_data_file (str): filename with path to csv of new data to be added
        start_data_state(str): name of state column of starting data
        new_data_state(str): name of state column of new data
        column (str): column from new data file to be added,
        only add one at a time,
        rerun function to add more than one colummn
        states(list): list of strings of the desired states
        new_file_name(str):name of new data file generated
    Returns:
        newfilename: the dataframe with the newly added data as a csv"""
    # Read the dataframe to add too
    basedata = pd.read_csv(start_data, index_col=0)
    # Read data being added as a dataframe
    newdf = pd.read_csv(new_data_file)
    # Find all non-desired states
    dropstates = []
    for eachstate in basedata[start_data_state]:
        if eachstate not in states:
            dropstates.append(eachstate)
    for eachstate in newdf[new_data_state]:
        if eachstate not in states:
            dropstates.append(eachstate)
    # Drop nondesired states
    basedata = basedata.loc[~basedata[start_data_state].isin(dropstates)]
    newdf = newdf.loc[~newdf[new_data_state].isin(dropstates)]
    # Merge datasets
    mergeddata = basedata.merge(newdf, left_on=start_data_state,
                                right_on=new_data_state)
    # write out file
    mergeddata.to_csv(new_file_name)
