from transformers import pipeline
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import random

# Initialize the text generation model
text_generator = pipeline("text-generation", model="gpt2")

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Set to male voice
engine.setProperty('voice', voices[0].id)  # Change index if needed
engine.setProperty('rate', 150)

# Define the dataset with Maveli's information and responses
maveli_responses = {
    "onam": [
        "എന്റെ സുഹൃത്തുക്കളെ! ഓണം സന്തോഷത്തിന്റെ സീസൺ ആണ്.",
        "ഞാൻ മാവേലി, എന്റെ ജനങ്ങൾക്കായുള്ള ഓണം, സന്തോഷത്തോടെ ആഘോഷിക്കാം!"
    ],
    "maveli": [
        "ഞാനാണ് മാവേലി, രാജാവെന്നുമെന്നെ വിളിക്കു.",
        "എന്റെ പ്രായം എപ്പോഴും 1000 വർഷമാണ്."
    ],
    # Add more responses as needed
}

def generate_response(prompt):
    """Generate a response using the predefined responses in Maveli's slang."""
    for keyword in maveli_responses:
        if keyword in prompt.lower():
            return random.choice(maveli_responses[keyword])
    return "മനസ്സിലായില്ല, എനിക്ക് ചോദിക്കണം."

def listen_to_voice():
    """Listen for audio input and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="ml-IN")
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def speak(text):
    """Convert the given text to speech using pyttsx3."""
    engine.say(text)
    engine.runAndWait()  # Wait until the speech is finished

def chat():
    """Handle text-based chat interaction."""
    while True:
        user_input = input("You (type 'exit' to go back): ")
        if user_input.lower() == 'exit':
            return  # Exit chat and return to the main menu
        response = generate_response(user_input)
        print(f"Maveli says: {response}")
        speak(response)  # Convert response to speech

def main():
    """Main function to choose interaction mode."""
    while True:
        print("Choose input method:")
        print("1. Voice")
        print("2. Text chat")
        print("3. Exit")
        choice = input("Enter 1, 2, or 3: ")
        
        if choice == '1':
            while True:
                user_input = listen_to_voice()
                if user_input:
                    if user_input.lower() == 'exit':
                        break  # Exit voice listening loop
                    response = generate_response(user_input)
                    print(f"Maveli says: {response}")
                    speak(response)  # Convert response to speech
        elif choice == '2':
            chat()  # Handle text chat
        elif choice == '3':
            print("Exiting... Goodbye!")
            break  # Exit the main loop
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
