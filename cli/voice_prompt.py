#!/usr/bin/env python3
"""
Voice Prompt Runner - Process audio prompts through AI pipeline
"""
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

class VoicePromptRunner:
    def __init__(self, audio_file: Path):
        self.audio_file = audio_file
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.base_name = self.audio_file.stem

        # Setup directories
        self.dirs = {
            'audio': Path('prompts/audio'),
            'transcript': Path('prompts/transcript/formatted'),
            'polished': Path('prompts/transcript/polished'),
            'output': Path('outputs')
        }

        # Configure Gemini
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file")
        genai.configure(api_key=api_key)

    def transcribe_audio(self) -> str:
        """Step 1: Transcribe audio using Gemini and apply light formatting"""
        print(f"\n[1/3] Transcribing audio: {self.audio_file.name}")

        # Upload audio file
        audio_file = genai.upload_file(str(self.audio_file))

        # Create model and transcribe
        model = genai.GenerativeModel('gemini-2.5-flash-lite')

        prompt = """Transcribe this audio file. Remove filler words (um, uh, like, you know) and add appropriate spacing between sentences. Keep the transcription natural and preserve the original meaning. Do not add headers, formatting, or interpretation - just provide a clean transcript."""

        response = model.generate_content(
            [audio_file, prompt],
            generation_config=genai.GenerationConfig(
                temperature=0.1,
            )
        )
        transcript = response.text.strip()

        # Save transcript
        transcript_path = self.dirs['transcript'] / f"raw_{self.base_name}_{self.timestamp}.txt"
        transcript_path.write_text(transcript)
        print(f"    Saved: {transcript_path}")

        return transcript

    def optimize_prompt(self, transcript: str) -> str:
        """Step 2: Optimize transcript for use as an AI prompt"""
        print(f"\n[2/3] Optimizing text for AI prompt")

        model = genai.GenerativeModel('gemini-2.5-flash-lite')

        prompt = """You are an expert at converting spoken ideas into well-structured AI prompts. Take the following transcript and optimize it for use as an AI prompt by:

1. Adding clear headers and structure
2. Organizing ideas into logical sections
3. Improving flow and clarity
4. Correcting any obvious transcription errors or mishearings (e.g., fixing misheard words, technical terms, or names based on context)
5. Maintaining the original intent and requirements
6. Using proper formatting (markdown)

Do not change the core meaning or add new requirements. Focus on clarity, organization, and fixing transcription mistakes.

Transcript:
""" + transcript

        response = model.generate_content(prompt)
        optimized = response.text.strip()

        # Save optimized prompt
        polished_path = self.dirs['polished'] / f"optimized_{self.base_name}_{self.timestamp}.md"
        polished_path.write_text(optimized)
        print(f"    Saved: {polished_path}")

        return optimized

    def execute_prompt(self, prompt: str) -> str:
        """Step 3: Execute the optimized prompt with an LLM"""
        print(f"\n[3/3] Executing prompt with LLM")

        model = genai.GenerativeModel('gemini-2.5-flash-lite')
        response = model.generate_content(prompt)
        result = response.text.strip()

        # Save final output
        output_path = self.dirs['output'] / f"{self.base_name}_{self.timestamp}.md"
        output_path.write_text(result)
        print(f"    Saved: {output_path}")

        return result

    def run(self):
        """Execute the complete pipeline"""
        print(f"\n{'='*60}")
        print(f"Voice Prompt Runner - Processing: {self.audio_file.name}")
        print(f"{'='*60}")

        try:
            # Step 1: Transcribe
            transcript = self.transcribe_audio()

            # Step 2: Optimize
            optimized = self.optimize_prompt(transcript)

            # Step 3: Execute
            result = self.execute_prompt(optimized)

            print(f"\n{'='*60}")
            print(f"✓ Pipeline completed successfully!")
            print(f"{'='*60}\n")

        except Exception as e:
            print(f"\n✗ Error: {e}", file=sys.stderr)
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Process audio prompts through AI pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example:
  python voice_prompt.py prompts/audio/demo.mp3
  python voice_prompt.py my_prompt.mp3
        """
    )
    parser.add_argument('audio_file', type=str, help='Path to audio file')

    args = parser.parse_args()

    # Validate audio file
    audio_path = Path(args.audio_file)
    if not audio_path.exists():
        print(f"Error: Audio file not found: {audio_path}", file=sys.stderr)
        sys.exit(1)

    # Run pipeline
    runner = VoicePromptRunner(audio_path)
    runner.run()


if __name__ == '__main__':
    main()
