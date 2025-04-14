#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Install required packages if not already installed
pip install flask requests pyinstaller pandas openpyxl

# Build the executable
pyinstaller naver_real_estate.spec

# Display information
echo ""
echo "Build completed."
echo "The executable is located at: dist/Naver_Real_Estate_Analyzer"
echo ""
echo "You can distribute this executable to users."
echo "Users need to double-click on the executable to run the application."
echo "The application will automatically open in their web browser."
echo "" 