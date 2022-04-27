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

used_names = set()

# generateAdministration generates rows for the administration table
def generateAdministration(num_of_rows):
    stmt = """INSERT INTO administration (WPM) VALUES (%s)"""
    tuples = []
    for i in range(num_of_rows):
        thisTuple = (random.randint(40,120),)
        tuples.append(thisTuple)
    return stmt, tuples


# generateAttraction generates rows for the attraction table
def generateAttraction(num_of_rows):
    stmt = """INSERT INTO attraction (attractionName, duration, passType, rideType, openHour, closeHour) VALUES (%s, %s, %s, %s, %s, %s)"""
    tuples = []
    for i in range(num_of_rows):
        # choose a unique attraction name so PK won't throw error
        chosen_name = static.nouns[random.randint(0,len(static.nouns)-1)]+' '+static.verbs[random.randint(0,len(static.verbs)-1)]
        while chosen_name in used_names:
            chosen_name = static.nouns[random.randint(0,len(static.nouns)-1)]+' '+static.verbs[random.randint(0,len(static.verbs)-1)]
        used_names.add(chosen_name)

        # build the tuple to insert
        thisTuple = (
            chosen_name,
            random.randint(4,15),
            static.passes[random.randint(0,len(static.passes)-1)],
            static.rideTypes[random.randint(0,len(static.rideTypes)-1)],
            random.randint(0,24),
            random.randint(0,24)
        )
        tuples.append(thisTuple)
    return stmt, tuples


# generateChild generates rows for the child table
def generateChild(num_of_rows):
    stmt = """INSERT INTO child (GID, relationship, fname, lname, age, gender) VALUES (%s, %s, %s, %s, %s, %s)"""
    tuples = []
    for i in range(num_of_rows):
        thisTuple = (
            random.randint(1,GUEST_ROWS),
            static.relationshipTypes[random.randint(0,len(static.relationshipTypes)-1)],
            static.firstnames[random.randint(0,len(static.firstnames)-1)],
            static.lastnames[random.randint(0,len(static.lastnames)-1)],
            random.randint(1,18),
            static.gender[random.randint(0,len(static.gender)-1)]
        )
        tuples.append(thisTuple)
    return stmt, tuples


# generateDepartment generates rows for the department table
def generateDepartment(num_of_rows):
    stmt = """INSERT INTO department (DeptType, Supervisor) VALUES (%s, %s)"""
    tuples = []
    for i in range(num_of_rows):
        thisTuple = (
            static.departmentTypes[random.randint(0,len(static.departmentTypes)-1)],
            random.randint(1,EMPLOYEE_ROWS)
        )
        tuples.append(thisTuple)
    return stmt, tuples


# generateDestination generates rows for the destination table
def generateDestination(num_of_rows):
    stmt = """INSERT INTO destination (managerID, destName, destType, parkOwned) VALUES (%s, %s, %s, %s)"""
    tuples = []
    for i in range(num_of_rows):
        suffix = static.destinationSuffix[random.randint(0,len(static.destinationSuffix)-1)]
        thisTuple = (
            random.randint(1,EMPLOYEE_ROWS),
            static.destinationPrefix[random.randint(0,len(static.destinationPrefix)-1)]+' '+suffix,
            suffix,
            bool(random.randint(0,1))
        )
        tuples.append(thisTuple)
    return stmt, tuples


# generateEmployee generates rows for the employee table
def generateEmployee(num_of_rows):
    stmt = """INSERT INTO employee (SSN, fname, lname, type, age, phoneNo, hours, EmpDept) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    tuples = []
    for i in range(num_of_rows):
        thisTuple = (
            random.randint(11111111,99999999),
            static.firstnames[random.randint(0,len(static.firstnames)-1)],
            static.lastnames[random.randint(0,len(static.lastnames)-1)],
            static.empTypes[random.randint(0,len(static.empTypes)-1)],
            random.randint(18,60),
            random.randint(1111111111,9999999999),
            random.randint(3,8),
            random.randint(1,DEPARTMENT_ROWS)
        )
        tuples.append(thisTuple)
    return stmt, tuples


def generateGuest(num_of_rows):
    stmt = """INSERT INTO guest (credCard, address, passType, fname, lname, age, phoneNo) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    tuples = []
    for i in range(num_of_rows):
        thisTuple = (
            random.randint(100000000000,9999999999999999),
            str(random.randint(1000,9999))+' '+static.addrA[random.randint(0,len(static.addrA)-1)]+' '+static.addrB[random.randint(0,len(static.addrB)-1)],
            static.passes[random.randint(0,len(static.passes)-1)],
            static.firstnames[random.randint(0,len(static.firstnames)-1)],
            static.lastnames[random.randint(0,len(static.lastnames)-1)],
            random.randint(21,70),
            random.randint(1111111111,9999999999)
        )
        tuples.append(thisTuple)
    return stmt, tuples


def generateLeisure(num_of_rows):
    stmt = """INSERT INTO leisure (hosp_index) VALUES (%s)"""
    tuples = []
    for i in range(num_of_rows):
        thisTuple = (random.randint(1,5),)
        tuples.append(thisTuple)
    return stmt, tuples


def generateRides(num_of_rows):
    stmt = """INSERT INTO rides (rides_nameAttrac, rides_GID) VALUES (%s, %s)"""
    tuples = []
    memo = {}
    for i in range(num_of_rows):
        thisTuple = (
            random.choice(list(used_names)),
            random.randint(1,GUEST_ROWS)
        )
        while thisTuple in memo:
            thisTuple = (
                random.choice(list(used_names)),
                random.randint(1,GUEST_ROWS)
            )
        memo[thisTuple] = True
        tuples.append(thisTuple)
    return stmt, tuples


