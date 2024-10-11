from tkinter import *
from tkinter import messagebox
import cv2
import datetime
import numpy as np
import smtplib
import os

pwd = ('0000')

def close():
    click=messagebox.askyesno('warning',message='do yoy want to close')
    if click==True:
        wn.destroy()
       
def cam():
        def close():
            click=messagebox.askyesno('warning',message='do yoy want to close')
            if click==True:
                window.destroy()
        global window
        window = Tk()
        window.title("SMART SURVILLENCE SYSTEM ")
        window.geometry('420x420')

        label1 = Label(window,text='CAMERA MODE ',fg='black',width = 20,height = 2,bg = 'grey',font=('Arial',12))
        label1.grid(row=1,column=0,padx=10,pady=10)
        label2 = Label(window,text='ALERT MODE ',fg='black',width = 20,height = 2,bg = 'grey',font=('Arial',12))
        label2.grid(row=2,column=0,padx=10,pady=10)
        label3 = Label(window,text='INFORM MODE ',fg='black',width = 20,height = 2,bg = 'grey',font=('Arial',12))
        label3.grid(row=3,column=0,padx=10,pady=10)
        label4 = Label(window,text='FIND MODE ',fg='black',width = 20,height = 2,bg = 'grey',font=('Arial',12))
        label4.grid(row=4,column=0,padx=10,pady=10)
        label5 = Label(window,text='ADVANCED MODE ',fg='black',width = 20,height = 2,bg = 'grey',font=('Arial',12))
        label5.grid(row=5,column=0,padx=10,pady=10)
        

        def project1():
            cap = cv2.VideoCapture(0)

            if (cap.isOpened() == False):
                print("Unable to read camera feed")

            frame_width = int(cap.get(3))
            frame_height = int(cap.get(4))

            out = cv2.VideoWriter('MODE_1.mp4', cv2.VideoWriter_fourcc('X','V','I','D'), 15, (frame_width, frame_height))

            while(True):
                ret, frame = cap.read()
                font  = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
                dt = str(datetime.datetime.now())
                frame = cv2.putText(frame, dt, (10, 40), font, 1, (10, 0, 700), 2, cv2.LINE_8)

                if ret == False:
                    break

                else:
                    cv2.flip(frame, 180)
                    out.write(frame)

                    cv2.imshow('frame', frame)

                    if cv2.waitKey(40) == 27:
                        break
            cv2.destroyAllWindows()
            cap.release()
            out.release()


        def project2():
            cap = cv2.VideoCapture(0)

            frame_width = int(cap.get(3))
            frame_height = int(cap.get(4))

            out = cv2.VideoWriter('MODE_2.mp4', cv2.VideoWriter_fourcc('X','V','I','D'), 15, (frame_width, frame_height))

            while(True):
                ret, frame = cap.read()
                ret, frame1 = cap.read()
                font  = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
                dt = str(datetime.datetime.now())
                frame = cv2.putText(frame, dt, (10, 40), font, 1, (10, 0, 700), 2, cv2.LINE_8)
                

                if ret == True:
                    cv2.flip(frame, 180)
                    out.write(frame)

                diff = cv2.absdiff(frame, frame1)
                gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (5,5), 0)
                _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _= cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                for contour in contours:
                    (x, y, w, h) = cv2.boundingRect(contour)
                    if cv2.contourArea(contour) < 1000:
                        continue
                    cv2.rectangle(frame1, (x, y), (x+y, y+h), (0, 255, 0), 2)
                    cv2.putText(frame1, "STATUS: ".format("MOVEMENT APPEARING"), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    
                cv2.imshow("inter", frame1)
                frame = frame1
                ret, frame1 = cap.read()
                if cv2.waitKey(40) == 27:
                    break
                    break
            cv2.destroyAllWindows()
            cap.release() 

        def project3():
            cap = cv2.VideoCapture(0)
            
            frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

            frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))

            fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

            out = cv2.VideoWriter("MODE_3.mp4", fourcc, 20.0, (1280,720))
 

            ret, frame1 = cap.read()
            ret, frame2 = cap.read()
            while cap.isOpened():
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (5,5), 0)
                _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                for contour in contours:
                    (x, y, w, h) = cv2.boundingRect(contour)
                    if cv2.contourArea(contour) < 1000:
                        continue
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login('arulselvan11201@gmail.com', 'Arul@100')
                    server.sendmail('arulselvan11201@gmail.com', 'arulbruce01@gmail.com', 'alert message from pycharm.... movements were identified')
                    cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame1, "Status: MOVEMENT ".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
                    break
                #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
  
                image = cv2.resize(frame1, (1280,720))
                font  = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
                dt = str(datetime.datetime.now())
                frame = cv2.putText(image, dt, (10, 40), font, 1, (10, 0, 700), 2, cv2.LINE_8)

                out.write(frame)
                cv2.imshow("feed", frame1)
                frame1 = frame2
                ret, frame2 = cap.read()

                if cv2.waitKey(40) == 27:
                    break

            cv2.destroyAllWindows()
            cap.release()
            out.release()

        def project4():
            cap = cv2.VideoCapture(0)

            ret, frame1 = cap.read()
            ret, frame2 = cap.read()
            ret, frame3 = cap.read()


            while cap.isOpened():
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (5,5), 0)
                _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _= cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                for contour in contours:
                    (x, y, w, h) = cv2.boundingRect(contour)
                    
                cv2.imshow("inter", gray)
                
                frame2 = frame3
                ret, frame3 = cap.read()
                if cv2.waitKey(40) == 27:
                    break
            cv2.destroyAllWindows()
            cap.release()
    
        def project5():
            cap = cv2.VideoCapture(0)
            ret, frame1 = cap.read()
            ret, frame2 = cap.read()

            while cap.isOpened:
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (5,5), 0)
                _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _= cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                for contour in contours:
                    (x, y, w, h) = cv2.boundingRect(contour)
                    if cv2.contourArea(contour) < 10000:
                        continue
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login('arulselvan11201@gmail.com', 'arul@100')
                    server.sendmail('arulselvan11201@gmail.com', 'arulbruce01@gmail.com', 'alert message from pycharm.... movements were identified')
                    cv2.destroyAllWindows()
        
                    cap = cv2.VideoCapture(0)    

                    frame_width = int(cap.get(3))
                    frame_height = int(cap.get(4))

                    out = cv2.VideoWriter('MODE_5.mp4', cv2.VideoWriter_fourcc('X','V','I','D'), 20, (frame_width, frame_height))

                    while(True):
                        ret, frame = cap.read()
                        font  = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
                        dt = str(datetime.datetime.now())
                        frame = cv2.putText(frame, dt, (10, 40), font, 1, (10, 0, 700), 2, cv2.LINE_8)

                        if ret == False:
                            break

                        else:
                            cv2.flip(frame, 180)
                            out.write(frame)

                            cv2.imshow('RECORDING', frame)

                            if cv2.waitKey(1) == 27:
                                break
                    cv2.destroyAllWindows()
                    cap.release()
                    out.release()
                
                
                
                frame1 = frame2
                ret, frame2 = cap.read()
                if cv2.waitKey(1) == 27:
                    break
            cv2.destroyAllWindows()
            cap.release()
            

            
        button1 = Button(window,command=project1,text='Mode-1',width = 20,height = 2,fg='black',font=('Arial',12))
        button1.grid(row=1,column=1,padx=10,pady=10)
        button2 = Button(window,command=project2,text='Mode-2',width = 20,height = 2,fg='black',font=('Arial',12))
        button2.grid(row=2,column=1,padx=10,pady=10)
        button3 = Button(window,command=project3,text='Mode-3',width = 20,height = 2,fg='black',font=('Arial',12))
        button3.grid(row=3,column=1,padx=10,pady=10)
        button4 = Button(window,command=project4,text='Mode-4',width = 20,height = 2,fg='black',font=('Arial',12))
        button4.grid(row=4,column=1,padx=10,pady=10)
        button5 = Button(window,command=project5,text='Mode-5',width = 20,height = 2,fg='black',font=('Arial',12))
        button5.grid(row=5,column=1,padx=10,pady=10)
        button6 = Button(window,command=close,text='Exit',width = 20,height = 2,fg='red',font=('Arial',12))
        button6.grid(row=6,column=1,padx=10,pady=10)
        button6 = Button(window,command=register,text='Register',width = 20,height = 2,fg='blue',font=('Arial',12))
        button6.grid(row=6,column=0,padx=10,pady=10)
       

