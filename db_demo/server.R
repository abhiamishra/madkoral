#
# This is the server logic of a Shiny web application. You can run the
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(RMySQL)
library(DBI)
library("odbc")
library(DBI)
library(reactable)

con <- dbConnect(odbc::odbc(),
                 .connection_string = "Driver={MySQL ODBC 8.0 Unicode Driver};", 
                 Server="localhost",
                 Database="my_guitar_shop",
                 UID = "root",
                 Port = 3306)

# Define server logic required to draw a histogram
shinyServer(function(input, output) {
    playerTable <- eventReactive(input$show,{
        
        print(input$text)
        rs = dbSendQuery(con,input$text)
        frame = dbFetch(rs)
        dbDisconnect(con)
        
        
        red_pal <- function(x) rgb(colorRamp(c("#30a2da", "#e5ae38", "#fc4f30"))(x), maxColorValue = 255)
        reactable(frame, filterable = TRUE,
                  defaultPageSize = 20,
                  theme = reactableTheme(
                      borderColor = "#dfe2e5",
                      stripedColor = "#f6f8fa",
                      highlightColor = "#f0f5f9",
                      cellPadding = "8px 12px",
                      style = list(fontFamily = "-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"),
                      searchInputStyle = list(width = "100%")
                  ))
    })
    
    output$playerData <- renderReactable({
        playerTable()
    })

})
