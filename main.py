import smtplib
import speech_recognition as sr
import pyttsx3
import collections
from email.message import EmailMessage


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_voice_info():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source, 3)
            info = listener.recognize_google(voice)
            print(info)
            return info
    except:
        print('Whoops exception')
        pass


def send_email(receiver, subject, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('sm880508@gmail.com',
                 'Sm4253232')
    email = EmailMessage()
    email['From'] = 'sm880508@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(msg)
    server.send(email)


email_list = {
    'Danny': 'yiweihuang1116@gmail.com',
    'Wei': 'sm880508@gmail.com'
}


def get_email_info():
    talk('To whom u want to send email')
    name = get_voice_info()
    email_address = email_list.get(name, 'Danny')
    print(email_address)
    talk('What is the subject of your email?')
    subject = get_voice_info()
    talk('What content do u want to send?')
    msg = get_voice_info()
    got_email = collections.namedtuple('email', ['address', 'subject', 'msg'])
    return got_email(email_address, subject, msg)


email_info = get_email_info()
send_email(email_info.address, email_info.subject, email_info.msg)
