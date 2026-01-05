import argparse
import json

from db.connection import conn, cursor
from data_io.load_data import insert_rooms, insert_students
from services.calculations import (
    get_rooms_with_students,
    get_rooms_with_min_avg_age,
    get_rooms_with_max_age_diff,
    get_mixed_gender_rooms,
)
from data_io.export_json import export_to_json
from repositories.schema import (
    create_rooms_table,
    create_indexes,
    create_students_table,
)
from data_io.import_json import import_rooms_info, import_students_info


def parse_args():
    parser = argparse.ArgumentParser(description="Rooms and students processing")
    parser.add_argument(
        "--rooms",
        required=True,
        help="Path to rooms JSON file"
    )
    parser.add_argument(
        "--students",
        required=True,
        help="Path to students JSON file"
    )
    parser.add_argument(
        "--output",
        default="result.json",
        help="Path to output JSON file"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    rooms = import_rooms_info(cursor, args)
    students = import_students_info(cursor, args)

    create_rooms_table(cursor)
    create_students_table(cursor)
    create_indexes(cursor)

    insert_rooms(cursor, rooms)
    insert_students(cursor, students)

    export_to_json(
        get_rooms_with_students(cursor),
        get_rooms_with_min_avg_age(cursor),
        get_rooms_with_max_age_diff(cursor),
        get_mixed_gender_rooms(cursor),
        filepath=args.output,
    )

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
