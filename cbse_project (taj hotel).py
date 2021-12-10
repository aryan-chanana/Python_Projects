import calendar
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkcalendar import *
import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="aryan",charset="utf8",database = "ttn_work")
cur = con.cursor()

window = tkinter.Tk()
window.title("TAJ MAHAL")
window.columnconfigure(0,minsize=250)
window.rowconfigure([0,1,2,3,4,5,6,7],minsize = 100)
window.configure(bg="#98AFC7")
LARGEFONT = ("Arial",24)
lablefont = ('times',20,'bold')
label = tkinter.Label(window, text = "WELCOME TO HOTEL TAJ MAHAL",font = LARGEFONT,fg = "red").grid(row=0,column=1)

cur.execute("select * from rooms")
total_rooms_available1 = cur.fetchall()
total_rooms_available = total_rooms_available1[0][0]
rooms_needed = tkinter.IntVar()
date = tkinter.StringVar()
month = tkinter.IntVar()
year = tkinter.IntVar()
def createNewWindow():
    newWindow = tkinter.Toplevel(window)
    newWindow.configure(bg="#98AFC7")
    newWindow.columnconfigure(0,minsize=250)
    newWindow.rowconfigure([0,1,2,3,4,5,6,7],minsize=100)
    label1 = tkinter.Label(newWindow, text="CHECK ROOMS AVAILABILITY", font=LARGEFONT, fg="red",bg="blue").grid(row=0, column=1)


    rooms_needed_2 = tkinter.Label(newWindow, text="Number Of Rooms", fg="#963D02").grid(row=2,column=0)
    year_2 = tkinter.Label(newWindow, text="Enter Year", fg="#963D02").grid(row=3,column=0)
    month_2 = tkinter.Label(newWindow, text="Enter Month", fg="#963D02").grid(row=4,column=0)
    date_2 = tkinter.Label(newWindow, text="Enter Date", fg="#963D02").grid(row=5,column=0)

    rooms_needed_1 = tkinter.Entry(newWindow, textvariable=rooms_needed, width=30).grid(row=2, column=1)
    year_1 = tkinter.Entry(newWindow, textvariable=year, width=30).grid(row=3, column=1)
    month_1 = tkinter.Entry(newWindow, textvariable=month, width=30).grid(row=4, column=1)
    date_1 = tkinter.Entry(newWindow, textvariable=date, width=30).grid(row=5, column=1)



    button_search = tkinter.Button(newWindow, text="SEARCH", command=getValue).grid(row=6, column=1)
    
def getValue():
    newWindow1 = tkinter.Toplevel(window)
    newWindow1.configure(bg="#98AFC7")
    newWindow1.columnconfigure(0,minsize=250)
    newWindow1.rowconfigure([0,1,2,3,4,5,6,7],minsize=250)
    month_2 = month.get()
    year_2 = year.get()
    global cal
    cal = Calendar(newWindow1, selectmode = "day", year=year_2, month=month_2)
    cal.pack(pady=20)

    label2 = tkinter.Label(newWindow1, font = LARGEFONT,text="", fg = "red", bg = "blue")
    label2.pack(pady=30)
    label3 = tkinter.Label(newWindow1, font = LARGEFONT,text="", fg = "red", bg = "blue")
    label3.pack(pady=40)

    if int(rooms_needed.get())<=total_rooms_available:
        label2.config(text = "rooms available")
        label3.config(text = total_rooms_available)
    else:
        label2.config(text = "rooms not available")
        label3.config(text = total_rooms_available)


first_name = tkinter.StringVar()
last_name = tkinter.StringVar()
dob = tkinter.StringVar()
age = tkinter.IntVar()
personal_id = tkinter.IntVar()
phone_no = tkinter.StringVar()
email_id = tkinter.StringVar()
room_allotted = tkinter.IntVar()
date_booking = tkinter.StringVar()
check_out_date_check = tkinter.StringVar()
def check():
    newWindow = tkinter.Toplevel(window)
    newWindow.configure(bg="#98AFC7")
    newWindow.columnconfigure(0,minsize=250)
    newWindow.rowconfigure([0,1,2,3,4,5],minsize=50)
    check_inn_button = tkinter.Button(newWindow, text="CHECK IN",width=32, height=3, bg = "#E67451", fg="green", cursor="hand2", command=booking).grid(row=1, column=0)
    check_out_button = tkinter.Button(newWindow, text="CHECK OUT", width=32, height=3, bg = "#E67451", fg="green", cursor="hand2",command=remove_booking).grid(row=1, column=1)

