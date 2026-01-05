import json


def export_to_json(
    rooms_with_students,
    min_avg_age_rooms,
    max_age_diff_rooms,
    mixed_gender_rooms,
    filepath="result.json"
):
    """
    exporting all the results of the programm into json file

    :param rooms_with_students: result of the first sql query(List of rooms and the number of students in each of them)
    :param min_avg_age_rooms: result of the second sql query(5 rooms with the smallest average age of students)
    :param max_age_diff_rooms: result of the third sql query(5 rooms with the largest difference in the age of students)
    :param mixed_gender_rooms: result of the fourth sql query(List of rooms where different-sex students live)
    :param filepath: file to output
    :return: json file with results
    """
    data = {
        "rooms_with_students": [
            {"room": room, "students": students}
            for room, students in rooms_with_students
        ],
        "rooms_with_min_avg_age": [
            {"room": room, "avg_age_days": age.days}
            for room, age in min_avg_age_rooms
        ],
        "rooms_with_max_age_diff": [
            {"room": room, "age_diff_days": diff.days}
            for room, diff in max_age_diff_rooms
        ],
        "rooms_with_mixed_gender": [
            {"room": room} for (room,) in mixed_gender_rooms
        ]
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
