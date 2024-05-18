from fn_process import special_round, get_total_values
from fn_reader import write_to_csv,timestamp

from numpy import array #type: ignore
from sklearn.cluster import KMeans #type: ignore
from sklearn.metrics import silhouette_score #type: ignore 
import matplotlib.pyplot as plt #type: ignore
from sklearn.manifold import TSNE #type: ignore
from matplotlib.table import Table #type: ignore

def get_descriptive_statistics(data):

    d = {"S1Played_Migrant"      :0, "S2Played_Migrant"      :0, "S1Played_Local"      :0, "S2Played_Local"      :0,
         "S1Interaction_Migrant" :0, "S2Interaction_Migrant" :0, "S1Interaction_Local" :0, "S2Interaction_Local" :0,
         "S1Help_Migrant"        :0, "S2Help_Migrant"        :0, "S1Help_Local"        :0, "S2Help_Local"        :0,
         "S1Score_Migrant"       :0, "S2Score_Migrant"       :0, "S1Score_Local"       :0, "S2Score_Local"       :0
    } 

    for row in data:    
        total_values = get_total_values(row)
        if total_values["Scenario1Question"]>0:
            if total_values["MigrantBackground"] == "No migratory background":
                d["S1Played_Local"]      += 1
                d["S1Interaction_Local"] += total_values["Scenario1Interaction"]
                d["S1Help_Local"]        += total_values["Scenario1Help"]
                d["S1Score_Local"]       += total_values["Scenario1Score"]
            else:
                d["S1Played_Migrant"]      += 1
                d["S1Interaction_Migrant"] += total_values["Scenario1Interaction"]
                d["S1Help_Migrant"]        += total_values["Scenario1Help"]
                d["S1Score_Migrant"]       += total_values["Scenario1Score"]
        if total_values["Scenario2Question"]>0:
            if total_values["MigrantBackground"] == "No migratory background":
                d["S2Played_Local"]      += 1
                d["S2Interaction_Local"] += total_values["Scenario2Interaction"]
                d["S2Help_Local"]        += total_values["Scenario2Help"]
                d["S2Score_Local"]       += total_values["Scenario2Score"]
            else:
                d["S2Played_Migrant"]      += 1
                d["S2Interaction_Migrant"] += total_values["Scenario2Interaction"]
                d["S2Help_Migrant"]        += total_values["Scenario2Help"]
                d["S2Score_Migrant"]       += total_values["Scenario2Score"]
    
    avg = {}
    avg["S1Played_Local"]        = d["S1Played_Local"]
    avg["S1Interaction_Local"]   = d["S1Interaction_Local"]/ d["S1Played_Local"] if d["S1Played_Local"] != 0 else 0
    avg["S1Help_Local"]          = d["S1Help_Migrant"]     / d["S1Played_Local"] if d["S1Played_Local"] != 0 else 0
    avg["S1Score_Local"]         = d["S1Score_Local"]      / d["S1Played_Local"] if d["S1Played_Local"] != 0 else 0
    avg["S1Played_Migrant"]      = d["S1Played_Migrant"]
    avg["S1Interaction_Migrant"] = d["S1Interaction_Migrant"]/ d["S1Played_Migrant"] if d["S1Played_Migrant"] != 0 else 0
    avg["S1Help_Migrant"]        = d["S1Help_Migrant"]       / d["S1Played_Migrant"] if d["S1Played_Migrant"] != 0 else 0
    avg["S1Score_Migrant"]       = d["S1Score_Migrant"]      / d["S1Played_Migrant"] if d["S1Played_Migrant"] != 0 else 0
    avg["S2Played_Local"]        = d["S2Played_Local"]
    avg["S2Interaction_Local"]   = d["S2Interaction_Local"]/ d["S2Played_Local"] if d["S2Played_Local"] != 0 else 0
    avg["S2Help_Local"]          = d["S2Help_Local"]       / d["S2Played_Local"] if d["S2Played_Local"] != 0 else 0
    avg["S2Score_Local"]         = d["S2Score_Local"]      / d["S2Played_Local"] if d["S2Played_Local"] != 0 else 0
    avg["S2Played_Migrant"]      = d["S2Played_Migrant"]
    avg["S2Interaction_Migrant"] = d["S1Interaction_Migrant"]/ d["S2Played_Migrant"] if d["S2Played_Migrant"] != 0 else 0
    avg["S2Help_Migrant"]        = d["S2Help_Migrant"]       / d["S2Played_Migrant"] if d["S2Played_Migrant"] != 0 else 0
    avg["S2Score_Migrant"]       = d["S2Score_Migrant"]      / d["S2Played_Migrant"] if d["S2Played_Migrant"] != 0 else 0


    playS1 = d["S1Played_Local"]      + d["S1Played_Migrant"]
    inteS1 = d["S1Interaction_Local"] + d["S1Interaction_Migrant"]
    helpS1 = d["S1Help_Local"]        + d["S1Help_Migrant"]
    scorS1 = d["S1Score_Local"]       + d["S1Score_Migrant"]
    playS2 = d["S2Played_Local"]      + d["S2Played_Migrant"]
    inteS2 = d["S2Interaction_Local"] + d["S2Interaction_Migrant"]
    helpS2 = d["S2Help_Local"]        + d["S2Help_Migrant"]
    scorS2 = d["S2Score_Local"]       + d["S2Score_Migrant"]

    play = playS1 + playS2
    inte = inteS1 + inteS2
    help = helpS1 + helpS2
    scor = scorS1 + scorS2

    avg["S1Played"]      = playS1
    avg["S1Interaction"] = inteS1/playS1 if playS1 != 0 else 0
    avg["S1Help"]        = helpS1/playS1 if playS1 != 0 else 0
    avg["S1Score"]       = scorS1/playS1 if playS1 != 0 else 0
    avg["S2Played"]      = playS2
    avg["S2Interaction"] = inteS2/playS2 if playS2 != 0 else 0
    avg["S2Help"]        = helpS2/playS2 if playS2 != 0 else 0
    avg["S2Score"]       = scorS2/playS2 if playS2 != 0 else 0
    
    avg["Played"]      = play
    avg["Interaction"] = inte/play if play != 0 else 0
    avg["Help"]        = help/play if play != 0 else 0
    avg["Score"]       = scor/play if play != 0 else 0

    return avg

