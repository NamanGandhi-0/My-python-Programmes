import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import time
import os
import random
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
def speak(text):
    """This function speaks any string passed to it."""
    engine.say(text)
    print(f"PYTHON said: {text}")
    engine.runAndWait()

def wishme():
    """This function wishes the user according to the time."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        whatwish = ("Good morning!")
    elif hour >= 12 and hour < 15:
        whatwish = ("Good afternoon!")
    else :
        whatwish = ("Good evening!")
    speak(f"Hey senor! {whatwish} I am PYTHON! How can I help you?")
def takeCommand():
    """This function takes microphone as the source and recognizes any thing said to it. It is currently using the google voice-recognition engine."""
    r = sr.Recognizer()
    with sr.Microphone(2) as source:
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        query = r.recognize_google(audio, language = 'en-in')
        print(f"Naman said: {query}\n")
    except Exception:
        speak("Pardon!")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Can you please tell me what to search about?")
            query = takeCommand()
            speak("Searching Wikipedia...")
            try:
                results = wikipedia.summary(query, sentences = 2)
                speak("Hmm..I've found something...")
                speak(f"According to wikipedia: {results}")
            except Exception:
                speak ("Can't find the page can you, please say it again.")
                query = takeCommand()
        elif "hi" or "hello" in query:
            hello_choices = ["Hello Sir!", "Hi Sir!", "How may I help you?"]
            speak(random.choice(hello_choices))
        elif "open youtube"  in query:
            webbrowser.get('windows-default').open('http://www.youtube.com')
            speak("Opening Youtube")
            time.sleep(4)
        elif "open stack overflow" in query:
            webbrowser.get('windows-default').open('http://www.stackoverflow.com')
            speak("Opening StackOverflow")
            time.sleep(4)
        elif "open twitter" in query:
            webbrowser.get('windows-default').open('http://www.twitter.com')
            speak("Opening Twitter")
            time.sleep(4)
        elif "open book website" in query:
            webbrowser.get('windows-default').open('http://www.b-ok.org')
            speak("Opening book website")
            time.sleep(4)
        elif "open google" in query:
            webbrowser.get('windows-default').open('http://www.google.com')
            speak("Opening Google")
            time.sleep(4)
        elif "play music" in query: 
            music_dir ="C:\\Users\\naman\\Music\\My songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))
            speak("Playing music")
            time.sleep(5)
        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%M")
            speak(f"The time is {strtime}")
        elif "open wattpad" in query:
            webbrowser.get('windows-default').open('http://www.wattpad.com')
            speak("Opening Wattpad")
            time.sleep(4)
        elif "thank you" in query :
            Welcomechoices  = ["You're welcome", "Always", "No problem"]
            speak(random.choice(Welcomechoices))
        elif "open vs code" in query:
            codepath = "C:\\Users\\naman\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)
            speak("Opening code")
            time.sleep(4)
        elif "open chrome" in query:
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
            speak("Opening Chrome")
            time.sleep(4)
        elif "quit" in query:
            break