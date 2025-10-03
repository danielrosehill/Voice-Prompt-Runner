# GUI Version

Streamlit web interface for Voice Prompt Runner. Deployable to Hugging Face Spaces.

## Run Locally

**Easy way (recommended)** - From the repository root:
```bash
./run_gui.sh
```

This script will automatically:
- Install `uv` if needed
- Create a virtual environment in `gui/.venv`
- Install dependencies
- Launch the Streamlit app

**Manual way** - If you prefer to manage the environment yourself:
```bash
cd gui
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
streamlit run app.py
```

Then open your browser to the URL shown (typically http://localhost:8501).

## Deploy to Hugging Face Spaces

1. Create a new Space on Hugging Face
2. Select "Streamlit" as the SDK
3. Upload `app.py` and `requirements.txt`
4. Users will enter their Gemini API key directly in the web interface

## Features

- **Browser Recording**: Record audio directly in the browser
- **File Upload**: Upload pre-recorded audio files (mp3, wav, ogg, m4a, flac)
- **Real-time Processing**: See progress through each pipeline step
- **Download Results**: Download transcript, optimized prompt, and final results
- **Secure**: API keys are entered by users and never stored
