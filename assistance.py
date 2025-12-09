import os
import sys
import threading
import datetime
import webbrowser
import pyttsx3
import wikipedia
import sounddevice as sd
import numpy as np
import speech_recognition as sr

# ---------------- Settings ----------------
ALEX_NAME = "alex"
MUSIC_FOLDER = os.path.expanduser('~/Music')

# ---------------- TTS Engine ----------------
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print(f"Alex: {text}")
    engine.say(text)
    engine.runAndWait()

# ---------------- Speech Recognition ----------------
recognizer = sr.Recognizer()
SAMPLE_RATE = 44100  # mic sample rate
DURATION = 5         # seconds to record each time

def listen():
    try:
        print("Listening...")
        recording = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
        sd.wait()
        audio_data = sr.AudioData(recording.tobytes(), sample_rate=SAMPLE_RATE, sample_width=2)
        text = recognizer.recognize_google(audio_data)
        print(f"You: {text}")
        return text.lower()
    except Exception:
        return ""

# ---------------- Features ----------------
def tell_time():
    now = datetime.datetime.now()
    time_str = now.strftime('%I:%M %p')
    speak('Current time is ' + time_str)

def open_website(domain_or_query):
    url = 'https://' + domain_or_query if '.' in domain_or_query else 'https://www.google.com/search?q=' + domain_or_query.replace(' ', '+')
    speak('Opening ' + domain_or_query)
    webbrowser.open(url)

def search_wikipedia(query, sentences=2):
    try:
        summary = wikipedia.summary(query, sentences=sentences)
        speak('According to Wikipedia: ' + summary)
    except Exception:
        speak('No information found on Wikipedia.')

def play_music():
    if not os.path.isdir(MUSIC_FOLDER):
        speak('Music folder not found.')
        return
    files = [f for f in os.listdir(MUSIC_FOLDER) if os.path.isfile(os.path.join(MUSIC_FOLDER, f))]
    if not files:
        speak('No music files found.')
        return
    track = os.path.join(MUSIC_FOLDER, files[0])
    speak('Playing ' + files[0])
    try:
        if sys.platform.startswith('win'):
            os.startfile(track)
        elif sys.platform.startswith('darwin'):
            os.system('open ' + '"' + track + '"')
        else:
            os.system('xdg-open ' + '"' + track + '"')
    except Exception:
        speak('Could not play music.')

def take_note(text):
    notes_dir = os.path.expanduser('~/alex_notes')
    os.makedirs(notes_dir, exist_ok=True)
    filename = datetime.datetime.now().strftime('note_%Y%m%d_%H%M%S.txt')
    path = os.path.join(notes_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    speak('Note saved.')

def set_reminder(delay_seconds, message):
    def reminder_action():
        speak('Reminder: ' + message)
    t = threading.Timer(delay_seconds, reminder_action)
    t.start()
    speak(f'Reminder set for {delay_seconds} seconds from now.')

# ---------------- Command Handler ----------------
def handle_command(command):
    if 'time' in command:
        tell_time()
        return
    if command.startswith('open '):
        open_website(command.replace('open ', '', 1))
        return
    if command.startswith('search '):
        q = command.replace('search ', '', 1)
        speak('Searching for ' + q)
        webbrowser.open('https://www.google.com/search?q=' + q.replace(' ', '+'))
        return
    if command.startswith('wikipedia '):
        q = command.replace('wikipedia ', '', 1)
        search_wikipedia(q)
        return
    if 'play music' in command or 'play song' in command:
        play_music()
        return
    if command.startswith('note '):
        text = command.replace('note ', '', 1)
        take_note(text)
        return
    if 'remind me in' in command:
        try:
            parts = command.split()
            if 'minutes' in parts:
                i = parts.index('minutes')
                secs = int(float(parts[i - 1]) * 60)
                message = ' '.join(parts[i + 2:]) if len(parts) > i + 2 else 'Reminder'
            elif 'seconds' in parts:
                i = parts.index('seconds')
                secs = int(parts[i - 1])
                message = ' '.join(parts[i + 2:]) if len(parts) > i + 2 else 'Reminder'
            else:
                secs = 60
                message = 'Reminder'
            set_reminder(secs, message)
        except Exception:
            speak('Could not set reminder.')
        return
    if 'exit' in command or 'quit' in command or 'stop' in command:
        speak('Goodbye!')
        sys.exit(0)
    speak('Sorry, I did not understand that.')

# ---------------- Main Loop ----------------
def main():
    speak('Hello! I am Alex, your personal assistant.')
    while True:
        text = listen()
        if not text:
            continue
        if ALEX_NAME in text:
            speak('Yes?')
            command = listen()
            if command:
                handle_command(command)

# ---------------- Run ----------------
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        speak('Shutting down. Bye!')
        sys.exit(0)
