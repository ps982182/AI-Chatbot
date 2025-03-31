from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

# Initialize chatbot
chatbot = ChatBot("SmartBot")
trainer = ChatterBotCorpusTrainer(chatbot)

# Train chatbot with built-in corpus
trainer.train("chatterbot.corpus.english")

# Speech recognition function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"User: {text}")
        return text
    except:
        return "Sorry, I couldn't understand you."

# Text-to-speech function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Get chatbot response
def get_response(user_input):
    response = str(chatbot.get_response(user_input))
    return response
