# Screen Shot and Email Script

## Requirements

*   Python 3.x
*   A Gmail account to send the emails from (with an "App Password" enabled).

## Dependencies

The script uses the following Python libraries:
*   `pyautogui`: For taking screenshots.
*   Standard libraries: `smtplib`, `ssl`, `os`, `time`, `email`.

## How to Run

1.  **Install Python:** If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

2.  **Clone or Download the Script:** Get the `5_screen_shot.py` file onto your local machine.

3.  **Install Dependencies:** Open your terminal or command prompt and install the required `pyautogui` library:
    ```bash
    pip install pyautogui
    ```

4.  **Configure the Script:** Open `5_screen_shot.py` in a text editor and modify the following configuration variables at the top of the file:

    *   `EMAIL_SENDER`: The Gmail address you want to send the screenshots from.
    *   `EMAIL_PASSWORD`: The **App Password** for your sender's Gmail account. **Do not use your regular password.** You can generate an App Password here: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
    *   `EMAIL_RECEIVER`: The email address where you want to receive the screenshots.
    *   `INTERVAL`: The time in seconds between each screenshot (e.g., `5` for 5 seconds).
    *   `BATCH_SIZE`: The number of screenshots to collect before sending them in a single email (e.g., `10`).

5.  **Run the Script:** Save your changes and run the script from your terminal:
    ```bash
    python 5_screen_shot.py
    ```

The script will now run in the background, capturing screenshots at the specified interval and emailing them once the batch size is reached. To stop the script, press `Ctrl+C` in the terminal.

## Disclaimer

This script is intended for legitimate monitoring purposes only. Please use it responsibly and ensure you have the necessary permissions to monitor the computer on which you are running it. The author is not responsible for any misuse of this tool.
