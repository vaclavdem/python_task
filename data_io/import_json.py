import json
from models.room import Room
from models.student import Student

def import_rooms_info(cursor, args):
    """
    importing of rooms.json file

    :param cursor: db cursor
    :param args: args of the command line
    :return: list of objects of Room class
    """
    with open(args.rooms, encoding="utf-8") as f:
        rooms_info = json.load(f)
        rooms = []
        for room in rooms_info:
            rooms.append(Room(room["id"], room["name"]))
    return rooms

def import_students_info(cursor, args):
    """
    importing of students.json file

    :param cursor: db cursor
    :param args: args of the command line
    :return: list of objects of Student class
    """
    with open(args.students, encoding="utf-8") as f:
        students_info = json.load(f)
        students = []
        for student in students_info:
            students.append(Student(student["birthday"], student["id"], student["name"],\
                                 student["room"], student["sex"]))
    return students