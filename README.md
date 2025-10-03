# Voice-Prompt-Runner

Transform spoken ideas into AI-powered results through intelligent multi-stage processing.

## Overview

Voice-Prompt-Runner implements a **voice prompting** workflow—a paradigm that leverages the convenience of voice input to capture detailed, long-form prompts. The system processes audio through multiple stages of AI-powered transcription and refinement to overcome transcription errors and produce high-quality, structured prompts ready for LLM execution.

### The Voice Prompting Concept

Voice prompting recognizes that speaking is often more natural and efficient than typing for capturing complex ideas, requirements, and context. However, raw speech-to-text transcription can contain errors. This tool addresses that challenge through a **multi-stage inference pipeline**:

1. **Audio → Clean Transcript**: Initial transcription with light formatting
2. **Transcript → Optimized Prompt**: Structural organization and error correction through contextual inference
3. **Prompt → AI Result**: Execution of the refined prompt to generate final output

Each stage uses AI models to infer and correct errors from previous stages, resulting in progressively higher quality output.

## Features

- **Multi-Input Support**: Record audio directly or upload existing files (MP3, WAV, OGG, M4A, FLAC)
- **Three-Stage Pipeline**: Transcription → Optimization → Execution
- **Error Correction**: Contextual inference fixes transcription mishearings automatically
- **Full Transparency**: Access raw transcripts, optimized prompts, and final results
- **Persistent Storage**: All intermediate and final outputs saved with timestamps
- **Dual Interface**: CLI for automation, GUI for interactive use

## Architecture

### CLI Version (`cli/`)
- Python-based command-line tool
- Batch processing of audio files
- Saves all artifacts to organized directories

### GUI Version (`gui/`)
- Streamlit-based web interface
- Live audio recording capability
- Interactive three-tab result viewer
- Deployable to Hugging Face Spaces

### Pipeline Flow

```
Audio File
    ↓
[Stage 1: Transcription]
    • Model: Gemini 2.5 Flash Lite
    • System Prompt: prompts/system_prompts/stage1_transcription_cleanup.txt
    • Removes filler words (um, uh, like)
    • Adds sentence spacing
    • Output: Clean text transcript
    ↓
[Stage 2: Optimization]
    • Model: Gemini 2.5 Flash Lite
    • System Prompt: prompts/system_prompts/stage2_prompt_optimization.txt
    • Adds structure and headers
    • Fixes transcription errors through context
    • Organizes into logical sections
    • Output: Markdown-formatted prompt
    ↓
[Stage 3: Execution]
    • Model: Gemini 2.5 Flash Lite
    • Processes optimized prompt
    • Output: Final AI-generated result
```

## Quick Start

### GUI (Recommended for Interactive Use)

```bash
./run_gui.sh
```

The GUI provides:
- In-browser audio recording
- File upload support
- Real-time processing status
- Tabbed results viewer (Transcript / Optimized / Result)
- Download buttons for all outputs

### CLI (Recommended for Automation)

```bash
cd cli
pip install -r requirements.txt
python voice_prompt.py path/to/audio.mp3
```

The CLI automatically:
- Creates organized directory structure
- Saves timestamped artifacts at each stage
- Displays progress through the pipeline

## Directory Structure

```
Voice-Prompt-Runner/
├── cli/                    # Command-line interface
│   ├── voice_prompt.py    # Main CLI script
│   └── requirements.txt   # CLI dependencies
├── gui/                    # Streamlit web interface
│   ├── app.py             # Main GUI application
│   └── requirements.txt   # GUI dependencies
├── prompts/               # Shared storage
│   ├── audio/            # Input audio files
│   ├── system_prompts/   # Stage prompts
│   │   ├── stage1_transcription_cleanup.txt
│   │   └── stage2_prompt_optimization.txt
│   └── transcript/
│       ├── formatted/    # Stage 1 outputs
│       └── polished/     # Stage 2 outputs
└── outputs/               # Stage 3 final results
```

## Configuration

Both versions require a Google Gemini API key:

**CLI**: Create `.env` file with:
```
GEMINI_API_KEY=your_api_key_here
```

**GUI**: Enter API key in sidebar (secure input field)

Get your API key at: https://makersuite.google.com/app/apikey

## Use Cases

- **Rapid Prototyping**: Speak feature ideas and get structured implementation plans
- **Documentation**: Dictate thoughts and receive organized markdown documentation
- **Code Generation**: Describe functionality verbally and get code outputs
- **Meeting Notes**: Record discussions and get actionable summaries
- **Content Creation**: Speak content ideas and receive polished drafts

## Technical Details

- **Transcription Model**: Gemini 2.5 Flash Lite (low temperature for accuracy)
- **Error Correction**: Contextual inference at optimization stage identifies and fixes mishearings
- **Format Preservation**: Maintains intent while improving structure
- **Artifact Tracking**: Timestamped outputs enable audit trail and iteration

## Deployment

The GUI version is designed for easy deployment to Hugging Face Spaces. See `gui/README.md` for deployment instructions.

## Requirements

- Python 3.8+
- Google Gemini API access
- Audio recording capability (for GUI live recording)

See `cli/README.md` and `gui/README.md` for detailed setup instructions.
