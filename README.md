## ALERT: NO SUPPORT FOR WINDOWS (APP VERSION), PLEASE USE MACOS OR LINUX, OTHER WISE, USE `bookingbot.py` FOR WINDOWS. IGNORE ALL MESSAGES

#### `Beta v2.5` includes:

- Working on implementing app version of the bot, using `tkinter` for the GUI

#### `Beta v2.4` includes:

- Implemented:
  - Windows support

#### `Beta v2.3` includes:

- `Beta v2.3.0`: Add check for UBCO Wifi connection

#### `Beta v2.2` includes:

- `Beta v2.2.10`: Fixed more of preprocessing issues
- `Beta v2.2.9`: Fixed preprocessing issues
- `Beta v2.2.8`: Restructured code to be more readable and efficient
- `Beta v2.2.7`: Fixed timing issues with countdown again (hopefully)
- `Beta v2.2.6`: Fixed updating issues
- `Beta v2.2.5`: Implemented updates from https://github.com/rin-williams/UBCOBookingBot/blob/main/bookingbot.py
- `Beta v2.2.4`: Fixed timing issues with countdown again
- `Beta v2.2.3`: Fixed index issues scriptInput and made terminal bigger when running in macOS
- `Beta v2.2.2`: Fixed timing issues with countdown
- `Beta v2.2.1`: Fixed checking for UBBuserdata.dat file

- Implemented:

  - Checking to see if user is on macOS, if they are, then check to see if Selenium is installed, if not, then install it
  - Keeping computer awake (as long as the script is running, max is 3hrs) using Selenium if on macOS
  - Wait if room is not bookable for fresh mode (someone else already booked the current time slot)
  - If extend mode does not find a room with the matching name, then it will default to fresh session instead.
  - Skipping headless mode question if UBBuserdata.dat is found
  - Countdown the last 9 seconds after waiting for the room to be bookable

#### `Beta v2.1` includes:

- Using `UBBuserdata.dat` for storing password, username, room number

- Customizable room name and room number for Commons Building Area only.

- Fixed AFK issues, bot will book as long as you are not letting your computer sleep

- Working on implementing wait time if room is not bookable for fresh mode

- Planning on adding a GUI for the bot

#### `Beta v2.0` includes:

- Scrapped & revised the old code for better readability and efficiency.

#### `Beta v1.0` includes:

- Improved readability and efficiency of the code.
