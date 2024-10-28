import tkinter as tk
from tkinter import filedialog, messagebox, Canvas, ttk
from gtts import gTTS
import os

# Function to upload the text file
def upload_file():
    global text_file_path
    text_file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")], 
        title="Select a Text File"
    )
    if text_file_path:
        file_label.config(text=f"File: {os.path.basename(text_file_path)}", fg="#5e52ad")
        root.bell()  # Play a bell sound when the file is uploaded

# Function to convert text to speech
def text_to_speech():
    if not text_file_path:
        messagebox.showerror("Error", "Please upload a text file first.")
        return
    
    with open(text_file_path, "r", encoding="utf-8") as file:
        text = file.read()

    try:
        selected_voice = voice_var.get()
        tts = gTTS(text)
        audio_file = "output.mp3"
        tts.save(audio_file)
        messagebox.showinfo("Success", "Audio file created successfully!")
        download_button.config(state=tk.NORMAL)
        root.bell()  # Play a bell sound when the conversion is successful
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert text to speech: {e}")

# Function to download the audio file
def download_audio():
    save_path = filedialog.asksaveasfilename(
        defaultextension=".mp3", 
        filetypes=[("Audio Files", "*.mp3")], 
        title="Save Audio File"
    )
    if save_path:
        os.rename("output.mp3", save_path)
        messagebox.showinfo("Success", "Audio file downloaded successfully!")
        root.bell()  # Play a bell sound when the download is successful

# Create a rounded rectangle button using Canvas
def create_rounded_button(parent, text, command, bg_color="#966982", fg_color="white"):
    # Create the button canvas
    button_canvas = Canvas(parent, width=200, height=50, bg=parent.cget("bg"), highlightthickness=0)
    
    # Draw rounded rectangle
    radius = 20
    button_canvas.create_arc((0, 0, radius*2, radius*2), start=90, extent=90, fill=bg_color, outline=bg_color)
    button_canvas.create_arc((200-radius*2, 0, 200, radius*2), start=0, extent=90, fill=bg_color, outline=bg_color)
    button_canvas.create_arc((0, 50-radius*2, radius*2, 50), start=180, extent=90, fill=bg_color, outline=bg_color)
    button_canvas.create_arc((200-radius*2, 50-radius*2, 200, 50), start=270, extent=90, fill=bg_color, outline=bg_color)
    button_canvas.create_rectangle((radius, 0, 200-radius, 50), fill=bg_color, outline=bg_color)
    button_canvas.create_rectangle((0, radius, 200, 50-radius), fill=bg_color, outline=bg_color)
    
    # Add button text
    button_canvas.create_text(100, 25, text=text, fill=fg_color, font=("League Spartan", 12))
    button_canvas.bind("<Button-1>", lambda event: command())
    button_canvas.pack(pady=10, anchor="w")
    return button_canvas

# Set up the main window
root = tk.Tk()
root.title("Recite: Text to Speech Application")
root.geometry("800x500")
root.configure(bg="#816d92")  # Set background color here

text_file_path = None

# Create a frame for the left side content
left_frame = tk.Frame(root, bg="#816d92")
left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")

# Add a header label on the left side
header_label = tk.Label(
    left_frame, text="Upload your text file to convert to speech", 
    font=("League Spartan", 18), 
    bg="#816d92", fg="white"
)
header_label.pack(pady=10, anchor="w")

# Create rounded rectangle buttons below the header on the left side
upload_button = create_rounded_button(left_frame, "Upload Text File", upload_file)
convert_button = create_rounded_button(left_frame, "Convert to Speech", text_to_speech)
download_button = create_rounded_button(left_frame, "Download Audio", download_audio)
download_button.config(state=tk.DISABLED)  # Initially disabled

# Label to show uploaded file status on the left side
file_label = tk.Label(left_frame, text="No file selected.", font=("League Spartan", 10), bg="#816d92", fg="white")
file_label.pack(pady=5, anchor="w")

# Create a dropdown for voice selection
voice_var = tk.StringVar(value="Select a voice")
voice_options = ["Bugs Bunny", "Donald Trump", "Male", "Female"]
voice_dropdown = ttk.Combobox(left_frame, textvariable=voice_var, values=voice_options, state="readonly")
voice_dropdown.pack(pady=10, anchor="w")

# Create a frame for the right side content (logo)
right_frame = tk.Frame(root, bg="#816d92")
right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="ne")

# Load the logo image and place it in the right frame
try:
    logo_image = tk.PhotoImage(file="recitelogo1.png")
    logo_label = tk.Label(right_frame, image=logo_image, bg="#816d92")
    logo_label.pack(pady=5, anchor="e")
except Exception as e:
    print(f"Error loading logo image: {e}") 

# Start the Tkinter loop
root.mainloop()