def print_descriptives(desc):
    with open('JDAT_results/'+timestamp+'/ANALYSIS/OutputReport.txt', 'a') as f:
        print("-------------------------------------------",file=f)
        print("Number of users who played the scenarios:",file=f)
        print("-------------------------------------------",file=f)
        print("Scenario 1 Total   => " + str(desc["S1Played"]),file=f)
        print("Scenario 1 Local   => " + str(desc["S1Played_Local"]),file=f)
        print("Scenario 1 Migrant => " + str(desc["S1Played_Migrant"]),file=f)
        print("-------------------------------------------",file=f)
        print("Scenario 2 Total   => " + str(desc["S2Played"]),file=f)
        print("Scenario 2 Local   => " + str(desc["S2Played_Local"]),file=f)
        print("Scenario 2 Migrant => " + str(desc["S2Played_Migrant"]),file=f)
        print("-------------------------------------------",file=f)

        print("Average number of interactions:",file=f)
        print("-------------------------------------------",file=f)
        print("Average            => " + str(special_round(desc["Interaction"])),file=f)
        print("-------------------------------------------",file=f)
        print("Scenario 1 Total   => " + str(special_round(desc["S1Interaction"])),file=f)
        print("Scenario 1 Local   => " + str(special_round(desc["S1Interaction_Local"])),file=f)
        print("Scenario 1 Migrant => " + str(special_round(desc["S1Interaction_Migrant"])),file=f)
        print("-------------------------------------------",file=f)
        print("Scenario 2 Total   => " + str(special_round(desc["S2Interaction"])),file=f)
        print("Scenario 2 Local   => " + str(special_round(desc["S2Interaction_Local"])),file=f)
        print("Scenario 2 Migrant => " + str(special_round(desc["S2Interaction_Migrant"])),file=f)
        print("-------------------------------------------",file=f)

        print("Average number of help requests:",file=f)
        print("-------------------------------------------",file=f)
        print("Average            => " + str(special_round(desc["Help"])),file=f)
        print("-------------------------------------------",file=f)
        print("Scenario 1 Total   => " + str(special_round(desc["S1Help"])),file=f)
        print("Scenario 1 Local   => " + str(special_round(desc["S1Help_Local"])),file=f)
        print("Scenario 1 Migrant => " + str(special_round(desc["S1Help_Migrant"])),file=f)
        print("-------------------------------------------",file=f)
        print("Scenario 2 Total   => " + str(special_round(desc["S2Help"])),file=f)
        print("Scenario 2 Local   => " + str(special_round(desc["S2Help_Local"])),file=f)
        print("Scenario 2 Migrant => " + str(special_round(desc["S2Help_Migrant"])),file=f)
        print("-------------------------------------------",file=f)

        print("Average scores (X/100):",file=f)
        print("-------------------------------------------",file=f)
        print("Average            => " + str(special_round(desc["Score"]*100)),file=f)
        print("-------------------------------------------",file=f)
        print("Scenario 1 Total   => " + str(special_round(desc["S1Score"]*100)),file=f)
        print("Scenario 1 Local   => " + str(special_round(desc["S1Score_Local"]*100)),file=f)
        print("Scenario 1 Migrant => " + str(special_round(desc["S1Score_Migrant"]*100)),file=f)
        print("-------------------------------------------",file=f)
        print("Scenario 2 Total   => " + str(special_round(desc["S2Score"]*100)),file=f)
        print("Scenario 2 Local   => " + str(special_round(desc["S2Score_Local"]*100)),file=f)
        print("Scenario 2 Migrant => " + str(special_round(desc["S2Score_Migrant"]*100)),file=f)
        print("-------------------------------------------",file=f)
    f.close()

