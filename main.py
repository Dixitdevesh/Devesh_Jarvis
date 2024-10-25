import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime,time,csv,random,musiclibrary,os,requests
from getpass import getpass
x=False
tell=pyttsx3.init()
r=sr.Recognizer()

def speak(text):
    tell.say(text)
    tell.runAndWait()
def listen():
     try: 
        with sr.Microphone() as source:
                print("Listening....")
                audio=r.listen(source,timeout=12,phrase_time_limit=15)
                print("Recognizing...")
                command=r.recognize_google(audio)
                print(f"You Said:{command}")
                return command
     except Exception as e :
        if x==False:
            process(listen())
        elif x==True:
            st()
        

def menu():
    print("  Jarvis Menu")
    print("  ------------")

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
    print("  9. Calculate 📝")
    print("  10. School Management 📚")
    
    

    print("\n  **Applications** 📈")
    print("  12. Open Application 📊")
    print("  13. Close Application ❌")

    print("\n  **About** 🤔")
    print("  14. Menu")
    print("  15.Details")

    print("\n  **Exit** 👋")
    print("  99. Exit Jarvis")



def name():
        try:
            with open("data.txt","a") as d:
                speak("Sir Please Tell me Your Name With Surname") 
                with sr.Microphone() as source:
                    print("Listening...")
                    r.pause_threshold=1
                    audio=r.listen(source)
                    print("Recognizing...")
                    name=r.recognize_google(audio)
                    if len(name.split())>2:
                        n=name.split()
                        name=n[-2]+' ' +n[-1]
                        x=random.choice(["Hello ","Nice to Meet you ","Welcome "])
                        print(x + " " + name)
                        speak(x + " " + name)
                        d.write(f"{name}\n")
                    else:
                        x=random.choice(["Hello ","Nice to Meet you ","Welcome "])
                        print(x + " " + name)
                        speak(x + " " + name)
                        d.write(f"{name}\n")

                    
        except Exception as e:
             print("Error" ,e)

def login():
    speak("Welcome to Jarvis. Do you have an account? Say yes i have a to log in or no i don't hava any to register.")
    response = listen()
    if "yes" in response.lower() :
        try:
           return authenticate_user()
        except Exception as e:
            print("Some Error occured")
            login()
    elif "no" in response.lower() :
        try:
            return register_user()
        except Exception as e:
            print("some error occured")
            login()
    else:
        speak("I didn't catch that. Please try again.")
        return login()

def authenticate_user():
    try:
        with open("users.csv", "r") as f:
            reader = csv.reader(f)
            users = {rows[0]: rows[1] for rows in reader}
    except FileNotFoundError:
        speak("No users found. Please register first.")
        return register_user()

    speak("Please Write your username.")
    username = input("Enter Your Username :")
    speak("Please Write your password.")
    password = getpass("Enter the Password:")

    if username in users and users[username] == password:
        speak("Login successful.")
        return True
    else:
        speak("Invalid username or password. Please try again.")
        return login()

def register_user():
    try:
        with open("users.csv", "a",newline='') as f:
            writer = csv.writer(f)
            speak("Please tell us  a username.")
            username = input("Enter Username :")
            speak("Please Create A password.")
            password = getpass("Enter your Password:")
            writer.writerow([username,password])
            f.flush()
            speak("Registration successful. You can now log in.")
            return authenticate_user()
    except Exception as e:
        print("Error:", e)
        speak("An error occurred during registration.")
        return False       
