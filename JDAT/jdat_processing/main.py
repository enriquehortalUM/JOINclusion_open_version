from os.path import exists
from os import mkdir
import warnings
warnings.filterwarnings("ignore")
from numpy import intersect1d,setdiff1d #type: ignore
from fn_reader import read_json_data,read_survey,read_db,clean_data
from fn_reader import timestamp
from fn_parser import parse_data
from fn_process import get_analysis_vector_set
from fn_analyzer import get_descriptive_statistics, print_descriptives
from fn_analyzer import determine_number_of_clusters, perform_clustering, plot_clusters
from fn_analyzer import export_student_clusters

def run():
    if not exists('JDAT_results/'+timestamp):
        mkdir('JDAT_results/'+timestamp)
        mkdir('JDAT_results/'+timestamp+'/DATA')
        mkdir('JDAT_results/'+timestamp+'/DATA/SURVEY')
        mkdir('JDAT_results/'+timestamp+'/DATA/DB')
        mkdir('JDAT_results/'+timestamp+'/ANALYSIS') 

    with open('JDAT_results/'+timestamp+'/ANALYSIS/OutputReport.txt', 'w') as f:
        print("-------------------------------------------",file=f)
    f.close()

    #survey_data, survey_users = read_survey('test')
    if exists('JDAT_results/'+timestamp+'/DATA/SURVEY/survey.json') and exists('JDAT_results/'+timestamp+'/DATA/SURVEY/survey_users.json'):
        survey_data = read_json_data('JDAT_results/'+timestamp+'/DATA/SURVEY/survey.json')
        survey_users = read_json_data('JDAT_results/'+timestamp+'/DATA/SURVEY/survey_users.json')
    else:
        survey_data, survey_users = read_survey('test')

    #db_data, db_users = read_db('test')
    if exists('JDAT_results/'+timestamp+'/DATA/DB/db.json') and exists('JDAT_results/'+timestamp+'/DATA/DB/db_users.json'):
        db_data = read_json_data('JDAT_results/'+timestamp+'/DATA/DB/db.json')
        db_users = read_json_data('JDAT_results/'+timestamp+'/DATA/DB/db_users.json')
    else:
        db_data, db_users = read_db('test')

    #cleaned_db_data, cleaned_survey_users, nodata, nolaunch = clean_data(db_data,survey_users)
    if exists('JDAT_results/'+timestamp+'/DATA/DB/db_cleaned.json')and exists('JDAT_results/'+timestamp+'/DATA/SURVEY/survey_cleaned_users.json'):
        cleaned_db_data = read_json_data('JDAT_results/'+timestamp+'/DATA/DB/db_cleaned.json')
        cleaned_survey_users = read_json_data('JDAT_results/'+timestamp+'/DATA/SURVEY/survey_cleaned_users.json')
        cleaned_survey_data = read_json_data('JDAT_results/'+timestamp+'/DATA/SURVEY/survey_cleaned.json')
        nolaunch = []
        nodata = []
    else:
        cleaned_db_data, cleaned_survey_data, cleaned_survey_users, nodata, nolaunch = clean_data(db_data,survey_data,survey_users)

    PRINT_STATISTICS = True
    if PRINT_STATISTICS:
        with open('JDAT_results/'+timestamp+'/ANALYSIS/OutputReport.txt', 'a') as f:
            print("Number of users:",file=f)
            print("-------------------------------------------",file=f)
            print("       Surveys : " + str(len(survey_users)),file=f)
            print("      Database : " + str(len(db_users)),file=f)
            print("    Both lists : " + str(len(intersect1d(db_users, survey_users))),file=f)
            print(" Launched only : " + str(len(nolaunch)),file=f)
            print("Did not launch : " + str(len(nodata)),file=f)
            print("-------------------------------------------",file=f)
            print("Users who are in the survey but not in DB: ",file=f)
            print("-------------------------------------------",file=f)
            print(str(setdiff1d(survey_users, db_users)),file=f)
            #print("-------------------------------------------")
            #print("Users who are in the DB but not in survey:")
            #print("-------------------------------------------")
            #print(setdiff1d(db_users, survey_users))
            print("-------------------------------------------",file=f)
            print("Users who only launched the game:",file=f)
            print("-------------------------------------------",file=f)
            print(nodata,file=f)
            print("-------------------------------------------",file=f)
            print("Users who didn't launch the game:",file=f)
            print("-------------------------------------------",file=f)
            print(nolaunch,file=f)
            print("-------------------------------------------",file=f)
            print("Number of rows in DB:",file=f)
            print("-------------------------------------------",file=f)
            print("Before cleaning: " + str(len(db_data)),file=f)
            print("After  cleaning: " + str(len(cleaned_db_data)),file=f)
            print("-------------------------------------------",file=f)
            print("Number of users in the survey:",file=f)
            print("-------------------------------------------",file=f)
            print("Before cleaning: " + str(len(survey_users)),file=f)
            print("After  cleaning: " + str(len(cleaned_survey_users)),file=f)
            print("-------------------------------------------",file=f)
        f.close()

    #full_user_data = fp.parse_data(cleaned_db_data,cleaned_survey_data,cleaned_survey_users)
    if exists('JDAT_results/'+timestamp+'/DATA/full_data_parsed.json'):
        full_user_data = read_json_data('JDAT_results/'+timestamp+'/DATA/full_data_parsed.json')
    else:
        full_user_data = parse_data(cleaned_db_data,cleaned_survey_data,cleaned_survey_users)

    DESCRIPTIVES = True
    if DESCRIPTIVES:
        descriptives = get_descriptive_statistics(full_user_data)
        print_descriptives(descriptives)

    CLUSTERING = True
    if CLUSTERING:
        demo_anlz_data, intr_anlz_data, full_anlz_data, analz_user = get_analysis_vector_set(full_user_data)
        demo_cluster = determine_number_of_clusters(demo_anlz_data)
        intr_cluster = determine_number_of_clusters(intr_anlz_data)
        full_cluster = determine_number_of_clusters(full_anlz_data)

        demo_labels = perform_clustering(demo_anlz_data,demo_cluster)
        plot_clusters(demo_anlz_data,demo_labels,"Demographic_Analysis")
        intr_labels = perform_clustering(intr_anlz_data,intr_cluster)
        plot_clusters(intr_anlz_data,intr_labels,"Interaction_Analysis")
        full_labels = perform_clustering(full_anlz_data,full_cluster)
        plot_clusters(full_anlz_data,full_labels,"Full_Analysis")

        export_student_clusters(analz_user, demo_labels, intr_labels, full_labels)

if __name__ == "__main__":
    run()