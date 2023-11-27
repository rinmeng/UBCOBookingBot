# This is a room booking bot for study rooms in the Commons Building at the UBCO

## This bot is not a finished project

### How to run:

- Download the script `bookingbot.py` and then store it in `/Users/(your username)` for `macOS` or `C:/Users/(your username)` for `Windows`. This is to make it convenient when running the actual program.

- You will need [Google Chrome](https://www.google.com/chrome/) installed on your device. This program will not work without it.

- You must have latest version of [Python](https://www.python.org/downloads/) installed on your device.

- Once installed, type in `python3 bookingbot.py` in your terminal to run the program.

### When running:

- Upon running this program, it will ask if you want to run in headless mode, if you do, it will not open a chrome window and it will just run in the background note that it is easier to see what is going on when you run in non-headless mode.

- Then it will ask for room name, number and your CWL credential to log into the `UBCO booking system`. It will not be stored anywhere besides on your machine in same place where you stored `bookingbot.py` as a file called `UBBuserdata.dat`.

- If you choose not to enter the right credentials, the program will not work and will ask you to rerun the program. Once you enter the right credentials, the program will save your credentials for next time and automatically run in headless mode and log you on for the next time.

### Some tips:

- if you want to change room number or room name, I suggest you deleting the `UBBuserdata.dat` file and rerun the program.

### Footnotes

- Program is not meant for malicious purposes, it is meant to help students who are busy and forget to book a room for themselves.

- Program is not meant to be used for commercial purposes, it is meant to be used by students who are enrolled in UBCO.

- Program is not meant to be used for any other purposes besides booking a room for COMS121 at UBCO.

- If you want to fork this project and make it better, please do so, but please do not use it for malicious purposes.
