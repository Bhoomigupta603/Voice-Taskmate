from tkinter import *
from PIL import Image, ImageTk, ImageDraw
import speech_to_text
import action

# Root window
root = Tk()
root.title("Voice Taskmate")
root.state('zoomed')  # Fullscreen
root.configure(bg="#ffffff")

# Gradient background function
def create_gradient(canvas, width, height, color1, color2):
    for i in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * i / height)
        g = int(color1[1] + (color2[1] - color1[1]) * i / height)
        b = int(color1[2] + (color2[2] - color1[2]) * i / height)
        canvas.create_line(0, i, width, i, fill=f"#{r:02x}{g:02x}{b:02x}")

# Coral gradient colors
color1 = (114, 90, 122)   # Mauve (#725a7a) Start
color2 = (255, 117, 130)  # Coral (#ff7582) End

# Canvas for background gradient
canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), highlightthickness=0)
canvas.pack(fill="both", expand=True)
create_gradient(canvas, root.winfo_screenwidth(), root.winfo_screenheight(), color1, color2)

# Heading text on canvas
canvas.create_text(
    root.winfo_screenwidth() // 2,  # Center of the screen width
    int(root.winfo_screenheight() * 0.09),  # Adjust Y position
    text="Voice Taskmate",
    font=("Comic Sans MS", 40, "bold"),
    fill="#ff7582",  # Foreground color
    anchor="center",
)

# Assistant image with circular shape and transparency
original_image = Image.open("image/assisstant_image.png").resize((350, 350), Image.Resampling.LANCZOS)
circular_image = Image.new("RGBA", original_image.size, (0, 0, 0, 0))
mask = Image.new("L", original_image.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, 350, 350), fill=255)

# Apply circular mask to the image
circular_image.paste(original_image, (0, 0), mask)
image = ImageTk.PhotoImage(circular_image)

# Place assistant image below the heading
# Set the background of the label to match the gradient color or make it transparent
image_label = Label(root, image=image, borderwidth=0, highlightthickness=0, bg="#8c6179")  # Matching bg to white
image_label.place(relx=0.5, rely=0.4, anchor=CENTER)  # Adjusted rely for placement



# Conversation display area
text_frame = Frame(root, bg="#9A617C")  # Slightly darker shade for the frame
text_frame.place(relx=0.5, rely=0.75, relwidth=0.5, relheight=0.15, anchor=CENTER)

# Text widget with a lighter shade of the gradient
text = Text(
    text_frame,
    font=("Courier", 14, "bold"),
    fg="#725a7a",  # Mauve text color
    bg="#e4b5c3",  # Light pink for background
    wrap=WORD,
    relief="flat",
    highlightthickness=0,
)
text.pack(fill="both", expand=True, padx=10, pady=10)


# Button design function
def create_button(parent, text, command, bg, fg, hover_bg, relx, rely):
    def on_enter(e):
        btn.config(bg=hover_bg)

    def on_leave(e):
        btn.config(bg=bg)

    btn = Button(
        parent,
        text=text,
        font=("Comic Sans MS", 14, "bold"),
        bg=bg,
        fg=fg,
        relief="flat",
        command=command,
        activebackground=bg,  # Ensures the background stays the same after being clicked
        activeforeground=fg,  # Ensures the text color stays the same after being clicked
    )
    btn.place(relx=relx, rely=rely, width=250, height=50, anchor=CENTER)  # Equal width/height
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# Ask function
# def ask():
#     user_val = speech_to_text.speech_to_text()
#     bot_val = action.Action(user_val)
#     text.insert(END, 'User ---> ' + user_val + "\n")
#     if bot_val is not None:
#         text.insert(END, "BOT <--- " + str(bot_val) + "\n")
        