def generateRidesDept(num_of_rows):
    stmt = """INSERT INTO rides_dept (showID, attractionName, skill_lvl) VALUES (%s, %s, %s)"""
    tuples = []
    for i in range(num_of_rows):
        thisTuple = (
            random.randint(1,SHOWS_ROWS),
            random.choice(list(used_names)),
            random.randint(1,10)
        )
        tuples.append(thisTuple)
    return stmt, tuples


def generateSecurity(num_of_rows):
    stmt = """INSERT INTO security (physicalIndex) VALUES (%s)"""
    tuples = []
    for i in range(num_of_rows):
        thisTuple = (
            random.randint(1,100),
        )
        tuples.append(thisTuple)
    return stmt, tuples


def generateShows(num_of_rows):
    stmt = """INSERT INTO shows (title, park, openHour, closeHour, duration) VALUES (%s, %s, %s, %s, %s)"""
    tuples = []
    for i in range(num_of_rows):
        thisTuple = (
            static.addrA[random.randint(0,len(static.addrA)-1)]+' '+static.nouns[random.randint(0,len(static.nouns)-1)]+' '+static.verbs[random.randint(0,len(static.verbs)-1)],
            static.destinationPrefix[random.randint(0,len(static.destinationPrefix)-1)]+' '+static.parkNames[random.randint(0,len(static.parkNames)-1)],
            random.randint(0,12),
            random.randint(13,24),
            random.randint(1,3)
        )
        tuples.append(thisTuple)
    return stmt, tuples


def generateVisits(num_of_rows):
    stmt = """INSERT INTO visits (visits_destID, visits_GID) VALUES (%s, %s)"""
    tuples = []
    memo = {}
    for i in range(num_of_rows):
        thisTuple = (random.randint(1,DESTINATION_ROWS), random.randint(1,GUEST_ROWS))
        while thisTuple in memo:
            thisTuple = (random.randint(1,DESTINATION_ROWS), random.randint(1,GUEST_ROWS))
        memo[thisTuple] = True
        tuples.append(thisTuple)
    return stmt, tuples


def generateWatches(num_of_rows):
    stmt = """INSERT INTO watches (watches_showID, watches_GID) VALUES (%s, %s)"""
    tuples = []
    memo = {}
    for i in range(num_of_rows):
        thisTuple = (random.randint(1,SHOWS_ROWS), random.randint(1,GUEST_ROWS))
        while thisTuple in memo:
            thisTuple = (random.randint(1,SHOWS_ROWS), random.randint(1,GUEST_ROWS))
        memo[thisTuple] = True
        tuples.append(thisTuple)
    return stmt, tuples


def generateWorksIn(num_of_rows):
    stmt = """INSERT INTO works_in (work_destID, work_deptID) VALUES (%s, %s)"""
    tuples = []
    memo = {}
    for i in range(num_of_rows):
        thisTuple = (random.randint(1,DESTINATION_ROWS), random.randint(1,DEPARTMENT_ROWS))
        while thisTuple in memo:
            thisTuple = (random.randint(1,DESTINATION_ROWS), random.randint(1,DEPARTMENT_ROWS))
        memo[thisTuple] = True
        tuples.append(thisTuple)
    return stmt, tuples



# commitInsert executes the statement alongside the generates tuples into the database
def commitInsert(tableName = "NAN", insert_query = "", tuples_to_insert = []):
    if insert_query == "" and len(tuples_to_insert) == 0:
        print('Invalid or missing parameters!')
        return
    
    try:
        connection = mysql.connector.connect(host='localhost',database='themepark',username='root')

        cursor = connection.cursor()
        cursor.executemany(insert_query, tuples_to_insert)
        connection.commit()
        print(cursor.rowcount,'rows inserted into the '+tableName+' table')
    except:
        print('Insertion failed for table:', tableName)
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

    #  insert 10 tuples into the department table
    query, tuples = generateDepartment(DEPARTMENT_ROWS)
    commitInsert("department", query, tuples)

    #  insert 10 tuples into the destination table
    query, tuples = generateDestination(DESTINATION_ROWS)
    commitInsert("destination", query, tuples)

    query, tuples = generateEmployee(EMPLOYEE_ROWS)
    commitInsert("employee", query, tuples)

    query, tuples = generateGuest(GUEST_ROWS)
    commitInsert("guest", query, tuples)

    query, tuples = generateLeisure(LEISURE_ROWS)
    commitInsert("leisure", query, tuples)

    query, tuples = generateRides(RIDES_ROWS)
    commitInsert("rides", query, tuples)

    query, tuples = generateRidesDept(RIDES_DEPT_ROWS)
    commitInsert("rides_dept", query, tuples)

    query, tuples = generateSecurity(SECURITY_ROWS)
    commitInsert("security", query, tuples)

    query, tuples = generateShows(SHOWS_ROWS)
    commitInsert("shows", query, tuples)

    query, tuples = generateVisits(VISITS_ROWS)
    commitInsert("visits", query, tuples)

    query, tuples = generateWatches(WATCHES_ROWS)
    commitInsert("watches", query, tuples)

    query, tuples = generateWorksIn(WORKS_IN_ROWS)
    commitInsert("works_in", query, tuples)