def close():
    click=messagebox.askyesno('warning',message='do yoy want to close')
    if click==True:
        screen.destroy()

def login_success():
    
    screen2.destroy()
    screen.destroy()
    cam()

def password_not_recognised():
    screen2.destroy()
    messagebox.showerror(title='Wrong password',message='Password is Wrong...')
    
    
def user_not_found():
    screen2.destroy()
    messagebox.showerror(title='Wrong Entry',message='Username is Wrong...')

def register_user():

    username_info=username.get()
    password_info=password.get()
    file=open(username_info, "w")
    file.write(username_info+"\n" )
    file.write(password_info)
    file.close()
    
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    
    Label(screen1,text="registration completed",fg="green",font=("calibri",12)).pack()
    screen1.destroy()
def forpwd_entry():
    if (username_entry5.get()==pwd) and (password_entry5.get()==pwd):
        screen5.destroy()
        screen4.destroy()
        screen.destroy()
        
        cam()
        
def forgot_password_entry():
    
    global screen5
    screen5=Toplevel(screen4)
    screen5.title("Register")
    screen5.geometry("300x250")

    global username5
    global password5
    global username_entry5
    global password_entry5

    username5=StringVar()
    password5=StringVar()
    Label(screen5,text="please enter details below",bg="grey",width="300",height="2",font=("calibri",13)).pack()
    Label(screen5,text="").pack()
    Label(screen5,text="username*").pack()
    
    username_entry5 = Entry(screen5,textvariable=username5)
    username_entry5.pack()
    Label(screen5,text = "password*").pack()
    password_entry5 = Entry(screen5,textvariable=password5)
    password_entry5.pack()
    Label(screen5,text = "").pack()
    Button(screen5,text = "login",width = 12,height = 1,command=forpwd_entry).pack()
    
    
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()
    
