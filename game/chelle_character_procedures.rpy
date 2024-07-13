
    # Chelle Character Procedures File

    # Paste this file into a story if you want to use Chelle.  These procedures animate Chelle as a speaker.
    # You'll also need to paste THIS line into your actual script above the script label whenever you're using Chelle:

define chell = Character("Chelle", callback=speaker("chell"))

    # This program assumes that the following folders exist:
    #     -"images/chelle"
    #     -"images/chelle/faces"
    #     -"images/chelle/mouths"

    # Chelle dynamically blinks and, while speaking, also moves her mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Chelle appear*:
    #  -->  show chelle with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Moving Chelle's fan*:
    #  -->  show chelle [keyword]
    #  List of body keywords:
    #     -->  normal (default), fan
    #          N O T E:  using "fan" will only look normal with "fan_eyes" / "fan_eyes_closed" and "fan_mouth" 

    # *Changing Chelle's eyes*:
    #  -->  show chelle [keyword]
    #  List of eye keywords:
    #     -->  neutral (default), angry, flinch, focused, focused2, pained, relaxed, sad, surprised,
    #            fan_eyes, fan_eyes_closed

    # *Changing Chelle's mouth*:
    #  -->  show chelle [keyword]
    #  List of mouth keywords:
    #     -->  smile1 (default), smile2, smile3, frown1, frown2, frown3, mutter1, shout1,
    #           fan_mouth

    # *Writing dialogue for Chelle*:
    #  --> chell "[Chelle's line here]"

    # *Making Chelle disappear*:
    #  --> hide chelle with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)




    # # # # #


layeredimage chelle:

    group body:
        
        attribute normal default:
            "images/chelle/chelle_body.png"

        attribute fan:
            "images/chelle/chelle_fan_body.png"

    group face:

        # 454/1028, 248/1028:
        pos (0.44163, 0.241245)

        attribute neutral default:
            "chelle_neutral_eyes"

        attribute focused:
            "chelle_focused_eyes"

        attribute angry:
            "chelle_angry_eyes"

        attribute flinch:
            "chelle_flinch_eyes"

        attribute surprised:
            "chelle_surprised_eyes"   

        attribute sad:
            "chelle_sad_eyes"

        attribute pained:
            "chelle_pained_eyes"
        
        attribute relaxed:
            "chelle_relaxed_eyes"

        attribute focused2:
            "chelle_focused2_eyes"

        attribute fan_eyes:
            "chelle_fan_eyes"

        attribute fan_eyes_closed:
            "images/chelle/faces/100015_02_parts_c001.png"
    


    group mouth:

        pos (0.44163, 0.241245)

        attribute smile1 default:
            "chelle_smile1"

        attribute mutter1:
            "chelle_mutter1"

        attribute smile2:
            "chelle_smile2"
            
        attribute shout1:
            "chelle_shout1"

        attribute frown2:
            "chelle_frown2"

        attribute frown1:
            "chelle_frown1"

        attribute frown3:
            "chelle_frown3"
        
        attribute smile3:
            "chelle_smile3"

        attribute fan_mouth:
            "images/chelle/mouths/100015_02_parts_c003.png"


## EYE animations start here.

image chelle_neutral_eyes:
    "images/chelle/faces/100015_01_parts_c000.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/chelle/faces/100015_01_parts_c001.png"
    0.05
    repeat

image chelle_focused_eyes:
    "images/chelle/faces/100015_01_parts_c003.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/chelle/faces/100015_01_parts_c004.png"
    0.05
    repeat

image chelle_angry_eyes:
    "images/chelle/faces/100015_01_parts_c010.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/chelle/faces/100015_01_parts_c011.png"
    0.05
    repeat

image chelle_flinch_eyes:
    "images/chelle/faces/100015_01_parts_c012.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/chelle/faces/100015_01_parts_c013.png"
    0.05
    repeat

image chelle_surprised_eyes:
    "images/chelle/faces/100015_01_parts_c014.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/chelle/faces/100015_01_parts_c015.png"
    0.05
    repeat

image chelle_sad_eyes:
    "images/chelle/faces/100015_01_parts_c016.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/chelle/faces/100015_01_parts_c017.png"
    0.05
    repeat

image chelle_pained_eyes:
    "images/chelle/faces/100015_01_parts_c025.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/chelle/faces/100015_01_parts_c026.png"
    0.05
    repeat

image chelle_relaxed_eyes:
    "images/chelle/faces/100015_01_parts_c027.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/chelle/faces/100015_01_parts_c028.png"
    0.05
    repeat

image chelle_focused2_eyes:
    "images/chelle/faces/100015_01_parts_c029.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/chelle/faces/100015_01_parts_c030.png"
    0.05
    repeat

image chelle_fan_eyes:
    "images/chelle/faces/100015_02_parts_c000.png"
    choice:
        2
    choice:
        3
    choice:
        4
    choice:
        5
    choice:
        6
    "images/chelle/faces/100015_02_parts_c001.png"
    0.05
    repeat



# MOUTH animations start here.

image chelle_smile1_nottalking = "images/chelle/mouths/100015_01_parts_c005.png"

image chelle_smile1_talking:
    "images/chelle/mouths/100015_01_parts_c006.png"
    0.15
    "images/chelle/mouths/100015_01_parts_c005.png"
    0.15
    repeat

image chelle_smile1 = WhileSpeaking("chell", "chelle_smile1_talking", "chelle_smile1_nottalking")


image chelle_mutter1_nottalking = "images/chelle/mouths/100015_01_parts_c008.png"

