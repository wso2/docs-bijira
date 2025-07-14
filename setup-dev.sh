#!/bin/bash

# Setup script for Bijira Documentation local development
echo "🚀 Setting up Bijira Documentation for local development..."

# Check if Python 3.12 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.12 or later."
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')
MAJOR_VERSION=$(echo $PYTHON_VERSION | cut -d. -f1)
MINOR_VERSION=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$MAJOR_VERSION" -eq 3 ] && [ "$MINOR_VERSION" -ge 12 ]; then
    echo "✅ Python $PYTHON_VERSION detected"
else
    echo "❌ Python 3.12 or later is required. Found Python $PYTHON_VERSION"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install Python dependencies
echo "📥 Installing Python dependencies..."
cd en
pip install -r requirements.txt

# Check if Node.js is available for optional tools
if command -v npm &> /dev/null; then
    echo "📦 Node.js detected. Installing optional validation tools..."
    npm install -g markdown-spellcheck markdown-link-check
else
    echo "⚠️  Node.js not found. Spell checking and link validation tools will not be available."
    echo "   You can still build and serve the documentation without these tools."
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the development server:"
echo "  cd en"
echo "  python -m mkdocs serve"
echo ""
echo "The documentation will be available at: http://localhost:8000/bijira/docs/"
echo ""
echo "To activate the virtual environment in the future:"
echo "  source venv/bin/activate"
