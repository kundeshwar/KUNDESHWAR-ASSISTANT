import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)
def talk(text):
     engine.say(text)
     engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "kundeshwar" in command:
                command = command.replace("kundeshwar","")
                print(command)
    except:
        pass

    return command
def run_kundeshwar():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play","")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("my name kundeshwar ,current time is" + time)

    elif "google" in command:
        person = command.replace("google","")
        info = wikipedia.summary(person,3)
        talk(info)

    elif "wikipedia" in command:
        person = command.replace("wikipedia","")
        info = wikipedia.summary(person,3)
        talk(info)

    elif "tell me " in command:
        person = command.replace("tell me","")
        info = wikipedia.summary(person,3)
        talk(info)

    elif "give the" in command:
        person = command.replace("give the","")
        info = wikipedia.summary(person,3)
        talk(info)
        
    elif "joke" in command:      
        talk(pyjokes.get_joke())

    elif "how are you" in command:
        talk("I fine, thanks for asking and what's about you ")

    elif "you are single" in command:
        talk("no, i am not single . i love with my mom and dad")

    elif "what is about your education" in command:
        talk(" I completed my school in my town gangakhed, I done my graduation in mechanical engineering from Dr.BATU college in lonere . currently i studied in Indian institude of techanology bombay (iit bombay) in esed department. I secured gate all india rank 155 in 2022 and also secured gate all india rank 1555 in 2021 , I also secures air 1 in my university ")
    
    elif "birthday" in command:
        talk("my birthday on 10th july and my birth date is 10th july 2000")

    elif "birth date" in command:
        talk("my birth date is 10th july 2000") 

    else:
        talk("I don't understand your voice plese repeat your sentence")

while True:
      run_kundeshwar()