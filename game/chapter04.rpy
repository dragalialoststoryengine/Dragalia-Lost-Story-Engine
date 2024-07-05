# I'm going to test to see if i can use characters outside of where i define them.

# The game starts here.

label chapter04:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image otherworld = "images/backgrounds/Sty_bg_0040_100_00.png"
    scene otherworld with dissolve

    show berserker with dissolve
    ber "Ah!  I'm here!  That means I was able to transcend the bounds of my own world and arrive here!"

    hide berserker with dissolve

    show pia_img with dissolve
    pia "Whoa, me too!"

    hide pia_img with dissolve

    show elisanne with dissolve
    elly "I have also arrived!"

    hide elisanne with dissolve

    show eirene with dissolve
    eir "Arrival in otherworld successful.  Proceeding with investigative protocols."
    hide eirene with dissolve

    show finni with dissolve
    fin "And I'm here, too!!!"
    hide finni with dissolve

    # This goes back to script

    jump start
