"""This module creates a base data set that add_data() build on.
add_data_csv(base_data, new_data, base_state_col, new_state_col,
use_state, how_join)
add_data_shapefile(start_data, new_data_file, start_data_state, new_data_state,
states, new_file_name)
The purpose of this module is to prepare data for visualization
"""
# Import Packages
import pandas as pd
import geopandas as gpd
# Read the coviddata from a csv into a dataframe
covid_data = pd.read_csv('data/raw_2_covid_latest.csv',
                         index_col=0)
# Read in shapefile and examine data
contiguous_usa = gpd.read_file('data/shapefiles/cb_2018_us_state_20m.shp')
# Merge shapefile with population data
case_states = contiguous_usa.merge(covid_data, left_on='NAME',
                                   right_on='State/Territory')
# Drop Alaska and Hawaii
case_states = case_states.loc[~case_states['NAME'].isin(['Alaska', "Hawaii",
                                                         "Puerto Rico"])]
case_states.to_csv('basedata.csv')
case_states.head()
# Define allstates
all_states = ["Maryland", "Iowa", "Delaware", "Ohio",
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


def add_data_csv(base_data, new_data, base_state_col, new_state_col,
                 use_state, how_join):
    """
    Args:
        base_data (str):filename with path of starting dataframe that
        new_data (str): filename with path to csv of new data to be added
        base_state_col(str): name of state column of base data
        new_state_col(str): name of state column of new data
        use_state (list): list of strings of the desired states
        how_join (string): (‘left’, ‘right’, ‘outer’, ‘inner’)

    Returns:
        merged_df: the dataframe with the newly added data
    """
    # Read the dataframe to add too
    base_df = pd.read_csv(base_data)
    # Read data being added as a dataframe
    new_df = pd.read_csv(new_data)

    # Drop nondesired states
    base_df = base_df.loc[base_df[base_state_col].isin(use_state)]
    new_df = new_df.loc[new_df[new_state_col].isin(use_state)]

    # Merge datasets
    merged_df = pd.merge(left=base_df, right=new_df, how=how_join,
                         left_on=[base_state_col], right_on=[new_state_col])
    return merged_df
 

def add_data_shapefile(start_data, new_data_file,
                       start_data_state, new_data_state,
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
    base_data = pd.read_csv(start_data, index_col=0)
    # Read data being added as a dataframe
    new_df = pd.read_csv(new_data_file)
    # Find all non-desired states
    drop_states = []
    for each_state in base_data[start_data_state]:
        if each_state not in states:
            drop_states.append(each_state)
    for each_state in new_df[new_data_state]:
        if each_state not in states:
            drop_states.append(each_state)
    # Drop nondesired states
    base_data = base_data.loc[~base_data[start_data_state].isin(drop_states)]
    new_df = new_df.loc[~new_df[new_data_state].isin(drop_states)]
    # Merge datasets
    merged_data = base_data.merge(new_df, left_on=start_data_state,
                                  right_on=new_data_state)
    # write out file
    merged_data.to_csv(new_file_name)
