import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import google.generativeai as genai
import os

#-->using gemini api key
os.environ['GOOGLE_API_KEY'] = "AIzaSyCPTIO-TyIH1OPGh8hP3ZOtZ-kBPRfRrvE"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


def ai(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    a=response.text
    print(a)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Navi Your Assistant. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()


    with sr.Microphone() as source:
        print('Listening')


        r.pause_threshold = 1
        audio = r.listen(source)


        try:
            print("Recognizing")


            Query = r.recognize_google(audio, language='en-in')
            print("User Input=", Query)

        except Exception as e:
            print(e)
            print("Say That Again Sir")
            return "None"

        return Query


def speak(audio):

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)

    #--> Method for the speaking of the assistant
    engine.say(audio)

    engine.runAndWait()


def tellDay():

    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("Today is " + day_of_the_week)



def Take_query():

    while (True):


        query = takeCommand().lower()

        #-->for student conenice we use students websites

        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks ")

            webbrowser.open("www.geeksforgeeks.com")
            continue
        elif "open javatpoint" in query:
            speak("Opening javatpoint ")


            webbrowser.open("www.javatpoint.com")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "which day it is" in query:
            tellDay()
            continue

        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "using gemini" in query:
            ai(prompt=query)

        #-->this will exit and terminate the program
        elif "bye" in query:
            speak("Bye. Check Out GFG for more exciting things")
            exit()


if __name__ == '__main__':

    wishMe()
    tellDay()
    Take_query()
