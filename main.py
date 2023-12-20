primary_color = "#393646"
secondary_color = "#F4EEE0"
accent_color = "#4F4557"
underHover_color = "#8f8a7f"

from tkinter import *
from detection import start_detection
from record import start_record, csv_file_name
import pickle
import threading
from train import train
from PIL import ImageTk, Image


root = Tk()
root.geometry("500x400")
root.configure(bg=primary_color)
root.iconbitmap("favicon.ico")
# root.resizable(width=False, height=False)

padx1 = 10
pady1 = 6

options_frame = Frame(root, bg=accent_color)

def hide_indicate():
    home_indicate.config(bg=accent_color)
    add_indicate.config(bg=accent_color)
    about_indicate.config(bg=accent_color)
    contact_indicate.config(bg=accent_color)
    learn_indicate.config(bg=accent_color)
    detect_indicate.config(bg=accent_color)

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


def show_indicate(lb, page):
    hide_indicate()
    lb.config(bg=secondary_color)
    delete_pages()
    page()
home_btn = Button(options_frame, text="Home", font=("Helvetica", "16"), fg=secondary_color, bd=0, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, command=lambda: show_indicate(home_indicate, home_page))
home_btn.place(x=10, y=50)

home_indicate = Label(options_frame, text=" ", background=accent_color)
home_indicate.place(x=3, y=50, width=5, height=40)

learn_btn = Button(options_frame, text="Learn", font=("Helvetica", "16"), fg=secondary_color, bd=0, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, command=lambda: show_indicate(learn_indicate, learn_page))
learn_btn.place(x=10, y=100)

learn_indicate = Label(options_frame, text=" ", background=accent_color)
learn_indicate.place(x=3, y=100, width=5, height=40)

add_btn = Button(options_frame, text="Add Sign", font=("Helvetica", "16"), fg=secondary_color, bd=0, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, command=lambda: show_indicate(add_indicate, add_page))
add_btn.place(x=10, y=150)

add_indicate = Label(options_frame, text=" ", background=accent_color)
add_indicate.place(x=3, y=150, width=5, height=40)

detect_btn = Button(options_frame, text="Detect", font=("Helvetica", "16"), fg=secondary_color, bd=0, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, command=lambda: show_indicate(detect_indicate, detect_page))
detect_btn.place(x=10, y=200)

detect_indicate = Label(options_frame, text=" ", background=accent_color)
detect_indicate.place(x=3, y=200, width=5, height=40)

about_btn = Button(options_frame, text="About", font=("Helvetica", "16"), fg=secondary_color, bd=0, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, command=lambda: show_indicate(about_indicate, about_page))
about_btn.place(x=10, y=250)

about_indicate = Label(options_frame, text=" ", background=accent_color)
about_indicate.place(x=3, y=250, width=5, height=40)

contact_btn = Button(options_frame, text="Contact", font=("Helvetica", "16"), fg=secondary_color, bd=0, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, command=lambda: show_indicate(contact_indicate, contact_page))
contact_btn.place(x=10, y=300)

contact_indicate = Label(options_frame, text=" ", background=accent_color)
contact_indicate.place(x=3, y=300, width=5, height=40)


options_frame.pack(side=LEFT)
options_frame.pack_propagate(False)
options_frame.configure(height=400, width=125)



##################################     MAIN         #######################
main_frame = Frame(root, bg=primary_color)

def switch_learn_pages(page):
    for frame in main_frame.winfo_children():
        frame.destroy()
    page()

