import mysql.connector
import random
import static

def generateAdministration(num_of_rows):
    stmt = """INSERT INTO administration (WPM) VALUES (%s)"""
    tuples = []
    for i in range(num_of_rows):
        thisTuple = (random.randint(40,200),)
        tuples.append(thisTuple)
    return stmt, tuples

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

# def generateChild(num_of_rows):
#     stmt = """INSERT INTO child (GID, relationship, fname, lname, type, age, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
#     tuples = []
#     for i in range(num_of_rows):
#         thisTuple = (
#             random.randint(1,num_of_rows),

#         )

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
    query, tuples = generateAdministration(10)
    commitInsert("administration", query, tuples)

    #  insert 10 tuples into the attraction table
    query, tuples = generateAttraction(10)
    commitInsert("attraction", query, tuples)

