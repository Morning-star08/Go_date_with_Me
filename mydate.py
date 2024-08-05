import tkinter as tk
from PIL import Image, ImageTk
import cv2

no_press_count = 0  # Counter for "No" button presses

def button_click(option):
    global no_press_count
    # Destroy current widgets
    for widget in root.winfo_children():
        widget.destroy()

    if option == "yes":
        yes_screen()
    elif option == "no":
        no_press_count += 1
        if no_press_count > 3:
            final_attempt_screen()
        else:
            no_screen()

def buttons():
    button1 = tk.Button(root, text="Yes", command=lambda: button_click("yes"), bg="#eaf6ff", bd=1, activebackground="#FFFFFF", activeforeground="#000000", highlightbackground="#eaf6ff", highlightcolor="#eaf6ff", font=("Trebuchet MS", 16), relief=tk.RAISED)
    button2 = tk.Button(root, text="No", command=lambda: button_click("no"), bg="#eaf6ff", bd=1, activebackground="#FFFFFF", activeforeground="#000000", highlightbackground="#eaf6ff", highlightcolor="#eaf6ff", font=("Trebuchet MS", 16), relief=tk.RAISED)
    button1.place(x=100, y=285)
    button2.place(x=225, y=285)

def second_screen():
    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    new_label = tk.Label(root, text="Would you go on a date with me?", font=("Trebuchet MS Bold", 18), bg="#eaf6ff", fg="#472836")
    new_label.pack(pady=10)
    buttons()

def yes_screen():
    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    new_label = tk.Label(root, text="LETS GOOO!", font=("Trebuchet MS Bold", 18), bg="#eaf6ff", fg="#472836")
    new_label.pack(pady=20)
    play_video(r"C:\Users\namas\OneDrive\Documents\date_file\ezgif-7-5b0e340db7.mp4", loop=True)

def no_screen():
    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    def play_video_multiple_times(repetitions=4):
        def play_next(repeat_count):
            if repeat_count > 0:
                new_label = tk.Label(root, text="WHY Pressing No..\n THINK AGAIN!", font=("Trebuchet MS Bold", 18), bg="#eaf6ff", fg="#472836")
                new_label.pack(pady=20)
                play_video(r"C:\Users\namas\OneDrive\Documents\date_file\ezgif-7-a62baf085e.mp4", 
                           after_playback=lambda: play_next(repeat_count - 1))
            else:
                second_attempt()

        play_next(repetitions)

    play_video_multiple_times()

def second_attempt():
    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    new_label = tk.Label(root, text="Would you go on a date with me?", font=("Trebuchet MS Bold", 18), bg="#eaf6ff", fg="#472836")
    new_label.pack(pady=10)
    play_video(r"C:\Users\namas\OneDrive\Documents\date_file\ezgif-7-533b9f976d.mp4", loop=True)
    buttons()

def final_attempt_screen():
    for widget in root.winfo_children():
        widget.destroy()
    new_label = tk.Label(root, text="NO MORE NOO", font=("Trebuchet MS Bold", 18), bg="#eaf6ff", fg="#472836")
    new_label.pack(pady=10)
    button1 = tk.Button(root, text="Yes", command=lambda: button_click("yes"), bg="#eaf6ff", bd=1, activebackground="#FFFFFF", activeforeground="#000000", highlightbackground="#eaf6ff", highlightcolor="#eaf6ff", font=("Trebuchet MS", 16), relief=tk.RAISED)
    image2 = Image.open("secondimage.png")
    icon_path = r"C:\Users\namas\OneDrive\Documents\date_file\icon.ico"
    icon_image = Image.open(icon_path)
    tk_icon_image = ImageTk.PhotoImage(icon_image)
    icon_label = tk.Label(root, image=tk_icon_image)
    icon_label.image = tk_icon_image  # Store a reference to the image
    icon_label.pack()
    button1.place(x=165, y=285)
    


def start_second_screen():
    # Destroy current widgets
    for widget in root.winfo_children():
        widget.destroy()
    second_screen()
    play_video(r"C:\Users\namas\OneDrive\Documents\date_file\dogs.mp4")

def play_video(video_path, after_video_path=None, after_playback=None, loop=False):
    cap = cv2.VideoCapture(video_path)

    def update_video():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (300, 200))  # Resize the frame
            frame = Image.fromarray(frame)
            frame = ImageTk.PhotoImage(frame)
            if video_label.winfo_exists():  # Check if the label still exists
                video_label.config(image=frame)
                video_label.image = frame
                root.after(30, update_video)  # Continue updating
        else:
            if loop:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset to the first frame
                update_video()
            else:
                cap.release()
                if video_label.winfo_exists():  # Check if the label still exists
                    video_label.destroy()
                if after_video_path:
                    play_video(after_video_path, after_playback=after_playback)
                elif after_playback:
                    for widget in root.winfo_children():
                        widget.destroy()
                    after_playback()  # Call the after_playback function if provided

    video_label = tk.Label(root)
    video_label.pack(pady=10)
    update_video()

root = tk.Tk()
root.title("Date with me?")
root.geometry("400x350")
root.resizable(False, False)
root.iconbitmap("icon.ico")
root.configure(bg="#eaf6ff")

image_path = "firstimage.png"
image = Image.open(image_path)
tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=tk_image)
image_label.image = tk_image  # Store a reference to the image
image_label.pack()

button = tk.Button(root, text="Hello", command=start_second_screen, bg="#eaf6ff", bd=1, activebackground="#FFFFFF", activeforeground="#000000", highlightbackground="#eaf6ff", highlightcolor="#eaf6ff", font=("Trebuchet MS", 16), relief=tk.RAISED)
button.place(x=165, y=285)

root.mainloop()
