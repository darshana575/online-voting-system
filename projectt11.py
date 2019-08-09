from tkinter import *
from PIL import ImageTk,Image
import ttkcalendar
from tkinter import messagebox as msg
import tkSimpleDialog
import sqlite3

root=Tk()
root.title('Voting System')
root.geometry('1600x800')
frame=Frame(root,width=1600,height=800)
frame.place(x=0,y=0)


def main(root,frame):
    img1=ImageTk.PhotoImage(Image.open('C:\\Users\ADMIN\Desktop\indiaa.png'))
    l1=Label(frame,image=img1)
    l1.place(x=0,y=0)



    
    img2=ImageTk.PhotoImage(Image.open('C:\\Users\ADMIN\Desktop\logo.png'))
    l21=Label(frame,image=img2)
    l21.place(x=500,y=300)


    
    B1=Button(frame,font=('courier',20,'bold'),bg='green',width=10, text='LOGIN',command=lambda:login_page(root,frame),bd=8)
    B1.place(x=280,y=600)

    
    L=Label(frame,font=('arial',14),text='Voting is a fundamental right of any citizen that enables them to choose the leaders of tomorrow.',width=120,bg='white',fg='orange')
    L.place(x=230,y=0)

    L1=Label(frame,font=('arial',14),text='In many countries, the minimum age for voting is 18 years.',width=120,bg='white',fg='orange')
    L1.place(x=230,y=28)

    L2=Label(frame,font=('arial',14),text='Voting not only enables the citizens to vote for political parties..',width=120,bg='white',fg='orange')
    L2.place(x=230,y=56)

    L3=Label(frame,font=('arial',14),text='Voting is a basic process that keeps a nations governmental system works.',width=120,bg='white',fg='blue')
    L3.place(x=230,y=84)

    L4=Label(frame,font=('arial',14),text=' It also helps them to realize the importance of citizenship.',width=120,bg='white',fg='blue')
    L4.place(x=230,y=112)

    L5=Label(frame,font=('arial',14),text='Many people do not vote thinking one vote will not make a change, but as a matter of fact, it does.',width=120,bg='white',fg='green')
    L5.place(x=230,y=140)

    L6=Label(frame,font=('arial',14),text='A nation’s political foundations are built using elections.',width=120,bg='white',fg='green')
    L6.place(x=230,y=168)
    
    L7=Label(frame,font=('arial',14),text=' So Voting is an IMPORTANT DUTY FOR EVERYONE',width=120,bg='white',fg='green')
    L7.place(x=230,y=196)

    B2=Button(frame,font=('courier',20,'bold'),bg='red',width=10,text='BACK',command=lambda:back(root,frame),bd=8)
    B2.place(x=1100,y=600)
    frame.mainloop()
    
class CalendarDialog(tkSimpleDialog.Dialog):
    """Dialog box that displays a calendar and returns the selected date"""
    def body(self, master):
        self.calendar = ttkcalendar.Calendar(master)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection

