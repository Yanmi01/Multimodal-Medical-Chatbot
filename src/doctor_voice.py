import os
import platform
import subprocess
import logging
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
logging.basicConfig(level=logging.INFO)

def text_to_speech(text, voice='kqVT88a5QfII1HNAEPTJ', output_path="final.mp3"):
    # 1. Generate & save MP3
    try:
        stream = ElevenLabs(api_key=ELEVENLABS_API_KEY).generate(
            text=text,
            voice=voice,
            model="eleven_turbo_v2",
            output_format="mp3_22050_32"
        )
        with open("output_path", "wb") as f:
            for chunk in stream:
                f.write(chunk)
    except Exception as e:
        logging.error(f"TTS generation failed: {e}")
        return

    logging.info("Audio saved as output.mp3")

    system = platform.system()
    try:
        if system == "Windows":
            os.startfile("output_path")              
        elif system == "Darwin":
            subprocess.run(["afplay", "output_path"], check=True)
        elif system == "Linux":
            subprocess.run(["aplay", "output_path"], check=True)
        else:
            logging.warning(f"No playback handler for OS: {system}")
    except Exception as e:
        logging.warning(f"Playback failed on {system}: {e}")