def booking():
    newWindow = tkinter.Toplevel(window)
    newWindow.configure(bg="#98AFC7")
    newWindow.columnconfigure(0,minsize=250)
    newWindow.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11],minsize=50)
    label1 = tkinter.Label(newWindow, text="Enter Details Of Room Booker", font=LARGEFONT, fg="red",bg="blue").grid(row=0, column=1)

    first_name_2 = tkinter.Label(newWindow, text="First Name", fg="#963D02").grid(row=2,column=0)
    last_name_2 = tkinter.Label(newWindow, text="Last Name", fg="#963D02").grid(row=3,column=0)
    dob_2 = tkinter.Label(newWindow, text="Date Of Birth", fg="#963D02").grid(row=4,column=0)
    age_2 = tkinter.Label(newWindow, text="Age", fg="#963D02").grid(row=5,column=0)
    personal_id_2 = tkinter.Label(newWindow, text="Aadhar Card Number", fg="#963D02").grid(row=6,column=0)
    phone_no_2 = tkinter.Label(newWindow, text="Phone Number", fg="#963D02").grid(row=7,column=0)
    email_id_2 = tkinter.Label(newWindow, text="Email Id", fg="#963D02").grid(row=8,column=0)
    room_allotted_2 = tkinter.Label(newWindow, text="Room Number", fg="#963D02").grid(row=9,column=0)
    date_booking_2 = tkinter.Label(newWindow, text="Check in Date", fg="#963D02").grid(row=10,column=0)

    first_name_1 = tkinter.Entry(newWindow, textvariable=first_name, width=30).grid(row=2, column=1)
    last_name_1 = tkinter.Entry(newWindow, textvariable=last_name, width=30).grid(row=3, column=1)
    dob_1 = tkinter.Entry(newWindow, textvariable=dob, width=30).grid(row=4, column=1)
    age_1 = tkinter.Entry(newWindow, textvariable=age, width=30).grid(row=5, column=1)
    personal_id_1 = tkinter.Entry(newWindow, textvariable=personal_id, width=30).grid(row=6, column=1)
    phone_no_1 = tkinter.Entry(newWindow, textvariable=phone_no, width=30).grid(row=7, column=1)
    email_id_1 = tkinter.Entry(newWindow, textvariable=email_id, width=30).grid(row=8, column=1)
    room_allotted_1 = tkinter.Entry(newWindow, textvariable=room_allotted, width=30).grid(row=9, column=1)
    date_booking_1 = tkinter.Entry(newWindow, textvariable=date_booking, width=30).grid(row=10, column=1)

    button_book = tkinter.Button(newWindow, text="BOOK", command=book).grid(row=11, column=1)

def book():
    newWindow = tkinter.Toplevel(window)
    newWindow.configure(bg="#98AFC7")
    newWindow.columnconfigure(0,minsize=20)
    newWindow.rowconfigure([0],minsize=50)
    first_name_3 = first_name.get()
    last_name_3 = last_name.get()
    dob_3 = dob.get()
    age_3 = age.get()
    personal_id_3 = personal_id.get()
    phone_no_3 = phone_no.get()
    email_id_3 = email_id.get()
    room_allotted_3 = room_allotted.get()
    date_booking_3 = date_booking.get()
    query = "insert into hotel values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    query1 = "insert into hotel_back_log values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    t = (first_name_3 , last_name_3 , dob_3 , age_3 , personal_id_3 , phone_no_3 , email_id_3 , room_allotted_3 , date_booking_3 , 'NULL')
    cur.execute(query,t)
    cur.execute(query1,t)
    con.commit()
    print("record successfully inserted!!!")
    global total_rooms_available
    total_rooms_available -= 1
    query2 = "update rooms set total_rooms_left = %s"
    t1 = (total_rooms_available,)
    cur.execute(query2,t1)
    con.commit()
    label1 = tkinter.Label(newWindow, text="ROOM BOOKED", font=LARGEFONT, fg="red",bg="blue").grid(row=0, column=1)



