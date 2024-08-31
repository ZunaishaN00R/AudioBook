# AudioBook Project: Text-to-Speech Conversion

## Description

The AudioBook Project converts text from a PDF document into an audio file using text-to-speech (TTS) technology. This project utilizes the `pyttsx3` library for TTS and `PyPDF2` for extracting text from a PDF. The goal is to create an audiobook from a PDF file, providing an accessible way to listen to the content.

## Features

- **PDF Text Extraction**: Extracts text from a specified range of pages in a PDF file.
- **Text-to-Speech Conversion**: Converts the extracted text into speech and saves it as an MP3 audio file.
- **Customizable Speech Rate**: Adjusts the speech rate for clear and comprehensible output.
- **Automatic File Saving**: Saves the generated speech to an MP3 file for easy playback.

## Requirements

- Python 3.x
- `pyttsx3` library
- `PyPDF2` library

You can install the required libraries using pip:

```bash
pip install pyttsx3 PyPDF2
