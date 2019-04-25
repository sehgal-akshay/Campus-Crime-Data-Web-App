

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


university_crimes_vawa_noYear = """
select Coalesce(sum(a.DOMESTIC_VIOLENCE),0) as sum_domestic, Coalesce(sum(a.DATING_VIOLENCE),0) as sum_dating, Coalesce(sum(a.STALKING),0) as sum_stalking from vawa a
inner join university i on i.univ_id = a.univ_id
where i.name = '{inst_name}' and a.Location = '{location}'
"""

university_crimes_hate_noYear = """
select Coalesce(sum(a.MURDER),0) as sum_murder, Coalesce(sum(a.RAPE),0) as total_rape, Coalesce(sum(a.FONDLING),0) as total_fondling, Coalesce(sum(a.INCEST),0) as total_incest,Coalesce(sum(a.STATUTORY_RAPE),0) as total_statutory_rape, 
Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson, Coalesce(sum(a.VANDALISM),0) as sum_vandalism, Coalesce(sum(a.INTIMIDATION),0) as sum_intimidation, 
Coalesce(sum(a.SIMPLE_ASSAULT),0) as sum_simple_assault, Coalesce(sum(a.LARCENY),0) as sum_larceny from hate a
inner join university i on i.univ_id = a.univ_id
where i.name = '{inst_name}' and a.location = '{location}'
"""
university_crimes_arrest_noYear = """
select Coalesce(sum(a.DRUGS),0) as sum_drugs, Coalesce(sum(a.WEAPONS), 0) as sum_weapons, Coalesce(sum(a.LIQUOR),0) as sum_liquor from UNIVERSITY u
inner join {crime_table} a on u.univ_id = a.univ_id
where u.name = '{inst_name}' and a.location = '{location}'
"""

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
Coalesce(sum(a.RAPE),0) as total_rape, Coalesce(sum(a.FONDLING),0) as total_fondling, Coalesce(sum(a.INCEST),0) as total_incest,Coalesce(sum(a.STATUTORY_RAPE),0) as total_statutory_rape,
Coalesce(sum(a.ROBBERY),0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS),0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY),0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT),0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON),0) as sum_arson
from criminal a
inner join university u on u.univ_id = a.univ_id
where u.name = '{inst_name}' and a.location = '{location}'"""

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
                                   "(select year, (MURDER + NEGLIGENT_MANSLAUGHTER + RAPE+FONDLING+INCEST+STATUTORY_RAPE+" \
                                   "ROBBERY+AGGRAVATED_ASSAULTS+BURGLARY+MOTOR_VEHICLE_THEFT+ARSON) " \
                                   "as CRIMINAL_OFFENCES from CRIMINAL C JOIN UNIVERSITY U on C.UNIV_ID = U.UNIV_ID " \
                                   "JOIN SECTOR S on U.SECTORID = S.ID {filter_condition}) group by YEAR"

all_hate_offences_year_group = "select YEAR, SUM(CRIMINAL_OFFENCES) from " \
                                   "(select year, (MURDER + RAPE+FONDLING+INCEST+STATUTORY_RAPE+" \
                                   "ROBBERY+AGGRAVATED_ASSAULTS+BURGLARY+MOTOR_VEHICLE_THEFT+ARSON+VANDALISM+INTIMIDATION+" \
                                   "SIMPLE_ASSAULT+LARCENY) " \
                                   "as CRIMINAL_OFFENCES from HATE C JOIN UNIVERSITY U on C.UNIV_ID = U.UNIV_ID " \
                                   "JOIN SECTOR S on U.SECTORID = S.ID {filter_condition}) group by  YEAR"

all_vawa_offences_year_group = "select YEAR, SUM(CRIMINAL_OFFENCES) from " \
                                   "(select year, (DOMESTIC_VIOLENCE+DATING_VIOLENCE+STALKING) " \
                                   "as CRIMINAL_OFFENCES from VAWA C JOIN UNIVERSITY U on C.UNIV_ID = U.UNIV_ID " \
                                   "JOIN SECTOR S on U.SECTORID = S.ID {filter_condition}) group by  YEAR"

all_da_year_group = "select YEAR, SUM(CRIMINAL_OFFENCES) from " \
                                   "(select year, (WEAPONS+DRUGS+LIQUOR) " \
                                   "as CRIMINAL_OFFENCES from DISCIPLINARY_ACTION D JOIN UNIVERSITY U on D.UNIV_ID = U.UNIV_ID " \
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
        from (select UNIVERSITY.NAME, SUM(MURDER + NEGLIGENT_MANSLAUGHTER + RAPE + FONDLING + INCEST + STATUTORY_RAPE
                                       + ROBBERY + AGGRAVATED_ASSAULTS 
                                        + BURGLARY + MOTOR_VEHICLE_THEFT + ARSON
                                        ) as criminal_count
                from criminal, UNIVERSITY where criminal.UNIV_ID = UNIVERSITY.UNIV_ID
                group by UNIVERSITY.name
            )
    )
where rownum <= 50"""

