import db_connect as db
from applogic import  db_queries

def get_all_institute_names():
    institutes = []
    rows = db.cursor.execute(db_queries.all_university_names).fetchall()
    #print (rows[0])

    # result is like list of tuples
    institutes = [i[0] for i in rows]

    print ('hii')
    print(f"total number of institutes: {len(institutes)}")
    institutes.sort()
    print(institutes)
    return institutes

def get_campus_crimes(uni_name, year, location):
    crime_tables = ['arrest', 'disciplinary_action']#'vawa', 'criminal']
    resultSet = []
    crime_data = {}


    if location == '--':
        if year == '--':
            #criminal
            rows = db.cursor.execute(db_queries.university_crimes_criminal_all.format(
                uni_name=uni_name,
                year=year,
                location=location)).fetchall()
            print(rows)
            resultSet.append(rows)

            #vawa
            rows = db.cursor.execute(db_queries.university_crimes_vawa_all.format(
                uni_name=uni_name,
                year=year,
                location=location)).fetchall()

            # print(rows)
            # temp = []
            # abc = [0, 0, 0]
            # for row in rows:
            #     #abc = list(row)
            #     for i, val in enumerate(row):
            #         print('val')
            #         print(val)
            #         if val == None:
            #             abc[i] = 0
            #         else:
            #            abc[i] = val
            #     temp.append(tuple(abc))
            #
            # print('1')
            # print(temp)
            #resultSet.append(rows)

            resultSet.append(rows)

            #hate
            rows = db.cursor.execute(db_queries.university_crimes_hate_all.format(
                uni_name=uni_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

        else:
            #criminal
            rows = db.cursor.execute(db_queries.university_crimes_criminal_noLoc.format(
                uni_name=uni_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)


            #vawa
            rows = db.cursor.execute(db_queries.university_crimes_vawa_noLoc.format(
                uni_name=uni_name,
                year=year,
                location=location)).fetchall()
            print(rows)
            abc = list(rows)
            for i, val in enumerate(abc):
                if val == "None":
                    abc[i] = 0
            rows = tuple(abc)

            print('vawa --')
            print(rows)

            resultSet.append(rows)

            #hate
            rows = db.cursor.execute(db_queries.university_crimes_hate_noLoc.format(
                uni_name=uni_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

    elif(year == '--'):
        if(location == '--'):
            #criminal
            rows = db.cursor.execute(db_queries.university_crimes_criminal_all.format(
                uni_name=uni_name,
                year=year,
                location=location)).fetchall()
            print(rows)
            resultSet.append(rows)

            #vawa
            rows = db.cursor.execute(db_queries.university_crimes_vawa_all.format(
                uni_name=uni_name,
                year=year,
                location=location)).fetchall()

            print(rows)

            abc = list(rows)
            for i, val in enumerate(abc):
                if val == "None":
                    abc[i] = 0
            rows = tuple(abc)

            print('vawa --')
            print(rows)

            resultSet.append(rows)

            #hate
            rows = db.cursor.execute(db_queries.university_crimes_hate_all.format(
                uni_name=uni_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)
        else:
            #criminal
            rows = db.cursor.execute(db_queries.university_crimes_criminal_noYear.format(
                uni_name=uni_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

            #vawa 
            rows = db.cursor.execute(db_queries.university_crimes_vawa_noYear.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            abc = list(rows)
            for i, val in enumerate(abc):
                if val == "None":
                    abc[i] = 0
            rows = tuple(abc)

            print('vawa --')
            print(rows)

            resultSet.append(rows)

            #hate
            rows = db.cursor.execute(db_queries.university_crimes_hate_noYear.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

    elif(year == '--' and location == '--'):
        #criminal
        rows = db.cursor.execute(db_queries.university_crimes_criminal_all.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)

        #vawa
        rows = db.cursor.execute(db_queries.university_crimes_vawa_all.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        abc = list(rows)
        for i, val in enumerate(abc):
            if val == "None":
                abc[i] = 0
        rows = tuple(abc)

        print('vawa --')
        print(rows)

        resultSet.append(rows)

        #hate
        rows = db.cursor.execute(db_queries.university_crimes_hate_all.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)

    else:
#        print('yooo')
        #criminal
        rows = db.cursor.execute(db_queries.university_crimes_criminal.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)

        #vawa
        rows = db.cursor.execute(db_queries.university_crimes_vawa.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        # abc = list(rows)
        # for i, val in enumerate(abc):
        #     if val == "None":
        #         abc[i] = 0
        # rows = tuple(abc)

        # print('vawa --')
        # print(rows)

        resultSet.append(rows)

        #hate
        rows = db.cursor.execute(db_queries.university_crimes_hate.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)


#------------- arrests/disciplinary action section -----------------
    for table in crime_tables:
        if (location == '--'):
            if (year == '--'):
                #arrests/disc
                rows = db.cursor.execute(db_queries.university_crimes_arrest_all.format(
                    inst_name=inst_name,
                    year=year,
                    crime_table=table,
                    location=location)).fetchall()

                resultSet.append(rows)
            else:
                #arrests/disc
                rows = db.cursor.execute(db_queries.university_crimes_arrest_noLoc.format(
                    inst_name=inst_name,
                    year=year,
                    crime_table=table,
                    location=location)).fetchall()

            resultSet.append(rows)

        elif(year == '--'):
            if(location == '--'):
                #arrests/disc
                rows = db.cursor.execute(db_queries.university_crimes_arrest_all.format(
                inst_name=inst_name,
                year=year,
                crime_table=table,
                location=location)).fetchall()

                resultSet.append(rows)

            else:
                #arrests/disc
                rows = db.cursor.execute(db_queries.university_crimes_arrest_noYear.format(
                inst_name=inst_name,
                year=year,
                crime_table=table,
                location=location)).fetchall()

                resultSet.append(rows)

        elif(year == '--' and location == '--'):
            #arrests/disc
            rows = db.cursor.execute(db_queries.university_crimes_arrest_all.format(
                inst_name=inst_name,
                year=year,
                crime_table=table,
                location=location)).fetchall()

            resultSet.append(rows)

        else:
            #arrests/disc
            rows = db.cursor.execute(db_queries.university_crimes_arrest.format(
                inst_name=inst_name,
                year=year,
                crime_table=table,
                location=location)).fetchall()

            resultSet.append(rows)


    #print(row[1])
    #crime_data[row[1]] = row[0]
    #resultSet.append({"crime_table": table.title(), "crime_data": crime_data})
    # print('in resultSet')
    # print(resultSet)

    return resultSet


def get_campus_crimes(inst_name, year, location):
    crime_tables = ['arrest', 'disciplinary_action']#'vawa', 'criminal']
    resultSet = []
    crime_data = {}
    print(inst_name)
    print(year)
    print(location)


    if location == '--':
        if year == '--':
            #criminal
            #1
            rows = db.cursor.execute(db_queries.university_crimes_criminal_all.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()
            print(rows)
            resultSet.append(rows)

            #vawa
            #2
            rows = db.cursor.execute(db_queries.university_crimes_vawa_all.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            # print(rows)
            # temp = []
            # abc = [0, 0, 0]
            # for row in rows:
            #     #abc = list(row)
            #     for i, val in enumerate(row):
            #         print('val')
            #         print(val)
            #         if val == None:
            #             abc[i] = 0
            #         else:
            #            abc[i] = val
            #     temp.append(tuple(abc))
            #
            # print('1')
            # print(temp)
            #resultSet.append(rows)

            resultSet.append(rows)

            #hate #3
            rows = db.cursor.execute(db_queries.university_crimes_hate_all.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

        else:
            #criminal
            rows = db.cursor.execute(db_queries.university_crimes_criminal_noLoc.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)


            #vawa
            rows = db.cursor.execute(db_queries.university_crimes_vawa_noLoc.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()
            print(rows)
            abc = list(rows)
            for i, val in enumerate(abc):
                if val == "None":
                    abc[i] = 0
            rows = tuple(abc)

            print('vawa --')
            print(rows)

            resultSet.append(rows)

            #hate
            rows = db.cursor.execute(db_queries.university_crimes_hate_noLoc.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

    elif(year == '--'):
        if(location == '--'):
            #criminal
            rows = db.cursor.execute(db_queries.university_crimes_criminal_all.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()
            print(rows)
            resultSet.append(rows)

            #vawa
            rows = db.cursor.execute(db_queries.university_crimes_vawa_all.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            print(rows)

            abc = list(rows)
            for i, val in enumerate(abc):
                if val == "None":
                    abc[i] = 0
            rows = tuple(abc)

            print('vawa --')
            print(rows)

            resultSet.append(rows)

            #hate
            rows = db.cursor.execute(db_queries.university_crimes_hate_all.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)
        else:
            #criminal
            rows = db.cursor.execute(db_queries.university_crimes_criminal_noYear.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

            #vawa
            rows = db.cursor.execute(db_queries.university_crimes_vawa_noYear.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            abc = list(rows)
            for i, val in enumerate(abc):
                if val == "None":
                    abc[i] = 0
            rows = tuple(abc)

            print('vawa --')
            print(rows)

            resultSet.append(rows)

            #hate
            rows = db.cursor.execute(db_queries.university_crimes_hate_noYear.format(
                inst_name=inst_name,
                year=year,
                location=location)).fetchall()

            resultSet.append(rows)

    elif(year == '--' and location == '--'):
        #criminal
        rows = db.cursor.execute(db_queries.university_crimes_criminal_all.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)

        #vawa
        rows = db.cursor.execute(db_queries.university_crimes_vawa_all.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        abc = list(rows)
        for i, val in enumerate(abc):
            if val == "None":
                abc[i] = 0
        rows = tuple(abc)

        print('vawa --')
        print(rows)

        resultSet.append(rows)

        #hate
        rows = db.cursor.execute(db_queries.university_crimes_hate_all.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)

    else:
#        print('yooo')
        #criminal
        rows = db.cursor.execute(db_queries.university_crimes_criminal.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)

        #vawa
        rows = db.cursor.execute(db_queries.university_crimes_vawa.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        # abc = list(rows)
        # for i, val in enumerate(abc):
        #     if val == "None":
        #         abc[i] = 0
        # rows = tuple(abc)

        # print('vawa --')
        # print(rows)

        resultSet.append(rows)

        #hate
        rows = db.cursor.execute(db_queries.university_crimes_hate.format(
            inst_name=inst_name,
            year=year,
            location=location)).fetchall()

        resultSet.append(rows)


#------------- arrests/disciplinary action section -----------------
    for table in crime_tables:
        if (location == '--'):
            if (year == '--'):
                #arrests/disc
                rows = db.cursor.execute(db_queries.university_crimes_arrest_all.format(
                    inst_name=inst_name,
                    year=year,
                    crime_table=table,
                    location=location)).fetchall()

                resultSet.append(rows)
            else:
                #arrests/disc
                rows = db.cursor.execute(db_queries.university_crimes_arrest_noLoc.format(
                    inst_name=inst_name,
                    year=year,
                    crime_table=table,
                    location=location)).fetchall()

            resultSet.append(rows)

        elif(year == '--'):
            if(location == '--'):
                #arrests/disc
                rows = db.cursor.execute(db_queries.university_crimes_arrest_all.format(
                inst_name=inst_name,
                year=year,
                crime_table=table,
                location=location)).fetchall()

                resultSet.append(rows)

            else:
                #arrests/disc
                rows = db.cursor.execute(db_queries.university_crimes_arrest_noYear.format(
                inst_name=inst_name,
                year=year,
                crime_table=table,
                location=location)).fetchall()

                resultSet.append(rows)

        elif(year == '--' and location == '--'):
            #arrests/disc
            rows = db.cursor.execute(db_queries.university_crimes_arrest_all.format(
                inst_name=inst_name,
                year=year,
                crime_table=table,
                location=location)).fetchall()

            resultSet.append(rows)

        else:
            #arrests/disc
            rows = db.cursor.execute(db_queries.university_crimes_arrest.format(
                inst_name=inst_name,
                year=year,
                crime_table=table,
                location=location)).fetchall()

            resultSet.append(rows)


    #print(row[1])
    #crime_data[row[1]] = row[0]
    #resultSet.append({"crime_table": table.title(), "crime_data": crime_data})
    # print('in resultSet')
    # print(resultSet)

    return resultSet

def get_university_names_like(query):
    institutes = []
    rows = db.cursor.execute(db_queries.university_names_like.format(
        query = query
    )).fetchall()
    # result is like list of tuples
    institutes = [i[0] for i in rows]
    print(f"total number of institutes: {len(institutes)}")
    institutes.sort()
    return institutes

 