def process(c):
    if c.lower()=="open google":
          print("Opening Google...")
          speak("Opening Google...")
          webbrowser.open("https://google.com")
    elif c.lower()=="open facebook":
          print("Opening Facebook...")
          speak("Opening Facebook...")
          webbrowser.open("https://facebook.com")
    elif c.lower()=="open instagram":
          print("Opening instagram...")
          speak("Opening instagram...")
          webbrowser.open("https://instagram.com")
    elif c.lower()=="open youtube":
          print("Opening Youtube...")
          speak("Opening Youtube...")
          webbrowser.open("https://youtube.com")
    elif "open email" in c.lower():
        print("Opening Email")
        speak("Opening Email")
        webbrowser.open("https://mail.google.com")
    elif c.lower().startswith("play"):
         song=c.lower().split(" ")[1]
         link=musiclibrary.music[song]
         speak(f"Playing {song}")
         webbrowser.open(link) 
    elif c.lower()=="calculate":
         speak("Initializing Calculator ...")
         def calculate(a,b,c):
                   a=int(a)
                   b=int(b)
                   
                   if c.lower()=='first':
                        return a+b
                   elif c.lower()=="second":
                        return a-b
                   elif c.lower()=="third":
                        return a*b
                   elif c.lower()=="fourth":
                        return a/b
                   elif c.lower()=="fifth":
                        a**b
                   else :
                        return "Sorry You are Using Wrong expression"

         while True:
              speak("Tell Me first Number :")
              a=listen()
              print(a)
              print(type(a))
              speak("Tell Me second Number :")
              b=listen()
              
              speak("Which Of the Following Expression Will Have to Use But in only Number :")
              print("first: ' + '\nsecond:'-' \nthird:'*' \nfourth:'\' \nfifth:'**' " )
              c=listen()
              
              print(calculate(a,b,c))
              speak(calculate(a,b,c))
              speak("SIr, Do You Want to Continue :")
              c=listen()
              if "no"  in c :
                   print("Exiting Calculator")
                   speak("Exiting.......")
                   break             
    elif "truth and dare" in c.lower():
       print("Welcome to Truth or Dare!")
       speak("Welcome to Truth or Dare!")
       game_log = "game_log.csv"
    
       with open(game_log, "a", newline="") as f:
           writer = csv.writer(f)
           if f.tell() == 0:
              writer.writerow(["Timestamp", "Player Name", "Choice", "Question/Dare", "Answer/Response"])
        
           while True:
             print("What is Your Name!")
             speak("What is Your Name!")
             player_name = listen()
             print("What Do You Want To Choose (Truth/Dare ) Please tell me sir")
             speak("What Do You Want To Choose (Truth/Dare ) Please tell me sir")
             choice = listen()
             if choice.lower() == "truth":
                print("You chose Truth!")
                speak("You chose Truth!")
                truth = random.choice(["What is your favorite food?", "What is your favorite hobby?", "What is your favorite movie?"])
                print(truth)
                speak(truth)
                print("Please answer the question: ")
                speak("Please answer the question: ")
                answer = listen()
                writer.writerow([datetime.datetime.now(), player_name, "Truth", truth, answer])
             elif choice.lower() == "d":
                speak("You chose Dare!")
                print("You chose Dare!")
                dare = random.choice(["Do 10 jumping jacks.", "Sing a silly song out loud.", "Do a funny dance."])
                print(dare)
                speak(dare)
                print("Did you complete the dare? (Y/N) ")
                response = listen()
                writer.writerow([datetime.datetime.now(), player_name, "Dare", dare, response])
             else:
                print("Invalid choice. Try again!")
                speak("Invalid Choice Try Again!")
             print("Do you want to play again? (Yes/No) ")
             play_again = listen()
             if play_again.lower() =="no":
                 break
    elif 'school management'  in c.lower():
        STUDENTS_FILE = 'students.csv'
        TEACHERS_FILE = 'teachers.csv'
        CLASSES_FILE = 'classes.csv'

        students = []
        teachers = []
        classes = []

        def save_data():
            global students, teachers, classes

            def write_data(file, fieldnames, data):
                with open(file, 'a', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    if f.tell() == 0:  # check if file is empty
                        writer.writeheader()
                    writer.writerows(data)

                write_data(STUDENTS_FILE, ['name', 'age', 'grade'], students)
                write_data(TEACHERS_FILE, ['name', 'subject'], teachers)
                write_data(CLASSES_FILE, ['name', 'teacher'], classes)

        def save_data():
            global students, teachers, classes

            with open(STUDENTS_FILE, 'a', newline='') as file:
                fieldnames = ['name', 'age', 'grade']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(students)

            with open(TEACHERS_FILE, 'a', newline='') as file:
                fieldnames = ['name', 'subject']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(teachers)

            with open(CLASSES_FILE, 'a', newline='') as file:
                fieldnames = ['name', 'teacher']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(classes)


        def add_student(name, age, grade):
            students.append({"name": name, "age": age, "grade": grade})
            save_data()

        def add_teacher(name, subject):
            teachers.append({"name": name, "subject": subject})
            save_data()

        def add_class(name, teacher):
            classes.append({"name": name, "teacher": teacher})
            save_data()

        def view_students():
            for student in students:
                print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

        def view_teachers():
            for teacher in teachers:
                print(f"Name: {teacher['name']}, Subject: {teacher['subject']}")

        def view_classes():
            for class_ in classes:
                print(f"Name: {class_['name']}, Teacher: {class_['teacher']}")

        def search_student(name):
            for student in students:
                if student["name"] == name:
                    return student
            return None

        def search_teacher(name):
            for teacher in teachers:
                if teacher["name"] == name:
                    return teacher
            return None

        def search_class(name):
            for class_ in classes:
                if class_["name"] == name:
                    return class_
            return None

        def main():
            while True:
                print("First. Add Student")
                print("Second. Add Teacher")
                print("Third. Add Class")
                print("Fourth. View Students")
                print("Fifth. View Teachers")
                print("Sixth. View Classes")
                print("Seventh. Search Student")
                print("Eigth. Search Teacher")
                print("Nineth. Search Class")
                print("Tenth. Exit")
                speak("CHoose The Appropriate Option")
                choice = listen()

                if 'first' in choice.lower():
                    print("Please Tell me Student Name")
                    speak("Please Tell me Student Name")
                    name = listen()
                    print("Please Tell me Student age")
                    speak("Please Tell me Student age")
                    age = listen()
                    print("Please Tell me Student Grade")
                    speak("Please Tell me Student Grade")
                    grade = listen()
                    add_student(name, age, grade)
                elif "second" in choice.lower():
                    print("Please Tell me Teacher Name ")
                    speak("Please Tell me Teacher Name")
                    name = listen()
                    print("Please Tell me Teacher Subject")
                    speak("Please Tell me Teacher Subject")
                    subject = listen()
                    add_teacher(name, subject)
                elif "third" in choice.lower():
                    print("Please Tell me Class Name ")
                    speak("Please Tell me Class Name ")
                    name = listen()
                    print("Please Tell me Class Teacher Name ")
                    speak("Please Tell me Class Teacher Name ")
                    teacher = listen()
                    add_class(name, teacher)
                elif "fourth" in choice.lower():
                    view_students()
                elif "fifth" in choice.lower():
                    view_teachers()
                elif "sixit" in choice.lower():
                    view_classes()
                elif "seventh" in choice.lower():
                    print("Which Student Do You Want to Search")
                    speak("Which Student Do You Want to Search")
                    name = listen()
                    student = search_student(name)
                    if student:
                        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
                    else:
                        print("Student not found")
                elif "eigth" in choice.lower():
                    print("Which Teacher Do You Want To Search")
                    speak("Which Teacher Do You Want To Search")
                    name = listen()
                    teacher = search_teacher(name)
                    if teacher:
                        print(f"Name: {teacher['name']}, Subject: {teacher['subject']}")
                    else:
                        print("Teacher not found")
                elif "nineth" in choice.lower():
                    print("Tell Me Which Class Info DO You Wanr ")
                    speak("Tell Me Which Class Info DO You Wanr ")
                    name = listen()
                    class_ = search_class(name)
                    if class_:
                        print(f"Name: {class_['name']}, Teacher: {class_['teacher']}")
                    else:
                        print("Class not found")
                elif "tenth" in choice.lower():
                    print("Exiting...")
                    speak("Exiting...")
                    break
                else:
                    print("Invalid choice! Please try again.")

        main()
    elif 'open application' in c.lower() or 'open' in c.lower() :
        def op(l):
            if l=='calculator':
                l='C:\Windows\SysWOW64\calc'
                speak(f"opening calculator...")
                os.system(l+".exe")
                speak("calculator Successfully opened")
            else:
                speak(f"Opening {l}...")
                os.system(l+".exe")
                speak("{l} Successfully opened")
                
            
        if len(c)==16:
            if 'application' in c.lower():
                print("Sir Please Tell Me Which Application Do You Want To Open")
                speak("Sir Please Tell Me Which Application Do You Want To Open")
                l=listen()
                op(l)
            else :
                x=c.split()
                if len(x)==2:
                    op(x[1])
                else:
                    print("Try Again")
                    speak("Try Again")
        else:
            x=c.split()
            if len(c)==2:
                op(x[1])
            else:
                op(x[-1])
    elif 'close application' in c.lower() or 'close' in c.lower():
        def op(l):
            if l=='calculator':
                l='calculatorapp'
                #l=r'C:\Windows\SysWOW64\calc'
                print(f"Closing Calculator...")
                speak(f"Closing Calculator...")
                os.system(f"taskkill /f /im {l}.exe")
                speak("Closed Successfully")
            else:
                print(f"Closing {l}...")
                speak(f"Closing {l}...")
                os.system(f"taskkill /im {l}.exe")
                speak("Closed Successfully")
                 
            
        if len(c)==17:
            if 'application' in c.lower():
                print("Sir Please Tell Me Which Application Do You Want To Close")
                speak("Sir Please Tell Me Which Application Do You Want To Close")
                l=listen()
                op(l)
            else :
                x=c.split()
                if len(x)==2:
                    op(x[1])
                else:
                    print("Try Again")
                    speak("Try Again")
        else:
            x=c.split()
            if len(c)==2:
                op(x[1])
            else:
                op(x[-1])    
    elif 'menu' in c.lower ():
        menu()   
    elif 'details' in c.lower():
          print("  Jarvis Details")
          print("  ------------")

          print("  1. Open Google - Open Google in your default browser")
          print("  2. Open Facebook - Open Facebook in your default browser")
          print("  3. Open Instagram - Open Instagram in your default browser")
          print("  4. Open YouTube - Open YouTube in your default browser")
          print("  5. Play Music - Play music On Youtube Using Links That are Given")
          print("  6. Calculate - Perform calculations using Jarvis")
          print("  7. Truth and Dare - Play a game of Truth and Dare")
          print("  9. Game - Rock/Paper/Seccior ")
          print("  8. School Management - Manage school-related tasks")
          print("  10. Countdown - Start a countdown timer")
          print("  11. Reminder - To Set a Reminder ")
          print("  12. Open Application - Open an application on your computer")
          print("  13. Close Application - Close an application on your computer")
          print("  19. Exit - Exit Jarvis")
    
def st():
        if login()==True:
            x=True
            name()
            while True:
                try:
                    print("Showing Menu Please Wait...")
                    speak("Showing Menu Please Wait...")
                    menu()  
                    
                    while True:
                        print("Taking Command, Please Speak ")
                        command = listen()
                        
                        if command.lower() == "exit" or "stop" in command.lower():
                            print("Exiting.....")
                            speak("Exiting......")
                            break 
                        else:
                            process(command)
                                    
                except Exception as e:
                    print("No Internet Connection",e)
                    
        
            

if __name__=='__main__':
    print("Initializing Jarvis...")
    speak("Initializing   Jarvis ......")
    st()           

        
