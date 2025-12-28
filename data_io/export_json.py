import json
from pathlib import Path


def export_to_json_first_query(rooms_with_students, filepath="result_first_query.json"):
    """
    exporting all the results of the program into json file

    :param rooms_with_students: result of the first sql query(List of rooms and the number of students in each of them)
    :param filepath: file to output
    :return: json file with results
    """
    data = {
        "rooms_with_students": [
            {"room": room, "students": students}
            for room, students in rooms_with_students
        ]
    }

    path = Path("output_files") / filepath
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Output first query successful")


def export_to_json_second_query(min_avg_age_rooms, filepath="result_second_query.json"):
    """
    exporting second query results of the program into json file

    :param min_avg_age_rooms: result of the second sql query(5 rooms with the smallest average age of students)
    :param filepath: file to output
    :return: json file with results
    """
    data = {
        "rooms_with_min_avg_age": [
            {"room": room, "avg_age_days": age.days}
            for room, age in min_avg_age_rooms
        ]
    }

    path = Path("output_files") / filepath
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Output second query successful")


def export_to_json_third_query(max_age_diff_rooms, filepath="result_third_query.json"):
    """
    exporting third query results of the program into json file

    :param max_age_diff_rooms: result of the third sql query(5 rooms with the largest difference in the age of students)
    :param filepath: file to output
    :return: json file with results
    """
    data = {
        "rooms_with_max_age_diff": [
            {"room": room, "age_diff_days": diff.days}
            for room, diff in max_age_diff_rooms
        ]
    }

    path = Path("output_files") / filepath
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Output third query successful")


def export_to_json_fourth_query(mixed_gender_rooms, filepath="result_fourth_query.json"):
    """
    exporting fourth query results of the program into json file

    :param mixed_gender_rooms: result of the fourth sql query(List of rooms where different-sex students live)
    :param filepath: file to output
    :return: json file with results
    """
    data = {
        "rooms_with_mixed_gender": [
            {"room": room} for (room,) in mixed_gender_rooms
        ]
    }

    path = Path("output_files") / filepath
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Output fourth query successful")