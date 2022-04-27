import mysql.connector
import random
import static

# Global constants
# If you want to change the number of rows being generated, change the value of the constant
ADMINISTRATION_ROWS = 10
ATTRACTION_ROWS = 10
CHILD_ROWS = 10
DEPARTMENT_ROWS = 10
DESTINATION_ROWS = 10
EMPLOYEE_ROWS = 10
GUEST_ROWS = 10
LEISURE_ROWS = 10
RIDES_ROWS = 10
RIDES_DEPT_ROWS = 10
SECURITY_ROWS = 10
SHOWS_ROWS = 10
VISITS_ROWS = 10
WATCHES_ROWS = 10
WORKS_IN_ROWS = 10


# generateAdministration generates rows for the administration table
def generateAdministration(num_of_rows):
    stmt = """INSERT INTO administration (WPM) VALUES (%s)"""
    tuples = []
    for i in range(num_of_rows):
        thisTuple = (random.randint(40,200),)
        tuples.append(thisTuple)
    return stmt, tuples


# generateAttraction generates rows for the attraction table
def generateAttraction(num_of_rows):
    stmt = """INSERT INTO attraction (attractionName, duration, passType, rideType, openHour, closeHour) VALUES (%s, %s, %s, %s, %s, %s)"""
    tuples = []
    used_names = set()
    for i in range(num_of_rows):
        # choose a unique attraction name so PK won't throw error
        chosen_name = static.nouns[random.randint(0,9)]+' '+static.verbs[random.randint(0,9)]
        while chosen_name in used_names:
            chosen_name = static.nouns[random.randint(0,9)]+' '+static.verbs[random.randint(0,9)]
        used_names.add(chosen_name)

        # build the tuple to insert
        thisTuple = (
            chosen_name,
            random.randint(4,15),
            static.passes[random.randint(0,3)],
            static.rideTypes[random.randint(0,4)],
            random.randint(0,24),
            random.randint(0,24)
        )
        tuples.append(thisTuple)
    return stmt, tuples


# generateChild generates rows for the child table
def generateChild(num_of_rows):
    stmt = """INSERT INTO child (GID, relationship, fname, lname, type, age, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    tuples = []
    for i in range(num_of_rows):
        thisTuple = (
            random.randint(1,GUEST_ROWS),
            static.relationshipTypes[random.randint(0,3)],
            static.firstnames[random.randint(0,12)],
            static.lastnames[random.randint(0,12)],
            "PLACEHOLDER - REMOVE",
            random.randint(1,18),
            static.gender[random.randint(0,1)]
        )
        tuples.append(thisTuple)
    return stmt, tuples


# commitInsert executes the statement alongside the generates tuples into the database
def commitInsert(tableName = "NAN", insert_query = "", tuples_to_insert = []):
    if insert_query == "" and len(tuples_to_insert) == 0:
        return
    
    try:
        connection = mysql.connector.connect(host='localhost',database='themepark',username='root')

        cursor = connection.cursor()
        cursor.executemany(insert_query, tuples_to_insert)
        connection.commit()
        print(cursor.rowcount, 'Rows Inserted Into The '+tableName+' Table')
    except:
        print('Insertion Failed for Table:', tableName)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('Connection Closed! \n')


if __name__ == "__main__":

    #  insert 10 tuples into the administration table
    query, tuples = generateAdministration(ADMINISTRATION_ROWS)
    commitInsert("administration", query, tuples)

    #  insert 10 tuples into the attraction table
    query, tuples = generateAttraction(ATTRACTION_ROWS)
    commitInsert("attraction", query, tuples)

    #  insert 10 tuples into the child table
    query, tuples = generateChild(CHILD_ROWS)
    commitInsert("child", query, tuples)

