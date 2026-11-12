import speech_recognition as sr
from pydub import AudioSegment
import os

# Define audio filenames
mp3_file = "sample.mp3"
wav_file = "sample.wav"

# Check whether input file exists
if not os.path.exists(mp3_file):
    print("Error: sample.mp3 not found")
    exit()

# Convert MP3 to WAV
print("Converting MP3 to WAV...")

audio = AudioSegment.from_mp3(mp3_file)
audio.export(wav_file, format="wav")

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Read WAV audio file
with sr.AudioFile(wav_file) as source:
    print("Reading audio file...")
    audio_data = recognizer.record(source)

# Convert speech into text
try:
    print("Converting speech to text...")

    text = recognizer.recognize_google(audio_data)

    print("\nRecognized Text:")
    print(text)

except sr.UnknownValueError:
    print("Sorry, speech could not be understood.")

except sr.RequestError as e:
    print("Google Speech Recognition error:", e)
