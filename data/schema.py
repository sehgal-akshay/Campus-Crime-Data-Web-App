create table users(USERNAME VARCHAR2(30),EMAIL VARCHAR2(30),PASSWORD VARCHAR2(30))
create table sector(id number(2) primary key, type varchar2(40));

create table university(univ_id number(10) primary key, branch varchar2(90), name varchar2(92), city
varchar2(35), street_address varchar2(105), state varchar2(4), zip varchar2(15), sectorID
number(2), constraint
fk_sectorp foreign key (sectorID) references sector(id));

create table location (id number(2), name varchar2(20) primary key);

create table criminal (
murder number(4),
negligent_manslaughter number(4),
rape number(4),
fondling number(4),
incest number(4),
statutory_rape number(4),
robbery number(4),
aggravated_assaults number(4),
burglary number(4),
motor_vehicle_theft number(4),
arson number(4),
univ_id number(10),
location varchar2(20),
year number(4),
primary key (univ_id, location, year),
constraint fk_criminal_institute foreign key (univ_id) references university(univ_id),
constraint fk_criminal_location foreign key (location) references location(name)
);

create table arrest(weapons number(4), drugs number(4), liquor number(4), univ_id
number(10), location varchar2(20), year number(4), primary key (univ_id, location, year),
constraint fk_arrest_institute foreign key (univ_id) references university(univ_id), constraint
fk_arrest_location foreign key (location) references location(name));

create table disciplinary_action(weapons number(4), drugs number(4), liquor number(4),
univ_id number(10), location varchar2(20), year number(4), primary key (univ_id,
location, year), constraint fk_discip_act_institute foreign key (univ_id) references
university(univ_id), constraint fk_discip_act_location foreign key (location) references
location(name));

create table vawa (domestic_violence number(4), dating_violence number(4), stalking
number(4), univ_id number(10), location varchar2(20), year number(4), primary key
(univ_id, location, year), constraint fk_vawa_institute foreign key (univ_id) references
university(univ_id), constraint fk_vawa_location foreign key (location) references location(name));

create table bias(id number(2) primary key, type varchar2(20));

create table hate (murder number(4), rape number(4),
fondling number(4),
incest number(4),
statutory_rape number(4),
robbery number(4), aggravated_assaults number(4), burglary number(4), motor_vehicle_theft
number(4), arson number(4), vandalism number(4), intimidation number(4), simple_assault
number(4), larceny number(4), univ_id number(10), location varchar2(20), year number(4),
bias_id number(2), primary key (univ_id, location, year, bias_id), constraint
fk_hate_bias foreign key (bias_id) references bias(id), constraint fk_hate_institute foreign
key (univ_id) references university(univ_id), constraint fk_hate_location foreign key (location)
references location(name));

insert into sector values(1,'Public, 4-year or above');
insert into sector values(2, 'Private non-profit, 4-year or above');
insert into sector values(3, 'Private for-profit , 4-year or above');
insert into sector values(4, 'Public, 2-year');
insert into sector values(5, 'Private non-profit, 2-year');
insert into sector values(6, 'Private for-profit, 2-year');
insert into sector values(7, 'Public, less-than-2-year');
insert into sector values(8, 'Private non-profit, less-than-2-year');
insert into sector values(9, 'Private for-profit, less-than-2-year');
commit;
insert into location values(1, 'noncampus');
insert into location values(2, 'oncampus');
insert into location values(3, 'publicproperty');
insert into location values(4, 'residencehall');
commit;

