
    # Notte Character Procedures File

    # Paste this file into a story if you want to use Notte.  These procedures animate Notte as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Notte:

define tho = Character("Thor", callback=speaker("tho"))

    # This program assumes that the following folders exist:
    #     -"images/thor"

    # Thor... doesn't really have any animations, he's kinda just there.

    # FUNCTIONS:

    # *Making Thor appear*:
    #  -->  show thor with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Writing dialogue for Notte*:
    #  --> tho "[Thor's line here]"

    # *Making Thor disappear*:
    #  --> hide thor with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage thor:

    always "images/thor/thor_body.png"



# The game starts here.

label thor_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image alberia_throne = "images/backgrounds/Sty_bg_0033_100_00.png"
    scene alberia_throne


    show thor with dissolve
    tho "..."
    tho "...I am Thor, the Fulminator."
    tho "If there is a battle to be fought, you may call upon me at any time."
    tho "..."
    tho "...You cannot be serious."
    tho "You want to see me... change facial expressions?"
    tho "How boring, and utterly demeaning for someone of my strength."
    tho "If you have need of any ACTUAL tasks worthy of Thor the Fulminator, I shall oblige."
    tho "Otherwise, I will take my leave, as I have much groom--I mean, matters far beyond the importance of ordinary mortals to attend."
    tho "...(ahem)."

    hide thor with dissolve


    # This goes back to script

    jump testfiles
