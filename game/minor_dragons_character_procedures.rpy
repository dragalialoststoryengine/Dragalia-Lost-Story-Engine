# This is a file for implementing dragons that are so minor that they only have a single sprite.
# Because they don't need complex rigging, it's easier just to group them together.


# Kagutsuchi:  dialogue tag "kagut"

define kagut = Character("Kagutsuchi", callback=speaker("kagut"))

image kagutsuchi = "images/kagutsuchi/kagutsuchi_body.png"


define rath = Character("Rathalos", callback=speaker("rath"))

image rathalos = "images/rathalos/rathalos_body.png"


define dkr = Character("Dreadking Rathalos", callback=speaker("dkr"))

image dreadking_rathalos = "images/rathalos/dreadking_rathalos_body.png"




label minor_dragon_character_procedures:

    image halidom_drawbridge_day = "images/backgrounds/Sty_bg_0017_100_00.png"
    scene halidom_drawbridge_day with fade
    
    show kagutsuchi with dissolve
    kagut "Ah, it seems many dragons are out and about today.  How do you do?"
    hide kagutsuchi with dissolve

    show rathalos with dissolve
    rath "ROAAAAAAAAAAAAAAAAAR!!!!"
    hide rathalos with dissolve

    show dreadking_rathalos with dissolve
    dkr "ROAAAAAAAAAAAAAAAAAAAAAAAAAAR!!!!"
    hide dreadking_rathalos with dissolve

    jump npctestfiles