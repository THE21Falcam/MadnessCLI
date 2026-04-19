# TODO: Image to Ascii art convertor Black & White
# TODO: Create LootTable

import os
import subprocess
import sys

Playing = True
Game_State = 0

Command_Text = "Command Line Enter Commands"

Text_Display = [["Type 'start' to Start the Game & 'q' to Quit the Game."]]

if __name__ == "__main__":
    while Playing:
        window_size = os.get_terminal_size()
        width = window_size.columns

        if sys.platform == "linux":
            subprocess.run("clear")
        elif sys.platform == "win32":
            os.system("cls")

        print("")
        print("Welcome to Dungeon Madness CLI".center(width))
        print("Type 'h' for Help in Command Line".center(width))
        print("")

        for items in Text_Display:
            print(items[0].center(width))

        print("")

        # Command Help

        CommandInput = input(f"{Command_Text} > ")

        if CommandInput == "h":
            Text_Display = [
                ["'q' for Quitting the Game"],
                ["'start' for Starting the Game"],
            ]

        elif CommandInput == "q":
            Playing = False

if sys.platform == "linux":
    subprocess.run("clear")
elif sys.platform == "win32":
    os.system("cls")
