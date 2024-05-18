# JDAT 

Put the DB file (<lrsql.sqlite.db>) under <JDAT_results> folder
Put the SURVEY file (<users.csv>) under <JDAT_results> folder

Run the following command in terminal: 
<python main.py>

The results will be prepared under <JDAT_results> folder

A folder will be created with the date and time of the command execution.

<Timestamp>
    <ANALYSIS>
        <Assigned_Clusters.jpg> A table with colored clusters for each student
        <Student_Clusters.csv> A table with clusters for each student
        <Demographic_Analysis.jpg> The cluster plot of the analysis with demographic values
        <Interaction_Analysis.jpg> The cluster plot of the analysis with interaction values
        <Full_Analysis.jpg> The cluster plot of the analysis with both demographic and interaction values
        <OutputReport.txt> The exploratory analysis results
    <DATA>
        <DB>
            <db_cleaned.json> The JSON of the cleaned database data
            <db_users.json> The JSON of the list of users in the database
            <db.json> The JSON of the raw database data 
        <SURVEY>
            <survey.json> The JSON of the raw survey data
            <survey_cleaned.json> The JSON of the cleaned survey data
            <survey_cleaned_users.json> The JSON of the cleaned list of users in the surveys
            <survey_users.json> The JSON of the list of all users in the surveys
        <full_data_parsed.json> The JSON of the parsed and processed data



