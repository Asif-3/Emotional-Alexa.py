from flask import Flask, request, jsonify
import speech_recognition as sr
import pyttsx3
import webbrowser
import time

app = Flask(__name__)

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)

commands = {
    "hello": {
        "response": "Hello! How are you?",
        "rate": 150,
        "volume": 1.0
    },
    "what's your name": {
        "response": "My name is Emotional Alexa.",
        "rate": 175,
        "volume": 0.9
    },
    "exit": {
        "response": "Goodbye!",
        "rate": 125,
        "volume": 0.8
    },
    "what time is it": {
        "response": f"The current time is {time.strftime('%I:%M %p')}",
        "rate": 160,
        "volume": 1.0
    },
    "tell me a joke": {
        "response": "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "rate": 180,
        "volume": 0.95
    },
    "play music": {
        "response": "Playing your favorite tunes!",
        "rate": 200,
        "volume": 1.0
    },
    "open google": {
        "response": "Opening Google for you.",
        "rate": 150,
        "volume": 1.0
    },
    "open firefox": {
        "response": "Opening Firefox for you.",
        "rate": 150,
        "volume": 1.0
    }
}

def recognize_speech():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            return None

def respond(command):
    if command in commands:
        response_data = commands[command]
        response = response_data["response"]
        rate = response_data["rate"]
        volume = response_data["volume"]

        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        
        engine.say(response)
        engine.runAndWait()

        if command == "open firefox":
            webbrowser.get('firefox').open_new("https://www.google.com")

        return response
    else:
        response = "Sorry, I didn't understand that."
        engine.say(response)
        engine.runAndWait()
        return response

@app.route('/speak', methods=['POST'])
def speak():
    command = recognize_speech()
    if command:
        response = respond(command)
        return jsonify({'response': response})
    else:
        return jsonify({'response': "Sorry, I didn't understand that."})

if __name__ == "__main__":
    app.run(debug=True)
