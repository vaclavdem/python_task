def create_rooms_table(cursor):
    """
    creating of room table in db

    :param cursor: cursor db
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL
        );
    """)


def create_students_table(cursor):
    """
        creating of students table in db

        :param cursor: cursor db
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            birthday DATE NOT NULL,
            sex TEXT NOT NULL,
            room INTEGER REFERENCES rooms(id)
        );
    """)