image chelle_mutter1_talking:
    "images/chelle/mouths/100015_01_parts_c009.png"
    0.15
    "images/chelle/mouths/100015_01_parts_c008.png"
    0.15
    repeat

image chelle_mutter1 = WhileSpeaking("chell", "chelle_mutter1_talking", "chelle_mutter1_nottalking")


image chelle_smile2_nottalking = "images/chelle/mouths/100015_01_parts_c018.png"

image chelle_smile2_talking:
    "images/chelle/mouths/100015_01_parts_c019.png"
    0.15
    "images/chelle/mouths/100015_01_parts_c018.png"
    0.15
    repeat

image chelle_smile2 = WhileSpeaking("chell", "chelle_smile2_talking", "chelle_smile2_nottalking")


image chelle_shout1_nottalking = "images/chelle/mouths/100015_01_parts_c020.png"

image chelle_shout1_talking:
    "images/chelle/mouths/100015_01_parts_c021.png"
    0.15
    "images/chelle/mouths/100015_01_parts_c020.png"
    0.15
    repeat

image chelle_shout1 = WhileSpeaking("chell", "chelle_shout1_talking", "chelle_shout1_nottalking")


image chelle_frown2_nottalking = "images/chelle/mouths/100015_01_parts_c022.png"

image chelle_frown2_talking:
    "images/chelle/mouths/100015_01_parts_c023.png"
    0.15
    "images/chelle/mouths/100015_01_parts_c022.png"
    0.15
    repeat

image chelle_frown2 = WhileSpeaking("chell", "chelle_frown2_talking", "chelle_frown2_nottalking")


image chelle_frown1_nottalking = "images/chelle/mouths/100015_01_parts_c022.png"

image chelle_frown1_talking:
    "images/chelle/mouths/100015_01_parts_c024.png"
    0.15
    "images/chelle/mouths/100015_01_parts_c022.png"
    0.15
    repeat

image chelle_frown1 = WhileSpeaking("chell", "chelle_frown1_talking", "chelle_frown1_nottalking")


image chelle_frown3_nottalking = "images/chelle/mouths/100015_01_parts_c031.png"

image chelle_frown3_talking:
    "images/chelle/mouths/100015_01_parts_c032.png"
    0.15
    "images/chelle/mouths/100015_01_parts_c031.png"
    0.15
    repeat

image chelle_frown3 = WhileSpeaking("chell", "chelle_frown3_talking", "chelle_frown3_nottalking")


image chelle_smile3_nottalking = "images/chelle/mouths/100015_01_parts_c033.png"

image chelle_smile3_talking:
    "images/chelle/mouths/100015_01_parts_c034.png"
    0.15
    "images/chelle/mouths/100015_01_parts_c033.png"
    0.15
    repeat

image chelle_smile3 = WhileSpeaking("chell", "chelle_smile3_talking", "chelle_smile3_nottalking")



# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label chelle_character_procedures:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image gran_fiore_interior = "images/backgrounds/Sty_bg_0043_100_00.png"
    scene gran_fiore_interior with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show chelle with dissolve

    chell "Ah, greetings, Nadine.  Care for some tea?  My servants have just brewed a fresh pot."

    show chelle neutral smile1
    chell "(neutral smile1) I suppose you're wondering why I've summoned you.  You see, I'm aware of the fact that you have a rather unique piece of technology."

    show chelle relaxed mutter1
    chell "(relaxed mutter1) ...'Clix,' you call it?  More accurately, I believe it is a materium-powered light mana distortion and processing device."

    show chelle focused smile2
    chell "(focused smile2) Well, no matter!  More importantly, I wish very much to see a demonstration of this otherworldly technology."

    show chelle focused2
    chell "(focused2) So:  if you would, please collect some images of me so I can witness the process in action."

    show chelle pained frown1
    chell "(pained frown1) ...A 'selfie?' Very well, if you must.  I suppose it's natural to commemorate one's meeting with royalty..."

    show chelle focused2 smile1
    pause 0.5
    image white_flash = "images/backgrounds/white.png"
    show white_flash
    pause 0.1
    hide white_flash

    show chelle flinch frown2
    chell "(flinch frown2) ...Astounding.  I wasn't expecting that flash to occur at the moment of capture."

    show chelle focused smile3
    chell "(smile3) Well, with that taken care of, shall we commit more images of moi to your device?  I would like to see if it can capture images from a greater distance."

    show chelle fan fan_eyes fan_mouth
    chell "(fan fan_eyes fan_mouth) Be sure to capture me at my most ravishing!  Hee hee!"

    pause 0.5
    show white_flash
    pause 0.1
    hide white_flash

    show chelle fan_eyes_closed
    chell "(fan_eyes_closed) Well, I must say, this technology holds a lot of promise.  Does it have any other capabilities you wish to mention?"

    show chelle normal surprised shout1
    chell "(normal surprised shout1) ...You say it can send the image to Lief?  Wh-Whyever would it even be CAPABLE of that??  This is entirely unexpected, please don't--"

    show chelle angry shout1
    chell "(angry) ...Oh, you are just terrible!  Did Euden put you up to teasing me??  How boorish!"

    show chelle sad frown3
    chell "(sad frown3) Honestly, it's not right to play with the heart of a lady!  Tell my brother that he's not the only one with compromising personal information that can be weaponized!"

    show chelle angry smile1
    chell "If Euden wants to play this game, I'm happy to cause him some embarrassment as well.  And... perhaps your 'Clix' could be involved in the payback, if you'd be interested in some mischief..."

    hide chelle with dissolve

    # This goes back to script

    jump testfiles