def determine_number_of_clusters(data):
    cluster = 0
    silhouettes = []
    for i in range(2, len(data)):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(data)
        labels = kmeans.labels_
        score = silhouette_score(data, labels)
        silhouettes.append(score)
    cluster = silhouettes.index(max(silhouettes))+2
    #print(f'Silhouette Score(n={cluster}): {max(silhouettes)}')
    return cluster

def perform_clustering(data,cluster):

    kmeans = KMeans(n_clusters=cluster)
    kmeans.fit(data)
    labels = kmeans.labels_

    return labels

def plot_clusters(data,labels,type):

    label_colors = {0: 'red', 1: 'blue', 2:'green', 3:'purple', 4:'pink'}

    if len(data)<30:
        tsne = TSNE(n_components=2, verbose=1, n_iter=300,perplexity=len(data)-1)
    else:
        tsne = TSNE(n_components=2, verbose=1, n_iter=300)
    tsne_data = array(data)
    components = tsne.fit_transform(tsne_data)

    x_values = components[:, 0]
    y_values = components[:, 1]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x_values, y_values, c=[label_colors[label] for label in labels], label=labels)

    plt.savefig(str('JDAT_results/'+timestamp+'/ANALYSIS/'+type+'.jpg'))

    return 0

def create_table(data, label_colors):
    
    #data = data[:5]
    fig = plt.figure(figsize=(8, len(data) * 0.25))
    ax = fig.add_subplot(111)
    ax.set_axis_off()

    col_labels = list(data[0].keys())

    cell_values = array([[row[col] for col in col_labels] for row in data])
    cell_values = [[row[0]] + [int(value) for value in row[1:]] for row in cell_values]

    cell_colors = [[label_colors[i] if i in label_colors else 'white' for i in row] for row in cell_values]

    table = ax.table(cellText=cell_values, colLabels=col_labels, loc='center')
    
    for i, row in enumerate(cell_colors,1):
        for j, cell in enumerate(row):
            table.get_celld()[i, j].set_facecolor(cell_colors[i-1][j])
            if j!=0:
                table.get_celld()[i, j].set_text_props(color='white')
    
    plt.savefig(str('JDAT_results/'+timestamp+'/ANALYSIS/Assigned_Clusters.jpg'))

def export_student_clusters(analz_user, demo_labels, intr_labels, full_labels):

    label_colors = {0: 'red', 1: 'blue', 2:'green', 3:'purple', 4:'pink'}
    students_data = [{'Name': name, 'Demo': demo, 'Intr': intr, 'Full': full} for name, demo, intr, full in zip(analz_user, demo_labels, intr_labels, full_labels)]
    
    write_to_csv(str('JDAT_results/'+timestamp+'/ANALYSIS/Student_Clusters.csv'),students_data)
    
    create_table(students_data, label_colors)



