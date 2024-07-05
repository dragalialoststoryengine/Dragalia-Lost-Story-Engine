
   # Go into "game/script.rpy", find this block of code with 'My Finni Valentine' and then put the second part underneath it.
   # It should already have the right indentation so just delete the hashtags.




#        "{color=#000000}'My Finni Valentine.'{/color}":
#            "Excellent choice.  Android lovers unite!"
#            jump myfinnivalentinemenu
#
#
#        "{color=#000000}Azul's Dragalia Chapter 1.{/color}":
#            "If you're reading this, it worked and you're about to go to the test chapter!"
#            jump azul_dragalia_chapter1








#  This is where this actual test file starts.  Put it in the same folder as the other .rpy files ('game' folder).



# This is where the main menu option will link to when you paste it in.

label azul_dragalia_chapter1:




    # This plays the music "Threatening Aura" from "audio/music" folder

    play music "audio/music/Threatening Aura intro.flac" fadeout 1.0
    queue music "audio/music/Threatening Aura.flac"


    # This text makes a background appear with a fade from black

    image church1 = "images/backgrounds/Sty_bg_0013_100_00.png"
    scene church1 with fade



    #  This text makes Zethia appear with an evil grin and the angry Other eyes.
    #  Then she delivers some dialogue

    show zethia other_angry grin1 with dissolve
    zeth "Oh, look, it's a church.  This is really pretty."
    zeth "It sure would be a shame if I--"



    # This text does another face to black with a ruined church instead

    image church2 = "images/backgrounds/Sty_bg_0013_101_00.png"
    scene church2 with fade



    # Zethia disappears if you use "with fade," so you need to make her reappear.

    show zethia other_focused grin1 with dissolve
    zeth "Heh heh heh, get pwned church losers lmfao deez."



    # This stops the music
    stop music fadeout 1.0



    #  This goes back to the main menu.

    jump start
