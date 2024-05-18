
from numpy import zeros # type: ignore
from math import floor

def special_round(value, decimal=4):
    return floor(value * 10 ** decimal) / 10 ** decimal

def get_one_hot(value, category):
    if category == "etnicity":
        categories = ["","Africa’s Horn","Arab","Chinese Asian","East and South African","East European","Iranian and Central Asian",
        "Jewish","Maritime and Muslim South-East Asian","North American","North-East Asian","Other North African and Middle Eastern",
        "South American","South Asian","South European","South-East European","West and Central African","West European"]
    elif category == "migrant":
        categories = ["Child and both parents foreign-born", "Child and one parent foreign-born", 
        "Child native-born both parents foreign-born", "Child native-born one parent foreign-born","No migratory background"]
    else: 
        categories = []

    one_hot_encoding = zeros(len(categories))
    index = categories.index(value)
    one_hot_encoding[index] = 1
    return one_hot_encoding.tolist()

def get_duration(data):
    duration = 0
    for session in data:
        duration += session["duration"]
    return duration

def get_character(data):
    character = {"ovtotal":0,"s1total":0,"s2total":0,"s1l1": 0,"s1l2":0,"s1l3": 0,"s1l4":0,"s2l1": 0,"s2l2":0,"s2l3": 0,"s2l4":0}
    
    for session in data:
        character["s1l1"] += session["interaction"]["character"]["breakdown"][0]["levels"][0]["count"]
        character["s1l2"] += session["interaction"]["character"]["breakdown"][0]["levels"][1]["count"]
        character["s1l3"] += session["interaction"]["character"]["breakdown"][0]["levels"][2]["count"]
        character["s1l4"] += session["interaction"]["character"]["breakdown"][0]["levels"][3]["count"]
        character["s2l1"] += session["interaction"]["character"]["breakdown"][1]["levels"][0]["count"]
        character["s2l2"] += session["interaction"]["character"]["breakdown"][1]["levels"][1]["count"]
        character["s2l3"] += session["interaction"]["character"]["breakdown"][1]["levels"][2]["count"]
        character["s2l4"] += session["interaction"]["character"]["breakdown"][1]["levels"][3]["count"]
    
    character["s1total"] = character["s1l1"]+character["s1l2"]+character["s1l3"]+character["s1l4"]
    character["s2total"] = character["s2l1"]+character["s2l2"]+character["s2l3"]+character["s2l4"]
    character["ovtotal"] = character["s1total"]+character["s2total"]

    return character

def get_scene(data):
    scene = {"ovtotal":0,"s1total":0,"s2total":0,"s1l1": 0,"s1l2":0,"s1l3": 0,"s1l4":0,"s2l1": 0,"s2l2":0,"s2l3": 0,"s2l4":0}
    
    for session in data:
        scene["s1l1"] += session["interaction"]["change_scene"]["breakdown"][0]["levels"][0]["count"]
        scene["s1l2"] += session["interaction"]["change_scene"]["breakdown"][0]["levels"][1]["count"]
        scene["s1l3"] += session["interaction"]["change_scene"]["breakdown"][0]["levels"][2]["count"]
        scene["s1l4"] += session["interaction"]["change_scene"]["breakdown"][0]["levels"][3]["count"]
        scene["s2l1"] += session["interaction"]["change_scene"]["breakdown"][1]["levels"][0]["count"]
        scene["s2l2"] += session["interaction"]["change_scene"]["breakdown"][1]["levels"][1]["count"]
        scene["s2l3"] += session["interaction"]["change_scene"]["breakdown"][1]["levels"][2]["count"]
        scene["s2l4"] += session["interaction"]["change_scene"]["breakdown"][1]["levels"][3]["count"]
    
    scene["s1total"] = scene["s1l1"]+scene["s1l2"]+scene["s1l3"]+scene["s1l4"]
    scene["s2total"] = scene["s2l1"]+scene["s2l2"]+scene["s2l3"]+scene["s2l4"]
    scene["ovtotal"] = scene["s1total"]+scene["s2total"]
    
    return scene

