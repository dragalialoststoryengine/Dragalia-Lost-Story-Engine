label dlse_story_writer:

    image white = "images/backgrounds/white.png"
    scene white with dissolve

    "Please choose a background."

    $ dlse_writer_line = renpy.input("Please enter the dialogue you want displayed.")

    "The text you input is [dlse_writer_line]"

    # $ dlse_input_file = renpy.open_file("game data files/DLSE Story Writer Input.txt")

    "Output to file..."

    #python:
    #    with open("game data files/DLSE Story Writer Output.txt","w") as egg:
    #        egg.write("Some text " + dlse_writer_line + " some more text")
    #    egg.closed

    jump start