// here is the simple code to convert mp3 files to wav files if you need them to train your TTS model 
// make sure you have bark, pydub, ffmpeg & AudioSegment installed on your device 

from pydub import Audio Segment 

#Load the .mp3 file 
audio = AudioSegment.from_mp3("path/to/file.mp3")

#Export it as a .wav file 
audio.export("path/to/file.wav", format="wav")

//Please note sometimes you'll have to add double forward or backward slashes. See below:

audio = AudioSegment.from_mp3("path//to//file.mp3") | audio = AudioSegment.from_mp3("path\\to\\file.mp3")
audio.export("path//to//file.wav", format="wav")    | audio.export("path\\to\\file.wav", format="wav")