def get_movement(data):
    movement = {"ovtotal":0,"s1total":0,"s2total":0,"s1l1": 0,"s1l2":0,"s1l3": 0,"s1l4":0,"s2l1": 0,"s2l2":0,"s2l3": 0,"s2l4":0}
    
    for session in data:
        movement["s1l1"] += session["interaction"]["movement"]["breakdown"][0]["levels"][0]["count"]
        movement["s1l2"] += session["interaction"]["movement"]["breakdown"][0]["levels"][1]["count"]
        movement["s1l3"] += session["interaction"]["movement"]["breakdown"][0]["levels"][2]["count"]
        movement["s1l4"] += session["interaction"]["movement"]["breakdown"][0]["levels"][3]["count"]
        movement["s2l1"] += session["interaction"]["movement"]["breakdown"][1]["levels"][0]["count"]
        movement["s2l2"] += session["interaction"]["movement"]["breakdown"][1]["levels"][1]["count"]
        movement["s2l3"] += session["interaction"]["movement"]["breakdown"][1]["levels"][2]["count"]
        movement["s2l4"] += session["interaction"]["movement"]["breakdown"][1]["levels"][3]["count"]
    
    movement["s1total"] = movement["s1l1"]+movement["s1l2"]+movement["s1l3"]+movement["s1l4"]
    movement["s2total"] = movement["s2l1"]+movement["s2l2"]+movement["s2l3"]+movement["s2l4"]
    movement["ovtotal"] = movement["s1total"]+movement["s2total"]

    return movement

def get_interaction(data):
    character   = get_character(data)
    scene       = get_scene(data)
    movement    = get_movement(data)

    interaction = {"ovtotal":0,"s1total":0,"s2total":0,"s1l1": 0,"s1l2":0,"s1l3": 0,"s1l4":0,"s2l1": 0,"s2l2":0,"s2l3": 0,"s2l4":0}
    
    interaction["s1l1"]  = character["s1l1"]+scene["s1l1"]+movement["s1l1"]
    interaction["s1l2"]  = character["s1l2"]+scene["s1l2"]+movement["s1l2"]
    interaction["s1l3"]  = character["s1l3"]+scene["s1l3"]+movement["s1l3"]
    interaction["s1l4"]  = character["s1l4"]+scene["s1l4"]+movement["s1l4"]
    interaction["s2l1"]  = character["s2l1"]+scene["s2l1"]+movement["s2l1"]
    interaction["s2l2"]  = character["s2l2"]+scene["s2l2"]+movement["s2l2"]
    interaction["s2l3"]  = character["s2l3"]+scene["s2l3"]+movement["s2l3"]
    interaction["s2l4"]  = character["s2l4"]+scene["s2l4"]+movement["s2l4"]

    interaction["s1total"] = interaction["s1l1"]+interaction["s1l2"]+interaction["s1l3"]+interaction["s1l4"]
    interaction["s2total"] = interaction["s2l1"]+interaction["s2l2"]+interaction["s2l3"]+interaction["s2l4"]
    interaction["ovtotal"] = interaction["s1total"]+interaction["s2total"]

    return character, scene, movement, interaction

def get_help(data):
    help = {"ovtotal":0,"s1total":0,"s2total":0,"s1l1": 0,"s1l2":0,"s1l3": 0,"s1l4":0,"s2l1": 0,"s2l2":0,"s2l3": 0,"s2l4":0}
    
    for session in data:
        help["s1l1"] += session["helps"]["breakdown"][0]["levels"][0]["count"]
        help["s1l2"] += session["helps"]["breakdown"][0]["levels"][1]["count"]
        help["s1l3"] += session["helps"]["breakdown"][0]["levels"][2]["count"]
        help["s1l4"] += session["helps"]["breakdown"][0]["levels"][3]["count"]
        help["s2l1"] += session["helps"]["breakdown"][1]["levels"][0]["count"]
        help["s2l2"] += session["helps"]["breakdown"][1]["levels"][1]["count"]
        help["s2l3"] += session["helps"]["breakdown"][1]["levels"][2]["count"]
        help["s2l4"] += session["helps"]["breakdown"][1]["levels"][3]["count"]
    
    help["s1total"] = help["s1l1"]+help["s1l2"]+help["s1l3"]+help["s1l4"]
    help["s2total"] = help["s2l1"]+help["s2l2"]+help["s2l3"]+help["s2l4"]
    help["ovtotal"] = help["s1total"]+help["s2total"]

    return help

