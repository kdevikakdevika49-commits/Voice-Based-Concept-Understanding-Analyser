import whisper

# Load the Whisper model only once
model = whisper.load_model("tiny")

def transcribe_audio(audio_file):
    """
    Transcribes the given audio file into text.
    """
    result = model.transcribe(audio_file)
    return result["text"]