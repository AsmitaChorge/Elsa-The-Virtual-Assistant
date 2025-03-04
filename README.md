# Elsa-The-Virtual-Assistant

Overview 
Elsa is a voice-activated virtual assistant built using Python. It can perform various tasks like opening applications, searching the web, providing Wikipedia summaries, telling the time, and playing YouTube videos. Elsa uses Speech Recognition, Text-to-Speech (TTS), and NLP to interact with users.

Features
✅ Responds to voice commands
✅ Searches Wikipedia for information
✅ Opens websites like Google, YouTube, and GitHub
✅ Plays YouTube videos based on user requests
✅ Tells the current time
✅ Opens system applications like Notepad, Calculator, and VS Code
✅ Continuous listening mode until the user exits

Technologies Used
Python (Main language)
SpeechRecognition (Voice input processing)
pyttsx3 (Text-to-Speech conversion)
Wikipedia API (Fetching Wikipedia summaries)
webbrowser (Opening web pages)
datetime (Handling time-based functions)
pywhatkit (Playing YouTube videos)
os (Executing system commands)

Installation Guide

Step 1: Clone the Repository

git clone https://github.com/AsmitaChorge/Elsa-The-Virtual-Assistant.git
cd Elsa-The-Virtual-Assistant

Step 2: Install Required Dependencies

Ensure you have Python installed, then install the necessary libraries:

pip install speechrecognition pyttsx3 wikipedia pywhatkit

Step 3: Run the Virtual Assistant

python elsa.py

Usage Instructions

Run the script and start speaking when prompted.

Example voice commands:

"Open Google"
"Tell me about Artificial Intelligence from Wikipedia"
"Play Faded on YouTube"
"What time is it?"
"Open Notepad"
"Exit" (to stop Elsa)

Project Workflow
Takes voice input using speech_recognition.
Processes commands and determines the required action.
Responds using pyttsx3 (TTS engine).
Performs the requested task (search, open apps, play music, etc.).
Future Enhancements

🚀 Add Wake Word Detection (e.g., "Hey Elsa")
🚀 Integrate ChatGPT API for smarter conversations
🚀 Include Weather & News Updates
🚀 Add WhatsApp messaging feature

Contributors
Asmita Chorge,
Siddhi Dalvi,
Sharvani Mahadik,
Ashwini Pawar.
