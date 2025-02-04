import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

# Initialize the voice engine
engine = pyttsx3.init()
engine.setProperty("rate", 180)
engine.setProperty("volume", 1.0)

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Takes voice input from the user and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I'm listening...")
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that. Please try again.")
        except sr.RequestError:
            speak("There seems to be an issue with the speech recognition service. Please check your connection.")
        except Exception as e:
            print(f"An error occurred: {e}")
            speak("An error occurred. Please try again.")
    return None

def get_formatted_datetime(format_type):
    """Returns the current time or date in a specific format."""
    now = datetime.datetime.now()
    if format_type == "time":
        return now.strftime("%I:%M %p")
    elif format_type == "date":
        return now.strftime("%B %d, %Y")

def handle_command(query):
    """Processes and executes user commands."""
    if "time" in query:
        speak(f"The time is {get_formatted_datetime('time')}")
    elif "date" in query:
        speak(f"Today's date is {get_formatted_datetime('date')}")
    elif "hello" in query:
        speak("Hello! I hope you're having a great day.")
    elif "open google" in query:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "search" in query:
        speak("What would you like to search for?")
        search_query = take_command()
        if search_query:
            speak(f"Searching for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif any(word in query for word in ["bye", "stop", "exit"]):
        speak("Goodbye! Have a great day.")
        return False
    else:
        speak("I didn't understand that. Please try again.")
    return True

def main():
    """Runs the assistant in a loop."""
    speak("Hello! I am your assistant. How can I assist you?")
    while True:
        query = take_command()
        if query and not handle_command(query):
            break
    speak("Shutting down. Goodbye!")

if _name_ == "_main_":
    main()
