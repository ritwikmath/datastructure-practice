def selection_sort(artists):
    length_of_arr = len(artists)
    for i in range(length_of_arr):
        bigger_index = None
        play_count = artists[i]["plays"]
        for j in range(i, length_of_arr):
            if artists[j]["plays"] > play_count:
                bigger_index = j
        if bigger_index:
            bigger_play_count = artists[j]
            artists[bigger_index] = artists[i]
            artists[i] = bigger_play_count


if __name__ == "__main__":
    artists = [
        {"name": "Artist A", "plays": 400},
        {"name": "Artist B", "plays": 50},
        {"name": "Artist C", "plays": 150},
        {"name": "Artist D", "plays": 300},
    ]
    selection_sort(artists)
    print(artists)