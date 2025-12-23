def get_rooms_with_students(cursor):
    """
    calculating of the first sql query(List of rooms and the number of students in each of them)

    :param cursor: db cursor
    :return: list[tuple[int, list[str]]]  (list[turple[room_id, list of sudents names]])
    """
    cursor.execute("""
        SELECT rooms.id,
               ARRAY_AGG(students.name ORDER BY students.name)
        FROM rooms
        LEFT JOIN students ON rooms.id = students.room
        GROUP BY rooms.id
        ORDER BY rooms.id;
    """)
    return cursor.fetchall()


def get_rooms_with_min_avg_age(cursor):
    """
    calculating of the second sql query(5 rooms with the smallest average age of students)

    :param cursor: cursor db
    :return: list[tuple[int, datetime.timedelta]]  (list[turple[room_id, smallest average age]])
    """
    cursor.execute("""
        SELECT rooms.id,
               AVG(AGE(CURRENT_DATE, students.birthday))
        FROM rooms
        JOIN students ON rooms.id = students.room
        GROUP BY rooms.id
        ORDER BY AVG DESC
        LIMIT 5;
    """)
    return cursor.fetchall()


def get_rooms_with_max_age_diff(cursor):
    """
    calculating of the first sql query(5 rooms with the largest difference in the age of students)

    :param cursor: cursor db
    :return: list[tuple[int, datetime.timedelta]]  (list[turple[room_id, largest difference in the age]])
    """
    cursor.execute("""
        SELECT rooms.id,
               AGE(MAX(students.birthday), MIN(students.birthday))
        FROM rooms
        JOIN students ON rooms.id = students.room
        GROUP BY rooms.id
        ORDER BY 2 DESC
        LIMIT 5;
    """)
    return cursor.fetchall()


def get_mixed_gender_rooms(cursor):
    """
    calculating of the fourth sql query(List of rooms where different-sex students live)

    :param cursor: cursor db
    :return: list[tuple[int, ]]   (list[tuple[room_id, ]])
    """

    cursor.execute("""
        SELECT room
        FROM students
        GROUP BY room
        HAVING COUNT(DISTINCT sex) = 2;
    """)
    return cursor.fetchall()
