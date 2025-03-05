import speech_recognition as sr
import pyttsx3
import random
import time
from datetime import datetime

# Initialize speech recognizer and pyttsx3 engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Set voice propertiesy('voices')[3].id)  # Select a different voice (optional)
engine.setProperty('rate', 80)  # Speed of the voice (adjust as needed)
engine.setProperty('volume', 2)  # Volume level (0.0 to 1.0)

# Define command-response pairs
commands = {
    "hello": "Hello! How are you today?",
    "what's your name": "I am Emotional Alexa, your personal assistant.",
    "how are you": "I'm doing great, thanks for asking!",
    "exit": "Goodbye, take care!",
    "what time is it": "Let me check the time for you...",
    "tell me a joke": "Why don’t skeletons fight each other? They don’t have the guts!"
}

# Define additional functions for advanced interaction
def get_time():
    """Returns the current time as a string"""
    return datetime.now().strftime("%I:%M %p")

def tell_joke():
    """Returns a random joke"""
    jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "What do you get when you cross a snowman and a vampire? Frostbite.",
        "Why did the math book look sad? Because it had too many problems."
    ]
    joke = random.choice(jokes)
    print(f"Assistant: {joke}")
    return joke

def recognize_speech():
    """Listen for a command from the user"""
    with sr.Microphone() as source:
        print("Listening...")
        engine.say("Listening...")
        engine.runAndWait()

        # Adjust for ambient noise before listening
        r.adjust_for_ambient_noise(source, duration=2)  # Adjust to ambient noise
        audio = r.listen(source, timeout=20)  # Add a timeout to prevent hanging
        try:
            command = r.recognize_google(audio).lower()  # Recognize speech
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            engine.say("Sorry, I didn't understand that. Can you repeat?")
            engine.runAndWait()
            return None
        except sr.RequestError:
            engine.say("There seems to be an issue with the speech recognition service.")
            engine.runAndWait()
            return None

def respond(command):
    """Respond to the user based on recognized command"""
    if "what time is it" in command:
        response = get_time()
    elif "tell me a joke" in command:
        response = tell_joke()
    else:
        response = commands.get(command, "Sorry, I didn't understand that.")
    
    print(f"Assistant: {response}")
    engine.say(response)
    engine.runAndWait()

def main():
    """Main loop for continuous listening and interaction"""
    engine.say("Emotional Alexa is ready to listen. Say 'exit' to stop.")
    engine.runAndWait()

    while True:
        command = recognize_speech()
        if command == "exit":
            respond(command)
            break
        if command:
            respond(command)

if __name__ == "__main__":
    main()
