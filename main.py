from class_01 import Music

song_name = str(input("Enter song name: "))
save_name = str(input("Enter downloaded name: "))

music = Music(song_name, save_name)

music.get_parse_name()
print(music.get_html())
music.get_current_url()
music.music_parse()
