

"insert into users values ({username}, {email}, {password})"

all_university_names = "select distinct(name) from university"

all_sector_ids = "select distinct(id) from sector"

validate_login = """Select * from users where email='{email}' and password='{password}'"""

total_tuple_count = """
select *
from (select (
              (select count(*) from arrest)
              + (select count(*) from bias)
              + (select count(*) from criminal)
              + (select count(*) from DISCIPLINARY_ACTION)
              + (select count(*) from hate)
              + (select count(*) from university)
              + (select count(*) from location)
              + (select count(*) from sector)
              + (select count(*) from vawa)
              ) as total_count
      from bias)
where rownum = 1"""

university_names_like = "select distinct(name) from university where lower(name) like '%' || lower('{query}') || '%'"

#coalesce function in SQL
university_crimes_criminal_all = """
select Coalesce(sum(c.MURDER),0) as total_murder, Coalesce(sum(c.NEGLIGENT_MANSLAUGHTER),0) as total_negligent_manslaughter, 
Coalesce(sum(c.RAPE),0) as total_rape, Coalesce(sum(c.FONDLING),0) as total_fondling, Coalesce(sum(c.INCEST),0) as total_incest,Coalesce(sum(c.STATUTORY_RAPE),0) as total_statutory_rape,
Coalesce(sum(c.ROBBERY),0) as total_robbery, Coalesce(sum(c.AGGRAVATED_ASSAULTS),0) as total_aggravated_assault,
Coalesce(sum(c.BURGLARY),0) as total_burglary, Coalesce(sum(c.MOTOR_VEHICLE_THEFT),0) as total_motor_vehicle_theft,
Coalesce(sum(c.ARSON),0) as total_arson
from criminal c
inner join university u on u.univ_id = c.univ_id
where u.name = '{inst_name}'"""

university_crimes_vawa_all = """
select Coalesce(sum(v.DOMESTIC_VIOLENCE),0) as DOMESTIC_VIOLENCE, Coalesce(sum(v.DATING_VIOLENCE),0) as DATING_VIOLENCE, Coalesce(sum(v.STALKING),0) as STALKING from vawa v
inner join university u on u.univ_id = v.univ_id
where u.name = '{inst_name}'
"""

university_crimes_hate_all = """
select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(c.RAPE),0) as total_rape, Coalesce(sum(c.FONDLING),0) as total_fondling, Coalesce(sum(c.INCEST),0) as total_incest,
Coalesce(sum(c.STATUTORY_RAPE),0) as total_statutory_rape, Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson, Coalesce(sum(a.VANDALISM),0) as sum_vandalism, Coalesce(sum(a.INTIMIDATION),0) as sum_intimidation, 
Coalesce(sum(a.SIMPLE_ASSAULT),0) as sum_simple_assault, Coalesce(sum(a.LARCENY),0) as sum_larceny from hate a
inner join university u on u.univ_id = a.univ_id
where u.name = '{inst_name}'
"""

university_crimes_criminal_noLoc = """
select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(a.NEGLIGENT_MANSLAUGHTER),0) as sum_negligent_manslaughter, 
Coalesce(sum(c.RAPE),0) as total_rape, Coalesce(sum(c.FONDLING),0) as total_fondling, Coalesce(sum(c.INCEST),0) as total_incest,Coalesce(sum(c.STATUTORY_RAPE),0) as total_statutory_rape,
Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson
from criminal a
inner join university i on i.id = a.instituteid
where i.name = '{inst_name}' and a.year = '{year}'"""

university_crimes_vawa_noLoc = """
select Coalesce(sum(a.DOMESTIC_VIOLENCE),0) as sum_domestic, Coalesce(sum(a.DATING_VIOLENCE),0) as sum_dating, Coalesce(sum(a.STALKING),0) as sum_stalking from vawa a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.year = {year}
"""

university_crimes_hate_noLoc = """
select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(c.RAPE),0) as total_rape, Coalesce(sum(c.FONDLING),0) as total_fondling, Coalesce(sum(c.INCEST),0) as total_incest,Coalesce(sum(c.STATUTORY_RAPE),0) as total_statutory_rape,
Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson, Coalesce(sum(a.VANDALISM),0) as sum_vandalism, Coalesce(sum(a.INTIMIDATION),0) as sum_intimidation, 
Coalesce(sum(a.SIMPLE_ASSAULT),0) as sum_simple_assault, Coalesce(sum(a.LARCENY),0) as sum_larceny from hate a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.year = {year}
"""

