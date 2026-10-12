def vacuum_cleaner(room):
    for place in room:
        if room[place] == "Dirty":
            print(place, "is dirty. Cleaning...")
            room[place] = "Clean"
        else:
            print(place, "is already clean.")

    print("Final Room Status:", room)

room = {
    "A": "Dirty",
    "B": "Dirty"
}

vacuum_cleaner(room)