import csv
from gtts import gTTS
import re
import speech_recognition as sr
import news
import time
import reminder
import music
import os
from word2number import w2n

initial = sr.Recognizer()


def audio_in():
    while True:
    try:
        with sr.Microphone() as source:
            initial.adjust_for_ambient_noise()
            com_out(statement)
            audio_input = initial.listen(source)
        y_text = initial.recognize_google(audio_input)
        y_text = text.lower()
        user_out(y_text)
        return y_text
    except:
        com_out('Sorry I can\'t hear you')
        abc = gTTS('Sorry I can\t hear you')
        abc.save('a.wav')
        os.system('start a.wav')
        time.sleep(2)


def com_out(message):
    print('Computer: ', message)

def user_out(message):
    print('User: ', message)


while True:
    try:
        with sr.Microphone() as source:
            initial.adjust_for_ambient_noise()
            com_out('Please Command me')
            audio_input = initial.listen(source)
        text = initial.recognize_google(audio_input)
        text = text.lower()
        user_out(text)
    except:
        pass



    if re.search('play', text) or re.search('music', text) or re.search('song', text):
        statement = 'Please name the song you want me to play or say random to let me play any song for you of my choice'
        audio_out = gTTS(statement)
        audio_out.save('a.wav')
        os.system('start a.wav')
        time.sleep(9)
        try:
            with sr.Microphone() as source:
                initial.adjust_for_ambient_noise()
                com_out(statement)
                audio_input = initial.listen(source)
            text = initial.recognize_google(audio_input)
            text = text.lower()
            user_out(text)
            music_path = music.music(text)
            command = 'start ' + music_path
            os.system(command)
        except:
            continue

    elif re.search('news', text) or re.search('headline', text):
        news_text = ''
        news.data()
        reader = csv.reader('news.csv')
        for row in reader:
            audio_out = gTTS(row)
            audio_out.save('a.wav')
            os.system('start a.wav')
            try:
                with sr.Microphone() as source:
                    initial.adjust_for_ambient_noise()
                    com_out(statement)
                    audio_input = initial.listen(source)
                news_text = initial.recognize_google(audio_input)
                news_text = text.lower()
                user_out(news_text)
            except:
                pass
            if re.search('exit', news_text) or re.search('stop', text):
                break
            else:
                pass
            time.sleep(6)

    elif re.search('add', text) and ('reminder', text):
        statement = 'Which year'
        audio_out = gTTS(statement)
        audio_out.save('a.wav')
        os.system('start a.wav')
        com_out(statement)
        time.sleep(1)
        year  = audio_in()
        if re.search('exit', year) or re.search('close', year) or re.search('stop', year):
            break
        statement = 'Which month'
        audio_out = gTTS(statement)
        audio_out.save('a.wav')
        os.system('start a.wav')
        com_out(statement)
        time.sleep(1)
        month = audio_in()
        if re.search('exit', month) or re.search('close', month) or re.search('stop', month):
            break
        statement = 'Which date'
        audio_out = gTTS(statement)
        audio_out.save('a.wav')
        os.system('start a.wav')
        com_out(statement)
        time.sleep(1)
        date = audio_in()
        if re.search('exit', date) or re.search('close', date) or re.search('stop', date):
            break
        statement = 'Hour of the day?'
        audio_out = gTTS(statement)
        audio_out.save('a.wav')
        os.system('start a.wav')
        com_out(statement)
        time.sleep(1)
        hour = audio_in()
        if re.search('exit', hour) or re.search('close', hour) or re.search('stop', hour):
            break
        statement = 'Purpose'
        audio_out = gTTS(statement)
        audio_out.save('a.wav')
        os.system('start a.wav')
        com_out(statement)
        time.sleep(1)
        purpose = audio_in()
        try:
            year = w2n.word_to_num(year)
            month = w2n.word_to_num(month)
            date = w2n.word_to_num(date)
            hour = w2n.word_to_num(hour)
            reminder.set(year, month, date, hour, purpose)
        except:
            statement = 'Sorry, unable to set reminder'
            audio_out = gTTS(statement)
            audio_out.save('a.wav')
            os.system('start a.wav')
            time.sleep(2)