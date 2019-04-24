import db_connect as db
from applogic import db_queries


def get_generic_pattern(category, subcategory, condition):
    print(db_queries.generic_year_group.format(
        sub_category_type = subcategory,
        category_type = category,
        filter_condition = condition
        )
    )
    output = db.cursor.execute(db_queries.generic_year_group.format(
        sub_category_type = subcategory,
        category_type = category,
        filter_condition = condition
    )
    ).fetchall()
    return output

def get_criminal_offences_pattern(condition):
    print(db_queries.all_criminal_offences_year_group.format(
        filter_condition=condition
    ))
    output = db.cursor.execute(db_queries.all_criminal_offences_year_group.format(
        filter_condition=condition
    )).fetchall()
    return output

def get_hate_pattern(condition):
    print(db_queries.all_hate_offences_year_group.format(
        filter_condition=condition
    ))
    output = db.cursor.execute(db_queries.all_hate_offences_year_group.format(
        filter_condition=condition
    )).fetchall()
    return output

def get_vawa_pattern(condition):
    print(db_queries.all_vawa_offences_year_group.format(
        filter_condition=condition
    ))
    output = db.cursor.execute(db_queries.all_vawa_offences_year_group.format(
        filter_condition=condition
    )).fetchall()
    return output

def get_arrest_pattern(condition):
    print(db_queries.all_criminal_offences_year_group.format(
        filter_condition=condition
    ))
    output = db.cursor.execute(db_queries.all_criminal_offences_year_group.format(
        filter_condition=condition
    )).fetchall()
    return output

def get_disciplinary_pattern(condition):
    print(db_queries.all_da_year_group.format(
        filter_condition=condition
    ))
    output = db.cursor.execute(db_queries.all_da_year_group.format(
        filter_condition=condition
    )).fetchall()
    return output

