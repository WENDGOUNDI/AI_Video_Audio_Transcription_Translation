import PySimpleGUI as sg
import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
from pathlib import Path
from deep_translator import GoogleTranslator
import os
import textract



sg.theme('DarkAmber')


tab1_layout  = [  [sg.Text('Video/Audio Translation & Translation')],
          [sg.Button('Browse File'), sg.Input(expand_x=True, key='File')],
          [sg.Button("Transcribe")],
          [sg.Button('Translate')],
            [sg.Text('Enter Languages for Translation'), sg.Input(expand_x=True, key='translation_language')],
          [sg.Output(size=(15,5), key="process_status")]]

instructions_var = """1. This Software allows video and audio transcription as well as text translation.
2. We make translatation in one or multiples languages.
3. For mutliple languages, languagues should be aligned as followed: 
    french, english, spanish."""

tab2_layout = [[sg.T(instructions_var)],
               [sg.Image('languages_list2.PNG') ],    
               ]

#layout = [[sg.TabGroup([[sg.Tab('Main', tab1_layout, tooltip='tip'), sg.Tab('How To Use', tab2_layout)]], tooltip='TIP2')]] 
layout = [[sg.TabGroup([[sg.Tab('Main', tab1_layout, ), sg.Tab('How To Use', tab2_layout)]])]] 


def video_transcription(video_path):
    transcribed_audio_file_name = "audio_func.wav"
    #zoom_video_file_name = "The_danger_of_silence _ Clint Smith.mp4"
    zoom_video_file_name = video_path
    audioclip = AudioFileClip(zoom_video_file_name)
    audioclip.write_audiofile(transcribed_audio_file_name)
    with contextlib.closing(wave.open(transcribed_audio_file_name, "r")) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        total_duration = math.ceil(duration / 60)
    #print(total_duration)
    r = sr.Recognizer()
    for i in range(0, total_duration):
        with sr.AudioFile(transcribed_audio_file_name) as source:
        #audio = r.record(source, offset=i*60, duration=60)
            audio = r.record(source)
        f = open("transcription_func.txt", "a", encoding="utf-8")
        f.write(r.recognize_google(audio, language="en-US"))
        f.write(" ")
    f.close()
    return f


def audio_transcription(audio_path):
    
    with contextlib.closing(wave.open(audio_path, "r")) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        total_duration = math.ceil(duration / 60)
    #print(total_duration)
    r = sr.Recognizer()
    for i in range(0, total_duration):
        with sr.AudioFile(audio_path) as source:
        #audio = r.record(source, offset=i*60, duration=60)
            audio = r.record(source)
        f = open("transcription_func.txt", "a", encoding="utf-8")
        f.write(r.recognize_google(audio, language="en-US"))
        f.write(" ")
    f.close()
    return f

def translation_file(trans_text, languages_translation,file_pre):
    #trans_file = open(file_path, "r")
    #trans_file = trans_file.readline()
    #to_translate = "Hello welcome to this quaterly all hands meeting."
    #lang_list = ["french", "english",'chinese (traditional)',"italian", "german"]
    for i in languages_translation:
        translated = GoogleTranslator(source='auto', target=i).translate(trans_text)
        file_name = f"{file_pre}_translation_{i}"+".txt"
        f = open(file_name, "a", encoding="utf-8")
        f.write(translated)
        f.close()



# Create the Window
window = sg.Window('TransSoft', layout,size=(800, 500), element_justification='center')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    #print('You entered ', values[0])
    
    if event == "Browse File":
        path = sg.popup_get_file(" ", no_window=True)
        window["File"].Update(path)
        if len(path)==0:
            pass
        else:
            path_s = os.path.normpath(path)
            path_s_final = path_s.split(os.sep)[-2]
        
    if event == "Transcribe":
        video_extension = (".avi", ".mp4")
        audio_extension = (".mp3", ".wav")

        if Path(path).suffix in video_extension:
            video_transcription(path)
            window["process_status"].Update(" PROCESS COMPLETED SUCCESSFULLY",background_color='green')
        elif Path(path).suffix in audio_extension:
            audio_transcription(path)
            window["process_status"].Update(" PROCESS COMPLETED SUCCESSFULLY",background_color='green')
            
    if event == "Translate":
        trans_language = values['translation_language']
        trans_language = trans_language.split(",")
        #print(trans_language)
        if len(trans_language)==0:
            window["process_status"].Update("NO TRANSLATED LANGUAGE HAS BEEN SELECTED",background_color='red')
        
        text_extension = (".txt",".doc",".docx")
        if Path(path).suffix in text_extension:
            #trans_file = open(path, "r+", encoding='utf-8')
            #trans_file = trans_file.readline()
            trans_file = textract.process("subtitles_in_text.txt")
            trans_file = trans_file.decode("utf-8")
            if len(trans_file)<5000:
                translation_file(trans_file, trans_language, path_s_final)
                window["process_status"].Update("COMPLETED",background_color='green')
            else:
                window["process_status"].Update("CHARACTERS TO BE TRANSLATED ARE LIMITTED TO 5000",background_color='red')
        else:
            window["process_status"].Update("WRONG FILE EXTENSION. ONLY '.TXT' IS UPPORTED",background_color='red')
    

window.close()