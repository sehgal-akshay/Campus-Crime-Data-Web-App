import db_connect as db
from applogic import  db_queries

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

#University Ranks based on category
def get_arrest_university_ranks():
    rows = db.cursor.execute(db_queries.arrest_university_rank).fetchall()
    return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]

def get_crime_university_ranks():
    rows = db.cursor.execute(db_queries.university_rank_criminal).fetchall()
    return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]

def get_disciplinary_university_ranks():
    rows = db.cursor.execute(db_queries.university_rank_disciplinary).fetchall()
    return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]

def get_vawa_university_ranks():
    rows = db.cursor.execute(db_queries.university_rank_vawa).fetchall()
    return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]

def get_hate_university_ranks():
    rows = db.cursor.execute(db_queries.university_rank_hate).fetchall()
    return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]
#---------------------------------------------------------------------------------------------------------------

def get_arrest_state_ranks():
    print(db_queries.arrest_state_rank)
    rows = db.cursor.execute(db_queries.arrest_state_rank).fetchall()
    return [{"element": states[row[0]], "rank": row[1], "count": row[2]}for row in rows if states.get(row[0])]

def get_crime_state_ranks():
    print(db_queries.crime_state_rank)
    rows = db.cursor.execute(db_queries.crime_state_rank).fetchall()
    return [{"element": states[row[0]], "rank": row[1], "count": row[2]}for row in rows if states.get(row[0])]

def get_vawa_state_ranks():
    print(db_queries.vawa_state_rank)
    rows = db.cursor.execute(db_queries.vawa_state_rank).fetchall()
    return [{"element": states[row[0]], "rank": row[1], "count": row[2]}for row in rows if states.get(row[0])]

def get_disciplinary_state_ranks():
    print(db_queries.disciplinary_state_rank)
    rows = db.cursor.execute(db_queries.disciplinary_state_rank).fetchall()
    return [{"element": states[row[0]], "rank": row[1], "count": row[2]}for row in rows if states.get(row[0])]

def get_hate_state_ranks():
    print(db_queries.hate_state_rank)
    rows = db.cursor.execute(db_queries.hate_state_rank).fetchall()
    return [{"element": states[row[0]], "rank": row[1], "count": row[2]}for row in rows if states.get(row[0])]

def get_categorize_arrest_institute_ranks(category):
    print(f"query: {db_queries.categorize_arrest_institute_rank.format(category=category)}")
    rows = db.cursor.execute(db_queries.categorize_arrest_institute_rank.format(category=category)).fetchall()
    return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]

def get_categorize_crime_institute_ranks(category):
    print(f"query: {db_queries.categorize_crime_institute_rank.format(category=category)}")
    rows = db.cursor.execute(db_queries.categorize_crime_institute_rank.format(category=category)).fetchall()
    return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]

def get_categorize_vawa_institute_ranks(category):
    print(f"query: {db_queries.categorize_vawa_institute_rank.format(category=category)}")
    rows = db.cursor.execute(db_queries.categorize_vawa_institute_rank.format(category=category)).fetchall()
    return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]

def get_categorize_hate_institute_ranks(category):
    print(f"query: {db_queries.categorize_hate_institute_rank.format(category=category)}")
    rows = db.cursor.execute(db_queries.categorize_hate_institute_rank.format(category=category)).fetchall()
    return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]

def get_categorize_disciplinary_institute_ranks(category):
    print(f"query: {db_queries.categorize_disciplinary_institute_rank.format(category=category)}")
    rows = db.cursor.execute(db_queries.categorize_disciplinary_institute_rank.format(category=category)).fetchall()
    return [{"element": row[0], "rank": row[1], "count": row[2]}for row in rows]
