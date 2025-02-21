# Voice TaskMate
Voice TaskMate is a smart virtual assistant with a Tkinter-based GUI that allows users to manage tasks, get real-time weather updates, listen to motivational quotes, jokes, and even open desktop applications using voice commands.

![Screenshot 2024-12-03 133417](https://github.com/user-attachments/assets/87fd9f2e-183c-4fe4-bb66-5f5b76b37a88)

## Features
- **🗣️ Voice Commands:** Perform multiple actions using voice input.
- **🎨 Tkinter GUI:** User-friendly graphical interface for easy interaction.
- **☁️ Real-Time Weather Updates:** Fetches current weather using an API.
- **📋 To-Do List Management:** Add, delete, and view tasks.
- **🏆 Motivational Quotes & Jokes:** Get inspired and entertained.
- **🖥️ Open Desktop Applications:** Launch common apps like Notepad, Calculator, etc.
- **🔊 Text-to-Speech (TTS):** Reads out responses using pyttsx3.
- **📌 Temporary Data Storage:** Uses Python lists and dictionaries to store tasks dynamically.

## Technologies Used

| Library/Technology      | Purpose                                         |
|------------------------|-------------------------------------------------|
| `Tkinter`             | GUI development for interactive user interface  |
| `PIL (Pillow)`        | Handling and processing images in GUI           |
| `speech_recognition`  | Convert voice input to text                      |
| `pyttsx3`             | Text-to-speech conversion                        |
| `requests`            | Fetch real-time weather updates from API         |
| `pytz`               | Handling time zones for accurate time reporting   |
| `wikipedia`          | Fetch summaries from Wikipedia                    |
| `pyjokes`            | Generate random jokes                             |
| `webbrowser`         | Open web applications like YouTube, Google, etc.  |
| `os`                 | Open system applications (Notepad, Calculator, etc.) |
| `datetime`           | Handle and format date/time information           |

## Installation Guide
### Step 1: Clone the Repository
git clone https://github.com/Bhoomigupta603/Voice-TaskMate.git
cd Voice-TaskMate

### Step 2: Install Dependencies
pip install tk pillow speechrecognition pyttsx3 requests pytz wikipedia pyjokes

### Step 3: Run the Application
python GUI.py

## How to Use Voice TaskMate
**1. Launch the App:** Run GUI.py to open the graphical interface.
**2. Click the Microphone Button 🎤:** Speak a command like:
- **🗂 "Add to do list: Buy groceries" →** Adds a new to-do item.
- **🌦 "weather" →** Fetches real-time weather.
- **🏆 "motivate me" →** Provides an inspirational quote.
- **🎭 "Tell me a joke" →** Makes you laugh.
- **🖥 "Open Notepad" →** Opens the Notepad application.
**3. Listen to the Response:** The system will process and reply using text-to-speech (TTS).

## 📞 Contact & Support  
For any queries or suggestions, feel free to connect:  
🌐 **GitHub**: [Your GitHub Profile](https://github.com/Bhoomigupta603)