def ask():
    user_val = speech_to_text.speech_to_text()
    if not user_val:  # If None or empty
        text.insert(END, "BOT <--- I'm not able to understand your input\n")
        return
    bot_val = action.Action(user_val)
    text.insert(END, 'User--->'+ user_val+"\n")
    if bot_val != None:
        text.insert(END, "VOice Taskmate<---"+str(bot_val)+"\n")
    if bot_val == "ok ma'am":
        root.destroy()            

# Delete function
def del_text():
    text.delete('1.0', "end")



# Buttons with hover effect as default colors
ask_button = create_button(root, "Click Here to Talk to Me!", ask, "#d63e55", "#ffffff", "#b02b43", 0.4, 0.9)

# Button1 = Button(root, text="ASK", font=("comic Sans ms", 14, "bold"), bg="#E491A6", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
# Button1.place(x = 70, y = 640) 

delete_button = create_button(root, "Delete", del_text, "#4e3a50", "#ffffff", "#3a2d3c", 0.6, 0.9)

# Run the application
root.mainloop()





























# # pink shade
# from tkinter import *
# from PIL import Image, ImageTk
# import speech_to_text
# import action

# # Root window
# root = Tk()
# root.title("Voice Taskmate")
# root.geometry("650x775")
# root.resizable(False, False)

# # Gradient background
# canvas = Canvas(root, width=650, height=775)
# canvas.pack(fill="both", expand=True)

# # Function to create gradient
# def create_gradient(canvas, width, height, color1, color2):
#     for i in range(height):
#         r = int(color1[0] + (color2[0] - color1[0]) * i / height)
#         g = int(color1[1] + (color2[1] - color1[1]) * i / height)
#         b = int(color1[2] + (color2[2] - color1[2]) * i / height)
#         canvas.create_line(0, i, width, i, fill=f"#{r:02x}{g:02x}{b:02x}")

# # Coral Gradient Colors (Orange, Mauve)
# color1 = (255, 117, 130)   # Coral (#ff7582) Start
# color2 = (114, 90, 122)    # Mauve (#725a7a) End
# create_gradient(canvas, 650, 775, color1, color2)

# # Ask function
# def ask():
#     user_val = speech_to_text.speech_to_text()
#     bot_val = action.Action(user_val)
#     text.insert(END, 'User ---> ' + user_val + "\n")
#     if bot_val is not None:
#         text.insert(END, "BOT <--- " + str(bot_val) + "\n")
#     if bot_val == "ok ma'am":
#         root.destroy()

# # Send function
# def send():
#     send_val = entry.get()
#     bot_val = action.Action(send_val)
#     text.insert(END, 'User ---> ' + send_val + "\n")
#     if bot_val is not None:
#         text.insert(END, "BOT <--- " + str(bot_val) + "\n")
#     if bot_val == "ok ma'am":
#         root.destroy()

# # Delete function
# def del_text():
#     text.delete('1.0', "end")

# # Frame for title and image
# frame = LabelFrame(root, borderwidth=3, relief="solid", bg="#ffffff")
# frame.place(x=75, y=30, width=500, height=300)

# # Inside the frame
# text_label = Label(frame, text="Voice Taskmate", font=("Comic Sans MS", 24, "bold"), bg="#ffffff", fg="#ff7582")
# text_label.pack(pady=10)

# image = ImageTk.PhotoImage(Image.open("image/assisstant.png").resize((200, 200), Image.Resampling.LANCZOS))
# image_label = Label(frame, image=image, bg="#ffffff")
# image_label.pack()

# # Text widget for conversation
# text = Text(root, font=("Courier", 12, "bold"), bg="#fce4ec", fg="#725a7a", wrap=WORD, relief="sunken", borderwidth=3)
# text.place(x=100, y=350, width=470, height=150)

# # Entry widget
# entry = Entry(root, font=("Comic Sans MS", 14), justify=CENTER, bg="#ffffff", fg="#ff7582", relief="solid", borderwidth=2)
# entry.place(x=100, y=520, width=470, height=40)

