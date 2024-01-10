# Voice-Controlled Virtual Assistant
This Python script creates a basic voice-controlled virtual assistant using speech recognition and text-to-speech capabilities. 
The assistant can perform some preprogrammed tasks based on voice commands given by the user.

## Features
- **Greeting**: Greets the user based on the time of day (Good Morning/Good Afternoon/Good Evening).
- **Open Notepad**: Opens the Notepad application.
- **Close Notepad**: Closes the currently opened Notepad instance.
- **Wikipedia Search**: Searches and retrieves a summary from Wikipedia based on the user's query.
- **Search Google**: Opens the default web browser and search based on user query.
- **Close Browser**: Checks all browser paths and closes the one that's still open.
- **Stop Listening**: Exits the continous listening loop.

## Requirements
Ensure you have the following installed:
- Python 3.11
- pyttsx3 (Text-to-speech library)
- speech_recognition (Speech recognition library)
- wikipedia (Wikipedia API)

## Usage
1. Install the required dependencies using `pip install pyttsx3 speech_recognition wikipedia`.
2. Run the Python script `voice_assistant.py`.
3. Once the assistant is initialized, it will listen for voice commands.
4. Speak commands clearly to perform various tasks supported by the assistant.

## Credits
This code is developed based on inspirations from various Python tutorials and documentation sources.
