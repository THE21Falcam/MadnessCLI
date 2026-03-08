#TODO: Image to Ascii art convertor Black & White
#TODO: Create LootTable 

impot sys, subprocess

Playing = True
Game_State = 0

Command_Text = "Command Line Enter Commands"

Text_Display = [
    ["Type 'start' to Start the Game & 'q' to Quit the Game"]
]

Username = ""

Loot_Table = {
    1:[], # [name, droprate, Rarity, metrics, discription]
}

while(Playing):

    subprocess.run('clear')

    print("")
    print("Welcome to Dungeon Madness CLI")
    print("Type 'h' for Help in Command Line ")
    print("")
    for items in Text_Display:
        print("    " + items[0])
    print("")
    
    # State Manager
    

    # Command Help
    
    CommandInput = input(f"{Command_Text} > ")
    
    if CommandInput == "h":

        Text_Display = [
            ["'q' for Quitting the Game"],
            ["'start' for Starting the Game"]
        ]
    
    elif CommandInput == "start":
    
        pass
    
    elif CommandInput == "q":
        
        playing = False
        break    

subprocess.run('clear')
