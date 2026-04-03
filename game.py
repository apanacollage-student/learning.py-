# ===================== IMPORTS =====================
import speech_recognition as sr
import pyttsx3
import datetime
import os
import wikipedia
import cv2
import pyautogui
import psutil
import random

# ===================== VOICE ENGINE =====================
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        return ""

# ===================== FACE DETECTION =====================
def face_scan():
    speak("Scanning face")
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    detected = False
    while True:
        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            detected = True

        cv2.imshow("Jarvis Face Scan", frame)

        if detected:
            speak("Face detected. Access granted.")
            break

        if cv2.waitKey(1) == 13:  # Enter key
            break

    cam.release()
    cv2.destroyAllWindows()

# ===================== PC CONTROL =====================
def shutdown_pc():
    speak("Shutting down system")
    os.system("shutdown /s /t 5")

def restart_pc():
    speak("Restarting system")
    os.system("shutdown /r /t 5")

def volume_up():
    pyautogui.press("volumeup")
    speak("Volume increased")

def volume_down():
    pyautogui.press("volumedown")
    speak("Volume decreased")

def mute_volume():
    pyautogui.press("volumemute")
    speak("Volume muted")

def take_screenshot():
    img = pyautogui.screenshot()
    img.save("jarvis_screenshot.png")
    speak("Screenshot taken")

def system_status():
    battery = psutil.sensors_battery()
    if battery:
        speak(f"Battery is at {battery.percent} percent")
    else:
        speak("Battery information not available")

# ===================== AI BRAIN (CHATGPT-STYLE) =====================
motivations = [
    "Consistency beats talent.",
    "You are already ahead because you started.",
    "Great things take time. Keep going.",
    "Future belongs to those who learn every day."
]

# ===================== START JARVIS =====================
speak("Hello.i am ayush")
print("🤖 ayush")

while True:
    command = listen()

    if command == "":
        continue

    # ---- TIME / DATE ----
    if "time" in command:
        speak(datetime.datetime.now().strftime("Time is %H:%M"))

    elif "date" in command:
        speak(str(datetime.date.today()))

    # ---- OPEN APPS ----
    elif "open chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open explorer" in command or "open files" in command:
        speak("Opening File Explorer")
        os.system("explorer")

    # ---- INTERNET BRAIN ----
    elif command.startswith("who is") or command.startswith("what is"):
        try:
            speak("Searching internet")
            result = wikipedia.summary(command, sentences=2)
            speak(result)
        except:
            speak("Sorry, I could not find a clear answer.")

    # ---- CHATGPT STYLE LOGIC ----
    elif "who are you" in command:
        speak("I am Jarvis. An artificial intelligence built to help you grow.")

    elif "motivate me" in command:
        speak(random.choice(motivations))

    elif " hello who am i" in command:
        speak("You are a future AI engineer in the making.")

    # ---- FACE SECURITY ----
    elif "scan my face" in command or "identify me" in command:
        face_scan()

    # ---- PC FULL CONTROL ----
    elif "shutdown pc" in command:
        shutdown_pc()

    elif "restart pc" in command:
        restart_pc()

    elif "volume up" in command:
        volume_up()

    elif "volume down" in command:
        volume_down()

    elif "mute volume" in command:
        mute_volume()

    elif "take screenshot" in command:
        take_screenshot()

    elif "system status" in command or "battery" in command:
        system_status()

    # ---- EXIT ----
    elif "exit" in command or "shutdown jarvis" in command:
        speak("Shutting down Jarvis. Remember, consistency beats talent.")
        break

    # ---- FALLBACK ----
    else:
        speak("I am still learning. Teach me more.")