def get_score(data):
    rawscore    = {"ovtotal":0,"s1total":0,"s2total":0,"s1l1": 0,"s1l2":0,"s1l3": 0,"s1l4":0,"s2l1": 0,"s2l2":0,"s2l3": 0,"s2l4":0}
    question    = {"ovtotal":0,"s1total":0,"s2total":0,"s1l1": 0,"s1l2":0,"s1l3": 0,"s1l4":0,"s2l1": 0,"s2l2":0,"s2l3": 0,"s2l4":0}
    maximum     = {"ovtotal":0,"s1total":0,"s2total":0,"s1l1": 0,"s1l2":0,"s1l3": 0,"s1l4":0,"s2l1": 0,"s2l2":0,"s2l3": 0,"s2l4":0}
    score       = {"ovtotal":0,"s1total":0,"s2total":0,"s1l1": 0,"s1l2":0,"s1l3": 0,"s1l4":0,"s2l1": 0,"s2l2":0,"s2l3": 0,"s2l4":0}

    for session in data:
        rawscore["s1l1"]  += session["scores"]["breakdown"][0]["levels"][0]["scaled"]
        rawscore["s1l2"]  += session["scores"]["breakdown"][0]["levels"][1]["scaled"]
        rawscore["s1l3"]  += session["scores"]["breakdown"][0]["levels"][2]["scaled"]
        rawscore["s1l4"]  += session["scores"]["breakdown"][0]["levels"][3]["scaled"]
        rawscore["s2l1"]  += session["scores"]["breakdown"][1]["levels"][0]["scaled"]
        rawscore["s2l2"]  += session["scores"]["breakdown"][1]["levels"][1]["scaled"]
        rawscore["s2l3"]  += session["scores"]["breakdown"][1]["levels"][2]["scaled"]
        rawscore["s2l4"]  += session["scores"]["breakdown"][1]["levels"][3]["scaled"]

        question["s1l1"]  += session["scores"]["breakdown"][0]["levels"][0]["question"]
        question["s1l2"]  += session["scores"]["breakdown"][0]["levels"][1]["question"]
        question["s1l3"]  += session["scores"]["breakdown"][0]["levels"][2]["question"]
        question["s1l4"]  += session["scores"]["breakdown"][0]["levels"][3]["question"]
        question["s2l1"]  += session["scores"]["breakdown"][1]["levels"][0]["question"]
        question["s2l2"]  += session["scores"]["breakdown"][1]["levels"][1]["question"]
        question["s2l3"]  += session["scores"]["breakdown"][1]["levels"][2]["question"]
        question["s2l4"]  += session["scores"]["breakdown"][1]["levels"][3]["question"]
        
        maximum["s1l1"]  += session["scores"]["breakdown"][0]["levels"][0]["max"]
        maximum["s1l2"]  += session["scores"]["breakdown"][0]["levels"][1]["max"]
        maximum["s1l3"]  += session["scores"]["breakdown"][0]["levels"][2]["max"]
        maximum["s1l4"]  += session["scores"]["breakdown"][0]["levels"][3]["max"]
        maximum["s2l1"]  += session["scores"]["breakdown"][1]["levels"][0]["max"]
        maximum["s2l2"]  += session["scores"]["breakdown"][1]["levels"][1]["max"]
        maximum["s2l3"]  += session["scores"]["breakdown"][1]["levels"][2]["max"]
        maximum["s2l4"]  += session["scores"]["breakdown"][1]["levels"][3]["max"]
    
    question["s1total"] = question["s1l1"]+question["s1l2"]+question["s1l3"]+question["s1l4"]
    question["s2total"] = question["s2l1"]+question["s2l2"]+question["s2l3"]+question["s2l4"]
    question["ovtotal"] = question["s1total"]+question["s2total"]

    score["s1l1"] = special_round(rawscore["s1l1"]/maximum["s1l1"]) if question["s1l1"] > 0 else 0
    score["s1l2"] = special_round(rawscore["s1l2"]/maximum["s1l2"]) if question["s1l2"] > 0 else 0
    score["s1l3"] = special_round(rawscore["s1l3"]/maximum["s1l3"]) if question["s1l3"] > 0 else 0
    score["s1l4"] = special_round(rawscore["s1l4"]/maximum["s1l4"]) if question["s1l4"] > 0 else 0
    score["s2l1"] = special_round(rawscore["s2l1"]/maximum["s2l1"]) if question["s2l1"] > 0 else 0
    score["s2l2"] = special_round(rawscore["s2l2"]/maximum["s2l2"]) if question["s2l2"] > 0 else 0
    score["s2l3"] = special_round(rawscore["s2l3"]/maximum["s2l3"]) if question["s2l3"] > 0 else 0
    score["s2l4"] = special_round(rawscore["s2l4"]/maximum["s2l4"]) if question["s2l4"] > 0 else 0
    
    score["s1total"] = special_round((score["s1l1"]+score["s1l2"]+score["s1l3"]+score["s1l4"])/4)
    score["s2total"] = special_round((score["s2l1"]+score["s2l2"]+score["s2l3"]+score["s2l4"])/4)
    score["ovtotal"] = special_round((score["s1total"]+score["s2total"])/2)

    return score, question

