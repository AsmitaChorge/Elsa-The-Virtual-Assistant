from tkinter import *
from PIL import Image
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import webbrowser
import os
from googletrans import Translator, LANGUAGES
from pywhatkit import sendwhatmsg
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from tkinter import messagebox
from newsapi import NewsApiClient
import pyautogui
import wmi

listener = sr.Recognizer()
engine = pyttsx3.init()

#gui
root = Tk()
root.title('Personal Virtual Assistant')
root.geometry("800x700")
root.configure(background='white')
frame = Frame(root, width=200, height=100)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# inserting images
img = ImageTk.PhotoImage(Image.open("C:/Users/SIDDHI/Desktop/11.jpg"))
text_label =Label(root, text="Hello,I am your \nVirtual Assistant",bg='white',fg='black',pady=10,padx=140,font=("Copperplate Gothic Bold",25,"bold"))
text_label.pack(anchor="center",padx=10,pady=10)


label = Label(frame, image = img)
label.pack()




listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()



#for listening and recognizing
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")

        # Define 'command' before entering the loop
        command = ""

        # Split the query into individual words
        words = query.split()

        # Iterate over each word in the query
        for word in words:
            # Append the word to the command string
            command += word + " "

        # Return the command string
        return command.strip()

    except Exception as e:
        print("Error: ", e)
        return ""


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('your email', 'your password')
    email = EmailMessage()
    email['From'] = 'your email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    talk(f"Here's what I found on Google for '{query}'")
email_list = {
    'dude': 'COOL_DUDE_EMAIL',
    'bts': 'diamond@bts.com',
    'pink': 'jennie@blackpink.com',
    'lisa': 'lisa@blackpink.com',
    'Ashwini': 'ashupawar2426@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = take_command()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = take_command()
    talk('Tell me the text in your email')
    message = take_command()
    send_email(receiver, subject, message)
    talk('Hey lazy ass. Your email is sent')

def get_email_info():
    talk('To Whom you want to send email')
    name = take_command()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = take_command()
    talk('Tell me the text in your email')
    message = take_command()
    send_email(receiver, subject, message)
    talk('Your email is sent')


def open_cmd_prompt():
    os.system("start cmd")
    talk('Command Prompt is opened.')
#creating a folder 
def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        talk(f"Folder '{folder_name}' has been created successfully.")
    except Exception as e:
        talk(f"An error occurred while creating the folder: {str(e)}")

# Taking screenshot 
def take_screenshot():

    # Capture the screenshot.
    screenshot = pyautogui.screenshot()

    # Save the screenshot to the desktop.
    screenshot.save(os.path.join(os.path.expanduser("~"), "Desktop", "screenshot.png"))
    talk('Screenshot taken and saved to the desktop.')

#open google
def open_website(website):
    try:
        # This will open the webpage in default web browser.
        webbrowser.open(website)
        talk(f'Opening {website}.')
    except Exception as e:
        talk(f"An error occurred while opening the website: {str(e)}")

#news update 
def get_news_update(update_category):
    newsapi = NewsApiClient(api_key='9976eb77552645f281bc012e109e8e18')
    top_headlines = newsapi.get_top_headlines(category=update_category)

    news = top_headlines['articles']
    news_string = ''

    for article in news:
        news_string += f"{article['title']}. "


    talk(news_string)
def run_Elsa():
    command = take_command()
    
    print(command)
    
    if 'translate' in command:
        lang_to = 'es'
        command = command.replace('translate', '')
        translator = Translator()
        translated = translator.translate(command, dest=lang_to)
        talk(f"Translation is: {translated.text}")

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'search' in command:
        query = command.replace('search', '')
        search_google(query)

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'owner' in command:
        talk('The owner of this device is ASHWINI ASMITA SIDDHI SHARVANI')
    elif 'who are you' in command:
        talk('hello my name is elsa. your virtual personal assistant') 
    elif "how are you" in command:
        talk('i am fine.how can i help you') 
    elif 'create folder' in command:
        folder_name = command.replace('create folder', '')
        create_folder(folder_name) 
        create_folder(folder_name)
    elif 'calculator' in command:
        try:
            # The command for opening the calculator in Windows is different in other OS.
            # Here is an example for Windows.
            os.system("start calc.exe")
            talk('Calculator is opened.')
        except Exception as e:
            talk(f"An error occurred while opening the calculator: {str(e)}")
    
    elif 'screenshot' in command:
        take_screenshot()

    elif 'news update' in command:
        news_category = command.replace('news update', '')
        get_news_update(news_category)

    elif 'open command prompt' in command:
            open_cmd_prompt()

    # elif 'send email' in command:
    #     # Check for sending an email command
    #     talk('To whom do you want to send an email?')
    #     recipient_name = take_command().lower()
        
    #     # Define your email list as a dictionary
    #     email_list = {
    #         'dude': 'COOL_DUDE_EMAIL',
    #         'asmita': 'chorgeasmita2104@gmail.com',
    #         'ashwini': 'ashupawar2426@gmail.com',
    #         'sharvani': 'mahadiksharvani@gmail.com',
    #         'irene': 'irene@redvelvet.com'
    #     }

    #     if recipient_name in email_list:
    #         recipient_email = email_list[recipient_name]
    #         talk(f'What is the subject of your email to {recipient_name}?')
    #         subject = take_command()
    #         talk(f'Tell me the text of your email to {recipient_name}.')
    #         message = take_command()
    #         send_email(recipient_email, subject, message)
    #         talk(f'Your email to {recipient_name} has been sent.')
    #     else:
    #         talk(f'Sorry, {recipient_name} is not in your email list.')
    elif 'send email' in command:
        # Check for sending an email command
        talk('To whom do you want to send an email?')
        recipient_name = take_command().lower()
        
        # Define your email list as a dictionary
        email_list = {
            'dude': 'COOL_DUDE_EMAIL',
            'bts': 'diamond@bts.com',
            'pink': 'jennie@blackpink.com',
            'lisa': 'lisa@blackpink.com',
            'irene': 'irene@redvelvet.com'
        }

        if recipient_name in email_list:
            recipient_email = email_list[recipient_name]
            talk(f'What is the subject of your email to {recipient_name}?')
            subject = take_command()
            talk(f'Tell me the text of your email to {recipient_name}.')
            message = take_command()
            send_email(recipient_email, subject, message)
            talk(f'Your email to {recipient_name} has been sent.')
        else:
            talk(f'Sorry, {recipient_name} is not in your email list.')

    elif 'open google' in command:
        website = command.replace('open website', '')
        open_website("www.google.com")

    if 'send message' in command:
        phone_number = '+91 add your number'
        message = command.replace('send message to ' + phone_number, '')
        sendwhatmsg(phone_number, message, 14, 29)
        talk(f"Message '{message}' will be sent to {phone_number} at 2:29 PM.")
    else:
        talk('Please say the command again.')

    
    
b1=Button(bg="#554994",fg="white",text="START",width=20,font=("Copperplate Gothic Bold",13,"bold"),command=run_Elsa)


b1.pack(side='bottom',pady=30)


root.mainloop()