vawa_institute_rank = """
select *
from (select name, rank() over (order by vawa_count desc), vawa_count
        from (select university.NAME, SUM(DOMESTIC_VIOLENCE+DATING_VIOLENCE+STALKING) as vawa_count
                from vawa, university where vawa.UNIV_ID = UNIVERSITY.UNIV_ID
                group by university.name
            )
    )
where rownum <= 50
"""

disciplinary_institute_rank = """
select *
from (select name, rank() over (order by diciplinary_count desc), diciplinary_count
        from (select university.NAME, SUM(WEAPONS+DRUGS+LIQUOR) as diciplinary_count
                from disciplinary_action, university where disciplinary_action.UNIV_ID = university.UNIV_ID
                group by university.name
            )
    )
where rownum <= 50
"""

hate_institute_rank = """
select *
from (select name, rank() over (order by hate_count desc), hate_count
        from (select university.NAME, SUM(MURDER + RAPE + FONDLING + INCEST + STATUTORY_RAPE
                                        + ROBBERY + AGGRAVATED_ASSAULTS + BURGLARY
                                        + MOTOR_VEHICLE_THEFT + ARSON + VANDALISM
                                        + INTIMIDATION + SIMPLE_ASSAULT + LARCENY) as hate_count
                from hate, university where hate.UNIV_ID = university.UNIV_ID
                group by university.name
            )
    )
where rownum <= 50
"""

arrest_state_rank = """
select state, rank() over (order by arrest_count desc), arrest_count
        from (select UNIVERSITY.STATE, SUM(weapons + drugs + liquor) as arrest_count
                from arrest,UNIVERSITY where arrest.UNIV_ID = UNIVERSITY.UNIV_ID and state is not null
                group by UNIVERSITY.STATE
            )"""

crime_state_rank = """
select state, rank() over (order by count desc), count
        from (select UNIVERSITY.STATE, SUM(MURDER + NEGLIGENT_MANSLAUGHTER + RAPE + FONDLING + INCEST + STATUTORY_RAPE
                                        + ROBBERY + AGGRAVATED_ASSAULTS 
                                        + BURGLARY + MOTOR_VEHICLE_THEFT + ARSON) as count
                from criminal,UNIVERSITY where criminal.UNIV_ID = UNIVERSITY.UNIV_ID and state is not null
                group by UNIVERSITY.STATE
            )"""

vawa_state_rank = """
select state, rank() over (order by count desc), count
        from (select UNIVERSITY.STATE, SUM(DOMESTIC_VIOLENCE+DATING_VIOLENCE+STALKING) as count
                from vawa,UNIVERSITY where vawa.UNIV_ID = UNIVERSITY.UNIV_ID and state is not null
                group by UNIVERSITY.STATE
            )
"""

disciplinary_state_rank = """
select state, rank() over (order by count desc), count
        from (select UNIVERSITY.STATE, SUM(weapons + drugs + liquor) as count
                from disciplinary_action,UNIVERSITY where disciplinary_action.UNIV_ID = UNIVERSITY.UNIV_ID and state is not null
                group by UNIVERSITY.STATE
            )
"""

hate_state_rank = """
select state, rank() over (order by count desc), count
        from (select UNIVERSITY.STATE, SUM(MURDER + RAPE + FONDLING + INCEST + STATUTORY_RAPE
                                        + ROBBERY + AGGRAVATED_ASSAULTS + BURGLARY
                                        + MOTOR_VEHICLE_THEFT + ARSON + VANDALISM
                                        + INTIMIDATION + SIMPLE_ASSAULT + LARCENY) as count
                from hate,UNIVERSITY where hate.UNIV_ID = UNIVERSITY.UNIV_ID and state is not null
                group by UNIVERSITY.STATE
            )
"""

state_student_rank = """
select state, rank() over (order by student_count desc), student_count
from (select state, sum(TOTAL) as student_count
      from UNIVERSITY
      where state is not null
      group by state)"""

