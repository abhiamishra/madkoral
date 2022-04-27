create database themepark;

use themepark;

create table Department(
	DeptID int,
    DeptType varchar(300),
    Supervisor varchar(300),
    primary key(DeptID)
);

create table Rides_Dept(
	deptID int,
    showID int,
    attractionName varchar(300),
    skill_lvl int,
    primary key(deptID)
);

create table Security(
	deptID int,
    physicalIndex int,
    primary key(deptID)
);

create table Leisure(
	deptID int,
    hosp_index int,
    primary key(deptID)
);

create table Administration(
	deptID int,
    WPM int,
    primary key(deptID)
);

-- show is a reserved word -- renamed to shows
create table Shows(
	showID int,
    title varchar(150),
    park varchar(300),
    openHour int,
    closeHour int,
    duration int,
    primary key(showID)
);

create table Destination(
	destID int,
    managerID varchar(300),
    destName varchar(300),
    destType varchar(300),
    parkOwned boolean,
	primary key(destID)
);

create table Attraction(
	attractionName varchar(300),
    duration int,
    passType varchar(50),
    rideType varchar(100),
    openHour int,
    closeHour int,
    primary key(attractionName)
);

create table Employee(
	EMPID int,
    SSN int,
    division varchar(50),
    fname varchar(50),
    lname varchar(50),
    type varchar(20),
    age int,
    phoneNo int,
    hours int,
    EmpDept int,
    primary key(EMPID)
);

create table Guest(
	GID int,
    credCard int,
    address varchar(100),
    passType varchar(50),
    fname varchar(50),
    lname varchar(50),
    age int,
    phoneNo int,
    primary key(GID)
);

create table Child(
	CID int,
    GID int,
    relationship varchar(100),
    fname varchar(50),
    lname varchar(50),
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





