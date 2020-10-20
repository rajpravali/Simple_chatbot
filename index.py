from tkinter import * #importing tkinter library used to create GUI applications.
root=Tk() #creating window

def send():#function
    send="YOU =>"+e.get()
    txt.insert(END,'\n'+send)
    if(e.get()=="hello"):
        txt.insert(END,'\n'+"Bot => hi")
    elif(e.get()=="hi"):
        txt.insert(END,'\n'+"Bot => Hello")
    elif(e.get()=="how are you"):
        txt.insert(END,'\n'+"BOt => Fine thank You, What about you")
    elif (e.get() == "Iam good"):
        txt.insert(END, '\n' + "BOt => Good to hear!!")
    elif(e.get()=="bye"):
        txt.insert(END,'\n'+"BOT => Bye!! see you later")
    else:
        txt.insert(END,'\n'+"Bot => Sorry i didnt get you")
    e.delete(0,END)

#creating text area, entry widget and send button
txt=Text(root)
txt.grid(row=0,column=0)
e=Entry(root,width=100)
send=Button(root,text='send', bg='black',fg='white',command=send).grid(row=1,column=1)
e.grid(row=1,column=0)#the grid geometry manager puts the widgets in a 2d table

root.title('simple chatbot') #adding title
root.mainloop() #method