def records():
    newWindow = tkinter.Toplevel(window)
    newWindow.configure(bg="#98AFC7")
    newWindow.columnconfigure(0,minsize=250)
    newWindow.rowconfigure([0,1,2,3],minsize=50)
    label1 = tkinter.Label(newWindow, text="CUSTOMER'S RECORDS", font=LARGEFONT, fg="red",bg="blue").grid(row=0, column=1)

    button_present = tkinter.Button(newWindow,text = "PRESENT CUSTOMER DETAILS", width=32, height=3, bg = "#E67451", fg="green", cursor="hand2", command=present_record).grid(row=1, column=0)
    button_past = tkinter.Button(newWindow,text = "ALL CUSTOMER RECORDS", width=32, height=3, bg = "#E67451", fg="green", cursor="hand2", command=past_record).grid(row=1, column=1)

def present_record():
    my_w = tkinter.Tk()
    my_w.geometry("400x250")
    mycursor = con.cursor()
    cols = ('First Name','Last Name','DOB','Age','Personal Id','Phone No','Email Id','Room Allotted','Check In Date')
    for k in cols:
        for j in range(len(cols)):
            f = Entry(my_w,width=20)
            f.config(background="yellow", foreground="blue")
            f.grid(row=0,column=j)
            f.insert(END,cols[j])

    mycursor.execute("select fname,lname,date_of_birth,age,personalid,phoneno,emailid,room_no,check_inn_date from hotel")
    a = mycursor.fetchall()
    i = 1
    for student in a:
        for j in range(len(student)):
            e = Entry(my_w,width=20)
            e.grid(row=i,column=j)
            e.insert(END,student[j])
        i += 1
    my_w.mainloop()
    
def past_record():
    my_w = tkinter.Tk()
    my_w.geometry("400x250")
    mycursor = con.cursor()
    cols = ('First Name','Last Name','DOB','Age','Personal Id','Phone No','Email Id','Room Allotted','Check Inn Date','Check Out Date')
    for k in cols:
        for j in range(len(cols)):
            f = Entry(my_w,width=20)
            f.config(background="yellow", foreground="blue")
            f.grid(row=0,column=j)
            f.insert(END,cols[j])

    mycursor.execute("select * from hotel_back_log")
    a = mycursor.fetchall()
    i = 1
    for student in a:
        for j in range(len(student)):
            e = Entry(my_w,width=20)
            e.grid(row=i,column=j)
            e.insert(END,student[j])
        i += 1
    my_w.mainloop()


remove_room_allotted = tkinter.IntVar()
remove_first_name = tkinter.StringVar()
remove_last_name = tkinter.StringVar()
remove_personal_id = tkinter.StringVar()
check_inn = tkinter.StringVar()
check_out_date = tkinter.StringVar()
def remove_booking():
    scores = tkinter.Toplevel(window)
    scores.configure(bg="Black")
    scores.columnconfigure(0,minsize=250)
    scores.rowconfigure([0,1,2,3,4,5,6,7],minsize=50)
    label = tkinter.Label(scores,text="CUSTOMER CHECK-OUT",font=("Arial,30")).grid(row=0,column=2)
    label1 = tkinter.Label(scores,text="Room No").grid(row=1,column=0)
    label2 = tkinter.Label(scores,text="First Name").grid(row=2,column=0)
    label3 = tkinter.Label(scores,text="Last Name").grid(row=3,column=0)
    label4 = tkinter.Label(scores,text="Aadhar Card No").grid(row=4,column=0)
    label5 = tkinter.Label(scores,text="Check In date").grid(row=5,column=0)
    label6 = tkinter.Label(scores,text="Check out date").grid(row=6,column=0)
    text1 = tkinter.Entry(scores,textvariable=remove_room_allotted,width=30).grid(row=1,column=1)
    text2 = tkinter.Entry(scores,textvariable=remove_first_name,width=30).grid(row=2,column=1)
    text3 = tkinter.Entry(scores,textvariable=remove_last_name,width=30).grid(row=3,column=1)
    text4 = tkinter.Entry(scores,textvariable=remove_personal_id,width=30).grid(row=4,column=1)
    text5 = tkinter.Entry(scores,textvariable=check_inn,width=30).grid(row=5,column=1)
    text6 = tkinter.Entry(scores,textvariable=check_out_date,width=30).grid(row=6,column=1)
    button1 = tkinter.Button(scores,text="Check Out",command=delete1).grid(row=7,column=0)
        