# # Button design function
# def create_button(text, command, x, y, bg, fg, hover_bg):
#     def on_enter(e):
#         btn.config(bg=hover_bg)

#     def on_leave(e):
#         btn.config(bg=bg)

#     btn = Button(root, text=text, font=("Comic Sans MS", 12, "bold"), bg=bg, fg=fg, relief="flat", command=command)
#     btn.place(x=x, y=y, width=120, height=50)
#     btn.bind("<Enter>", on_enter)
#     btn.bind("<Leave>", on_leave)

# # Buttons with hover effects
# create_button("ASK", ask, x=70, y=600, bg="#ff7582", fg="#ffffff", hover_bg="#d63e55")
# create_button("DELETE", del_text, x=270, y=600, bg="#725a7a", fg="#ffffff", hover_bg="#4e3a50")
# create_button("SEND", send, x=470, y=600, bg="#ff7582", fg="#ffffff", hover_bg="#d63e55")

# # Run the application
# root.mainloop()


































































# Actual Code that was written
# from tkinter import*
# from PIL import Image, ImageTk
# import speech_to_text
# import action
# root = Tk()
# root.title("Voice Taskmate")
# root.geometry("650x775")
# root.resizable(False, False)
# root.config(bg="#845763")

# # ask fun
# def ask():
#     user_val = speech_to_text.speech_to_text()
#     if not user_val:  # If None or empty
#         text.insert(END, "BOT <--- I'm not able to understand your input\n")
#         return
#     bot_val = action.Action(user_val)
#     text.insert(END, 'User--->'+ user_val+"\n")
#     if bot_val != None:
#         text.insert(END, "BOT <---"+str(bot_val)+"\n")
#     if bot_val == "ok ma'am":
#         root.destroy()    
    
# # send fun
# def send():
#     send = entry.get()  
#     bot =  action.Action(send) 
#     text.insert(END, 'User--->'+ send+"\n")
#     if bot != None:
#         text.insert(END, "BOT <---"+str(bot)+"\n")
#     if bot == "ok ma'am":
#         root.destroy() 
    
# # delete fun
# def del_text():
#     text.delete('1.0', "end")    
     

# # frame 

# frame = LabelFrame(root, padx = 140, pady = 7, borderwidth = 3, relief= "raised")
# frame.config(bg="#845763")
# frame.grid(row = 0, column = 1, padx = 55, pady = 10)

# #inside the frame 
# # 1. text label
# text_label = Label(frame, text = "Voice Taskmate", font=("comic Sans ms", 14, "bold"), bg="#E491A6")
# text_label.grid(row = 0, column = 0, padx = 20, pady = 10)

# #Image
# image = ImageTk.PhotoImage(Image.open("image/assisstant.png"))
# image_label = Label(frame, image=image)
# image_label.grid(row = 1, column = 0)

# # # Adding Text View Widget 
# text = Text(root, font= ('courier 10 bold'), bg="#E491A6")
# text.grid(row = 2, column = 0)
# text.place(x = 100, y = 460, width = 470, height = 100)

# # Entry widget

# entry = Entry(root, justify=CENTER)
# entry.place(x = 100, y = 580, width = 470, height= 30)

# # Button 1
# Button1 = Button(root, text="ASK", font=("comic Sans ms", 14, "bold"), bg="#E491A6", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
# Button1.place(x = 70, y = 640) 

# # Button 2
# Button2 = Button(root, text="DELETE", font=("comic Sans ms", 14, "bold"),  bg="#E491A6", pady=16, padx=40, borderwidth=3, relief=SOLID, command=del_text)
# Button2.place(x = 240, y = 640) 

# # Button 3
# Button3 = Button(root, text="SEND", font=("comic Sans ms", 14, "bold"),  bg="#E491A6", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
# Button3.place(x = 440, y = 640) 


# root.mainloop()
















# orange color
# from tkinter import *
# from PIL import Image, ImageTk
# import speech_to_text
# import action

