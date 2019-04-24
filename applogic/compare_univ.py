import db_connect as db
from applogic import db_queries

# def get_data():
#     crime_tables = ['arrest', 'disciplinary_action']#'vawa', 'criminal']
#     result = []

#     crime_tables = ['arrest']
#     for table in crime_tables:
#         print(db_queries.compare_university)

#         rows = db.cursor.execute(db_queries.compare_university).fetchall()
#         print(rows)
#         result.append({"compare_table": table.title(), "compare_data": rows})
#     return result

def get_comparison_arrest(uni_names, year, uni_count):
    #crime_tables = ['arrest']
    result = []
    #for table in crime_tables:
    for name in uni_names:
        rows = db.cursor.execute(db_queries.compare_university_arrest.format(
                uni_name = name,
                year = year
             )).fetchall()
            
        rows[0] = list(rows[0])
        for index, item in enumerate(rows[0]):
            if item == None:
               rows[0][index] = 0
        rows[0] = tuple(rows[0])
        result.append({"uni_name": name.title(), "compare_data": rows})
    temp = []
    if(uni_count == 2):
        for a, b in zip(result[0]['compare_data'][0], result[1]['compare_data'][0]):
            temp.append([a,b])
    elif(uni_count == 3):
        for a, b, c in zip(result[0]['compare_data'][0], result[1]['compare_data'][0], result[2]['compare_data'][0]):
            temp.append([a,b,c])
    #print(temp)
    result.append({"pairwise_data": temp})
   # print(result)
    return result

def get_comparison_disc_action(uni_names, year, uni_count):
    #crime_tables = ['disciplinary_action']
    result = []
    #for table in crime_tables:
    for name in uni_names:
        rows = db.cursor.execute(db_queries.compare_university_disc_action.format(
                uni_name = name,
                year = year
            )).fetchall()
        #print(rows)
        rows[0] = list(rows[0])
        for index, item in enumerate(rows[0]):
            if item == None:
                rows[0][index] = 0
        rows[0] = tuple(rows[0])
        result.append({"uni_name": name.title(), "compare_data": rows})
    temp = []
    if(uni_count == 2):
        for a, b in zip(result[0]['compare_data'][0], result[1]['compare_data'][0]):
            temp.append([a,b])
    elif(uni_count == 3):
        for a, b, c in zip(result[0]['compare_data'][0], result[1]['compare_data'][0], result[2]['compare_data'][0]):
            temp.append([a,b,c])
    #print(temp)
    result.append({"pairwise_data": temp})
    #print(result)
    return result

def get_comparison_criminal(uni_names, year, uni_count):
    #crime_tables = ['criminal']
    result = []
    #for table in crime_tables:
    for name in uni_names:
        rows = db.cursor.execute(db_queries.compare_university_criminal.format(
                uni_name = name,
                year = year
            )).fetchall()
        #print(rows)
        rows[0] = list(rows[0])
        for index, item in enumerate(rows[0]):
            if item == None:
                rows[0][index] = 0
        rows[0] = tuple(rows[0])
        result.append({"uni_name": name.title(), "compare_data": rows})
    temp = []
    if(uni_count == 2):
        for a, b in zip(result[0]['compare_data'][0], result[1]['compare_data'][0]):
            temp.append([a,b])
    elif(uni_count == 3):
        for a, b, c in zip(result[0]['compare_data'][0], result[1]['compare_data'][0], result[2]['compare_data'][0]):
            temp.append([a,b,c])
    #print(temp)
    result.append({"pairwise_data": temp})
    #print(result)
    return result

def get_comparison_vawa(uni_names, year, uni_count):
    #crime_tables = ['vawa']
    result = []
    #for table in crime_tables:
    for name in uni_names:
        print(db_queries.compare_university_vawa.format(
            uni_name=name,
            year=year
            )
        )
        rows = db.cursor.execute(db_queries.compare_university_vawa.format(
                uni_name = name,
                year = year
            )).fetchall()
        #print(rows)
        rows[0] = list(rows[0])
        for index, item in enumerate(rows[0]):
            if item == None:
                rows[0][index] = 0
        rows[0] = tuple(rows[0])

        result.append({"uni_name": name.title(), "compare_data": rows})
    temp = []
    if(uni_count == 2):
        for a, b in zip(result[0]['compare_data'][0], result[1]['compare_data'][0]):
            temp.append([a,b])
    elif(uni_count == 3):
        for a, b, c in zip(result[0]['compare_data'][0], result[1]['compare_data'][0], result[2]['compare_data'][0]):
            temp.append([a,b,c])
    #print(temp)
    result.append({"pairwise_data": temp})
    #print(result)
    return result

def get_comparison_hate(uni_names, year, uni_count):
    #crime_tables = ['hate']
    result = []
    #for table in crime_tables:
    for name in uni_names:
        rows = db.cursor.execute(db_queries.compare_university_hate.format(
                    uni_name = name,
                    year = year
                )).fetchall()
            #print(rows)
        rows[0] = list(rows[0])
        for index, item in enumerate(rows[0]):
            if item == None:
                rows[0][index] = 0
        rows[0] = tuple(rows[0])

        result.append({"uni_name": name.title(), "compare_data": rows})
    temp = []
    if(uni_count == 2):
        for a, b in zip(result[0]['compare_data'][0], result[1]['compare_data'][0]):
            temp.append([a,b])
    elif(uni_count == 3):
        for a, b, c in zip(result[0]['compare_data'][0], result[1]['compare_data'][0], result[2]['compare_data'][0]):
            temp.append([a,b,c])
    result.append({"pairwise_data": temp})
    #print(result)
    return result