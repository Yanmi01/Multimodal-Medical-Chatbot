import os
import gradio as gr
from patient_voice import transcribe_audio
from doctor_voice import text_to_speech
from main import analyze_image_with_query, encode_image_to_base64

SYSTEM_PROMPT = """You have to act as a professional doctor, I know you are not but this is for learning purposes. 
What's in this image? Do you find anything wrong with it medically? 
If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in 
your response. Your response should be in one long paragraph. Also always answer as if you are answering a real person.
Do not say 'In the image I see' but say 'With what I see, I think you have ....'
Don’t respond as an AI model in markdown, your answer should mimic that of an actual doctor, not an AI bot. 
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please."""

def process_inputs(audio_filepath, image_filepath):
    # 1) Speech-to-Text
    transcript = transcribe_audio(audio_filepath) or "⏺️ (no speech detected)"

    # 2) Image + LLM Analysis
    if image_filepath:
        img64 = encode_image_to_base64(image_filepath)
        prompt = SYSTEM_PROMPT + " " + transcript
        doctor_response = analyze_image_with_query(
            query=prompt,
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            encoded_image=img64
        )
    else:
        doctor_response = "No image provided."

    # 3) Text-to-Speech Output
    output_mp3 = "final.mp3"
    text_to_speech(doctor_response, voice='CwhRBWXzGAHq8TQ4Fs17')

    return transcript, doctor_response, output_mp3

gr_interface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(label="Medical Image", type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Transcription"),
        gr.Textbox(label="Doctor’s Response"),
        gr.Audio(label="Doctor’s Voice", type="filepath")
    ],
    title="Multimodal AI Doctor"
)

if __name__ == "__main__":
    gr_interface.launch(debug=True, share=False)