# university_crimes_criminal_all = """
# select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(a.NEGLIGENT_MANSLAUGHTER),0) as sum_negligent_manslaughter, 
# Coalesce(sum(a.FORCIBLE_SEX),0) as sum_forcible_sex,  Coalesce(sum(a.NONFORCIBLE_SEX),0) as sum_nonforcible_sex, 
# Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
# Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
# Coalesce(sum(a.ARSON),0) as sum_arson
# from criminal a
# inner join institute i on i.id = a.instituteid
# where i.name = '{inst_name}'"""

# university_crimes_vawa_all = """
# select Coalesce(sum(a.DOMESTIC_VIOLENCE),0) as DOMESTIC_VIOLENCE, Coalesce(sum(a.DATING_VIOLENCE),0) as DATING_VIOLENCE, Coalesce(sum(a.STALKING),0) as STALKING from vawa a
# inner join institute i on i.id = a.instituteid
# where i.name = '{inst_name}'
# """

university_crimes_hate_all = """
select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(a.RAPE),0) as total_rape, Coalesce(sum(a.FONDLING),0) as total_fondling, Coalesce(sum(a.INCEST),0) as total_incest,Coalesce(sum(a.STATUTORY_RAPE),0) as total_statutory_rape,
Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson, Coalesce(sum(a.VANDALISM),0) as sum_vandalism, Coalesce(sum(a.INTIMIDATION),0) as sum_intimidation, 
Coalesce(sum(a.SIMPLE_ASSAULT),0) as sum_simple_assault, Coalesce(sum(a.LARCENY),0) as sum_larceny from hate a
inner join university u on u.univ_id = a.univ_id
where u.name = '{inst_name}'
"""

university_crimes_criminal_noYear = """
select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(a.NEGLIGENT_MANSLAUGHTER),0) as sum_negligent_manslaughter, 
Coalesce(sum(c.RAPE),0) as total_rape, Coalesce(sum(c.FONDLING),0) as total_fondling, Coalesce(sum(c.INCEST),0) as total_incest,Coalesce(sum(c.STATUTORY_RAPE),0) as total_statutory_rape,
Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson
from criminal a
inner join institute i on i.id = a.instituteid
where i.name = '{inst_name}' and a.location = '{location}'"""

university_crimes_arrest_all = """
select Coalesce(sum(a.DRUGS),0) as sum_drugs, Coalesce(sum(a.WEAPONS),0) as sum_weapons, Coalesce(sum(a.LIQUOR),0) as sum_liquor from university i
inner join {crime_table} a on i.univ_id = a.univ_id
where i.name = '{inst_name}'
"""

##Queries from annual_pattern.py

generic_year_group = "select year,sum({sub_category_type}) from" \
                     "(select * from {category_type} C JOIN UNIVERSITY U on C.UNIV_ID = U.UNIV_ID " \
                     "JOIN SECTOR S on U.SECTORID = S.ID" \
                     " {filter_condition}) group by YEAR"

all_criminal_offences_year_group = "select YEAR, SUM(CRIMINAL_OFFENCES) from " \
                                   "(select year, (MURDER + NEGLIGENT_MANSLAUGHTER + FORCIBLE_SEX+NONFORCIBLE_SEX+" \
                                   "ROBBERY+AGGRAVATED_ASSAULTS+BURGLARY+MOTOR_VEHICLE_THEFT+ARSON) " \
                                   "as CRIMINAL_OFFENCES from CRIMINAL C JOIN UNIVERSITY U on C.UNIV_ID = U.UNIV_ID " \
                                   "JOIN SECTOR S on U.SECTORID = S.ID {filter_condition}) group by YEAR"

