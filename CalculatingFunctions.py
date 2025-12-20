from db_config import cur

def CalculatungRoomsAndPeople(cur):
    cur.execute("SELECT rooms.id,\
        ARRAY_AGG(students.name ORDER BY students.name) AS students\
        FROM rooms\
        LEFT JOIN students ON rooms.id = students.room\
        GROUP BY rooms.id\
        ORDER BY rooms.id ASC;")
    rooms_and_people = cur.fetchall()
    return rooms_and_people

def CalculatungMinAvgAge(cur):
    cur.execute("SELECT rooms.id,\
        AVG(AGE(CURRENT_DATE, students.birthday)) AS AVG_AGE\
        FROM rooms\
        JOIN students ON rooms.id = students.room\
        GROUP BY rooms.id\
        ORDER BY AVG_AGE ASC\
        LIMIT 5")
    min_avg_age = cur.fetchall()
    return min_avg_age

def CalculatungMaxAgeDiff(cur):
    cur.execute("SELECT rooms.id,\
        AGE(MAX(students.birthday), MIN(students.birthday)) AS MAX_DIFF\
        FROM rooms\
        JOIN students ON rooms.id = students.room\
        GROUP BY rooms.id\
        ORDER BY MAX_DIFF DESC\
        LIMIT 5")
    max_age_diff = cur.fetchall()
    return max_age_diff

def CalculatungMixedGenderRooms(cur):
    cur.execute("SELECT rooms.id\
        FROM rooms\
        JOIN students ON rooms.id = students.room\
        GROUP BY rooms.id\
        HAVING COUNT(DISTINCT students.sex) = 2\
        ORDER BY rooms.id;")
    mixed_gender_rooms = cur.fetchall()
    return mixed_gender_rooms