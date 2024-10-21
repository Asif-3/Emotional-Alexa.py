
import speech_recognition as sr
import pyttsx3

Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

Define voice commands and responses
commands = {
    "hello": "Hello! How are you?",
    "what's your name": "My name is Assistant",
    "exit": "Goodbye!",
}

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None

def respond(command):
    response = commands.get(command, "Sorry, I didn't understand that.")
    print(f"Assistant: {response}")
    engine.say(response)
    engine.runAndWait()

def main():
    while True:
        command = recognize_speech()
        if command == "exit":
            break
        respond(command)

if __name__ == "__main__":
    main()
