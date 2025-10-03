# CLI Version

Command-line interface for Voice Prompt Runner.

## Setup

```bash
cd cli
pip install -r requirements.txt
```

Create a `.env` file in the project root with your API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

```bash
python voice_prompt.py path/to/audio.mp3
```

The script will:
1. Transcribe the audio
2. Optimize the transcript into a structured prompt
3. Execute the prompt and generate results

All outputs are saved to `../prompts/` and `../outputs/` directories.