all_hate_offences_year_group = "select YEAR, SUM(CRIMINAL_OFFENCES) from " \
                                   "(select year, (MURDER + FORCIBLE_SEX+NONFORCIBLE_SEX+" \
                                   "ROBBERY+AGGRAVATED_ASSAULTS+BURGLARY+MOTOR_VEHICLE_THEFT+ARSON+VANDALISM+INTIMIDATION+" \
                                   "SIMPLE_ASSAULT+LARCENY) " \
                                   "as CRIMINAL_OFFENCES from HATE C JOIN UNIVERSITY U on C.UNIV_ID = U.UNIV_ID " \
                                   "JOIN SECTOR S on U.SECTORID = S.ID {filter_condition}) group by  YEAR"

all_vawa_offences_year_group = "select YEAR, SUM(CRIMINAL_OFFENCES) from " \
                                   "(select year, (DOMESTIC_VIOLENCE+DATING_VIOLENCE+STALKING) " \
                                   "as CRIMINAL_OFFENCES from VAWA C JOIN UNIVERSITY U on C.UNIV_ID = UNIV_.ID " \
                                   "JOIN SECTOR S on U.SECTORID = S.ID {filter_condition}) group by  YEAR"

#Queries from compare_uni.py
compare_university_arrest = """select sum(WEAPONS), sum(DRUGS), sum(LIQUOR) 
                                          from arrest, (select univ_id from university where name = '{uni_name}') u 
                                          where arrest.univ_id = u.univ_id and arrest.year = {year}"""

compare_university_disc_action = """select sum(WEAPONS), sum(DRUGS), sum(LIQUOR) 
                                          from disciplinary_action, (select univ_id from university where name = '{uni_name}') u 
                                          where disciplinary_action.univ_id = u.univ_id and disciplinary_action.year = {year}"""

compare_university_criminal = """select sum(MURDER), sum(NEGLIGENT_MANSLAUGHTER),sum(RAPE),sum(FONDLING), sum(INCEST),
                                          sum(STATUTORY_RAPE), sum(ROBBERY), sum(AGGRAVATED_ASSAULTS),
                                          sum(BURGLARY), sum(MOTOR_VEHICLE_THEFT), sum(ARSON)
                                          from criminal, (select univ_id from university where name = '{uni_name}') u 
                                          where criminal.univ_id = u.univ_id and criminal.year = {year}"""


compare_university_vawa = """select sum(DOMESTIC_VIOLENCE), sum(DATING_VIOLENCE), sum(STALKING) 
                                          from vawa, (select univ_id from university where name = '{uni_name}') u 
                                          where vawa.univ_id = u.univ_id and vawa.year = {year}"""

compare_university_hate = """select sum(MURDER), sum(VANDALISM), sum(RAPE),sum(FONDLING), sum(INCEST),
                                          sum(STATUTORY_RAPE), sum(ROBBERY), sum(AGGRAVATED_ASSAULTS),
                                          sum(BURGLARY), sum(MOTOR_VEHICLE_THEFT), sum(ARSON),
                                          sum(INTIMIDATION), sum(SIMPLE_ASSAULT), sum(LARCENY)
                                          from hate, (select univ_id from university where name = '{uni_name}') u
                                          where hate.univ_id = u.univ_id and hate.year = {year}"""


#from ranking.py
arrest_university_rank = """
select *
from (select name, rank() over (order by arrest_count desc), arrest_count
        from (select university.NAME, SUM(weapons + drugs + liquor) as arrest_count
                from arrest,university where arrest.univ_id = university.univ_id
                group by university.name
            )
    )
where rownum <= 50"""

criminal_institute_rank = """
select *
from (select name, rank() over (order by criminal_count desc), criminal_count
        from (select institute.NAME, SUM(MURDER + NEGLIGENT_MANSLAUGHTER + FORCIBLE_SEX
                                        + NONFORCIBLE_SEX + ROBBERY + AGGRAVATED_ASSAULTS 
                                        + BURGLARY + MOTOR_VEHICLE_THEFT + ARSON
                                        ) as criminal_count
                from criminal, institute where criminal.INSTITUTEID = institute.ID
                group by institute.name
            )
    )
where rownum <= 50"""

vawa_institute_rank = """
select *
from (select name, rank() over (order by vawa_count desc), vawa_count
        from (select institute.NAME, SUM(DOMESTIC_VIOLENCE+DATING_VIOLENCE+STALKING) as vawa_count
                from vawa, institute where vawa.INSTITUTEID = institute.ID
                group by institute.name
            )
    )
where rownum <= 50
"""

