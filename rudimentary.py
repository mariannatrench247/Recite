import tkinter as tk
from tkinter import filedialog, messagebox, Canvas
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
        file_label.config(text=f"File: {os.path.basename(text_file_path)}", fg="#ffe176")
        root.bell()  # Play a bell sound when the file is uploaded

# Function to convert text to speech
def text_to_speech():
    if not text_file_path:
        messagebox.showerror("Error", "Please upload a text file first.")
        return
    
    with open(text_file_path, "r", encoding="utf-8") as file:
        text = file.read()

    try:
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
def create_rounded_button(parent, text, command, bg_color="#ffe176", fg_color="black"):
    button_canvas = Canvas(parent, width=200, height=50, bg="grey", highlightthickness=0)
    # Draw rounded rectangle
    radius = 20
    button_canvas.create_arc((0, 0, radius*2, radius*2), start=90, extent=90, fill=bg_color, outline=bg_color)
    button_canvas.create_arc((200-radius*2, 0, 200, radius*2), start=0, extent=90, fill=bg_color, outline=bg_color)
    button_canvas.create_arc((0, 50-radius*2, radius*2, 50), start=180, extent=90, fill=bg_color, outline=bg_color)
    button_canvas.create_arc((200-radius*2, 50-radius*2, 200, 50), start=270, extent=90, fill=bg_color, outline=bg_color)
    button_canvas.create_rectangle((radius, 0, 200-radius, 50), fill=bg_color, outline=bg_color)
    button_canvas.create_rectangle((0, radius, 200, 50-radius), fill=bg_color, outline=bg_color)
    # Add button text
    button_canvas.create_text(100, 25, text=text, fill=fg_color, font=("Hussar Bold", 12))
    button_canvas.bind("<Button-1>", lambda event: command())
    button_canvas.pack(pady=10, anchor="w")
    return button_canvas

# Set up the main window
root = tk.Tk()
root.title("Recite: Text to Speech Application")
root.geometry("800x500")
root.configure(bg="grey")

text_file_path = None

# Create a frame for the left side content
left_frame = tk.Frame(root, bg="grey")
left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")

# Add a header label on the left side
header_label = tk.Label(
    left_frame, text="Upload your text file to convert to speech", 
    font=("Hussar Bold", 18), 
    bg="grey", fg="#ffe176"
)
header_label.pack(pady=10, anchor="w")

# Create rounded rectangle buttons below the header on the left side
upload_button = create_rounded_button(left_frame, "Upload Text File", upload_file)
convert_button = create_rounded_button(left_frame, "Convert to Speech", text_to_speech)
download_button = create_rounded_button(left_frame, "Download Audio", download_audio)
download_button.config(state=tk.DISABLED)  # Initially disabled

# Label to show uploaded file status on the left side
file_label = tk.Label(left_frame, text="No file selected.", font=("Hussar Bold", 10), bg="grey", fg="white")
file_label.pack(pady=5, anchor="w")

# Create a frame for the right side content (logo)
right_frame = tk.Frame(root, bg="grey")
right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="ne")

# Load the logo image and place it in the right frame
try:
    logo_image = tk.PhotoImage(file="ReciteLogo1.png")
    logo_label = tk.Label(right_frame, image=logo_image, bg="grey")
    logo_label.pack(pady=5, anchor="e")
except Exception as e:
    print(f"Error loading logo image: {e}")

# Start the Tkinter loop
root.mainloop()
