from tkinter import *
from tkinter import  messagebox

root = Tk()

root.geometry("475x275")

root.title("Questionnaire")

root["bg"]="green"

questions=["Did you receive grade A in recent terminal examination?","Did you receive grade B in recent terminal examination?","Did you receive first prize in any inter house sports events?"," Did you receive first prize in any inter house co curricular events(dance, music, art etc)?","Did you receive first prize in any inter school sports events?",
           "Did you receive second prize in any inter school sports events?","Did you receive first prize in any inter school co curricular events(dance, music, art etc)?","Did you receive second prize in any inter school co curricular events(dance, music, art etc)?","Did you receive second prize in any inter school co curricular events(dance, music, art etc)?",
           "Did you win any prizes in any district/national/state level tournaments?","Have you volunteered for any charity event/campaign?"]

options=[["YES" ,"NO" ],["YES" ,"NO" ],["YES" ,"NO" ],["YES" ,"NO" ],["YES" ,"NO" ],["YES" ,"NO" ],["YES" ,"NO" ],["YES" ,"NO" ],["YES" ,"NO" ],["YES" ,"NO" ],["YES" ,"NO" ]]

answers=['1','1','1','1','1','1','1','1','1','1','1']

i=result1=0

v = StringVar(root, "1")
que=StringVar()
option1=StringVar()
option2=StringVar()

Label1=Label(root, width="300", text="Questionnaire", bg="orange", fg="black",font='Algerian 50 bold')
Label1.pack()

Label2=Label(root,text='',textvariable=que,bg="yellow",fg="black",font='Algerian 19 bold')
Label2.place(x=10,y=105)


def viewSelected():
    choice  = var.get()
    if choice == 1:
       output = "YES"

    elif choice == 2:
       output =  "NO"

    return messagebox.showinfo('QUESTIONNAIRE', f'You Selected {output}.')
    
var = IntVar()
r1=Radiobutton(root, text="YES", variable=var, value=1, command=viewSelected)
r1.place(x=530,y=280)
r2=Radiobutton(root, text="NO", variable=var, value=2, command=viewSelected)
r2.place(x=530,y=320)


que.set("Q.1 "+questions[0])

option=options[0]

option1.set(option[0])
option2.set(option[1])

i+=1

def bonus():

    global i
    global result1


    if i<=len(questions):

        if var.get() == answers[0]:
             result1+=100
             print(result1)
        if var.get() == answers[1]:
             result1+=70
             print(result1)
        if var.get() == answers[2]:
             result1+=50
             print(result1)
        if var.get()== answers[3]:
             result1+=50
             print(result1)
        if var.get() == answers[4]:
             result1+=100
             print(result1)
        if var.get() == answers[5]:
             result1+=80
             print(result1)
        if var.get() == answers[6]:
             result1+=100
             print(result1)
        if var.get() == answers[7]:
             result1+=80
             print(result1)
        if var.get() == answers[8]:
             result1+=100
             print(result1)
        if var.get() == answers[9]:
             result1+=150
             print(result1)
        if var.get() == answers[10]:
             result1+=200
             print(result1)
        
    if(i!=len(questions)):

          que.set("Q."+str(i+1)+" "+(questions[i]))
          option=options[i]

          option1.set(option[0])
          option2.set(option[1])
      
    else:
          
          messagebox.showinfo("Result","Total Question:"+str(len(questions))+"\nResult:"+str((result1)))

    i += 1

Label7=Label(root,text="Select your option",font='Algerian 30',bg="black",fg="yellow")
Label7.place(x=200,y=200)

Button1=Button(root,text="Next",command=bonus,bg="blue",fg="white",width="10",font='Algerian 30')
Button1.place(x=410,y=400)

root.mainloop()
