#!/bin/bash

# Voice Prompt Runner - GUI Launcher
# Sets up virtual environment with uv and launches Streamlit app

set -e

GUI_DIR="gui"
VENV_DIR="gui/.venv"

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Error: uv is not installed"
    echo "Install with: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment with uv..."
    cd "$GUI_DIR"
    uv venv
    cd ..
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Install/update dependencies
echo "Installing dependencies with uv..."
cd "$GUI_DIR"
uv pip install -r requirements.txt

# Launch Streamlit
echo "Launching Streamlit app..."
echo "========================================="
streamlit run app.py

# Deactivate on exit
deactivate
