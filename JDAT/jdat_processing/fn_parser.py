from datetime import datetime
from fn_reader import write_to_json,timestamp

def get_duration_of_sessions(user_data):
    sessions = []
    for row in user_data:
        if "context" in row: 
            if "extensions" in row["context"]:
                if "https://joinclusion.fse.maastrichtuniversity.nl/session" in row["context"]["extensions"]:
                    #print(row)
                    if row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/session"] not in sessions:
                        sessions.append(row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/session"])
    #print(sessions)
    session_durations = []
    for session in sessions:
        min = datetime.now()
        max = datetime.strptime('1900-05-08T13:00:52Z',"%Y-%m-%dT%H:%M:%SZ")
        data = {}
        for row in user_data: 
            if "context" in row and "extensions" in row["context"] and "https://joinclusion.fse.maastrichtuniversity.nl/session" in row["context"]["extensions"]:
                if row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/session"] == session:
                    timestamp = datetime.strptime(row["timestamp"].rstrip('_'), '%Y-%m-%dT%H:%M:%SZ')
                    if timestamp< min:
                        min = timestamp
                    if timestamp> max:
                        max = timestamp  
        data["session"] = session
        data["duration"] = (max-min).seconds
        session_durations.append(data)
    return session_durations

def get_number_of_interactions(user_data, sessions):
    sessions_updated = []
    for session in sessions:
        sid = session["session"]
        count_char = 0
        count_scene_change = 0
        #count_line = 0
        count_else = 0
        count_movement = 0

        character_counting = [{"scenario": 1,
        "levels": [{"level": 1, "count": 0},{"level": 2, "count": 0},{"level": 3, "count": 0},{"level": 4, "count": 0}],
        "total": 0},
        {"scenario": 2,
        "levels": [{"level": 1, "count": 0},{"level": 2, "count": 0},{"level": 3, "count": 0},{"level": 4, "count": 0}],
        "total": 0}]
        scene_change_counting = [{"scenario": 1,
        "levels": [{"level": 1, "count": 0},{"level": 2, "count": 0},{"level": 3, "count": 0},{"level": 4, "count": 0}],
        "total": 0},
        {"scenario": 2,
        "levels": [{"level": 1, "count": 0},{"level": 2, "count": 0},{"level": 3, "count": 0},{"level": 4, "count": 0}],
        "total": 0}]
        movement_counting = [{"scenario": 1,
        "levels": [{"level": 1, "count": 0},{"level": 2, "count": 0},{"level": 3, "count": 0},{"level": 4, "count": 0}],
        "total": 0},
        {"scenario": 2,
        "levels": [{"level": 1, "count": 0},{"level": 2, "count": 0},{"level": 3, "count": 0},{"level": 4, "count": 0}],
        "total": 0}]

        for row in user_data:
            if "context" in row and "extensions" in row["context"] and "https://joinclusion.fse.maastrichtuniversity.nl/session" in row["context"]["extensions"]:
                if row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/session"]==sid:
                    #count_line += 1
                    if row["verb"]["id"] == "http://adlnet.gov/expapi/verbs/interacted" and "https://joinclusion.fse.maastrichtuniversity.nl/character" in row["context"]["extensions"]:
                        count_char += 1
                        if "https://joinclusion.fse.maastrichtuniversity.nl/scenario" in row["context"]["extensions"]:
                                scenario_id = row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/scenario"]
                                level_id = row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/level"]
                                character_counting[int(scenario_id)-1]["levels"][int(level_id)-1]["count"] += 1
                                character_counting[int(scenario_id)-1]["total"] += 1
                    elif row["verb"]["id"] == "http://adlnet.gov/expapi/verbs/interacted" and "https://joinclusion.fse.maastrichtuniversity.nl/initial_scene" in row["context"]["extensions"]:
                        count_scene_change += 1    
                        if "https://joinclusion.fse.maastrichtuniversity.nl/scenario" in row["context"]["extensions"]:
                                scenario_id = row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/scenario"]
                                level_id = row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/level"]
                                scene_change_counting[int(scenario_id)-1]["levels"][int(level_id)-1]["count"] += 1
                                scene_change_counting[int(scenario_id)-1]["total"] += 1
                    elif row["verb"]["id"] == "http://adlnet.gov/expapi/verbs/interacted" and "https://joinclusion.fse.maastrichtuniversity.nl/movement" in row["context"]["extensions"]:
                        count_movement += 1    
                        if "https://joinclusion.fse.maastrichtuniversity.nl/scenario" in row["context"]["extensions"]:
                                scenario_id = row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/scenario"]
                                level_id = row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/level"]
                                movement_counting[int(scenario_id)-1]["levels"][int(level_id)-1]["count"] += 1
                                movement_counting[int(scenario_id)-1]["total"] += 1
                    else:
                        count_else += 1
    
        count_str = {}
        #count_str["character"] = count_char
        character = {}
        character["total"]     = count_char
        character["breakdown"] = character_counting
        count_str["character"] = character
        
        scene = {}
        scene["total"]     = count_scene_change
        scene["breakdown"] = scene_change_counting
        count_str["change_scene"] = scene
        
        movement = {}
        movement["total"]     = count_movement
        movement["breakdown"] = movement_counting
        count_str["movement"] = movement

        count_str["total_interactions"] = count_char+count_scene_change+count_movement
        #count_str["all_interactions"] = count_char+count_scene_change+count_movement+count_else
        #count_str["all_statements"] = count_line
        session["interaction"] = count_str
        sessions_updated.append(session)

    return sessions_updated

def get_scores(user_data, sessions):
    sessions_updated = []
    for session in sessions:
        sid = session["session"]

        score_counting = [{"scenario": 1,
        "levels": [{"level": 1, "score": 0, "scaled": 0, "max": 0, "question": 0},{"level": 2, "score": 0, "scaled": 0, "max": 0, "question": 0},{"level": 3, "score": 0, "scaled": 0, "max": 0, "question": 0},{"level": 4, "score": 0, "scaled": 0, "max": 0, "question": 0}],
        "total_score": 0, "total_scaled": 0, "max_score": 0, "total_question": 0},
        {"scenario": 2,
        "levels": [{"level": 1, "score": 0, "scaled": 0, "max": 0, "question": 0},{"level": 2, "score": 0, "scaled": 0, "max": 0, "question": 0},{"level": 3, "score": 0, "scaled": 0, "max": 0, "question": 0},{"level": 4, "score": 0, "scaled": 0, "max": 0, "question": 0}],
        "total_score": 0, "total_scaled": 0, "max_score": 0, "total_question": 0}]

        count_score    = 0
        count_scaled   = 0
        count_max      = 0
        count_question = 0
        count_NAN      = 0

        for row in user_data:
            if "context" in row and "extensions" in row["context"] and "https://joinclusion.fse.maastrichtuniversity.nl/session" in row["context"]["extensions"]:
                if row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/session"]==sid:
                    if row["verb"]["id"] == "https://w3id.org/xapi/tla#scored" and "https://joinclusion.fse.maastrichtuniversity.nl/question_id" in row["context"]["extensions"]:
                        if row["result"]["score"]["max"] >= 0:
                            if "https://joinclusion.fse.maastrichtuniversity.nl/scenario" in row["context"]["extensions"]:
                                    scenario_id = row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/scenario"]
                                    level_id = row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/level"]
                                    score_counting[int(scenario_id)-1]["levels"][int(level_id)-1]["score"]    += row["result"]["score"]["raw"]
                                    score_counting[int(scenario_id)-1]["levels"][int(level_id)-1]["scaled"]   += row["result"]["score"]["scaled"]
                                    score_counting[int(scenario_id)-1]["levels"][int(level_id)-1]["max"]      += row["result"]["score"]["max"]
                                    score_counting[int(scenario_id)-1]["levels"][int(level_id)-1]["question"] += 1
                                    score_counting[int(scenario_id)-1]["total_score"]    += row["result"]["score"]["raw"]
                                    score_counting[int(scenario_id)-1]["total_scaled"]   += row["result"]["score"]["scaled"]
                                    score_counting[int(scenario_id)-1]["max_score"]      += row["result"]["score"]["max"]
                                    score_counting[int(scenario_id)-1]["total_question"] += 1
                                    count_score    += row["result"]["score"]["raw"]
                                    count_scaled   += row["result"]["score"]["scaled"]
                                    count_max      += row["result"]["score"]["max"]
                                    count_question += 1
                        else:
                            count_NAN += 1
    
        score_str = {}        
        score_str["breakdown"]      = score_counting
        score_str["total_score"]    = count_score
        score_str["total_scaled"]   = count_scaled
        score_str["max_score"]      = count_max
        score_str["total_question"] = count_question
        score_str["non_scored"]     = count_NAN

        session["scores"]           = score_str
        sessions_updated.append(session)
    return sessions_updated

def get_help_requests(user_data, sessions):
    sessions_updated = []
    for session in sessions:
        sid = session["session"]

        help_counting = [{"scenario": 1,
        "levels": [{"level": 1, "count": 0},{"level": 2, "count": 0},{"level": 3, "count": 0},{"level": 4, "count": 0}],
        "total": 0},
        {"scenario": 2,
        "levels": [{"level": 1, "count": 0},{"level": 2, "count": 0},{"level": 3, "count": 0},{"level": 4, "count": 0}],
        "total": 0}]

        count_help = 0

        for row in user_data:
            if "context" in row and "extensions" in row["context"] and "https://joinclusion.fse.maastrichtuniversity.nl/session" in row["context"]["extensions"]:
                if row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/session"]==sid:
                    if row["verb"]["id"] == "http://adlnet.gov/expapi/verbs/asked":
                        if "https://joinclusion.fse.maastrichtuniversity.nl/scenario" in row["context"]["extensions"]:
                                    scenario_id = row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/scenario"]
                                    level_id = row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/level"]
                                    help_counting[int(scenario_id)-1]["levels"][int(level_id)-1]["count"] += 1
                                    help_counting[int(scenario_id)-1]["total"] += 1
                                    count_help += 1
    
        help_str = {}        
        help_str["breakdown"]  = help_counting
        help_str["total_help"] = count_help
        session["helps"]       = help_str
        sessions_updated.append(session)
    return sessions_updated

def get_user_data(data,user):
    user_data = []
    for row in data:
        if "context" in row and "extensions" in row["context"] and "https://joinclusion.fse.maastrichtuniversity.nl/session" in row["context"]["extensions"]:
            if row["context"]["extensions"]["https://joinclusion.fse.maastrichtuniversity.nl/student"] == user:
                user_data.append(row)    
    return user_data

def get_survey_data(data,user):
    for survey in data:
        if survey["Nickname"] == user:
            return survey

def parse_user_data(data):
    parsed_data = []
    parsed_data = get_duration_of_sessions(data)
    parsed_data = get_number_of_interactions(data, parsed_data)
    parsed_data = get_scores(data, parsed_data)
    parsed_data = get_help_requests(data, parsed_data)
    return parsed_data

def parse_data(data,sdata,users):
    full_parsed_data = []
    i=0
    for user in users:
        user_data   = get_user_data(data, user)
        if i == 27:
            write_to_json('TestUser.json', user_data)
        parsed_data = parse_user_data(user_data)
        survey_data = get_survey_data(sdata, user)
        
        full_data = {}
        full_data["student"] = user
        full_data["data"]    = parsed_data
        full_data["survey"]  = survey_data
        
        full_parsed_data.append(full_data)
        i+=1
    
    savepath = 'JDAT_results/'+timestamp+'/DATA/full_data_parsed.json'
    write_to_json(savepath, full_parsed_data)

    return full_parsed_data
