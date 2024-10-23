#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Список песен группы Depeche Mode со временем звучания
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Функция для вычисления времени звучания песен из списка
def get_sound_time_from_song_list(song_list: list, songs: [str]):
    song_list_map = {song[0]: song[1] for song in song_list}
    time = 0
    for song in songs:
        time += song_list_map[song]
    return time

# Расчет времени звучания трех песен
time1 = get_sound_time_from_song_list(violator_songs_list, ['Halo', 'Enjoy the Silence', 'Clean'])
print(f"Три песни звучат {round(time1, 2)} минут")

# Словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# Функция для вычисления времени звучания песен из словаря
def get_sound_time_from_song_dict(song_dict: dict, songs: [str]):
    time = 0
    for song in songs:
        time += song_dict[song]
    return time

# Расчет времени звучания трех других песен
def solve():
    time2 = get_sound_time_from_song_dict(violator_songs_dict, ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'])
    print(f"А другие три песни звучат {round(time2)} минут")
