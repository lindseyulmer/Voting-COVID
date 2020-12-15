# Covid and Elections

## Project Scope
- Our Goal: Visualize COVID-19 and election data in the same place so that people can more easily draw conclusions about how the pandemic affected American’s political views.
- Background: The coronavirus pandemic has created unprecedented circumstances in the United States, affecting every aspect of American life including the election process. Rising cases and concern over the government’s response to the pandemic could have greatly influenced how and who Americans voted for. Data on coronavirus cases, election results, and the proportion of mail-in votes are all readily available, but coronavirus and election data are not readily available in the same place for comparison.
- Tasks: 
    * Gather COVID case data, 2020 election results and proportion mail in voting, 2016 election results, and poll results on COVID as a top voting issue.
    * Investigate necessary packages to visualize data in interactive maps.
    * Create visualizations comparing COVID cases to 2020 results for all states.
    * Create visulizations comparing 2016 election results to 2020 overall and early voting results for all States.
    * Create visulizations comparing COVID cases, number of mail in votes, and poll results on COVID as a top voting issue for key swing states.

## Data Sources
- <a href= 'https://covid.cdc.gov/covid-data-tracker/#cases_casesper100klast7days'>COVID-19 Cases Data</a>: COVID-19 Cases Data will be downloaded from the CDC's website as a CSV file.
- <a href= 'http://healthyelections.org/map/'>2016 vote by mail data</a>: 2016 vote by mail data will be downloaded from healthy elections.org as a CSV file.
- <a href= 'https://www.fec.gov/documents/1890/federalelections2016.xlsx'>2016 overall election results</a>: 2016 overall election results will be downloaded from the FEC as an excel spreadsheet. 
- <a href= 'https://www.commonwealthfund.org/publications/2020/sep/election-2020-battleground-state-health-care-poll'>Poll data on covid as a voting issue</a>: Poll data on covid as a voting issue will be downloaded from commonwealthfund.
- <a href= 'https://www.nbcnews.com/politics/2020-elections/president-results'>2020 results</a>: 2020 results will be copied from nbcnews.com as a CSV.
- <a href= 'https://www.nytimes.com/interactive/2020/us/elections/early-voting-results.html'>2020 mail-in voting data</a>: 2020 mail-in voting data will be copied from the guardian into a CSV.<br/>
(Some of this data had to be copied into spreadsheets instead of downloaded as a table because the data was not available in a downloadable format at the time of this project because results were still being finalized.)

## User Profile
The user can be anyone who is interested in visualizing covid and election data. This can be anyone from people who work in public policy to just citizens who are interested in the election or covid data. They do not need experience any experience to interact with pre-generated figures but would need some familiarity with python and jupyter notebooks to add new data and create new figures. For example, a user can be a US citizen who is concerned about the COVID and election. She once used python before but doesn’t know how to make plots. Also a user can be a news reporter. He wants to help people got the right information. He may have some other state-level data. A users can just be a person who is interested in the Covid and Us voting. He can view our visualized results.

## Use Cases
### Use Case 1: Adding Additional Data to Our Base Data
If the user had additional data they wanted in an interactive map, they could upload more data, and alter what columns in the combined data frame are plotted to include their newly added data. Users doing this should have some experience with python.
### Use Case 2: Creating Maps for All States
Users will run a python file as is to generate the desired interactive map figure for all states.
### Use Case 3: Creating Figures for Only Swing States
If a user was only interested in the data of swing states. He can use our functions to generate the desired interactive plots for the swing states.
### Use Case 4: Viewing preloaded plots
If a user is interested in our visualized results, he can view our example plots, and does not need any coding experience.