disciplinary_institute_rank = """
select *
from (select name, rank() over (order by diciplinary_count desc), diciplinary_count
        from (select institute.NAME, SUM(WEAPONS+DRUGS+LIQUOR) as diciplinary_count
                from disciplinary_action, institute where disciplinary_action.INSTITUTEID = institute.ID
                group by institute.name
            )
    )
where rownum <= 50
"""

hate_institute_rank = """
select *
from (select name, rank() over (order by hate_count desc), hate_count
        from (select institute.NAME, SUM(MURDER + FORCIBLE_SEX + NONFORCIBLE_SEX
                                        + ROBBERY + AGGRAVATED_ASSAULTS + BURGLARY
                                        + MOTOR_VEHICLE_THEFT + ARSON + VANDALISM
                                        + INTIMIDATION + SIMPLE_ASSAULT + LARCENY) as hate_count
                from hate, institute where hate.INSTITUTEID = institute.ID
                group by institute.name
            )
    )
where rownum <= 50
"""

categorize_arrest_institute_rank = """
select *
from (select name, rank() over (order by count desc), count 
    from (select name, student_count, count, case
            when student_count > 30000 then 'huge'
            when student_count between 15000 and 30000 then 'large'
            when student_count between 5000 and 14999 then 'medium'
            when student_count < 5000 then 'small'
        end as category
    from (select institute.NAME, SUM(weapons + drugs + liquor) as count,
                  sum(TOTAL) as student_count
          from arrest, institute
          where arrest.INSTITUTEID = institute.ID
          group by institute.name) categorized_institutes)
    where category = '{category}')
where rownum <= 50"""

categorize_crime_institute_rank = """
select *
from (select name, rank() over (order by count desc), count 
    from (select name, student_count, count, case
            when student_count > 30000 then 'huge'
            when student_count between 15000 and 30000 then 'large'
            when student_count between 5000 and 14999 then 'medium'
            when student_count < 5000 then 'small'
        end as category
    from (select institute.NAME, SUM(MURDER + NEGLIGENT_MANSLAUGHTER + FORCIBLE_SEX
                                    + NONFORCIBLE_SEX + ROBBERY + AGGRAVATED_ASSAULTS 
                                    + BURGLARY + MOTOR_VEHICLE_THEFT + ARSON) as count,
                  sum(TOTAL) as student_count
          from criminal, institute
          where criminal.INSTITUTEID = institute.ID
          group by institute.name) categorized_institutes)
    where category = '{category}')
where rownum <= 50"""

categorize_vawa_institute_rank = """
select *
from (select name, rank() over (order by count desc), count 
    from (select name, student_count, count, case
            when student_count > 30000 then 'huge'
            when student_count between 15000 and 30000 then 'large'
            when student_count between 5000 and 14999 then 'medium'
            when student_count < 5000 then 'small'
        end as category
    from (select institute.NAME, SUM(DOMESTIC_VIOLENCE+DATING_VIOLENCE+STALKING) as count,
                  sum(TOTAL) as student_count
          from vawa, institute
          where vawa.INSTITUTEID = institute.ID
          group by institute.name) categorized_institutes)
    where category = '{category}')
where rownum <= 50"""

categorize_disciplinary_institute_rank = """
select *
from (select name, rank() over (order by count desc), count 
    from (select name, student_count, count, case
            when student_count > 30000 then 'huge'
            when student_count between 15000 and 30000 then 'large'
            when student_count between 5000 and 14999 then 'medium'
            when student_count < 5000 then 'small'
        end as category
    from (select institute.NAME, SUM(WEAPONS+DRUGS+LIQUOR) as count,
                  sum(TOTAL) as student_count
          from disciplinary_action, institute
          where disciplinary_action.INSTITUTEID = institute.ID
          group by institute.name) categorized_institutes)
    where category = '{category}')
where rownum <= 50"""

