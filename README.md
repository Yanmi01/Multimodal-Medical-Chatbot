# Multimodal-Medical-Chatbot

An AI-powered medical assistant that accepts patient voice and medical image inputs, processes them through a multimodal RAG pipeline, and returns realistic doctor-like spoken responses.
[Try it here](https://huggingface.co/spaces/Yanmife/Multimodal_AI_Doctor)

## Overview
This project demonstrates a full-stack, multimodal chatbot designed for simulated medical consultations. It leverages state-of-the-art models for speech-to-text (STT), image-based diagnostic reasoning, and text-to-speech (TTS) to create an interactive, human-like AI doctor assistant.

## Features
- Voice Input: Transcribe patient speech into text using Groq's Whisper API.

- Image Diagnosis: Analyze medical images (e.g., X-rays, dermatology photos) with LLaMA-4 Scout via Groq for diagnostic insights.

- Speech Output: Convert AI-generated responses into natural-sounding doctor voices with ElevenLabs.

- Web Interface: User-friendly Gradio UI for recording audio and uploading images to receive text and audio feedback.

- Prompt Engineering: Tailored system prompts to ensure concise, human-like, and clinically appropriate responses.

## Tech Stack

- Backend: `Python 3.10`

- Frontend: Gradio

- STT: Groq Whisper (`whisper-large-v3`)

- Image Analysis: `meta-llama/llama-4-scout-17b-16e-instruct` on Groq

- TTS: ElevenLabs API (`eleven_turbo_v2`)

- Containerization: Docker (optional for GPU-based Space)

- Deployment: Hugging Face Spaces

## Installation
1. Clone the repository
   ```bash
       git clone https://github.com/yourusername/multimodal-medical-chatbot.git
       cd multimodal-medical-chatbot
   ```
2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux / macOS
   venv\Scripts\activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables: Create a `.env` file in the project root:
   ```bash
   GROQ_API_KEY=your_groq_api_key
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   ```

##  Usage
Start the Gradio app locally:
```bash
python app.py
```

Open your browser at http://localhost:7860, then:

1. Upload or record patient audio.

2. Upload a medical image.

3. View the transcribed text and AI doctor’s diagnosis.

4. Listen to the spoken response.
