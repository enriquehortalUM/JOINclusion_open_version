from csv import DictReader,DictWriter
from json import loads, dumps
import datetime
import sqlite3
from pandas import read_sql_query #type: ignore
import numpy as np #type: ignore

def get_timestamp():
    now = datetime.datetime.now()
    
    year    = '{:02d}'.format(now.year)
    month   = '{:02d}'.format(now.month)
    day     = '{:02d}'.format(now.day)
    hour    = '{:02d}'.format(now.hour)
    minute  = '{:02d}'.format(now.minute)
    second  = '{:02d}'.format(now.second)
    
    timestamp = '{}_{}_{}_{}_{}_{}'.format(year, month, day, hour, minute, second)
    return timestamp
timestamp = get_timestamp()
#timestamp = str(111)

def write_to_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as jsonf:
        jsonString = dumps(data, indent=4)
        jsonf.write(jsonString)

def csv_to_json(filename, savename):
    data = []
    with open(filename, encoding='utf-8-sig', newline='') as csvf:
        csvReader = DictReader(csvf)
        for row in csvReader:
            data.append(row)
    write_to_json(savename, data)

def read_json_data(filename):
    f = open(filename, "r")
    data = loads(f.read())
    f.close()
    return data

def read_survey(filename,PRINT_EXAMPLE_DATA=0):
    filename = 'JDAT_results/users.csv'
    raw_filename = 'JDAT_results/'+timestamp+'/DATA/SURVEY/survey.json'

    csv_to_json(filename, raw_filename)
    survey_data = read_json_data(raw_filename)
        
    survey_users = []
    for row in survey_data:
        if row["Nickname"] not in survey_users:
            survey_users.append(row["Nickname"])

    user_filename = 'JDAT_results/'+timestamp+'/DATA/SURVEY/survey_users_.json'
    write_to_json(user_filename, survey_users)

    if PRINT_EXAMPLE_DATA:
        print("Survey data example:")
        print("-------------------------------------------")
        print(survey_data[0])
        print("-------------------------------------------")
    return survey_data,survey_users  

def get_statement_count(user,data):
    count = 0
    for row in data:
        if row["actor"]["name"] == user:
            count = count+1
    return count

def get_statement_count_and_last_statement(user,data):
    count = 0
    for row in data:
        if row["actor"]["name"] == user:
            count = count+1
            statement = row["verb"]["id"]
    if count != 1:
        statement = ''
    return count, statement

def get_launch_count(user,data):
    count = 0
    for row in data:
        if row["actor"]["name"] == user and row["verb"]["id"] == 'https://w3id.org/xapi/tla#launched2':
            count = count+1
    return count

def clean_user_list(data, users):
    nolaunch = []
    nolaunchremoved = []
    cleaned_users = []
    for user in users:
        launch_count = get_launch_count(user,data)
        if launch_count == 0:
            nolaunch.append(user)
        else:
            nolaunchremoved.append(user)
    nodata = []
    for user in nolaunchremoved:
        statement_count = get_statement_count(user,data)
        if statement_count < 4:
            nodata.append(user)
        else:
            cleaned_users.append(user)
    return cleaned_users, nodata, nolaunch

def read_db(filename,PRINT_EXAMPLE_DATA=0):
    filename = 'JDAT_results/lrsql.sqlite.db'
    #raw_filename = 'JDAT_results/'+timestamp+'/DATA/DB/raw_data.npy'

    cnx = sqlite3.connect(filename)
    df = read_sql_query("SELECT * FROM xapi_statement", cnx)
    cnx.commit()
    cnx.close()

    payload = df['payload'].to_numpy()

    db_data = []
    for row in payload:
        db_data.append(loads(row.decode('UTF-8')))
    #np.savez_compressed(raw_filename, db_data)

    db_users = []
    for row in db_data:
        if row["actor"]["name"] not in db_users:
            #db_users.append(((row["actor"]["name"].strip()).lower()).upper())
            db_users.append(row["actor"]["name"])

    user_filename = 'JDAT_results/'+timestamp+'/DATA/DB/db_users.json'
    data_filename = 'JDAT_results/'+timestamp+'/DATA/DB/db.json'
    write_to_json(user_filename, db_users)
    write_to_json(data_filename, db_data)

    if PRINT_EXAMPLE_DATA:
        print("DB data example:")
        print("-------------------------------------------")
        print(db_data[0])
        print("-------------------------------------------")
    return db_data,db_users   

def clean_data(db_data, sv_data, users):
    #raw_filename = 'JDAT_results/'+timestamp+'/DATA/DB/db_cleaned.npy'
    cleaned1st = []
    cleaned2nd = []
    for row in db_data:
        if "context" in row and "extensions" in row["context"] and "https://joinclusion.fse.maastrichtuniversity.nl/session" in row["context"]["extensions"]:
            if row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/student"] in users:
                cleaned1st.append(row)
    cleaned_users, nodata, nolaunch = clean_user_list(cleaned1st, users)
    for row in cleaned1st:
        if "context" in row and "extensions" in row["context"] and "https://joinclusion.fse.maastrichtuniversity.nl/session" in row["context"]["extensions"]:
            if row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/student"] in cleaned_users:
                cleaned2nd.append(row)
    #np.savez_compressed(raw_filename, cleaned2nd)
    
    cleaned_sv_data = []
    for row in sv_data:
        if row["Nickname"] in cleaned_users:
            cleaned_sv_data.append(row)
    
    cleaned_users.sort()
    
    db_data_filename = 'JDAT_results/'+timestamp+'/DATA/DB/db_cleaned.json'
    user_filename = 'JDAT_results/'+timestamp+'/DATA/SURVEY/survey_cleaned_users.json'
    sv_data_filename = 'JDAT_results/'+timestamp+'/DATA/SURVEY/survey_cleaned.json'
    write_to_json(db_data_filename, cleaned2nd)
    write_to_json(user_filename, cleaned_users)
    write_to_json(sv_data_filename, cleaned_sv_data)

    return cleaned2nd, cleaned_sv_data, cleaned_users, nodata, nolaunch

def write_to_csv(filename, data):
    fields = list(data[0].keys())
    with open(filename, 'w', newline='') as csvfile:
        writer = DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for row in data:
            writer.writerow(row)