def learn1_page():
    
    learn1_frame = Frame(main_frame)
    
    img = Image.open("Assets/Sign6.png")
    #resized_img = img.resize((200, 200), Image.ANTIALIAS)
    img_obj = ImageTk.PhotoImage(img)

    heading = Label(learn1_frame, text="Drinking", background=secondary_color, font=("Helvetica", "22"), foreground=secondary_color, bg=primary_color, padx=200)
    img_frame = Frame(learn1_frame, bg=primary_color, padx=15, pady=4)
    desc_img_label = Label(img_frame, image=img_obj, bg=primary_color)
    desc_img_label.image = img_obj
    desc = Label(learn1_frame, text="Make a C shape with your hand and\ntip it towards your mouth", background=secondary_color, font=("Helvetica", "14"), padx=100, pady=6, foreground=secondary_color, bg=primary_color)
    
    tryout_btn_frame = Frame(learn1_frame, bg=primary_color, padx=120)
    tryout_btn = Button(tryout_btn_frame, text="Try Yourself!", command=lambda: detect_func(skeleton, invalid_dir_label),  font=("Helvetica", "16"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, padx=5, pady=4)
    
    navigator = Frame(learn1_frame, bg=primary_color, padx=170)
    next_btn_frame = Frame(navigator, bg=primary_color)
    next_btn = Button(next_btn_frame, text=">>", command=lambda: switch_learn_pages(learn2_page),  font=("Helvetica", "12"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color)
    
    
    heading.pack()
    desc_img_label.pack(padx=45)
    img_frame.pack()
    desc.pack()
    tryout_btn_frame.pack()
    tryout_btn.pack()
    next_btn_frame.grid(row=0, column=1)
    next_btn.pack(padx=5, pady=5)
    navigator.pack()
    
    learn1_frame.pack(pady=10)

def learn2_page():
     
    learn2_frame = Frame(main_frame)
    
    img = Image.open("Assets/Sign2.png")
    #resized_img = img.resize((200, 200), Image.ANTIALIAS)
    img_obj = ImageTk.PhotoImage(img)

    heading = Label(learn2_frame, text="Play", background=secondary_color, font=("Helvetica", "22"), foreground=secondary_color, bg=primary_color, padx=200)
    img_frame = Frame(learn2_frame, bg=primary_color, padx=15, pady=4)
    desc_img_label = Label(img_frame, image=img_obj, bg=primary_color)
    desc_img_label.image = img_obj
    desc = Label(learn2_frame, text="Wingle your fingers in front of you", background=secondary_color, font=("Helvetica", "14"), padx=100, pady=17, foreground=secondary_color, bg=primary_color)
    
    tryout_btn_frame = Frame(learn2_frame, bg=primary_color, padx=120)
    tryout_btn = Button(tryout_btn_frame, text="Try Yourself!", command=lambda: detect_func(skeleton, invalid_dir_label),  font=("Helvetica", "16"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, padx=5, pady=4)
    
    navigator = Frame(learn2_frame, bg=primary_color, padx=146)
    next_btn_frame = Frame(navigator, bg=primary_color)
    next_btn = Button(next_btn_frame, text=">>", command=lambda: switch_learn_pages(learn3_page),  font=("Helvetica", "12"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color)
    prev_btn_frame = Frame(navigator, bg=primary_color)
    prev_btn = Button(prev_btn_frame, text="<<", command=lambda: switch_learn_pages(learn1_page),  font=("Helvetica", "12"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color)
    
    heading.pack()
    desc_img_label.pack(padx=45)
    img_frame.pack()
    desc.pack()
    tryout_btn_frame.pack()
    tryout_btn.pack()
    prev_btn_frame.grid(row=0, column=0)
    prev_btn.pack(padx=5, pady=5)
    next_btn_frame.grid(row=0, column=1)
    next_btn.pack(padx=5, pady=5)
    navigator.pack()
    
    learn2_frame.pack(pady=10)

def learn3_page():
     
    learn3_frame = Frame(main_frame)
    
    img = Image.open("Assets/Sign3.png")
    #resized_img = img.resize((200, 200), Image.ANTIALIAS)
    img_obj = ImageTk.PhotoImage(img)

    heading = Label(learn3_frame, text="Finish", background=secondary_color, font=("Helvetica", "22"), foreground=secondary_color, bg=primary_color, padx=200)
    img_frame = Frame(learn3_frame, bg=primary_color, padx=15, pady=4)
    desc_img_label = Label(img_frame, image=img_obj, bg=primary_color)
    desc_img_label.image = img_obj
    desc = Label(learn3_frame, text="Open both hands and flip over", background=secondary_color, font=("Helvetica", "14"), padx=100, pady=17, foreground=secondary_color, bg=primary_color)
    
    tryout_btn_frame = Frame(learn3_frame, bg=primary_color, padx=120)
    tryout_btn = Button(tryout_btn_frame, text="Try Yourself!", command=lambda: detect_func(skeleton, invalid_dir_label),  font=("Helvetica", "16"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, padx=5, pady=4)
    
    navigator = Frame(learn3_frame, bg=primary_color, padx=146)
    next_btn_frame = Frame(navigator, bg=primary_color)
    next_btn = Button(next_btn_frame, text=">>", command=lambda: switch_learn_pages(learn4_page),  font=("Helvetica", "12"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color)
    prev_btn_frame = Frame(navigator, bg=primary_color)
    prev_btn = Button(prev_btn_frame, text="<<", command=lambda: switch_learn_pages(learn2_page),  font=("Helvetica", "12"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color)
    
    heading.pack()
    desc_img_label.pack(padx=45)
    img_frame.pack()
    desc.pack()
    tryout_btn_frame.pack()
    tryout_btn.pack()
    prev_btn_frame.grid(row=0, column=0)
    prev_btn.pack(padx=5, pady=5)
    next_btn_frame.grid(row=0, column=1)
    next_btn.pack(padx=5, pady=5)
    navigator.pack()
    
    learn3_frame.pack(pady=10)

def learn4_page():
     
    learn4_frame = Frame(main_frame)
    
    img = Image.open("Assets/Sign4.png")
    #resized_img = img.resize((200, 200), Image.ANTIALIAS)
    img_obj = ImageTk.PhotoImage(img)

    heading = Label(learn4_frame, text="Sorry", background=secondary_color, font=("Helvetica", "22"), foreground=secondary_color, bg=primary_color, padx=200)
    img_frame = Frame(learn4_frame, bg=primary_color, padx=15, pady=4)
    desc_img_label = Label(img_frame, image=img_obj, bg=primary_color)
    desc_img_label.image = img_obj
    desc = Label(learn4_frame, text="Close your wrist and rotate\nyour hand around your chest", background=secondary_color, font=("Helvetica", "14"), padx=100, pady=6, foreground=secondary_color, bg=primary_color)
    
    tryout_btn_frame = Frame(learn4_frame, bg=primary_color, padx=120)
    tryout_btn = Button(tryout_btn_frame, text="Try Yourself!", command=lambda: detect_func(skeleton, invalid_dir_label),  font=("Helvetica", "16"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, padx=5, pady=4)
    
    navigator = Frame(learn4_frame, bg=primary_color, padx=146)
    next_btn_frame = Frame(navigator, bg=primary_color)
    next_btn = Button(next_btn_frame, text=">>", command=lambda: switch_learn_pages(learn5_page),  font=("Helvetica", "12"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color)
    prev_btn_frame = Frame(navigator, bg=primary_color)
    prev_btn = Button(prev_btn_frame, text="<<", command=lambda: switch_learn_pages(learn3_page),  font=("Helvetica", "12"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color)
    
    heading.pack()
    desc_img_label.pack(padx=45)
    img_frame.pack()
    desc.pack()
    tryout_btn_frame.pack()
    tryout_btn.pack()
    prev_btn_frame.grid(row=0, column=0)
    prev_btn.pack(padx=5, pady=5)
    next_btn_frame.grid(row=0, column=1)
    next_btn.pack(padx=5, pady=5)
    navigator.pack()
    
    learn4_frame.pack(pady=10)


def learn5_page():
     
    learn5_frame = Frame(main_frame)
    
    img = Image.open("Assets/Sign5.png")
    #resized_img = img.resize((200, 200), Image.ANTIALIAS)
    img_obj = ImageTk.PhotoImage(img)

    heading = Label(learn5_frame, text="Blue", background=secondary_color, font=("Helvetica", "22"), foreground=secondary_color, bg=primary_color, padx=200)
    img_frame = Frame(learn5_frame, bg=primary_color, padx=15, pady=4)
    desc_img_label = Label(img_frame, image=img_obj, bg=primary_color)
    desc_img_label.image = img_obj
    desc = Label(learn5_frame, text="Fold your thumb finger and \n open four fingers", background=secondary_color, font=("Helvetica", "14"), padx=100, pady=6, foreground=secondary_color, bg=primary_color)
    
    tryout_btn_frame = Frame(learn5_frame, bg=primary_color, padx=120)
    tryout_btn = Button(tryout_btn_frame, text="Try Yourself!", command=lambda: detect_func(skeleton, invalid_dir_label),  font=("Helvetica", "16"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, padx=5, pady=4)
    
    navigator = Frame(learn5_frame, bg=primary_color, padx=170)
    prev_btn_frame = Frame(navigator, bg=primary_color)
    prev_btn = Button(prev_btn_frame, text="<<", command=lambda: switch_learn_pages(learn4_page),  font=("Helvetica", "12"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color)
    
    
    heading.pack()
    desc_img_label.pack(padx=45)
    img_frame.pack()
    desc.pack()
    tryout_btn_frame.pack()
    tryout_btn.pack()
    prev_btn_frame.grid(row=0, column=1)
    prev_btn.pack(padx=5, pady=5)
    navigator.pack()
    
    learn5_frame.pack(pady=10)
   
def home_page():
    home_frame = Frame(main_frame)

    
    heading = Label(home_frame, text="SignSense", background=secondary_color, font=("Helvetica", "28"), foreground=secondary_color, bg=primary_color, padx=200)
    sub_heading = Label(home_frame, text="Real-Time Sign Language Recognition", background=secondary_color, font=("Helvetica", "14"), padx=100, foreground=secondary_color, bg=primary_color)
    
    img = Image.open("Assets/favicon.png")
    resized_img = img.resize((200, 200), Image.ANTIALIAS)
    img_obj = ImageTk.PhotoImage(resized_img)
    img_frame = Frame(home_frame, bg=primary_color, padx=88, pady=30)
    logo_img_label = Label(img_frame, image=img_obj, bg=primary_color)
    logo_img_label.image = img_obj

    heading.pack()
    sub_heading.pack()
    logo_img_label.pack()
    img_frame.pack()


    home_frame.pack(pady=20)

def learn_page():
    learn_home_frame = Frame(main_frame)
    
    heading = Label(learn_home_frame, text="Learn", background=secondary_color, font=("Helvetica", "28"), foreground=secondary_color, bg=primary_color, padx=200)
    sub_heading = Label(learn_home_frame, text="Real-Time Sign Language Recognition", background=secondary_color, font=("Helvetica", "14"), padx=100, pady=8, foreground=secondary_color, bg=primary_color)

    lesson1_frame = Frame(learn_home_frame, bg=primary_color, padx=50)
    lesson1_btn = Button(lesson1_frame, text="Lesson 1 : Drink", command=lambda: switch_learn_pages(learn1_page),  font=("Helvetica", "16"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, padx=55, pady=2)
    
    lesson2_frame = Frame(learn_home_frame, bg=primary_color, padx=50)
    lesson2_btn = Button(lesson2_frame, text="Lesson 2 : Play", command=lambda: switch_learn_pages(learn2_page),  font=("Helvetica", "16"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, padx=60, pady=2)
    
    lesson3_frame = Frame(learn_home_frame, bg=primary_color, padx=50)
    lesson3_btn = Button(lesson3_frame, text="Lesson 3 : Finish", command=lambda: switch_learn_pages(learn3_page),  font=("Helvetica", "16"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, padx=55, pady=2)

    lesson4_frame = Frame(learn_home_frame, bg=primary_color, padx=50)
    lesson4_btn = Button(lesson4_frame, text="Lesson 4 : Sorry", command=lambda: switch_learn_pages(learn4_page),  font=("Helvetica", "16"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, padx=55, pady=2)

    lesson5_frame = Frame(learn_home_frame, bg=primary_color, padx=50)
    lesson5_btn = Button(lesson5_frame, text="Lesson 5 : Blue", command=lambda: switch_learn_pages(learn5_page),  font=("Helvetica", "16"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, padx=60, pady=2)


    heading.pack()
    sub_heading.pack()

    lesson1_btn.pack(pady=5)
    lesson1_frame.pack()
    lesson2_btn.pack(pady=5)
    lesson2_frame.pack()
    lesson3_btn.pack(pady=5)
    lesson3_frame.pack()
    lesson4_btn.pack(pady=5)
    lesson4_frame.pack()
    lesson5_btn.pack(pady=5)
    lesson5_frame.pack()

    learn_home_frame.pack(pady=20)

def add_page():
    add_frame = Frame(main_frame)

    addTop_frame = Frame(add_frame, bg=primary_color)
    addBottom_frame = Frame(add_frame, bg=primary_color)
    
    #heading = Label(homeTop_frame, text="SignSense", background=secondary_color, font=("Helvetica", "28"), foreground=secondary_color, bg=primary_color, padx=200)
    sub_heading = Label(addTop_frame, text="Add in your own Signs and Gestures", background=secondary_color, font=("Helvetica", "16"), padx=100, foreground=secondary_color, bg=primary_color)

    instruction = Label(addTop_frame, text="Instructions:\n\n1. Train the machine by providing 50 video sequences\n\n2. Each Video Sequence consist of 30 frames\n\n3. Repeat your action/sign every sequence\n\n4. A two seconds gap is given between\nevery sequences for the user to reposition", background=secondary_color, font=("Helvetica", "11"), padx=100, foreground=secondary_color, bg=primary_color, pady=25)
    
    button_frame = Frame(addBottom_frame, bg=primary_color, padx=140)
    input_frame = Frame(addBottom_frame, bg=primary_color, padx=20)
    
    skeleton = IntVar()
    #skeleton_checkbox = Checkbutton(addBottom_frame, onvalue=1, offvalue=0, text="Skeletal Mode", variable=skeleton, font=("Helvetica", "14"), fg="#4C6E83" ,bg=primary_color, activebackground=primary_color)
    action_input_field = Entry(input_frame, width=25, font=("Helvetica", "12"))
    name_text = Label(input_frame, text="Name: ", background=secondary_color, font=("Helvetica", "12"), padx=5, foreground=secondary_color, bg=primary_color)

    loading_text = Label(addBottom_frame, text="", background=secondary_color, font=("Helvetica", "12"), padx=5, foreground=secondary_color, bg=primary_color)
    add_btn = Button(addBottom_frame, text="New Sign", command=lambda:add_func(action_input_field.get(), action_input_field, loading_text),  font=("Helvetica", "16"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, padx=15, pady=4)
    
    # heading.pack()
    sub_heading.pack()
    instruction.pack()
    name_text.grid(row=0, column=0)
    action_input_field.grid(row=0, column=1)
    input_frame.pack()
    loading_text.pack()
    #input_frame.pack_propagate(False)
    add_btn.pack()
    button_frame.pack()
    #skeleton_checkbox.pack()
    
    addTop_frame.pack(side=TOP)
    addTop_frame.pack_propagate(False)
    addTop_frame.configure(height=250, width=500)

    addBottom_frame.pack(side=BOTTOM)
    addBottom_frame.pack_propagate(False)
    addBottom_frame.configure(height=200, width=500)

    add_frame.pack(pady=20)

def detect_page():
    home_frame = Frame(main_frame)

    homeTop_frame = Frame(home_frame, bg=primary_color)
    homeBottom_frame = Frame(home_frame, bg=primary_color)
    
    heading = Label(homeTop_frame, text="Detect Signs", background=secondary_color, font=("Helvetica", "22"), foreground=secondary_color, bg=primary_color, padx=200)
    sub_heading = Label(homeTop_frame, text="Detect all signs recorded and test yourself", background=secondary_color, font=("Helvetica", "14"), padx=100,pady=15 ,foreground=secondary_color, bg=primary_color)
    
    skeleton = IntVar()
    skeleton_checkbox = Checkbutton(homeBottom_frame, onvalue=1, offvalue=0, text="Skeletal Mode", variable=skeleton, font=("Helvetica", "14"), fg="#4C6E83" ,bg=primary_color, activebackground=primary_color)
    
    button_frame = Frame(homeBottom_frame, bg=primary_color, padx=140)
    invalid_dir_label = Label(homeBottom_frame, text="", background=secondary_color, font=("Helvetica", "12"), padx=100, foreground=secondary_color, bg=primary_color)
    detect_btn = Button(homeBottom_frame, text="Detect", command=lambda: detect_func(skeleton, invalid_dir_label),  font=("Helvetica", "16"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, padx=15, pady=4)
    
    
    heading.pack()
    sub_heading.pack()
    detect_btn.pack()
    button_frame.pack()
    skeleton_checkbox.pack()
    invalid_dir_label.pack()
    
    homeTop_frame.pack(side=TOP)
    homeTop_frame.pack_propagate(False)
    homeTop_frame.configure(height=250, width=500)

    homeBottom_frame.pack(side=BOTTOM)
    homeBottom_frame.pack_propagate(False)
    homeBottom_frame.configure(height=200, width=500)

    home_frame.pack(pady=20)

def about_page():
    about_frame = Frame(main_frame)

    aboutTop_frame = Frame(about_frame, bg=primary_color)
    aboutBottom_frame = Frame(about_frame, bg=primary_color)
    
    heading = Label(aboutTop_frame, text="About", background=secondary_color, font=("Helvetica", "28"), foreground=secondary_color, bg=primary_color, padx=200)
    text = Label(aboutBottom_frame, text="SignSense is a real-time hand sign detection\n software designed to empower users in effective\n communication through sign language.\n Leveraging advanced computer vision and \nmachine learning, the software captures \nlive video input, tracks hand movements,\n and recognizes diverse hand signs in real-time. \n\n\nThis software is made as a prototype for SIH 2023", background=secondary_color, font=("Helvetica", "13"), padx=100,pady=10 ,foreground=secondary_color, bg=primary_color)

    #button_frame = Frame(aboutBottom_frame, bg=primary_color, padx=140)
    #detect_btn = Button(aboutBottom_frame, text="Detect", command=detect_func,  font=("Helvetica", "16"), fg=secondary_color, bg=accent_color, activeforeground=underHover_color, activebackground=accent_color, padx=15, pady=4)
    
    #heckbox = Checkbutton(aboutBottom_frame, onvalue=1, offvalue=0, text="Skeletal Mode", variable=skeleton, font=("Helvetica", "14"), fg="#4C6E83" ,bg=primary_color, activebackground=primary_color)
    
    
    heading.pack()
    text.pack()
    #detect_btn.pack()
    # button_frame.pack()
    # skeleton_checkbox.pack()
    
    aboutTop_frame.pack(side=TOP)
    aboutTop_frame.pack_propagate(False)
    aboutTop_frame.configure(height=80, width=500)

    aboutBottom_frame.pack(side=BOTTOM)
    aboutBottom_frame.pack_propagate(False)
    aboutBottom_frame.configure(height=200, width=500)

    
    about_frame.pack(pady=20)


def contact_page():
    contact_frame = Frame(main_frame)
    
    sub_heading = Label(contact_frame, text="For any queries related to the software,\nPlease contact\n\nPh no: 8130337161, 8618079805\n\nEmail: karthiksureshnair6@gmail.com", background=secondary_color, font=("Helvetica", "14"), padx=100, pady=85, foreground=secondary_color, bg=primary_color)
    
    skeleton = IntVar()
    # skeleton_checkbox = Checkbutton(homeBottom_frame, onvalue=1, offvalue=0, text="Skeletal Mode", variable=skeleton, font=("Helvetica", "14"), fg="#4C6E83" ,bg=primary_color, activebackground=primary_color)
    
    
    # heading.pack()
    sub_heading.pack()
    # detect_btn.pack()
    # button_frame.pack()
    # skeleton_checkbox.pack()



    contact_frame.pack(pady=20)



main_frame.pack(side=RIGHT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=500)

def detect_func(skeleton_value, text_label):
    if(not start_detection(skeleton_value.get())):
        text_label.config(text="ERROR: Couldn't find trained model data")

def add_func(action_name, input_field, loading_label):
    threading.Thread(target=start_record(action_name)).start()
    input_field.delete(0, END)
    loading_label.config(text="Recording...")
    threading.Thread(target=lambda: train(loading_label, csv_file_name)).start()


show_indicate(home_indicate, home_page)



root.mainloop()