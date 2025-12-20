import json
from InputOperations import CreateRoomTable, CreateStudentsTable, CreateIndexesTable, ExtractingRoomsInfo, ExtractingStudentsInfo
from CalculatingFunctions import CalculatungRoomsAndPeople, CalculatungMixedGenderRooms, CalculatungMinAvgAge, CalculatungMaxAgeDiff
from OutputOperations import OutputJSON
from db_config import conn, cur

rooms_data = json.load(open("rooms.json"))
students_data = json.load(open("students.json"))

CreateRoomTable(cur)
CreateStudentsTable(cur)
CreateIndexesTable(cur)

ExtractingRoomsInfo(cur, rooms_data)
ExtractingStudentsInfo(cur, students_data)

rooms_and_people = CalculatungRoomsAndPeople(cur)
min_avg_age = CalculatungMinAvgAge(cur)
max_age_diff = CalculatungMaxAgeDiff(cur)
mixed_gender_rooms = CalculatungMixedGenderRooms(cur)

OutputJSON(rooms_and_people, min_avg_age, max_age_diff, mixed_gender_rooms)

conn.commit()
cur.close()
conn.close()