categorize_hate_institute_rank = """
select *
from (select name, rank() over (order by count desc), count 
    from (select name, student_count, count, case
            when student_count > 30000 then 'huge'
            when student_count between 15000 and 30000 then 'large'
            when student_count between 5000 and 14999 then 'medium'
            when student_count < 5000 then 'small'
        end as category
    from (select institute.NAME, SUM(MURDER + FORCIBLE_SEX + NONFORCIBLE_SEX
                                            + ROBBERY + AGGRAVATED_ASSAULTS + BURGLARY
                                            + MOTOR_VEHICLE_THEFT + ARSON + VANDALISM
                                            + INTIMIDATION + SIMPLE_ASSAULT + LARCENY) as count,
                  sum(TOTAL) as student_count
                    from hate, institute where hate.INSTITUTEID = institute.ID
                    group by institute.name) categorized_institutes)
    where category = '{category}')
where rownum <= 50
"""

arrest_state_rank = """
select state, rank() over (order by arrest_count desc), arrest_count
        from (select institute.STATE, SUM(weapons + drugs + liquor) as arrest_count
                from arrest,institute where arrest.INSTITUTEID = institute.ID and state is not null
                group by institute.STATE
            )"""

crime_state_rank = """
select state, rank() over (order by count desc), count
        from (select institute.STATE, SUM(MURDER + NEGLIGENT_MANSLAUGHTER + FORCIBLE_SEX
                                        + NONFORCIBLE_SEX + ROBBERY + AGGRAVATED_ASSAULTS 
                                        + BURGLARY + MOTOR_VEHICLE_THEFT + ARSON) as count
                from criminal,institute where criminal.INSTITUTEID = institute.ID and state is not null
                group by institute.STATE
            )"""

vawa_state_rank = """
select state, rank() over (order by count desc), count
        from (select institute.STATE, SUM(DOMESTIC_VIOLENCE+DATING_VIOLENCE+STALKING) as count
                from vawa,institute where vawa.INSTITUTEID = institute.ID and state is not null
                group by institute.STATE
            )
"""

disciplinary_state_rank = """
select state, rank() over (order by count desc), count
        from (select institute.STATE, SUM(weapons + drugs + liquor) as count
                from disciplinary_action,institute where disciplinary_action.INSTITUTEID = institute.ID and state is not null
                group by institute.STATE
            )
"""

hate_state_rank = """
select state, rank() over (order by count desc), count
        from (select institute.STATE, SUM(MURDER + FORCIBLE_SEX + NONFORCIBLE_SEX
                                        + ROBBERY + AGGRAVATED_ASSAULTS + BURGLARY
                                        + MOTOR_VEHICLE_THEFT + ARSON + VANDALISM
                                        + INTIMIDATION + SIMPLE_ASSAULT + LARCENY) as count
                from hate,institute where hate.INSTITUTEID = institute.ID and state is not null
                group by institute.STATE
            )
"""

state_student_rank = """
select state, rank() over (order by student_count desc), student_count
from (select state, sum(TOTAL) as student_count
      from institute
      where state is not null
      group by state)"""

state_sector_rank = """
select state, rank() over (order by count desc), count
from (select state, count(*) as count
      from institute
      where state is not null and sectorid in ({sector})
      group by state)
"""



# from tuple count
tuple_count = """
select count(*) from {table}"""

#from ranking.py
university_rank_arrest = """
select *
from (select name, rank() over (order by arrest_count desc), arrest_count
       from (select university.name, SUM(weapons + drugs + liquor) as arrest_count
       from arrest,university where arrest.univ_id = university.univ_id
       group by university.name
            )
    )
where rownum <= 50"""

university_rank_criminal = """
select *
from (select name, rank() over (order by criminal_count desc), criminal_count
        from (select university.NAME, SUM(MURDER + NEGLIGENT_MANSLAUGHTER + RAPE + INCEST + FONDLING + STATUTORY_RAPE 
              + ROBBERY + AGGRAVATED_ASSAULTS 
                   + BURGLARY + MOTOR_VEHICLE_THEFT + ARSON
                   ) as criminal_count
                     from criminal, university where criminal.univ_id = university.univ_id
                     group by university.name
            )
    )
where rownum <= 50"""

university_rank_vawa = """
select *
from (select name, rank() over (order by vawa_count desc), vawa_count
       from (select university.NAME, SUM(DOMESTIC_VIOLENCE+DATING_VIOLENCE+STALKING) as vawa_count
       from vawa, university where vawa.univ_id = university.univ_id
       group by university.name
            )
    )
where rownum <= 50
"""

