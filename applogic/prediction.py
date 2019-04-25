import db_connect as db
from applogic import  db_queries

def get_prediction_data_all(uni_name):
    rows = db.cursor.execute(db_queries.university_avg.format(    
    uni_name=uni_name
    )).fetchall()
    print(rows)
    return rows

def get_prediction_data_cat(uni_name, cat_type):
    if cat_type == 'Criminal':
        rows = db.cursor.execute(db_queries.university_criminal_avg.format(    
        uni_name=uni_name
        )).fetchall()

    elif cat_type == 'Arrest':
        rows = db.cursor.execute(db_queries.university_arrest_avg.format(
        uni_name=uni_name
        )).fetchall()

    elif cat_type == 'Vawa':
        rows = db.cursor.execute(db_queries.university_vawa_avg.format(
        uni_name=uni_name
        )).fetchall()

    elif cat_type == 'Hate':
        rows = db.cursor.execute(db_queries.university_hate_avg.format(
        uni_name=uni_name
        )).fetchall()

    elif cat_type == 'Disciplinary':
        rows = db.cursor.execute(db_queries.university_disciplinary_avg.format(
        uni_name=uni_name
        )).fetchall()
    print(rows)
    return rows

# def get_prediction_data_subcat(uni_name, cat_type, sub_cat):
#     if cat_type == 'Criminal':
#         rows = db.cursor.execute(db_queries.university_criminal_avg.format(    
#         uni_name=uni_name,
#         sub_cat=sub_cat
#         )).fetchall()

#     elif cat_type == 'Arrest':
#         rows = db.cursor.execute(db_queries.university_arrest_avg.format(
#         uni_name=uni_name,
#         sub_cat=sub_cat
#         )).fetchall()

#     elif cat_type == 'Vawa':
#         rows = db.cursor.execute(db_queries.university_vawa_avg.format(
#         uni_name=uni_name,
#         sub_cat=sub_cat
#         )).fetchall()

#     elif cat_type == 'Hate':
#         rows = db.cursor.execute(db_queries.university_hate_avg.format(
#         uni_name=uni_name,
#         sub_cat=sub_cat
#         )).fetchall()

#     elif cat_type == 'Disciplinary':
#         rows = db.cursor.execute(db_queries.university_disciplinary_avg.format(
#         uni_name=uni_name,
#         sub_cat=sub_cat
#         )).fetchall()
#     print(rows)
#     return rows

def get_prediction_data_subcat(uni_name, cat_type, sub_cat):
    if cat_type == 'Criminal':   
        rows = db.cursor.execute(db_queries.university_subcat_avg.format(    
        uni_name=uni_name,
        sub_cat=sub_cat,
        table_name='Criminal'
        )).fetchall()

    elif cat_type == 'Arrest':
        rows = db.cursor.execute(db_queries.university_subcat_avg.format(
        uni_name=uni_name,
        sub_cat=sub_cat,
        table_name='Arrest'
        )).fetchall()

    elif cat_type == 'Vawa':
        rows = db.cursor.execute(db_queries.university_subcat_avg.format(
        uni_name=uni_name,
        sub_cat=sub_cat,
        table_name='Vawa'
        )).fetchall()

    elif cat_type == 'Hate':
        rows = db.cursor.execute(db_queries.university_subcat_avg.format(
        uni_name=uni_name,
        sub_cat=sub_cat,
        table_name='Hate'
        )).fetchall()

    elif cat_type == 'Disciplinary':
        rows = db.cursor.execute(db_queries.university_subcat_avg.format(
        uni_name=uni_name,
        sub_cat=sub_cat,
        table_name='Disciplinary_Action'
        )).fetchall()
    print(rows)
    return rows
# def get_university_crime_avg():
#     rows = db.cursor.execute(db_queries.university_criminal_avg).fetchall()
#     print("test")
#     print(rows)
#     return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]

# def get_university_vawa_avg():
#     rows = db.cursor.execute(db_queries.university_vawa_avg).fetchall()
#     return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]

# def get_university_hate_avg():
#     rows = db.cursor.execute(db_queries.university_hate_avg).fetchall()
#     return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]

# def get_university_arrest_avg():
#     rows = db.cursor.execute(db_queries.university_arrest_avg).fetchall()
#     return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]

# def get_university_disciplinary_avg()():
#     rows = db.cursor.execute(db_queries.university_disciplinary_avg).fetchall()
#     return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]