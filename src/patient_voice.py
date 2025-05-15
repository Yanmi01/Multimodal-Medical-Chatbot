

# # setup Audio recorder

# from pydub import AudioSegment
# import speech_recognition as sr
# import logging
# from io import BytesIO

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# def record_audio(file_path, timeout=40, phrase_time_limit=None):
#     """
#     Record audio for a specified duration.
#     :param duration: Duration in seconds to record audio.
#     :return: Recorded audio as a BytesIO object.
#     """
#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()

#     try:
#         with microphone as source:
#             logging.info("Recording audio...")
#             recognizer.adjust_for_ambient_noise(source, duration=1)
#             recognizer.pause_threshold = 2.0
#             recognizer.energy_threshold = 300
#             logging.info("Please start speaking...")
            
#             audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
#             logging.info("Audio recording finished.")

#             # Convert the recorded audio to mp3 format
#             wav_audio = audio_data.get_wav_data()
#             audio_segment = AudioSegment.from_wav(BytesIO(wav_audio))
#             audio_segment.export(file_path, format="mp3", bitrate="128k")
           
#             logging.info(f"Audio saved to {file_path}")


#         # # Convert the recorded audio to BytesIO
#         # audio_bytes = BytesIO(audio_data.get_wav_data())
#         # logging.info("Audio recording complete.")
        
#     except Exception as e:
#         logging.error(f"Error recording audio: {e}")

# audio_file_path="patient_voice.mp3"
# record_audio(audio_file_path)

# # set up speech to text

# from groq import Groq
# import os
# from dotenv import load_dotenv
# load_dotenv()
# # Load environment variables from .env file
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# stt_model = "whisper-large-v3"

# def transcribe_audio(file_path):
#     """
#     Transcribe audio to text using Groq API.
#     :param file_path: Path to the audio file.
#     :return: Transcribed text.
#     """
#     try:
#         with open(audio_file_path, "rb") as audio_file:
#             audio_data = audio_file.read()
#             logging.info("Transcribing audio...")
#             groq = Groq(api_key=GROQ_API_KEY)
#             response = groq.audio.transcriptions.create(
#                 model=stt_model,
#                 file =audio_file,
#                 language="en",
#                 response_format="text"
#                 )
#             logging.info("Audio transcription complete.")
#             return response
#     except Exception as e:
#         logging.error(f"Error transcribing audio: {e}")
#         return None
# # Transcribe the audio file
# # transcribed_text = transcribe_audio(audio_file_path)
# # if transcribed_text:
# #     logging.info(f"Transcribed text: {transcribed_text}")

import logging
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
stt_model = "whisper-large-v3"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transcribe_audio(file_path):
    """
    Transcribe audio to text using Groq Whisper.
    :param file_path: Path to the audio file.
    :return: Transcribed text.
    """
    try:
        with open(file_path, "rb") as audio_file:
            audio_data = audio_file.read()
            logging.info("Transcribing audio...")
            groq = Groq(api_key=GROQ_API_KEY)
            response = groq.audio.transcriptions.create(
                model=stt_model,
                file=audio_data,
                language="en",
                response_format="text"
            )
            logging.info("Audio transcription complete.")
            return response
    except Exception as e:
        logging.error(f"Error transcribing audio: {e}")
        return "Transcription failed. Check logs."
