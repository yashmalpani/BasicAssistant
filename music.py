import csv
import random

music_dir = 'MUSIC_DIRECTORY'

def music(title):
    music_list = csv.reader(open('music.csv','r+'), delimiter = ',')

    if title != 'random':
        for music in music_list:
            if title == music[0]:
                return music_dir + music[1] + '.mp3'

    else:
        with open('music.csv','r') as f:
            reader = csv.reader(f)
            row = random.choice(reader)
            return music_dir + row[1] + '.mp3'