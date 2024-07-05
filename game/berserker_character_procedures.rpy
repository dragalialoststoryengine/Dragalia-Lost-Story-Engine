    # Berserker Character Procedures File

    # Paste this file into a story if you want to use Berserker.  These procedures animate Berserker as a speaker.


define bers = Character("Berserker", callback=speaker("bers"))

    # This program assumes that the following folders exist:
    #     -"images/berserker"
    #     -"images/berserker/faces"

    # Berserker dynamically blinks and, while speaking, also moves his mouth along with the text scroll.

    # FUNCTIONS:

    # *Making Berserker appear*:
    #  -->  show berserker with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)

    # *Changing Berserker's eyes*:
    #  -->  show berserker [keyword]
    #  List of eye keywords:
    #     -->  neutral (default), closed_neutral, askance, burn, burn2,
    #          downcast, glint, glint2, surprised,

    # *Writing dialogue for Berserker*:
    #  --> bers "[Linus's line here]"

    # *Making Berserker disappear*:
    #  --> hide berserker with dissolve
    #       ("with dissolve" is optional but makes transitions cleaner)



layeredimage berserker:

    always "images/berserker/berserker_body.png"

    group face:

        pos (0.35059, 0.19629)

        attribute neutral default:
            "berserker_neutral_eyes"

        attribute closed_neutral:
            "images/berserker/faces/110050_01_parts_c001.png"

        attribute glint:
            "berserker_glint_eyes"

        attribute burn:
            "berserker_burn_eyes"

        attribute surprised:
            "berserker_surprised_eyes"

        attribute askance:
            "berserker_askance_eyes"

        attribute downcast:
            "berserker_downcast_eyes"

        attribute glint2:
            "berserker_glint2_eyes"

        attribute burn2:
            "berserker_burn2_eyes"



image berserker_neutral_eyes:
        "images/berserker/faces/110050_01_parts_c000.png"
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
        "images/berserker/faces/110050_01_parts_c001.png"
        0.05
        repeat

# 002 is the same as 000.  Deleted.

image berserker_glint_eyes:
        "images/berserker/faces/110050_01_parts_c003.png"
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
        "images/berserker/faces/110050_01_parts_c004.png"
        0.05
        repeat

image berserker_burn_eyes:
        "images/berserker/faces/110050_01_parts_c008.png"
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
        "images/berserker/faces/110050_01_parts_c009.png"
        0.05
        repeat

image berserker_surprised_eyes:
        "images/berserker/faces/110050_01_parts_c010.png"
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
        "images/berserker/faces/110050_01_parts_c011.png"
        0.05
        repeat

image berserker_askance_eyes:
        "images/berserker/faces/110050_01_parts_c012.png"
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
        "images/berserker/faces/110050_01_parts_c013.png"
        0.05
        repeat

image berserker_downcast_eyes:
        "images/berserker/faces/110050_01_parts_c015.png"
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
        "images/berserker/faces/110050_01_parts_c016.png"
        0.05
        repeat

image berserker_glint2_eyes:
        "images/berserker/faces/110050_01_parts_c017.png"
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
        "images/berserker/faces/110050_01_parts_c018.png"
        0.05
        repeat

image berserker_burn2_eyes:
        "images/berserker/faces/110050_01_parts_c019.png"
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
        "images/berserker/faces/110050_01_parts_c020.png"
        0.05
        repeat










# The game starts here.

label berserker_character_procedures:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image village_night = "images/backgrounds/Sty_bg_0015_300_00.png"
    scene village_night at middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show berserker

    bers "Ah, greetings.  I did not expect you to join me on my night patrol."

    show berserker neutral
    bers "(neutral) As it happens, I once performed several jobs for this village back when I was a freelance mercenary."

    show berserker closed_neutral
    bers "(closed_neutral) What kinds of jobs?  I would rather not trouble you with those details."

    show berserker downcast
    bers "(downcast) Back in those days, I didn't bother to question the morality of my jobs.  As long as the commission provided a challenge, I relished it."

    show berserker glint
    bers "(glint) There are, of course, days when I miss the freedom of that sort of lifestyle.  Everyone was a potential opponent, and I did not have to temper my nature."

    show berserker glint2
    bers "(glint2) Fufufu... there was a particularly notorious bandit who had captured hostages.  He was a strong, skilled fighter, and at the time, I intentionally drew out our fight, relishing the clash of steel on steel!"

    show berserker askance
    bers "(askance) ...Ahem.  My apologies, I became carried away for a moment."

    show berserker surprised
    bers "(surprised) In any case, since joining your cause, I've had to practice more restraint, but... I've found a unique form of gratification in wielding my sword to save lives rather than claiming them."

    show berserker neutral
    bers "It's rather fulfilling.  I'm not sure if it exactly makes me feel 'alive' like I desire, but my sleep has come easier than in the past."
    bers "Of course, it may be possible that these new times of peace are dulling my fighters' instincs..."

    show berserker burn
    bers "(burn) You promised you would fight me in dragon form as often as necessary, correct?  There is a field right over there.  Surely we could spare ten minutes to..."

    show berserker burn2
    bers "(burn2) ...Yes, \"right now!!!\"  My bloodlust burns, and I must release it!!!  LET ME FIGHT THE BEAST!!!"
    bers "RAAAAAAAAAAAAH!!!!"

    hide berserker with dissolve


    # This goes back to script

    jump testfiles