def delete1():
    newWindow = tkinter.Toplevel(window)
    newWindow.configure(bg="#98AFC7")
    newWindow.columnconfigure(0,minsize=20)
    newWindow.rowconfigure([0],minsize=50)
    room_no = remove_room_allotted.get()
    fname = remove_first_name.get()
    lname = remove_last_name.get()
    adhar = remove_personal_id.get()
    check_inn_date = check_inn.get()
    check_out = check_out_date.get()
    cur = con.cursor()
    query1 = "update hotel_back_log set check_out_date = %s where room_no = %s and check_in_date = %s"
    t1 = (check_out , room_no , check_inn_date)
    cur.execute(query1,t1)
    query2 = "delete from hotel where room_no = %s and fname = %s and lname = %s and personalid = %s"
    t2=(room_no,fname,lname,adhar)
    cur.execute(query2,t2)
    con.commit()
    print(cur.rowcount,"Record successfully deleted")
    global total_rooms_available
    total_rooms_available += 1
    query2 = "update rooms set total_rooms_left = %s"
    t1 = (total_rooms_available,)
    cur.execute(query2,t1)
    con.commit()
    label1 = tkinter.Label(newWindow, text="THANK YOU! PLEASE VISIT AGAIN", font=LARGEFONT, fg="red",bg="blue").grid(row=0, column=1)



def change():
    newWindow = tkinter.Toplevel(window)
    newWindow.configure(bg="#98AFC7")
    newWindow.columnconfigure(0,minsize=250)
    newWindow.rowconfigure([0,1,2,3],minsize=50)

    button_present = tkinter.Button(newWindow,text = "CANCEL BOOKING", width=32, height=3, bg = "#E67451", fg="green", cursor="hand2", command=cancel).grid(row=1, column=0)
    button_past = tkinter.Button(newWindow,text = "UPDATE RECORDS", width=32, height=3, bg = "#E67451", fg="green", cursor="hand2",command=update).grid(row=1, column=1)

cancel_room_allotted = tkinter.IntVar()
cancel_first_name = tkinter.StringVar()
cancel_last_name = tkinter.StringVar()
cancel_dob = tkinter.StringVar()
cancel_personal_id = tkinter.IntVar()
cancel_phone_no = tkinter.StringVar()
cancel_date_booking = tkinter.StringVar()
def cancel():
    scores = tkinter.Toplevel(window)
    scores.configure(bg="Black")
    scores.columnconfigure(0,minsize=250)
    scores.rowconfigure([0,1,2,3,4,5,6,7,8],minsize=50)
    label = tkinter.Label(scores,text="CANCELLATION OF BOOKING",font=("Arial,30")).grid(row=0,column=2)
    label1 = tkinter.Label(scores,text="Room No").grid(row=1,column=0)
    label2 = tkinter.Label(scores,text="First Name").grid(row=2,column=0)
    label3 = tkinter.Label(scores,text="Last Name").grid(row=3,column=0)
    label4 = tkinter.Label(scores,text="Date of birth").grid(row=4,column=0)
    label5 = tkinter.Label(scores,text="Phone No.").grid(row=5,column=0)
    label6 = tkinter.Label(scores,text="Aadhar Card No").grid(row=6,column=0)
    label7 = tkinter.Label(scores,text="Check In date").grid(row=7,column=0)
    text1 = tkinter.Entry(scores,textvariable=cancel_room_allotted,width=30).grid(row=1,column=1)
    text2 = tkinter.Entry(scores,textvariable=cancel_first_name,width=30).grid(row=2,column=1)
    text3 = tkinter.Entry(scores,textvariable=cancel_last_name,width=30).grid(row=3,column=1)
    text4 = tkinter.Entry(scores,textvariable=cancel_dob,width=30).grid(row=4,column=1)
    text5 = tkinter.Entry(scores,textvariable=cancel_phone_no,width=30).grid(row=5,column=1)
    text6 = tkinter.Entry(scores,textvariable=cancel_personal_id,width=30).grid(row=6,column=1)
    text7 = tkinter.Entry(scores,textvariable=cancel_date_booking,width=30).grid(row=7,column=1)
    button1 = tkinter.Button(scores,text="Cancel booking",command=cancel1).grid(row=8,column=0)

