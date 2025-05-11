# quiz-app

A simple flashcard-style application written in Python and Tkinter to help you memorize vocabulary (or any paired data) in a fun, interactive way—similar to Quizlet.

## Features

- Random selection of words from your custom word list  
- Card-flip animation: English prompt on the front, translation on the back  
- User input validation to check your answer  
- Continue learning automatically after each attempt  
- Easily extendable word database  

## Prerequisites

- Python 3.6 or newer  
- Tkinter (usually bundled with Python)  

## Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/quiz-app.git
   cd quiz-app
   ```
2. Ensure the `dane/slowa.txt` file exists and follows the format:
   ```
   word_in_english, word_in_target_language
   ```
3. (Optional) Review or replace images in `zdjecia/` to customize card visuals.

## Usage

Run the main application script:

```bash
python main.py
```

- A window will appear showing an English word.  
- Type your translation in the entry field and click **Accept** (or use the right/wrong buttons).  
- If correct, the next card appears; if wrong, the console will log the correct answer.  

## Project Structure

```
quiz-app/
├── dane/               # Your word lists (e.g., slowa.txt)
├── licencja/           # Project license text
├── zdjecia/            # Images for card front/back and buttons
├── main.py             # Primary application entry point
├── pom.py              # Alternate module with helper functions
└── README.md           # This documentation
```

## License

GNU GPL V3 @ Krzychu 2023
