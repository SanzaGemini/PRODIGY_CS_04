# PRODIGY_CS_04
# Key Logger Program

## Overview

This is a simple key logger script that records all the keys pressed on your keyboard while the program is active. The keys are saved to a `keyfile.txt` file. The application is meant for **educational purposes only** and should be used responsibly.

## Features

- **Key Logging**: Captures all key presses (including special keys such as `Enter`, `Space`, etc.) and writes them to a text file.
- **User Prompt**: Asks for user permission before starting the key logging process.
- **User Warnings**: Provides warnings about potential security risks and anti-virus flags.
- **Graceful Exit**: Allows the user to stop the key logging process by entering `1`.

## Requirements

- Python 3.x
- Python libraries:
  - `pynput`: Used for keyboard event handling.
  - `colorama` and `termcolor`: Used for colored terminal output (for warnings and prompts).

You can install these libraries using pip:

```bash
pip install pynput colorama termcolor
```

## How to Run

1. **Clone or download** the project files to your local machine.
2. Open a terminal in the project directory.
3. Run the script using Python:

```bash
python key_logger.py
```

4. Upon running, the program will:
    - Display a warning and disclaimer.
    - Ask for your permission to continue with the key logging.
    - If permission is granted, it will begin logging keys to a file named `keyfile.txt`.
    - To end the key logging, enter `1` when prompted.
    
5. All recorded keys will be saved in `keyfile.txt`.

## Important Notes

- **Warning**: This application may be flagged as malicious by some antivirus programs due to its nature of logging keystrokes.
- You might need to explicitly **allow the application to run** on your machine by overriding any security warnings.
- **Disclaimer**: The creator of this application is not responsible for any misuse of this program. The application is strictly for **educational use only**.

## Example Output

If you type `Hello World!`, the content of `keyfile.txt` would look something like this:

```
h e l l o  [Key.space] w o r l d [Key.space] !
```
When runnig the application would look like this:
```
*** Welcome To The Key Logger Program. ***
This Application Is For Educational Use Only!!!

This Application Might Be Flagged By Your Anti-Virus As Malware!!!
You Might Need to Give It Permission To Run On Your Machine.

NB: This Application Will Keep Record Of All The Keys You Type While It's Active.

Would You Like To Continue With The Application? (yes(y)/no(n))
y
To end the program, press '1'.
1
*** Thank You For Using The Key Logger Program ***
```

## License

This project is open-source and is must be used for educational use only. Please use this project responsibly and only for legitimate purposes.
