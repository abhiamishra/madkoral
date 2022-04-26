install.packages("RMySQL")
library(RMySQL)
library(DBI)

install.packages("odbc")
library("odbc")

library(DBI)
con <- dbConnect(odbc::odbc(),
                 .connection_string = "Driver={MySQL ODBC 8.0 Unicode Driver};", 
                 Server="localhost",
                 Database="ap",
                 UID = "root",
                 Port = 3306)

#Get entire database
dbListTables(con)

#Get a single table
table <- dbReadTable(con, "terms")

text = "SELECT * FROM terms WHERE terms_due_days < 50"
rs = dbSendQuery(con, text)
frame = dbFetch(rs)

frame

dbDisconnect(con)