def login_page(root,frame):
    def login_success(root,frame):
        ans=msg.askquestion('ask question','do you want to proceed??')
        print(ans)
        if ans=='yes':
            print('yes pressed')
            conn=sqlite3.connect('voters.db')
            txt1=E.get()
            txt2=E1.get()
            #txt3=int(E2.get())
            txt4=E3.get()
            txt5=E4.get()
            txt6=int(E5.get())
            txt7=int(E6.get())
            txt8=int(E7.get())
            print(txt1)
            print(txt2)
            #print(txt3)
            print(txt4)
            print(txt5)
            print(txt6)
            print(txt7)
            print(txt8)
            
            print(type(txt1))
            print(type(txt2))
           # print(type(txt3))
            print(type(txt4))
            print(type(txt5))
            print(type(txt6))
            print(type(txt7))
            print(type(txt8))
            cursor=conn.execute('select * from voting')

                 
            
            for row in cursor:
                if row[0]==txt1 and row[1]==txt2 and row[3]==txt4  and row[4]==txt5 and row[5]==txt6 and row[6]==txt7 and row[7]==txt8:
                    print('login success')

                    ###########function call for new page for displaying candidate      
                    conn.close()
                    selection()
                    
            else:
                print('invalid login details')
                login_page(root,frame)
                conn.close()
        else:
            print('no pressed')   
        
        

    def getdate(frame):
        cd = CalendarDialog(frame)
        result = cd.result
        selected_date.set(result.strftime("%d-%m-%Y"))
    frame.destroy()
    frame=Frame(root,width=1600,height=800,bg='light blue')
    frame.place(x=0,y=0)


    img1=ImageTk.PhotoImage(Image.open('C:\\Users\ADMIN\Desktop\\vote.png'))
    l11=Label(frame,image=img1,width=630,height=800)
    l11.place(x=0,y=0)
    
    L=Label(frame,font=('arial',15),text='NAME')
    L.place(x=650,y=100)

    L1=Label(frame,font=('arial',15),text='D.O.B')
    L1.place(x=650,y=150)

    L2=Label(frame,font=('arial',15),text='STATE')
    L2.place(x=650,y=200)

    L3=Label(frame,font=('arial',15),text='CITY')
    L3.place(x=650,y=250)

    L4=Label(frame,font=('arial',15),text='CENTER')
    L4.place(x=650,y=300)

    L5=Label(frame,font=('arial',15),text='AADHAR CARD NO.')
    L5.place(x=650,y=350)

    L6=Label(frame,font=('arial',15),text='VOTERS_ID_NO.')
    L6.place(x=650,y=400)

    L7=Label(frame,font=('arial',15),text='PIN')
    L7.place(x=650,y=450)

    L8=Label(frame,font=('arial',24),text='THANKS FOR VOTING!!!',width=90,bg='black',fg='orange')
    L8.place(x=0,y=750)
    
    selected_date= StringVar()
    date=StringVar()
    E=Entry(frame,bd=3)
    E.place(x=900,y=100)

    E1=Entry(frame,bd=3,textvariable=selected_date,width=25)
    E1.place(x=900,y=150)
    b1=Button(frame,text='Choose a date',command=lambda:getdate(frame),width=22)
    b1.place(x=1070,y=150)                    
    state=StringVar()
    state.set('Rajasthan')

    E2=OptionMenu(frame,state,'Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal')
    E2.place(x=900,y=200)

    E3=Entry(frame,bd=3)
    E3.place(x=900,y=250)

    E4=Entry(frame,bd=3)
    E4.place(x=900,y=300)

    E5=Entry(frame,bd=3)
    E5.place(x=900,y=350)

    E6=Entry(frame,bd=5)
    E6.place(x=900,y=410)

    E7=Entry(frame,bd=3)
    E7.place(x=900,y=460)

    B2=Button(frame,font=('courier',19,'bold'),text='login',command=lambda:login_success(root,frame),bd=8)
    B2.place(x=700,y=600)

    B3=Button(frame,font=('courier',19,'bold'),text='Back',command=lambda:back(root,frame),bd=8)
    B3.place(x=900,y=600)

    frame.mainloop()

def selection():
    #L=Label(frame,font=('arial',15),text='NAME')
    #L.place(x=0,y=0) 
   selection = "You selected the option " + str(radio.get())  
   label.config(text = selection)
   top = Tk()
   top.geometry("300x150")
   radio = IntVar()  
   lbl = Label(text = "THE PARTICIPATED CANDIDATES ARE :")  
   lbl.pack()  
   R1 = Radiobutton(top, text="AMAN", variable=radio, value=1,  
                  command=selection)  
   R1.pack( anchor = W )  
  
   R2 = Radiobutton(top, text="RAMAN", variable=radio, value=2,  
                  command=selection)  
   R2.pack( anchor = W )  
  
   R3 = Radiobutton(top, text="KARAN", variable=radio, value=3,  
                  command=selection)  
   R3.pack( anchor = W)  
  
   label = Label(top)  
   label.pack()  
   top.mainloop()  

    

    
    

def back(root,frame):
    ans=msg.askquestion('ask question','do you want to go back??')
    print(ans)
    if ans=='yes':
        print('yes pressed')
        frame.destroy()
        frame=Frame(root,width=1600,height=800)
        frame.place(x=0,y=0)
        main(root,frame)

    else:
        print('no pressed')
        return

    



main(root,frame)
