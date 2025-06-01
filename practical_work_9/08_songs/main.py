violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

num_songs = int(input("Сколько песен выбрать? ")) #Кол-во песен
my_songs = [] #Плейлист
total_time = 0 #Общее время плейлиста

for i_song in range(num_songs): #Цикл из кол-ва песен
    song_name = input(f"Название {i_song + 1} песни: ") #Вводим название песни
    for song in violator_songs: #Ищем нужную песню в списке
        if song[0] == song_name: #Если находим, то добавляем ее в наш плейлист и суммируем время
            total_time += song[1]
            my_songs.append(song)

print(f"Общее время звучания песен: {round(total_time, 2)} минуты") #Выводим общее время плейлиста
