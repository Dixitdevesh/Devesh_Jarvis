import speech_recognition as sr
import webbrowser
import pyttsx3
import random
import os

tell = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    tell.say(text)
    tell.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            audio = r.listen(source, timeout=12, phrase_time_limit=15)
            print("Recognizing...")
            command = r.recognize_google(audio)
            print(f"You Said: {command}")
            return command
    except Exception as e:
        print(f"Error: {e}")
        return ""

def menu():
    print("\n" + "="*30)
    print("  Jarvis Menu")
    print("="*30)
    print("  **Web Browsing** 📊")
    print("  1. Open Google 🌐")
    print("  2. Open Facebook 👥")
    print("  3. Open Instagram 📸")
    print("  4. Open YouTube 📺")
    print("  5. Open Email 📧")
    
    print("\n  **Entertainment** 🎵")
    print("  6. Play Music 🎶")
    print("  7. Truth and Dare 😜")
    
    print("\n  **Productivity** 📊")
    print("  8. Calculate 📝")
    
    print("\n  **Applications** 📈")
    print("  9. Open Application 📊")
    print("  10. Close Application ❌")
    
    print("\n  **Help** 🤔")
    print("  11. Show Help")
    
    print("\n  **About** 🤔")
    print("  12. About Jarvis")
    
    print("\n  **Conversation** 💬")
    print("  13. Talk to me!")
    
    print("\n  **Exit** 👋")
    print("  99. Exit Jarvis")
    print("="*30)

def about():
    print("\n" + "="*30)
    print("  About Jarvis")
    print("="*30)
    print("  Created by: Devesh Dixit")
    print("  Assisted by: Sumit Kumar")
    print("="*30)

def process(command):
    command = command.lower()
    if command == "open google":
        print("Opening Google...")
        speak("Opening Google...")
        webbrowser.open("https://google.com")
    elif command == "open facebook":
        print("Opening Facebook...")
        speak("Opening Facebook...")
        webbrowser.open("https://facebook.com")
    elif command == "open instagram":
        print("Opening Instagram...")
        speak("Opening Instagram...")
        webbrowser.open("https://instagram.com")
    elif command == "open youtube":
        print("Opening YouTube...")
        speak("Opening YouTube...")
        webbrowser.open("https://youtube.com")
    elif "open email" in command:
        print("Opening Email...")
        speak("Opening Email...")
        webbrowser.open("https://mail.google.com")
    elif command.startswith("search on google"):
        search_term = command.replace("search on google", "").strip()
        if search_term:
            speak(f"Searching Google for {search_term}...")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        else:
            speak("Please specify what you want to search on Google.")
    elif command.startswith("search on youtube"):
        search_term = command.replace("search on youtube", "").strip()
        if search_term:
            speak(f"Searching YouTube for {search_term}...")
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_term}")
        else:
            speak("Please specify what you want to search on YouTube.")
    elif command.startswith("play"):
        song = command.split("play ")[-1]
        speak(f"Searching and playing {song}...")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    elif command == "truth and dare":
        play_truth_and_dare()
    elif command == "calculate":
        speak("Initializing Calculator ...")
        while True:
            speak("Tell me the first number:")
            a = listen()
            speak("Tell me the second number:")
            b = listen()
            speak("What operation would you like to perform? (add, subtract, multiply, divide)")
            operation = listen().lower()

            try:
                a = float(a)
                b = float(b)
                if operation == 'add':
                    result = a + b
                elif operation == 'subtract':
                    result = a - b
                elif operation == 'multiply':
                    result = a * b
                elif operation == 'divide':
                    result = a / b
                else:
                    result = "Invalid operation."
                speak(f"The result is {result}.")
                print(f"The result is {result}.")
            except ValueError:
                speak("Please provide valid numbers.")

            speak("Do you want to continue? (yes or no)")
            continue_calculating = listen().lower()
            if "no" in continue_calculating:
                break
    elif "open application" in command:
        speak("Please tell me which application you want to open.")
        app_name = listen()
        os.system(f'start {app_name}.exe')  # Assumes .exe files are in the PATH
        speak(f"Opening {app_name}...")
    elif "close application" in command:
        speak("Please tell me which application you want to close.")
        app_name = listen()
        os.system(f'taskkill /f /im {app_name}.exe')  # Assumes the app is running
        speak(f"Closing {app_name}...")
    elif "help" in command:
        menu()
    elif "about" in command:
        about()
    elif "talk to me" in command:
        engage_conversation()
    elif command in ["exit", "stop"]:
        print("Exiting.....")
        speak("Exiting......")
        return False
    else:
        print("Command not recognized.")
        speak("I'm sorry, I didn't understand that.")
    return True

def play_truth_and_dare():
    print("Welcome to Truth or Dare!")
    speak("Welcome to Truth or Dare!")
    while True:
        speak("Do you choose Truth or Dare?")
        choice = listen().lower()
        if "truth" in choice:
            truth = random.choice([
                "What is your biggest fear?",
                "What is one thing you would change about yourself?",
                "Who is your crush?",
                "What is the most embarrassing thing that has ever happened to you?",
                "What secret do you keep from everyone?",
                "If you could have dinner with anyone in the world, who would it be?",
                "What is your biggest pet peeve?",
                "What is the weirdest dream you have ever had?",
            ])
            speak(truth)
        elif "dare" in choice:
            dare = random.choice([
                "Dance like nobody's watching for 30 seconds.",
                "Sing your favorite song loudly.",
                "Do 10 push-ups.",
                "Try to lick your elbow.",
                "Let someone give you a funny hairstyle.",
                "Talk in an accent for the next 3 minutes.",
                "Post an embarrassing photo on social media.",
                "Do your best impression of a celebrity.",
            ])
            speak(dare)
        else:
            speak("Please choose either Truth or Dare.")
        
        speak("Do you want to play again? (yes or no)")
        play_again = listen().lower()
        if "no" in play_again:
            speak("Thanks for playing!")
            break

def engage_conversation():
    speak("I'm here to chat! What would you like to talk about?")
    while True:
        topic = listen().lower()
        if "exit" in topic or "stop" in topic:
            speak("Okay, I will stop talking now.")
            break
        elif "how are you" in topic:
            speak("I'm just a program, but I'm here to help you! How can I assist you today?")
        elif "what can you do" in topic:
            speak("I can help you browse the web, play games, calculate, and much more! What would you like to do?")
        elif "tell me a joke" in topic:
            joke = random.choice([
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "I told my computer I needed a break, and now it won't stop sending me beach wallpapers!",
                "Why don’t scientists trust atoms? Because they make up everything!",
                "Why did the bicycle fall over? Because it was two-tired!",
            ])
            speak(joke)
        else:
            speak("That's interesting! Can you tell me more?")

def st():
    while True:
        print("Showing Menu, Please Wait...")
        speak("Showing Menu, Please Wait...")
        menu()
        
        while True:
            print("Taking Command, Please Speak.")
            command = listen()
            if not process(command):
                break

if __name__ == '__main__':
    print("Initializing Jarvis...")
    speak("Initializing Jarvis...")
    st()