state_sector_rank = """
select state, rank() over (order by count desc), count
from (select state, count(*) as count
      from UNIVERSITY
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
Select riskfactor, total_incidents from (
select total_incidents, case
    when total_incidents < 50 then 'safe'
    when total_incidents between 50 and 100 then 'moderate'
    when total_incidents > 100 then 'high'
    end as riskfactor
    from(
select total_murder+total_negligent_manslaughter+total_rape+total_fondling+total_incest+total_statutory_rape+total_robbery+total_aggravated_assault+total_burglary+total_motor_vehicle_theft+
total_arson as total_incidents from(
select Coalesce(sum(c.MURDER)/3,0) as total_murder, Coalesce(sum(c.NEGLIGENT_MANSLAUGHTER)/3,0) as total_negligent_manslaughter, 
Coalesce(sum(c.RAPE)/3,0) as total_rape, Coalesce(sum(c.FONDLING)/3,0) as total_fondling, Coalesce(sum(c.INCEST)/3,0) as total_incest,Coalesce(sum(c.STATUTORY_RAPE)/3,0) as total_statutory_rape,
Coalesce(sum(c.ROBBERY)/3,0) as total_robbery, Coalesce(sum(c.AGGRAVATED_ASSAULTS)/3,0) as total_aggravated_assault,
Coalesce(sum(c.BURGLARY)/3,0) as total_burglary, Coalesce(sum(c.MOTOR_VEHICLE_THEFT)/3,0) as total_motor_vehicle_theft,
Coalesce(sum(c.ARSON)/3,0) as total_arson
from criminal c
inner join university u on u.univ_id = c.univ_id
where u.name = '{uni_name}')))
"""

university_vawa_avg = """
Select riskfactor, total_incidents from (
select total_incidents, case
    when total_incidents < 50 then 'safe'
    when total_incidents between 50 and 100 then 'moderate'
    when total_incidents > 100 then 'high'
    end as riskfactor
    from(
Select DOMESTIC_VIOLENCE+DATING_VIOLENCE+STALKING as total_incidents from(
select Coalesce(sum(v.DOMESTIC_VIOLENCE)/3,0) as DOMESTIC_VIOLENCE, Coalesce(sum(v.DATING_VIOLENCE)/3,0) as DATING_VIOLENCE, Coalesce(sum(v.STALKING)/3,0) as STALKING from vawa v
inner join university u on u.univ_id = v.univ_id
where u.name = '{uni_name}')))
"""

university_hate_avg = """
Select riskfactor, total_incidents from (
select total_incidents, case
    when total_incidents < 50 then 'safe'
    when total_incidents between 50 and 100 then 'moderate'
    when total_incidents > 100 then 'high'
    end as riskfactor
    from(
select sum_murder+total_rape+total_fondling+total_incest+total_statutory_rape+sum_robbery+sum_aggravated_assault+sum_burglary+sum_motor_vehicle_theft+
sum_arson+sum_vandalism+sum_intimidation+sum_simple_assault+sum_larceny as total_incidents from(  
select Coalesce(sum(a.MURDER)/3,0) as sum_murder, Coalesce(sum(a.RAPE)/3,0) as total_rape, Coalesce(sum(a.FONDLING)/3,0) as total_fondling, Coalesce(sum(a.INCEST)/3,0) as total_incest,
Coalesce(sum(a.STATUTORY_RAPE)/3,0) as total_statutory_rape, Coalesce(sum(a.ROBBERY)/3,0) as sum_robbery, Coalesce(sum(a.AGGRAVATED_ASSAULTS)/3,0) as sum_aggravated_assault,
Coalesce(sum(a.BURGLARY)/3,0) as sum_burglary, Coalesce(sum(a.MOTOR_VEHICLE_THEFT)/3,0) as sum_motor_vehicle_theft,
Coalesce(sum(a.ARSON)/3,0) as sum_arson, Coalesce(sum(a.VANDALISM)/3,0) as sum_vandalism, Coalesce(sum(a.INTIMIDATION)/3,0) as sum_intimidation, 
Coalesce(sum(a.SIMPLE_ASSAULT)/3,0) as sum_simple_assault, Coalesce(sum(a.LARCENY)/3,0) as sum_larceny from hate a
inner join university u on u.univ_id = a.univ_id
where u.name = '{uni_name}')))
"""


university_arrest_avg = """
Select riskfactor, total_incidents from (
select total_incidents, case
    when total_incidents < 50 then 'safe'
    when total_incidents between 50 and 100 then 'moderate'
    when total_incidents > 100 then 'high'
    end as riskfactor
    from(
select sum_drugs+sum_weapons+sum_liquor as total_incidents from(
select Coalesce(sum(a.DRUGS)/3,0) as sum_drugs, Coalesce(sum(a.WEAPONS)/3,0) as sum_weapons, Coalesce(sum(a.LIQUOR)/3,0) as sum_liquor from university i
inner join Arrest a on i.univ_id = a.univ_id
where i.name = '{uni_name}')))
"""

