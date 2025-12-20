from db_config import cur

def CreateRoomTable(cur):
    cur.execute("CREATE TABLE rooms (\
        id      INTEGER PRIMARY KEY,\
        name    TEXT NOT NULL\
    );")

def CreateStudentsTable(cur):
    cur.execute("CREATE TABLE students (\
        id          INTEGER PRIMARY KEY,\
        name        TEXT NOT NULL,\
        birthday    DATE NOT NULL,\
        sex         CHAR(1) NOT NULL CHECK (sex IN ('M', 'F')),\
        room     INTEGER NOT NULL,\
        CONSTRAINT fk_students_room\
            FOREIGN KEY (room)\
            REFERENCES rooms (id)\
            ON DELETE RESTRICT\
    );")

def CreateIndexesTable(cur):
    cur.execute("CREATE INDEX idx_students_room_id\
        ON students(room);")

def ExtractingRoomsInfo(cur, rooms_data):
    for room in rooms_data:
        id = room['id']
        name = room['name']
        cur.execute(f"INSERT INTO rooms (id, name)\
            VALUES ({id}, '{name}');")

def ExtractingStudentsInfo(cur, students_data):
    for student in students_data:
        id = student['id']
        name = student['name']
        birthday = student['birthday']
        room = student['room']
        sex = student['sex']
        cur.execute(f"INSERT INTO students (id, name, birthday, sex, room)\
            VALUES ({id}, '{name}', '{birthday}', '{sex}', {room});")