# # Root window
# root = Tk()
# root.title("Voice Taskmate")
# root.geometry("650x775")
# root.resizable(False, False)

# # Gradient background
# canvas = Canvas(root, width=650, height=775)
# canvas.pack(fill="both", expand=True)

# # Function to create gradient
# def create_gradient(canvas, width, height, color1, color2):
#     for i in range(height):
#         r = int(color1[0] + (color2[0] - color1[0]) * i / height)
#         g = int(color1[1] + (color2[1] - color1[1]) * i / height)
#         b = int(color1[2] + (color2[2] - color1[2]) * i / height)
#         canvas.create_line(0, i, width, i, fill=f"#{r:02x}{g:02x}{b:02x}")

# # Coral Gradient Colors (Light Orange to Pink)
# color1 = (255, 153, 102)   # Coral (#FF9966) Start
# color2 = (255, 94, 98)     # Pinkish Coral (#FF5E62) End
# create_gradient(canvas, 650, 775, color1, color2)

# # Ask function
# def ask():
#     user_val = speech_to_text.speech_to_text()
#     bot_val = action.Action(user_val)
#     text.insert(END, 'User ---> ' + user_val + "\n")
#     if bot_val is not None:
#         text.insert(END, "BOT <--- " + str(bot_val) + "\n")
#     if bot_val == "ok ma'am":
#         root.destroy()

# # Send function
# def send():
#     send_val = entry.get()
#     bot_val = action.Action(send_val)
#     text.insert(END, 'User ---> ' + send_val + "\n")
#     if bot_val is not None:
#         text.insert(END, "BOT <--- " + str(bot_val) + "\n")
#     if bot_val == "ok ma'am":
#         root.destroy()

# # Delete function
# def del_text():
#     text.delete('1.0', "end")

# # Frame for title and image
# frame = LabelFrame(root, borderwidth=3, relief="solid", bg="#ffffff")
# frame.place(x=75, y=30, width=500, height=300)

# # Inside the frame
# text_label = Label(frame, text="Voice Taskmate", font=("Comic Sans MS", 24, "bold"), bg="#ffffff", fg="#FF9966")
# text_label.pack(pady=10)

# image = ImageTk.PhotoImage(Image.open("image/assisstant.png").resize((200, 200), Image.Resampling.LANCZOS))
# image_label = Label(frame, image=image, bg="#ffffff")
# image_label.pack()

# # Text widget for conversation
# text = Text(root, font=("Courier", 12, "bold"), bg="#FFE0D6", fg="#FF5E62", wrap=WORD, relief="sunken", borderwidth=3)
# text.place(x=100, y=350, width=470, height=150)

# # Entry widget
# entry = Entry(root, font=("Comic Sans MS", 14), justify=CENTER, bg="#ffffff", fg="#FF5E62", relief="solid", borderwidth=2)
# entry.place(x=100, y=520, width=470, height=40)

# # Button design function
# def create_button(text, command, x, y, bg, fg, hover_bg):
#     def on_enter(e):
#         btn.config(bg=hover_bg)

#     def on_leave(e):
#         btn.config(bg=bg)

#     btn = Button(root, text=text, font=("Comic Sans MS", 12, "bold"), bg=bg, fg=fg, relief="flat", command=command)
#     btn.place(x=x, y=y, width=120, height=50)
#     btn.bind("<Enter>", on_enter)
#     btn.bind("<Leave>", on_leave)

# # Buttons with hover effects
# create_button("ASK", ask, x=70, y=600, bg="#FF9966", fg="#ffffff", hover_bg="#E67357")
# create_button("DELETE", del_text, x=270, y=600, bg="#FF5E62", fg="#ffffff", hover_bg="#E14D5A")
# create_button("SEND", send, x=470, y=600, bg="#FF9966", fg="#ffffff", hover_bg="#E67357")

# # Run the application
# root.mainloop()
