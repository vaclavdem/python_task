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
from data_io.export_json import (
    export_to_json_fourth_query,
    export_to_json_first_query,
    export_to_json_third_query,
    export_to_json_second_query,
)
from repositories.schema import (
    create_students_table,
    create_rooms_table,
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
        "--output_first_query",
        default="result_first_query.json",
        help="Path to output JSON file for first query"
    )
    parser.add_argument(
        "--output_second_query",
        default="result_second_query.json",
        help="Path to output JSON file for second query"
    )
    parser.add_argument(
        "--output_third_query",
        default="result_third_query.json",
        help="Path to output JSON file for third query"
    )
    parser.add_argument(
        "--output_fourth_query",
        default="result_fourth_query.json",
        help="Path to output JSON file for fourth query"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    rooms = import_rooms_info(cursor, args)
    students = import_students_info(cursor, args)

    create_rooms_table(cursor)
    create_students_table(cursor)

    insert_rooms(cursor, rooms)
    insert_students(cursor, students)

    export_to_json_first_query(get_rooms_with_students(cursor), filepath=args.output_first_query)
    export_to_json_second_query(get_rooms_with_min_avg_age(cursor), filepath=args.output_second_query)
    export_to_json_third_query(get_rooms_with_max_age_diff(cursor), filepath=args.output_third_query)
    export_to_json_fourth_query(get_mixed_gender_rooms(cursor), filepath=args.output_fourth_query)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
