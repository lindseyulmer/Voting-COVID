# Covid and Elections

## Software Components
The software components are importing data, structuring data to one dataframe and adding shapefile information for use with Geopandas, and creating and exporting the interactive map with Bokeh. Summarizing it is importing data, reformatting data, and creating and exporting map visualizations.

## Possible Components
#### `add_data_shapefile`
- description: prepare data to create figure
- input: Two data sets as csvs, the new one that's being added on and a datafile containing geopandas shape information
- output: one combined data set as a csv
#### `add_data_csv`
- description: prepare data to create figure
- input: Two data sets as csvs without geopandas shape information
- output: one combined data set as a csv
#### `make_plot_2020_and_2016`
- description: make plots with the preloaded data for all states
- input: datasets including the Covid counts, U.S. shape data, and election voting data
- output: plots with tabs on top
#### `make_plot_map`
- description: make a map to show the different years’ election results in the swing states
- input: datasets including the Covid counts, U.S. shape data, and election voting data
- output: interactive figures
#### `make_plot_scatter`
- description: make a scatter plot to show the relationship among COVID-19 positive cases, deaths and election results in the swing states
- input: datasets including the Covid counts, U.S. shape data, and election voting data
- output: interactive figures
#### `make_plot_bar`
- description: make a bar chart to compare the percentage of turnout by mail in 2016 and 2020 election
- input: datasets including the Covid counts, U.S. shape data, and election voting data
- output: interactive figures
#### `make_plot_time_series`
- description: make a time series chart to show the total cumulative cases for states where each party won in the election
- input: datasets including the Covid counts, U.S. shape data, and election voting data
- output: interactive figures

## Interactions To Accomplish Use Cases
The imported data with be combined by the reformatting component to one data frame, and that data frame will be used by the visualization creation component. General steps for this are:
- Reading in data (import component)
- Merging data to one data frame (reformat component)
- Using the Geopandas package to add state shapes to a data frame (reformat component)
- Using Bokeh to perform plotting/visualization (also to save the plot to file) (visualization component)
- Using Bokeh to make the interactive plot to better illustrate the data (visualization component)

## Preliminary Plan
- Gather COVID case data, 2020 election results and proportion mail-in voting, 2016 election results, and poll results
- Investigate necessary packages to visualize data in interactive maps.
- Create visualizations comparing COVID cases to 2020 results for all states.
- Create visualizations comparing 2016 election results to 2020 overall and early voting results for all States.
- Create visualizations comparing COVID cases, number of mail-in votes, and poll results on COVID as a top voting issue for key swing states.
