drop database if exists themepark;

create database themepark;

use themepark;

create table Department(
	DeptID int not null auto_increment,
    DeptType varchar(300),
    Supervisor int,
    primary key(DeptID)
);

create table Employee(
	EMPID int not null auto_increment,
    SSN bigint not null,
    fname varchar(50) not null,
    lname varchar(50) not null,
    type varchar(20),
    age int,
    phoneNo bigint,
    hours int,
    EmpDept int,
    primary key(EMPID),
    foreign key(EmpDept) references Department(DeptID)
);

create table Rides_Dept(
	deptID int not null,
    skill_lvl int,
    primary key(deptID),
    foreign key(deptID) references Department(DeptID)
);

create table Security(
	deptID int not null,
    physicalIndex int,
    primary key(deptID),
    foreign key(deptID) references Department(DeptID)
);

create table Leisure(
	deptID int not null,
    hosp_index int,
    primary key(deptID),
    foreign key(deptID) references Department(DeptID)
);

create table Administration(
	deptID int not null,
    WPM int,
    primary key(deptID),
    foreign key(deptID) references Department(DeptID)
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
    park varchar(300),
    openHour int,
    closeHour int,
    primary key(attractionName)
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
    age int,
    gender varchar(1),
    primary key(CID,GID),
    foreign key(GID) references Guest(GID)
);

create table watches(
	watches_showID int,
    watches_GID int,
    primary key(watches_showID, watches_GID),
    foreign key(watches_showID) references Shows(showID),
    foreign key(watches_GID) references Guest(GID)
);

create table visits(
	visits_destID int,
    visits_GID int,
    primary key(visits_destID, visits_GID),
    foreign key(visits_destID) references Destination(destID),
    foreign key(visits_GID) references Guest(GID)
);

create table rides(
	rides_nameAttrac varchar(300),
    rides_GID int,
    primary key(rides_nameAttrac, rides_GID),
    foreign key(rides_nameAttrac) references Attraction(attractionName),
    foreign key(rides_GID) references Guest(GID)
);

create table works_in(
	works_EMPID int,
    works_destID int,
    primary key(works_EMPID, works_destID),
    foreign key(works_EMPID) references Employee(EMPID),
    foreign key(works_destID) references Destination(destID)
);

create table performs_in(
	perf_EMPID int,
    perf_showID int,
    primary key(perf_EMPID, perf_showID),
    foreign key(perf_EMPID) references Employee(EMPID),
    foreign key(perf_showID) references Shows(showID)
);

create table operates_in(
	oper_attrName varchar(300),
    oper_EMPID int,
    primary key(oper_attrName, oper_EMPID),
    foreign key(oper_attrName) references Attraction(attractionName),
    foreign key(oper_EMPID) references Employee(EMPID)
);







