Alex Personal Assistant

Alex is a Python-based voice-controlled personal assistant that can perform tasks like telling time, opening websites, searching Wikipedia, playing music, taking notes, and setting reminders. It uses speech recognition and text-to-speech (TTS) for interactive user experience.

Features:

Voice recognition and command execution

Tell current time

Open websites or search queries in browser

Search and read Wikipedia summaries

Play music from local folder

Take and save notes

Set reminders with notifications

Exit/stop commands

Technologies Used:

Python 3

pyttsx3 (Text-to-Speech)

speech_recognition

sounddevice & numpy (record audio)

Wikipedia API

threading (for reminders)

webbrowser module

Project Structure:
Alex_Assistant/
├── alex.py # Main program file
└── README.txt

How to Run:

Install Python 3 if not already installed.

Install required packages:
pip install pyttsx3 wikipedia sounddevice numpy SpeechRecognition

Run the assistant:
python alex.py

How It Works:

Run the program, Alex greets you.

Say "Alex" to activate.

Give commands such as:

"Alex, tell me the time"

"Alex, open youtube.com"

"Alex, search Python programming"

"Alex, wikipedia Artificial Intelligence"

"Alex, play music"

"Alex, note Buy groceries"

"Alex, remind me in 5 minutes Take a break"

Alex will respond via speech and perform the task.

Command Examples:

time → Tells current time

open <website> → Opens website in browser

search <query> → Searches Google for the query

wikipedia <topic> → Reads summary from Wikipedia

play music / play song → Plays first music file from ~/Music

note <text> → Saves a note to ~/alex_notes folder

remind me in <time> <msg> → Sets a reminder

exit / quit / stop → Stops Alex

Folder Setup:

Music folder: ~/Music

Notes folder: ~/alex_notes (auto-created when taking notes)

Purpose:

Demonstrate voice-controlled personal assistant functionality

Practice Python OOP, modules, and threading

Integrate TTS and speech recognition

Build a real-world interactive Python application

Future Improvements:

Add more natural language understanding

Integrate calendar and email features

Support multiple languages

Improve music player with playlist support

Author: Mohsin Atta
