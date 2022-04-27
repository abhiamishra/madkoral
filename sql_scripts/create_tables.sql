create database themepark;

use themepark;

create table Department(
	DeptID int not null auto_increment,
    DeptType varchar(300),
    Supervisor int,
    primary key(DeptID)
);

create table Rides_Dept(
	deptID int not null auto_increment,
    showID int,
    attractionName varchar(300),
    skill_lvl int,
    primary key(deptID)
);

create table Security(
	deptID int not null auto_increment,
    physicalIndex int,
    primary key(deptID)
);

create table Leisure(
	deptID int not null auto_increment,
    hosp_index int,
    primary key(deptID)
);

create table Administration(
	deptID int not null auto_increment,
    WPM int,
    primary key(deptID)
);

-- show is a reserved word -- renamed to shows
create table Shows(
	showID int not null auto_increment,
    title varchar(150),
    park varchar(300),
    openHour int,
    closeHour int,
    duration int,
    primary key(showID)
);

create table Destination(
	destID int not null auto_increment,
    managerID int,
    destName varchar(300),
    destType varchar(300),
    parkOwned boolean,
	primary key(destID)
);

create table Attraction(
	attractionName varchar(300) not null,
    duration int,
    passType varchar(50),
    rideType varchar(100),
    openHour int,
    closeHour int,
    primary key(attractionName)
);

create table Employee(
	EMPID int not null auto_increment,
    SSN bigint not null,
    division varchar(50),
    fname varchar(50) not null,
    lname varchar(50) not null,
    type varchar(20),
    age int,
    phoneNo bigint,
    hours int,
    EmpDept int,
    primary key(EMPID)
);

create table Guest(
	GID int not null auto_increment,
    credCard bigint,
    address varchar(100),
    passType varchar(50),
    fname varchar(50) not null,
    lname varchar(50) not null,
    age int,
    phoneNo bigint,
    primary key(GID)
);

create table Child(
	CID int not null auto_increment,
    GID int not null,
    relationship varchar(100),
    fname varchar(50) not null,
    lname varchar(50) not null,
    type varchar(20),
    age int,
    gender varchar(1),
    primary key(CID,GID)
);

create table works_in(
	work_destID int,
    work_deptID int,
    primary key(work_destID, work_deptID)
);

create table watches(
	watches_showID int,
    watches_GID int,
    primary key(watches_showID, watches_GID)
);

create table visits(
	visits_destID int,
    visits_GID int,
    primary key(visits_destID, visits_GID)
);

create table rides(
	rides_nameAttrac varchar(300),
    rides_GID int,
    primary key(rides_nameAttrac, rides_GID)
);





