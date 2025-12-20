import json

def OutputJSON(rooms_and_people, min_avg_age, max_age_diff, mixed_gender_rooms):
    data = {
        "rooms_and_residents": [
            {"room": room, "residents": people}
            for room, people in rooms_and_people
        ],
        "rooms_with_min_avg_age": [
            {"room": r, "min_avg_age_days": td.days}
            for r, td in min_avg_age
        ],
        "rooms_with_max_age_diff": [
            {"room": r, "max_age_diff_days": td.days}
            for r, td in max_age_diff
        ],
        "rooms_with_mixed_gender": [
            {"room": r[0]} for r in mixed_gender_rooms
        ]
    }

    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)