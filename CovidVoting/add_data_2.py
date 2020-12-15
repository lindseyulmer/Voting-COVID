"""This module creates a base data set that add_data() build on.
add_data(startdata,newdatafile,startdatastate, newdatastate, states,
newfilename)
The purpose of this module is to prepare data for visualization
"""
# Import Packages
import pandas as pd

def add_data_new(base_data, new_data, base_state_col, new_state_col,
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