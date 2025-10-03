import streamlit as st
import google.generativeai as genai
from pathlib import Path
from datetime import datetime
import tempfile
import os
from audio_recorder_streamlit import audio_recorder

st.set_page_config(
    page_title="Voice Prompt Runner",
    page_icon="🎤",
    layout="wide"
)

# Initialize session state
if 'transcript' not in st.session_state:
    st.session_state.transcript = None
if 'optimized' not in st.session_state:
    st.session_state.optimized = None
if 'result' not in st.session_state:
    st.session_state.result = None

def process_audio(audio_data, api_key):
    """Process audio through the complete pipeline"""
    try:
        # Configure Gemini
        genai.configure(api_key=api_key)

        # Create temporary file for audio
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
            tmp_file.write(audio_data)
            tmp_path = tmp_file.name

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Step 1: Transcribe
        with st.status("Step 1: Transcribing audio...", expanded=True) as status:
            audio_file = genai.upload_file(tmp_path)
            model = genai.GenerativeModel('gemini-2.5-flash-lite')

            prompt = """Transcribe this audio file. Remove filler words (um, uh, like, you know) and add appropriate spacing between sentences. Keep the transcription natural and preserve the original meaning. Do not add headers, formatting, or interpretation - just provide a clean transcript."""

            response = model.generate_content(
                [audio_file, prompt],
                generation_config=genai.GenerationConfig(temperature=0.1)
            )
            transcript = response.text.strip()
            st.session_state.transcript = transcript
            status.update(label="✓ Step 1: Transcription complete", state="complete")

        # Step 2: Optimize
        with st.status("Step 2: Optimizing prompt...", expanded=True) as status:
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
            st.session_state.optimized = optimized
            status.update(label="✓ Step 2: Optimization complete", state="complete")

        # Step 3: Execute
        with st.status("Step 3: Executing prompt...", expanded=True) as status:
            model = genai.GenerativeModel('gemini-2.5-flash-lite')
            response = model.generate_content(optimized)
            result = response.text.strip()
            st.session_state.result = result
            status.update(label="✓ Step 3: Execution complete", state="complete")

        # Clean up temp file
        os.unlink(tmp_path)

        return True

    except Exception as e:
        st.error(f"Error: {str(e)}")
        return False

# Header
st.title("🎤 Voice Prompt Runner")
st.markdown("Transform your voice recordings into AI-powered results")

# Sidebar for API key
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        help="Enter your Google Gemini API key"
    )

    st.divider()
    st.markdown("""
    ### How it works:
    1. **Transcribe**: Audio → Text
    2. **Optimize**: Text → Structured Prompt
    3. **Execute**: Prompt → AI Response
    """)

# Main content
if not api_key:
    st.warning("⚠️ Please enter your Gemini API key in the sidebar to continue")
else:
    # Audio input options
    st.header("📥 Input Audio")

    tab1, tab2 = st.tabs(["🎙️ Record Audio", "📁 Upload File"])

    with tab1:
        st.markdown("Click the microphone to start/stop recording:")
        audio_bytes = audio_recorder(
            text="",
            recording_color="#e74c3c",
            neutral_color="#95a5a6",
            icon_size="3x"
        )

        if audio_bytes:
            st.audio(audio_bytes, format="audio/wav")
            if st.button("Process Recording", type="primary", key="process_recording"):
                if process_audio(audio_bytes, api_key):
                    st.success("✓ Processing complete!")

    with tab2:
        uploaded_file = st.file_uploader(
            "Choose an audio file",
            type=['mp3', 'wav', 'ogg', 'm4a', 'flac'],
            help="Upload a pre-recorded audio file"
        )

        if uploaded_file:
            st.audio(uploaded_file)
            if st.button("Process Upload", type="primary", key="process_upload"):
                audio_data = uploaded_file.read()
                if process_audio(audio_data, api_key):
                    st.success("✓ Processing complete!")

    # Results section
    if st.session_state.transcript or st.session_state.optimized or st.session_state.result:
        st.divider()
        st.header("📊 Results")

        result_tab1, result_tab2, result_tab3 = st.tabs(["📝 Transcript", "✨ Optimized Prompt", "🎯 Final Result"])

        with result_tab1:
            if st.session_state.transcript:
                st.markdown("### Raw Transcript")
                st.text_area(
                    "Transcript",
                    st.session_state.transcript,
                    height=200,
                    label_visibility="collapsed"
                )
                st.download_button(
                    "Download Transcript",
                    st.session_state.transcript,
                    file_name=f"transcript_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )

        with result_tab2:
            if st.session_state.optimized:
                st.markdown("### Optimized Prompt")
                st.markdown(st.session_state.optimized)
                st.download_button(
                    "Download Optimized Prompt",
                    st.session_state.optimized,
                    file_name=f"optimized_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown"
                )

        with result_tab3:
            if st.session_state.result:
                st.markdown("### Final Result")
                st.markdown(st.session_state.result)
                st.download_button(
                    "Download Result",
                    st.session_state.result,
                    file_name=f"result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown"
                )

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #7f8c8d;'>
    <small>Voice Prompt Runner | Powered by Google Gemini</small>
</div>
""", unsafe_allow_html=True)
