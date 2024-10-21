# Recite

Personal Text to Speech App - machine learning application written in python using TKinter & Google’s TTS API

![Recite Logo](https://github.com/user-attachments/assets/2cc1351e-c300-4158-88ab-b0f515d37e4f)


# Text-to-Speech Application

This is a simple text-to-speech (TTS) Python application using the `gTTS` library. It converts a text string into an audio file (MP3). 

** It's later version will use a TTS model that I trained using datasets from <img width="159" alt="Screenshot 2024-10-20 at 11 05 24 PM" src="https://github.com/user-attachments/assets/f88c6b0b-9eb6-45d8-aeff-044f4e68096f"> including the use of Suno | Bark a transformer-based text-to-audio model released in April 2023 licensed by MIT. Here's the original github repo: [Suno - Bark](https://github.com/suno-ai/bark). **



Here's a minimal script that you can add: find it in simple_tts.py, run the script python simple_tts.py in your terminal once you save to your computer.

# simple_tts.py
from gtts import gTTS        
                     
def text_to_speech(text, output_file="output.mp3"):       
    try:       
        tts = gTTS(text)      
        tts.save(output_file)      
        print(f"Audio file saved as {output_file}")       
    except Exception as e:       
        print(f"Error: {e}")       

# Example usage         
if __name__ == "__main__":         
    text = "Hello, this is a simple text-to-speech example."        
    text_to_speech(text)       

