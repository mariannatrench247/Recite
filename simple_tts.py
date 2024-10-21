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

