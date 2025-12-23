def create_rooms_table(cursor):
    """
    creating of room table in db

    :param cursor: cursor db
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
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
            sex CHAR(1) NOT NULL CHECK (sex IN ('M', 'F')),
            room INTEGER NOT NULL REFERENCES rooms(id)
        );
    """)


def create_indexes(cursor):
    """
        creating of indexes in db

        :param cursor: cursor db
    """
    cursor.execute(
        "CREATE INDEX IF NOT EXISTS idx_students_room ON students(room);"
    )