def get_total_values(user_data):
    duration       = get_duration(user_data["data"])
    interaction    = get_interaction(user_data["data"])[3]
    help           = get_help(user_data["data"])
    score,question = get_score(user_data["data"])
    
    total_values = {}
    total_values["Duration"]             = duration
    total_values["Score"]                = score["ovtotal"]
    total_values["Scenario1Question"]    = question["s1total"]
    total_values["Scenario1Interaction"] = interaction["s1total"]
    total_values["Scenario1Help"]        = help["s1total"]
    total_values["Scenario1Score"]       = score["s1total"]
    total_values["Scenario2Question"]    = question["s2total"]
    total_values["Scenario2Interaction"] = interaction["s2total"]
    total_values["Scenario2Help"]        = help["s2total"]
    total_values["Scenario2Score"]       = score["s2total"]
    total_values["MigrantBackground"]    = user_data["survey"]["MigrantBackground"]

    return total_values

def get_analysis_vector(user_data):
    help     = get_help(user_data["data"])
    score    = get_score(user_data["data"])[0]
    #duration = get_duration(user_data["data"])
    character, scene, movement,_ = get_interaction(user_data["data"])

    age                = int(user_data["survey"]["Age"]) 
    migration_age      = int(user_data["survey"]["MigrationAge"]) if user_data["survey"]["MigrationAge"] != "" else -1
    ethnicity          = get_one_hot(user_data["survey"]["Ethnicity"], "etnicity")
    migrant_background = get_one_hot(user_data["survey"]["MigrantBackground"], "migrant")
    roma_child         = [0 if user_data["survey"]["Roma"] == 'No' else 1]
    adoption           = [0 if user_data["survey"]["Adopted"] == 'No' else 1]
    gender_sex         = [0 if user_data["survey"]["Sex"] == 'Boy' else 1]
    #language          = get_one_hot(user_data["survey"]["Language"], "language")
    
    session_breakdown = [score["s1total"],score["s2total"],character["s1total"],character["s2total"],scene["s1total"],scene["s2total"],
    movement["s1total"],movement["s2total"],help["s1total"],help["s2total"]]
    #level_breakdown = 

    demographic_vector = [age,migration_age]
    demographic_vector.extend(ethnicity)
    demographic_vector.extend(migrant_background)
    demographic_vector.extend(gender_sex)
    demographic_vector.extend(roma_child)
    demographic_vector.extend(adoption) 
    #demographic_vector.extend(language)
                         
    interaction_vector = [score["ovtotal"],character["ovtotal"],scene["ovtotal"],movement["ovtotal"],help["ovtotal"]]
    interaction_vector.extend(session_breakdown)

    full_vector = [score["ovtotal"],character["ovtotal"],scene["ovtotal"],movement["ovtotal"],help["ovtotal"],age,migration_age]
    full_vector.extend(session_breakdown)
    full_vector.extend(ethnicity)
    full_vector.extend(migrant_background)
    full_vector.extend(gender_sex)
    full_vector.extend(roma_child)
    full_vector.extend(adoption) 
    #full_vector.extend(language)
    
    return demographic_vector, interaction_vector, full_vector

def get_analysis_vector_set(data):
    demo_analysis_data = []
    intr_analysis_data = []
    full_analysis_data = []
    analysis_user = []
    for row in data:
        demo_vector, intr_vector, full_vector = get_analysis_vector(row)
        demo_analysis_data.append(demo_vector)
        intr_analysis_data.append(intr_vector)
        full_analysis_data.append(full_vector)
        analysis_user.append(row["student"])

    return demo_analysis_data, intr_analysis_data, full_analysis_data, analysis_user