university_disciplinary_avg = """
Select riskfactor, total_incidents from (
select total_incidents, case
    when total_incidents < 50 then 'safe'
    when total_incidents between 50 and 100 then 'moderate'
    when total_incidents > 100 then 'high'
    end as riskfactor
    from(
select sum_drugs+sum_weapons+sum_liquor as total_incidents from(
select Coalesce(sum(a.DRUGS)/3,0) as sum_drugs, Coalesce(sum(a.WEAPONS)/3,0) as sum_weapons, Coalesce(sum(a.LIQUOR)/3,0) as sum_liquor from university i
inner join Disciplinary_action a on i.univ_id = a.univ_id
where i.name = '{uni_name}')))
"""

university_subcat_avg = """Select riskfactor, total_incidents from (
select total_incidents, case
    when total_incidents < 10 then 'safe'
    when total_incidents between 10 and 30 then 'moderate'
    when total_incidents > 30 then 'high'
    end as riskfactor
    from (select Coalesce(sum(t.{sub_cat})/3,0) as total_incidents from {table_name} t
inner join university u on u.univ_id = t.univ_id
where u.name = '{uni_name}'))
"""

university_avg = """Select riskfactor, total_incidents from (
select total_incidents, case
    when total_incidents < 100 then 'safe'
    when total_incidents between 100 and 300 then 'moderate'
    when total_incidents > 300 then 'high'
    end as riskfactor
    from(select sum(total) as total_incidents from (
(select (Coalesce(sum(c.MURDER)/3,0)+Coalesce(sum(c.NEGLIGENT_MANSLAUGHTER)/3,0)+
Coalesce(sum(c.RAPE)/3,0)+ Coalesce(sum(c.FONDLING)/3,0) + Coalesce(sum(c.INCEST)/3,0)+Coalesce(sum(c.STATUTORY_RAPE)/3,0) +
Coalesce(sum(c.ROBBERY)/3,0)+ Coalesce(sum(c.AGGRAVATED_ASSAULTS)/3,0)+
Coalesce(sum(c.BURGLARY)/3,0)+ Coalesce(sum(c.MOTOR_VEHICLE_THEFT)/3,0)+
Coalesce(sum(c.ARSON)/3,0)) as total
from criminal c
inner join university u on u.univ_id = c.univ_id
where u.name =  '{uni_name}') UNION ALL
(select (Coalesce(sum(v.DOMESTIC_VIOLENCE)/3,0)+Coalesce(sum(v.DATING_VIOLENCE)/3,0)
+Coalesce(sum(v.STALKING)/3,0)) as total from vawa v
inner join university u on u.univ_id = v.univ_id
where u.name =  '{uni_name}') UNION ALL
(select (Coalesce(sum(h.MURDER)/3,0)+Coalesce(sum(h.RAPE)/3,0) +
Coalesce(sum(h.FONDLING)/3,0) + Coalesce(sum(h.INCEST)/3,0) +
Coalesce(sum(h.STATUTORY_RAPE)/3,0) + Coalesce(sum(h.ROBBERY)/3,0) +
Coalesce(sum(h.AGGRAVATED_ASSAULTS)/3,0) +
Coalesce(sum(h.BURGLARY)/3,0)+ Coalesce(sum(h.MOTOR_VEHICLE_THEFT)/3,0) +
Coalesce(sum(h.ARSON)/3,0) + Coalesce(sum(h.VANDALISM)/3,0) + Coalesce(sum(h.INTIMIDATION)/3,0) +
Coalesce(sum(h.SIMPLE_ASSAULT)/3,0) + Coalesce(sum(h.LARCENY)/3,0)) as total from hate h
inner join university u on u.univ_id = h.univ_id
where u.name =  '{uni_name}') UNION ALL
(select (Coalesce(sum(ar.DRUGS)/3,0) + 
Coalesce(sum(ar.WEAPONS)/3,0) + Coalesce(sum(ar.LIQUOR)/3,0)) as total from university i
inner join arrest ar on i.univ_id = ar.univ_id
where i.name =  '{uni_name}') UNION ALL
(select (Coalesce(sum(dis.DRUGS)/3,0)+ Coalesce(sum(dis.WEAPONS)/3,0) 
+ Coalesce(sum(dis.LIQUOR)/3,0)) as total from university i
inner join disciplinary_action dis on i.univ_id = dis.univ_id
where i.name =  '{uni_name}'))))"""










