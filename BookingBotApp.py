import os
import requests
import platform
import subprocess
import tkinter as tk
from tkinter import ttk

# Check for updates ---------------------------------------------------------
isRunningFromSource = False
info_file = "UBBuserdata.dat"
# Check if we are running from source
if (
    os.path.exists("INFOS.md")
    or os.path.exists("LICENSE.md")
    or os.path.exists("README.md")
):
    isRunningFromSource = True
else:
    isRunningFromSource = False

# check if user has the bookingbot.py script, if not,
# download from https://raw.githubusercontent.com/rin-williams/UBCOBookingBot/main/bookingbot.py
if isRunningFromSource == False:
    url = "https://raw.githubusercontent.com/rin-williams/UBCOBookingBot/main/bookingbot.py"
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        if not os.path.exists("bookingbot.py"):
            response = requests.get(url)
            with open("bookingbot.py", "w") as file:
                file.write(response.text)


# Check if the request was successful
if isRunningFromSource == False:
    url = "https://raw.githubusercontent.com/rin-williams/UBCOBookingBot/main/BookingBotApp.py"
    response = requests.get(url)
    if response.status_code == 200:
        # Read the content of the local script
        with open("BookingBotApp.py", "r") as file:
            local_script = file.read()

        # Compare with the GitHub script
        if response.text != local_script:
            # If the scripts don't match, update the local script
            with open("BookingBotApp.py", "w") as file:
                file.write(response.text)
# ---------------------------------------------------------------------------


# App -----------------------------------------------------------------------
APPVERSION = "1.0"

root = tk.Tk()
root.title("UBCO Booking Bot App v" + APPVERSION)
root.geometry("400x400")
root.resizable(False, False)

welcome_message = ttk.Label(root, text="Welcome!")
welcome_message.pack()

username_frame = ttk.Frame(root)
username_frame.pack(pady=10)

username_label = ttk.Label(username_frame, text="Username:")
username_label.pack(side="left", padx=(0, 10))
username_entry = ttk.Entry(username_frame)
# set username to the last used username
if os.path.exists(info_file):
    with open(info_file, "r") as file:
        for line in file:
            if "username" in line:
                username_entry.insert(0, line.split("=")[1].strip())
                break
username_entry.pack(side="left")

password_frame = ttk.Frame(root)
password_frame.pack(pady=10)

password_label = ttk.Label(password_frame, text="Password:")
password_label.pack(side="left", padx=(0, 10))
password_entry = ttk.Entry(password_frame, show="*")
# set password to the last used password
if os.path.exists(info_file):
    with open(info_file, "r") as file:
        for line in file:
            if "password" in line:
                password_entry.insert(0, line.split("=")[1].strip())
                break
password_entry.pack(side="left")


building_frame = ttk.Frame(root)
building_frame.pack(pady=10)

building = tk.StringVar()

building_label = ttk.Label(building_frame, text="Building:")
building_label.pack(side="left", padx=(0, 10))
building_option = ttk.Combobox(
    building_frame,
    textvariable=building,
    values=["EME", "COM: 0th Floor", "COM: 1st Floor", "COM: 3rd Floor", "LIB"],
    state="readonly",
)
# set building to the last used building
if os.path.exists(info_file):
    with open(info_file, "r") as file:
        for line in file:
            if "com" in line:
                floor_number = line.split("=")[1].strip()[
                    0
                ]  # Get the first digit of the room number
                if floor_number == "0":
                    building_option.set("COM: 0th Floor")
                elif floor_number == "1":
                    building_option.set("COM: 1st Floor")
                elif floor_number == "3":
                    building_option.set("COM: 3rd Floor")
                break
            elif "eme" in line:
                building_option.set("EME")
                break
            elif "lib" in line:
                building_option.set("LIB")
                break
building_option.pack(side="left")

room_frame = ttk.Frame(root)
room_frame.pack(pady=10)

room_label = ttk.Label(room_frame, text="Room:")
room_label.pack(side="left", padx=(0, 10))
room_option = ttk.Combobox(room_frame, state="readonly")
# set room to the last used room
if os.path.exists(info_file):
    with open(info_file, "r") as file:
        for line in file:
            if "lastUsedRoom" in line:
                room_option.set(line.split("=")[1].strip())
                break
