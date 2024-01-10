import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os

# Initialize the speech synthesis engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Setting the voice index to the default voice

# Flag to check if the assistant should stop listening
stop_listening = False

# Function to speak out the provided text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to stop listening
def stop_listening_command():
    global stop_listening
    stop_listening = True
    speak("See you later!")

# Function to greet the user based on the current time
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Welcome, I am your virtual assistant")

# Function to open Notepad
def open_notepad():
    try:
        os.startfile("notepad.exe")
        speak("Notepad has been opened")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't open Notepad")

# Function to close Notepad
def close_notepad():
    try:
        os.system("taskkill /f /im notepad.exe")
        speak("Notepad has been closed")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't close Notepad")

# Function to open a web browser and search on Google
def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching Google for {query}")

# Function to close the web browser
def close_browser():
    browsers = ['chrome.exe', 'firefox.exe', 'msedge.exe']
    closed = False

    for browser in browsers:
        os.system(f"taskkill /f /im {browser}")
        closed = True

    if closed:
        speak("Browser has been closed")
    else:
        speak("No browser process found to close")

# Function to search on Wikipedia and print the spoken content
def wikipedia_search(query):
    try:
        speak(f"Searching Wikipedia for {query}")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)

        # Display the spoken content on the terminal
        print(f"Search query: {query}")
        print("According to Wikipedia:")
        print(results)
    except wikipedia.exceptions.PageError as pe:
        print(pe)
        speak("Sorry, I couldn't find information on Wikipedia for this topic")
    except wikipedia.exceptions.DisambiguationError as de:
        print(de)
        speak("There are multiple matches for this topic. Please be more specific.")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't find information on Wikipedia")

if __name__ == "__main__":
    greet()

    while True:
        if not stop_listening:
            recognizer = sr.Recognizer()

            with sr.Microphone() as source:
                print("Listening...")
                recognizer.pause_threshold = 1
                audio = recognizer.listen(source)

            try:
                print("Recognizing...")
                query = recognizer.recognize_google(audio, language='en-US')
                print(f"User said: {query}\n")

                if 'hello' in query.lower():
                    speak("Hello! How can i help you?")
                    print("Hello! How can I help you?")
                elif 'stop listening' in query.lower():
                    stop_listening_command()
                    print("Assistant stopped listening.")
                elif 'open notepad' in query.lower():
                    open_notepad()
                elif 'close notepad' in query.lower():
                    close_notepad()
                elif 'wikipedia' in query.lower():
                    query = query.replace("wikipedia", "")
                    wikipedia_search(query)
                elif 'search google for' in query.lower():
                    search_query = query.lower().replace("search google for", "").strip()
                    search_google(search_query)
                elif 'close browser' or 'close google' or 'close my browser' in query.lower():
                    close_browser()
                else:
                    print("Command not recognized. Please try again.")

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as re:
                print(f"Could not request results from Google Speech Recognition service; {re}")
            except Exception as e:
                print(e)
                print("Say that again, please...")
        else:
            print("Assistant stopped listening.")
            break  # Exiting the loop when the assistant stops listening