def cancel1():
    newWindow = tkinter.Toplevel(window)
    newWindow.configure(bg="#98AFC7")
    newWindow.columnconfigure(0,minsize=20)
    newWindow.rowconfigure([0],minsize=50)
    room_no = cancel_room_allotted.get()
    fname = cancel_first_name.get()
    lname = cancel_last_name.get()
    adhar = cancel_personal_id.get()
    check_inn_date = cancel_date_booking.get()
    cur = con.cursor()
    query1 = "update hotel_back_log set check_out_date = %s where room_no = %s and check_in_date = %s and fname = %s"
    t1 = ("CANCELLED" , room_no , check_inn_date , fname)
    cur.execute(query1,t1)
    query2 = "delete from hotel where room_no = %s and fname = %s and lname = %s and personalid = %s"
    t2=(room_no,fname,lname,adhar)
    cur.execute(query2,t2)
    con.commit()
    print(cur.rowcount,"Booking Cancelled")
    global total_rooms_available
    total_rooms_available += 1
    query2 = "update rooms set total_rooms_left = %s"
    t1 = (total_rooms_available,)
    cur.execute(query2,t1)
    con.commit()
    label1 = tkinter.Label(newWindow, text="BOOKING CANCELLED", font=LARGEFONT, fg="red",bg="blue").grid(row=0, column=1)

update_room_allotted = tkinter.IntVar()
update_first_name = tkinter.StringVar()
update_last_name = tkinter.StringVar()
update_dob = tkinter.StringVar()
update_personal_id = tkinter.IntVar()
update_phone_no = tkinter.StringVar()
update_date_booking = tkinter.StringVar()

new_room_allotted = tkinter.IntVar()
new_first_name = tkinter.StringVar()
new_last_name = tkinter.StringVar()
new_dob = tkinter.StringVar()
new_personal_id = tkinter.IntVar()
new_phone_no = tkinter.StringVar()
new_date_booking = tkinter.StringVar()
def update():
    scores = tkinter.Toplevel(window)
    scores.configure(bg="Black")
    scores.columnconfigure(0,minsize=250)
    scores.rowconfigure([0,1,2,3,4,5,6,7,8],minsize=75)
    label = tkinter.Label(scores,text="Enter All Details").grid(row=0,column=0)
    label1 = tkinter.Label(scores,text="Old Room No").grid(row=1,column=0)
    label2 = tkinter.Label(scores,text="Old First Name").grid(row=2,column=0)
    label3 = tkinter.Label(scores,text="Old Last Name").grid(row=3,column=0)
    label4 = tkinter.Label(scores,text="Old Date of birth").grid(row=4,column=0)
    label5 = tkinter.Label(scores,text="Old Phone No.").grid(row=5,column=0)
    label6 = tkinter.Label(scores,text="Old Aadhar Card No").grid(row=6,column=0)
    label7 = tkinter.Label(scores,text="Old Check In date").grid(row=7,column=0)
    text1 = tkinter.Entry(scores,textvariable=update_room_allotted,width=30).grid(row=1,column=1)
    text2 = tkinter.Entry(scores,textvariable=update_first_name,width=30).grid(row=2,column=1)
    text3 = tkinter.Entry(scores,textvariable=update_last_name,width=30).grid(row=3,column=1)
    text4 = tkinter.Entry(scores,textvariable=update_dob,width=30).grid(row=4,column=1)
    text5 = tkinter.Entry(scores,textvariable=update_phone_no,width=30).grid(row=5,column=1)
    text6 = tkinter.Entry(scores,textvariable=update_personal_id,width=30).grid(row=6,column=1)
    text7 = tkinter.Entry(scores,textvariable=update_date_booking,width=30).grid(row=7,column=1)

    label9 = tkinter.Label(scores,text="New Room No").grid(row=1,column=4)
    label10 = tkinter.Label(scores,text="New First Name").grid(row=2,column=4)
    label11 = tkinter.Label(scores,text="New Last Name").grid(row=3,column=4)
    label12 = tkinter.Label(scores,text="New Date of birth").grid(row=4,column=4)
    label13 = tkinter.Label(scores,text="New Phone No.").grid(row=5,column=4)
    label14 = tkinter.Label(scores,text="New Aadhar Card No").grid(row=6,column=4)
    label15 = tkinter.Label(scores,text="New Check In date").grid(row=7,column=4)
    text8 = tkinter.Entry(scores,textvariable=new_room_allotted,width=30).grid(row=1,column=5)
    text9 = tkinter.Entry(scores,textvariable=new_first_name,width=30).grid(row=2,column=5)
    text10 = tkinter.Entry(scores,textvariable=new_last_name,width=30).grid(row=3,column=5)
    text11 = tkinter.Entry(scores,textvariable=new_dob,width=30).grid(row=4,column=5)
    text12 = tkinter.Entry(scores,textvariable=new_phone_no,width=30).grid(row=5,column=5)
    text13 = tkinter.Entry(scores,textvariable=new_personal_id,width=30).grid(row=6,column=5)
    text14 = tkinter.Entry(scores,textvariable=new_date_booking,width=30).grid(row=7,column=5)
    button1 = tkinter.Button(scores,text="Update Details",command=update1).grid(row=8,column=1)

