import os
import sys
import json
from dotenv import load_dotenv
import base64
# from PIL import Image
from groq import Groq
# import requests

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

image_path = "image/boil_1.jpeg"
if not os.path.exists(image_path):
    print(f"Image file {image_path} does not exist.")
    sys.exit(1)

model = "meta-llama/llama-4-scout-17b-16e-instruct"
query = "What is the diagnosis of this image?"
# query = "What is the diagnosis of this image? Please provide a detailed explanation of the findings and any relevant differential diagnoses."


def encode_image_to_base64(image_path):
    """
    Encode an image to base64 format.
    :param image_path: Path to the image file.
    :return: Base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string


def analyze_image_with_query(query, model, encoded_image):
    client=Groq()  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content
