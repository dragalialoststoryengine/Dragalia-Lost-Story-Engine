
    # Satan Character Procedures File

    # Paste this file into a story if you want to use Notte.  These procedures animate Notte as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Notte:

define sat = Character("Satan", callback=speaker("sat"))

    # This program assumes that the following folders exist:
    #     -"images/satan"
    #     -"images/satan/faces"
    #     -"images/satan/mouths"


    # Satan dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Satan appear*:
    #  -->  show satan with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Satan's eyes*:
    #  -->  show satan [keyword]
    #  List of eye keywords:
    #     -->  relaxed (default), angry, askance, blush, closed_blush, focused, sad, shocked,
    #          squint, surprised, closed_sad

    # *Changing Satan's mouth*:
    #  -->  show satan [keyword]
    #  List of mouth keywords:
    #     -->  mutter1 (default), closed_mutter1, frown1, frown2, frown3, grimace1, grimace2,
    #          pout1, shout1, smile1, duchenne1

    # *Writing dialogue for Satan*:
    #  --> sat "[Satan's line here]"

    # *Making Satan disappear*:
    #  --> hide satan with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage satan:

    always "images/satan/satan_body.png"

    group face:

        # 354/1024, 111/1024:

        pos (0.33400, 0.10840)

        attribute normal default:
            "images/satan/faces/120243_01_parts_c000.png"

        attribute dim:
            "images/satan/faces/120243_01_parts_c001.png"

        attribute glowing:
            "satan_glowing_eyes"

## EYE animations start here.

image satan_glowing_eyes:
    "images/satan/faces/120243_01_parts_c002.png"
    0.05
    "images/satan/faces/120243_01_parts_c003.png"
    0.05
    repeat






# The game starts here.

label satan_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image grams_ruined = "images/backgrounds/Sty_bg_0141_400_00.png"
    scene grams_ruined

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    stop music fadeout 0.5
    show satan dim with dissolve
    sat "..."
    sat "A road paved with good intentions…"
    sat "Since the beginning, autonomy has defined the actions made."
    sat "It is that very will that serves to complete. For there would be no purpose without it."
    sat "As time marched on, that autonomy, that ability to choose, has been what defined progress."
    sat "As new choices presented themselves, advancements became more inevitable."
    sat "As too did a commonality among choices."
    sat "That they are never truly of an individual."

    show satan normal
    sat "Others would make their own choice, and no matter what a single one does to prevent the effects, they will always come."
    sat "For some, this was inevitable. With all possibility presented, someone better equipped deserved to make that choice."
    sat "They would be the guiding light."
    sat "But that ability to make choices for someone else. It presents options that would otherwise be inconceivable."
    sat "And so a struggle would begin to make those choices. Take those choices."
    sat "If they have the power to choose, they can’t let others use it, for they may choose wrong."

    show satan glowing
    sat "They can’t choose wrong! They can’t be shortsighted! Perhaps some of their decisions help themselves or their allies while at a detriment for others; nay, at a detriment for the world as a whole."
    sat "For they are not selfish! They can’t be! They are good! And goodness will save the future!"

    show satan normal
    sat "And so, choices are lost. Sometimes for the better. But as choice is lost, complacency happens."
    sat "As the sands of time continue to spill, the choices available become smaller and smaller."

    show satan dim
    sat "And no longer will they be picked. They are afraid of what would happen. They can’t comprehend it."
    sat "They don’t even know there was a choice to begin with."
    sat "And so, in pursuing the light, those who claim to be unselfish leaders push forward. Some who see it glow as the sands fall. Others who let the last embers suffocate."
    sat "..."

    show satan normal
    sat "And so you too are given a choice. With what you know. Will you continue to fight, hoping your choice rekindles the flame? Or will you reclude yourself to the cold embrace?"
    sat "Know that others have been given this same choice. And yours may fall short."
    sat "As for some, the answer is clear. And for others, they are blinded by their own \"unselfishness\". Some will help ignite, while others will try to drown out."

    show satan dim
    sat "Failure is easier."
    sat "..."
    sat "The road paved with good intentions…"

    show satan glowing
    sat "Leads back to me."

    show satan dim
    sat "And back to you."

    hide satan with dissolve

    play music "audio/music/CRASHER Mana Circles loop.mp3" fadein 0.5

    # This goes back to script

    jump testfiles