def update1():
    newWindow = tkinter.Toplevel(window)
    newWindow.configure(bg="#98AFC7")
    newWindow.columnconfigure(0,minsize=20)
    newWindow.rowconfigure([0],minsize=50)
    room_no = update_room_allotted.get()
    fname = update_first_name.get()
    lname = update_last_name.get()
    dob = update_dob.get()
    phone = update_phone_no.get()
    adhar = update_personal_id.get()
    check_inn_date = update_date_booking.get()

    room_no1 = new_room_allotted.get()
    fname1 = new_first_name.get()
    lname1 = new_last_name.get()
    dob1 = new_dob.get()
    phone1 = new_phone_no.get()
    adhar1 = new_personal_id.get()
    check_inn_date1 = new_date_booking.get()
    cur = con.cursor()
    query1 = "update hotel_back_log set room_no = %s , fname = %s , lname = %s , date_of_birth = %s , phoneno = %s , personalid = %s , check_in_date = %s where room_no = %s and fname = %s and check_in_date = %s"
    t1 = (room_no1,fname1,lname1,dob1,phone1,adhar1,check_inn_date1,room_no,fname,check_inn_date)
    cur.execute(query1,t1)
    query2 = "update hotel set room_no = %s , fname = %s , lname = %s , date_of_birth = %s , phoneno = %s , personalid = %s , check_inn_date = %s where room_no = %s and fname = %s and check_inn_date = %s"
    t2 = (room_no1,fname1,lname1,dob1,phone1,adhar1,check_inn_date1,room_no,fname,check_inn_date)
    cur.execute(query2,t2)
    con.commit()
    print(cur.rowcount,"Update")
    label1 = tkinter.Label(newWindow, text="RECORDS UPDATED", font=LARGEFONT, fg="red",bg="blue").grid(row=0, column=1)


button_1 = tkinter.Button(window,text = "ROOMS AVAILABILITY", width=32, height=3, bg = "#E67451", fg="green", cursor="hand2", command=createNewWindow).grid(row=3, column=0)
button_2 = tkinter.Button(window,text = "CHECK IN & CHECK OUT", width=32, height=3, bg = "#E67451", fg="green", cursor="hand2", command=check).grid(row=3, column=2)
button_3 = tkinter.Button(window,text = "CUSTOMER'S DETAILS", width=32, height=3, bg = "#E67451", fg="green", cursor="hand2",command=records).grid(row=5, column=0)
button_4 = tkinter.Button(window,text = "CANCEL OR UPDATE", width=32, height=3, bg = "#E67451", fg="green", cursor="hand2",command=change).grid(row=5, column=2)
window.mainloop()