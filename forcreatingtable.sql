
create table course
(
courseid int auto_increment primary key,
cname varchar(50) not null,
duration int,
fee float)

create table enquiry
(
enquiryid int auto_increment primary key,
firstname varchar(50) not null,
lastname varchar(50),
hno varchar(50),
street varchar(50),
city varchar(50),
pin varchar(6),
cell varchar(10) not null,
email varchar(50),
courseid int,
fee float,
duration int,
remarks varchar(200))