university_rank_disciplinary = """
select *
from (select name, rank() over (order by diciplinary_count desc), diciplinary_count
        from (select university.name, SUM(WEAPONS+DRUGS+LIQUOR) as diciplinary_count
                from disciplinary_action, university where disciplinary_action.univ_id = university.univ_id
                group by university.name
            )
    )
where rownum <= 50
"""

university_rank_hate = """
select *
from (select name, rank() over (order by hate_count desc), hate_count
        from (select university.NAME, SUM(MURDER + RAPE + INCEST + FONDLING + STATUTORY_RAPE
                                        + ROBBERY + AGGRAVATED_ASSAULTS + BURGLARY
                                        + MOTOR_VEHICLE_THEFT + ARSON + VANDALISM
                                        + INTIMIDATION + SIMPLE_ASSAULT + LARCENY) as hate_count
                from hate, university where hate.univ_id = university.univ_id
                group by university.name
            )
    )
where rownum <= 50
"""

#from prediction.py
university_criminal_avg = """
select Coalesce(sum(c.MURDER)/3,0) as total_murder, Coalesce(sum(c.NEGLIGENT_MANSLAUGHTER)/3,0) as total_negligent_manslaughter, 
Coalesce(sum(c.RAPE)/3,0) as total_rape, Coalesce(sum(c.FONDLING)/3,0) as total_fondling, Coalesce(sum(c.INCEST)/3,0) as total_incest,Coalesce(sum(c.STATUTORY_RAPE)/3,0) as total_statutory_rape,
Coalesce(sum(c.ROBBERY)/3,0) as total_robbery, Coalesce(sum(c.AGGRAVATED_ASSAULTS)/3,0) as total_aggravated_assault,
Coalesce(sum(c.BURGLARY)/3,0) as total_burglary, Coalesce(sum(c.MOTOR_VEHICLE_THEFT)/3,0) as total_motor_vehicle_theft,
Coalesce(sum(c.ARSON)/3,0) as total_arson
from criminal c
inner join university u on u.univ_id = c.univ_id
where u.name = '{uni_name}'"""

university_vawa_avg = """
select Coalesce(sum(v.DOMESTIC_VIOLENCE)/3,0) as DOMESTIC_VIOLENCE, Coalesce(sum(v.DATING_VIOLENCE)/3,0) as DATING_VIOLENCE, Coalesce(sum(v.STALKING)/3,0) as STALKING from vawa v
inner join university u on u.univ_id = v.univ_id
where u.name = '{uni_name}'
"""

university_hate_avg = """
select Coalesce(sum(a.MURDER)/3,0) as sum_murder, Coalesce(sum(c.RAPE)/3,0) as total_rape, Coalesce(sum(c.FONDLING)/3,0) as total_fondling, Coalesce(sum(c.INCEST)/3,0) as total_incest,
Coalesce(sum(c.STATUTORY_RAPE)/3,0) as total_statutory_rape, Coalesce(sum(a.ROBBERY)/3,0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS)/3,0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY)/3,0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT)/3,0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON)/3,0) as sum_arson, Coalesce(sum(a.VANDALISM)/3,0) as sum_vandalism, Coalesce(sum(a.INTIMIDATION)/3,0) as sum_intimidation, 
Coalesce(sum(a.SIMPLE_ASSAULT)/3,0) as sum_simple_assault, Coalesce(sum(a.LARCENY)/3,0) as sum_larceny from hate a
inner join university u on u.univ_id = a.univ_id
where u.name = '{uni_name}'
"""


university_arrest_avg = """
select Coalesce(sum(a.DRUGS)/3,0) as sum_drugs, Coalesce(sum(a.WEAPONS)/3,0) as sum_weapons, Coalesce(sum(a.LIQUOR)/3,0) as sum_liquor from university i
inner join Arrest a on i.univ_id = a.univ_id
where i.name = '{uni_name}'
"""

niversity_disciplinary_avg = """
select Coalesce(sum(a.DRUGS)/3,0) as sum_drugs, Coalesce(sum(a.WEAPONS)/3,0) as sum_weapons, Coalesce(sum(a.LIQUOR)/3,0) as sum_liquor from university i
inner join Disciplinary_action a on i.univ_id = a.univ_id
where i.name = '{uni_name}'
"""