def register():
    global screen1
    screen1=Toplevel(window)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username=StringVar()
    password=StringVar()
    Label(screen1,text="please enter details below",bg="grey",width="300",height="2",font=("calibri",13)).pack()
    Label(screen1,text="").pack()
    Label(screen1,text="username*").pack()
    
    username_entry = Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text = "password*").pack()
    password_entry = Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text = "").pack()
    Button(screen1,text = "Register",width = 12,height = 1,command=register_user).pack()

    
    
def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("login")
    screen2.geometry("300x250")
    
    Label(screen2,text="please enter details below to login",bg="grey",width="300",height="2",font=("calibri",13)).pack()
    Label(screen2,text="").pack()

    global username_verify
    global password_verify

    global username_entry1
    global password_entry1

    username_verify = StringVar()
    password_verify = StringVar()
    
    Label(screen2,text="Username* ").pack()
    username_entry1=Entry(screen2,textvariable = username_verify)
    username_entry1.pack()
    Label(screen2,text="").pack()
    Label(screen2,text="password*").pack()
    password_entry1=Entry(screen2,textvariable=password_verify, show= "*")
    password_entry1.pack()
    Label(screen2,text="").pack()
    Button(screen2,text = "login",width = 10,height = 1,command=login_verify).pack()
def helps():
    global screen4
    screen4=Tk()
    screen4.geometry("250x100")
    screen4.title("Help window")
    Label(screen4,text="").pack()
    Button(screen4,text="forgot password",height="2",width="30",fg='red',command=forgot_password_entry).pack()
    Label(screen4,text="").pack()
    
def main_screen():
    global screen
    screen=Tk()
    screen.geometry("350x300")
    screen.title("SMART SURVEILLANCE")
    Label(screen,text="").pack()
    Label(text="password entry",bg="grey",width="300",height="2",font=("calibri",13)).pack()
    Label(screen,text="").pack()
    Button(text="Login",height="2",width="30",command=login).pack()
    Label(screen,text="").pack()
    Button(text="help",height="2",width="10",fg= 'blue',command=helps).pack()
    Label(screen,text="").pack()
    Button(text="exit",height="2",width="10",command=close,fg='red').pack()
    screen.mainloop()

main_screen()