room_option.pack(side="left")

roomName_frame = ttk.Frame(root)
roomName_frame.pack(pady=10)

roomName_label = ttk.Label(roomName_frame, text="Room name:")
roomName_label.pack(side="left", padx=(0, 10))
roomName_label = ttk.Entry(roomName_frame)
# set room name to the last used room name
if os.path.exists(info_file):
    with open(info_file, "r") as file:
        for line in file:
            if "roomName" in line:
                roomName_label.insert(0, line.split("=")[1].strip())
                break
roomName_label.pack(side="left")


def update_options(*args):
    if building.get() == "EME":
        options = ["not yet implemented"]
    elif building.get() == "COM: 0th Floor":
        options = [
            "COM 005 (4 people)",
            "COM 006 (4)",
            "COM 007 (4)",
            "COM 008 (4)",
        ]
    elif building.get() == "COM: 1st Floor":
        options = [
            "*COM 121 (10)",
            "COM 108 (4 people)",
            "COM 109 (4)",
            "COM 110 (10)",
            "COM 111 (10)",
            "COM 112 (6)",
            "COM 113 (4)",
            "COM 114 (6)",
            "COM 115 (4)",
            "COM 116 (6)",
            "COM 117 (6)",
            "COM 118 (6)",
            "COM 119 (6)",
            "COM 120 (6)",
        ]
    elif building.get() == "COM: 3rd Floor":
        options = [
            "COM 301 (4 people)",
            "COM 302 (4)",
            "COM 303 (4)",
            "COM 304 (4)",
            "COM 305 (6)",
            "COM 306 (4)",
            "COM 307 (6)",
            "COM 308 (4)",
            "COM 309 (6)",
            "COM 312 (4)",
            "COM 314 (4)",
            "COM 316 (4)",
            "COM 318 (4)",
        ]
    else:
        options = ["not yet implemented"]

    room_option["values"] = options


building.trace("w", update_options)

message_var = tk.StringVar()
message_var.set("Please select a building and room")
running = False


def run_bot():
    global running
    room_number = ""
    if not running:
        if building_option.get() != "" and room_option.get() != "":
            message_var.set("Running bot...")
            running = True
            run_button.config(state="disabled")
            stop_button.config(state="normal")

            # Open the file
            with open(info_file, "w") as file:
                building = building_option.get()
                file.write("lastUsedRoom=" + room_option.get() + "\n")
                room_number = room_option.get().split(" ")[1]
                if "COM" in building:
                    file.write("com=" + room_number + "\n")
                elif "EME" in building:
                    file.write("eme=" + room_number + "\n")
                elif "LIB" in building:
                    file.write("lib=" + room_number + "\n")

                file.write("username=" + username_entry.get() + "\n")
                file.write("password=" + password_entry.get() + "\n")
                file.write("roomName=" + roomName_label.get() + "\n")
                file.truncate()

            # run the bot if on mac
            if platform.system() == "Darwin":
                subprocess.Popen(
                    [
                        "python3",
                        "bookingbot.py",
                    ]
                )
        else:
            if building_option.get() == "":
                message_var.set("Please select a building!")
            elif room_option.get() == "":
                message_var.set("Please select a room!")


def stop_bot():
    global running
    if running:
        message_var.set("Bot stopped.")
        running = False
        run_button.config(state="normal")
        stop_button.config(state="disabled")
    # stop the bot if on mac
    if platform.system() == "Darwin":
        subprocess.Popen(
            [
                "pkill",
                "-f",
                "bookingbot.py",
            ]
        )


button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

run_button = ttk.Button(button_frame, text="Run Bot", command=run_bot)
run_button.pack(side="left", padx=(0, 10))

stop_button = ttk.Button(
    button_frame, text="Stop Bot", command=stop_bot, state="disabled"
)
stop_button.pack(side="left")

message_label = ttk.Label(root, textvariable=message_var)
message_label.pack()

root.mainloop()
