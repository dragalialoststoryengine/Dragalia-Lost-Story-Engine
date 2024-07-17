# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

init python:

    def dismiss_callback():
        renpy.play("audio/sound/page flip.mp3")
        return True

    config.say_allow_dismiss = dismiss_callback

    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None

    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)

    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking

        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None

    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

label splashscreen:
    scene black

    image nottegif:
        "images/notte loading icon/notte loading 1.png"
        0.08
        "images/notte loading icon/notte loading 2.png"
        0.08
        "images/notte loading icon/notte loading 3.png"
        0.08
        "images/notte loading icon/notte loading 4.png"
        0.08
        "images/notte loading icon/notte loading 5.png"
        0.08
        "images/notte loading icon/notte loading 6.png"
        0.08
        "images/notte loading icon/notte loading 7.png"
        0.08
        "images/notte loading icon/notte loading 8.png"
        0.08
        "images/notte loading icon/notte loading 9.png"
        0.08
        "images/notte loading icon/notte loading 10.png"
        0.08
        "images/notte loading icon/notte loading 11.png"
        0.08
        "images/notte loading icon/notte loading 12.png"
        0.08
        "images/notte loading icon/notte loading 13.png"
        0.08
        "images/notte loading icon/notte loading 14.png"
        0.08
        "images/notte loading icon/notte loading 15.png"
        0.08
        "images/notte loading icon/notte loading 16.png"
        0.08
        repeat

    show nottegif

    show text "{color=#ffffff}This game is a non-profit fan-based recreation of the Dragalia Lost story engine, motivated by the game's end-of-service.{/color}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(0.25)

    show text "{color=#ffffff}Its intention is to provide community members an outlet to create new stories using the beloved characters of this franchise.{/color}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(0.25)

    show text "{color=#ffffff}Unless stated otherwise, all art assets and characters are the property of Nintendo and Cygames.{/color}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(0.25)

    show text "{color=#ffffff}Please support Cygames, Nintendo, and any official current OR future releases in the Dragalia Lost franchise.{/color}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    hide nottegif with dissolve
    with Pause(1)

    return




label start:


    play music "audio/music/CRASHER Mana Circles loop.mp3" fadeout 1

    image library = "images/backgrounds/Sty_bg_0042_100_00.png"
    scene library at middle

    menu:
        "What stories do you want to read?"

        "{color=#000000}TUTORIAL{/color}":
            "Welcome!  We hope you enjoy the Dragalia Lost Story Engine!"
            jump tutorialmenu

        "{color=#000000}'My Finni Valentine.'{/color}":
            "Excellent choice.  Android army unite!"
            jump myfinnivalentinemenu

        #"{color=#000000}'DLSE Story Writer.'{/color}":
        #    "This is a test at making a GUI to assist in the story writing process."
        #    jump dlse_story_writer

        "{color=#000000}Character test files.{/color}":
            jump testfiles

        "{color=#000000}NPC test files.{/color}":
            jump npctestfiles

        "{color=#000000}Fan character test files.{/color}":
            jump octestfiles

        "{color=#000000}Other test files.{/color}":
            jump othertestfiles

        "{color=#000000}Nothing.{/color}":
            return

label tutorialmenu:

    queue music "audio/music/CRASHER Mana Circles loop.mp3"

    image twilightsky = "images/backgrounds/Sty_bg_0147_100_00.png"
    scene twilightsky with fade

    menu:

        "{color=#000000}1) Introduction{/color}":
            jump tutorial_start

        "{color=#000000}2) Backgrounds{/color}":
            jump tutorial_bgs

        "{color=#000000}3) Characters{/color}":
            jump tutorial_chars

        "{color=#000000}4) Writing Dialogue{/color}":
            jump tutorial_writing_dialogue

        "{color=#000000}5) Music and Audio{/color}":
            jump tutorial_music_and_audio

        "{color=#000000}6) Implementing Characters{/color}":
            jump tutorial_implementing_characters

        "{color=#000000}Main Menu{/color}":
            jump start





label testfiles:

    queue music "audio/music/CRASHER Mana Circles loop.mp3"

    image library = "images/backgrounds/Sty_bg_0042_100_00.png"
    scene library with fade


    menu:

        "What test chapter do you want to read?"

        "{color=#000000}Akasha's{/color}":
            "How exciting.  Will you ultimately revel in mysteries with me, perhaps?"
            jump akasha_character_procedures

        "{color=#000000}Alex's{/color}":
            "As you wish.  Perhaps through this, she shall continue to atone for her sins."
            jump alex_character_procedures

        "{color=#000000}Alex's (Gala){/color}":
            "A phantom in the night, and a loyal friend."
            jump alexG_character_procedures

        "{color=#000000}Alex's (Summer){/color}":
            "Out of the shadows, into the sunny breeze!"
            jump alexS_character_procedures

        "{color=#000000}Berserker's{/color}":
            "Sounds good!  Just don't expect him to take off his helmet or anything."
            jump berserker_character_procedures

        "{color=#000000}Brunhilda's{/color}":
            "Ahh!  She knew you would come eventually, darling!"
            jump brunhilda_character_procedures

        "{color=#000000}Chelle's{/color}":
            "Very well.  I suppose SOME royal appearances are in keeping wtih the principle of bread and circuses..."
            jump chelle_character_procedures

        "{color=#000000}Chelsea's (Valentine){/color}":
            "Ahh, love!  Hope you're ready for her to gush about Luca."
            jump chelseaV_character_procedures

        "{color=#000000}Cibella's{/color}":
            "Note to self:  put something clever here later."
            jump cibella_character_procedures
        
        "{color=#000000}Cleo's{/color}":
            "Of course.  She will be with you presently, after she finishes preparing the evening's meal."
            jump cleo_character_procedures

        "{color=#000000}Curran's{/color}":
            "Gotcha.  I'll bring you right to his fest tile."
            jump curran_character_procedures

        "{color=#000000}Eirene's{/color}":
            "Confirmed.  Engaging stone-cold female protocols."
            jump eirene_character_procedures

        "{color=#000000}Elisanne's{/color}":
            "Understood!  She shall do her best to assist you!"
            jump elisanne_character_procedures

        "{color=#000000}Elisanne's (Summer){/color}":
            "Whether on the battlefield or on the sands of the beach, her spear is yours!"
            jump elisanneS_character_procedures

        "{color=#000000}Emile's (Gala){/color}":
            "Naturally; he's OBVIOUSLY the best choice, although he DOES make anyone look dull and untalented by comparison."
            jump emileG_character_procedures

        "{color=#000000}Euden's{/color}":
            "The OG.  The Boi.  The harem-gatherer."
            jump euden_character_procedures

        "{color=#000000}Euden's (Gala){/color}":
            "Our lad in shining armor!"
            jump eudenG_character_procedures

        "{color=#000000}Euden's (Bondforged){/color}":
            "\"My friends are my power!\"  Wait, wrong line."
            jump eudenBF_character_procedures

        "{color=#000000}Finni's{/color}":
            "Pop a wheelie for me!  If you're reading this, the script updated."
            jump finni_character_procedures

        "{color=#000000}Giovanni's{/color}":
            "Bravissimo!  Let the waves of sound wash over you, and carry you to new realms of the heart!"
            jump giovanni_character_procedures

        "{color=#000000}Grace's{/color}":
            "I see.  So you wish to spend time with a bereaved woman, then?  So be it."
            jump grace_character_procedures

        "{color=#000000}Heinwald's{/color}":
            "Indubitably.  I hope you reach the answers you seek."
            jump heinwald_character_procedures

        "{color=#000000}Ilia's{/color}":
            "Sure thing!  Uh... lemme just quickly construct the Omega Key and connect the opposing poles for you..."
            jump ilia_character_procedures

        "{color=#000000}Ilia's (Dragonyule){/color}":
            "Awesome!  Merry Dragonyule 2022!"
            jump iliaDY_character_procedures

        "{color=#000000}Jupiter's{/color}":
            "...Hmm... Very well, I guess he can indulge you.  Just make it interesting for him, ok?"
            jump jupiter_character_procedures

        "{color=#000000}Karl's{/color}":
            "Aha!!!  Bear witness to the epitome of JUSTICE!!!"
            jump karl_character_procedures

        "{color=#000000}Kleimann's{/color}":
            "Ah, yes!  Come, would you like to participate in the next experiment?  Whee-ha-ha-hoo!!"
            jump kleimann_character_procedures

        "{color=#000000}Lathna's{/color}":
            "How foolish.  You refuse the greatest mercy, the inability of the human mind to correlate the world's contents?"
            "In that case... recoil."
            jump lathna_character_procedures

        "{color=#000000}Laxi's{/color}":
            "Understood.  Character test procedures at 72\% completion and rising."
            jump laxi_character_procedures

        "{color=#000000}Linus's{/color}":
            "Hmph.  Well, get it over with, then.  No need to stare."
            jump linus_character_procedures

        "{color=#000000}Luca's{/color}":
            "HA!  You just got pranked!!!  There's no test files for Luca!!!"
            "...Just kidding.  I'll take you to him now..."
            jump luca_character_procedures

        "{color=#000000}Mascula's{/color}":
            "Really?!  His own test file?!  Understood, he'll try his best not to fail in this task."
            jump mascula_character_procedures

        "{color=#000000}Mercury's{/color}":
            "Of course.  May gentle waters wash away your fatigue."
            jump mercury_character_procedures

        "{color=#000000}Midgardsormr's{/color}":
            "Very well.  Prove that your courage is unbreakable."
            jump midgardsormr_character_procedures

        "{color=#000000}Mym's{/color}":
            "Of course, darling!!  She'll be with you right away in all her dragonly glory."
            jump mym_character_procedures

        "{color=#000000}Nino's{/color}":
            "Of course.  Any newcomer is a new experience."
            jump nino_character_procedures

        "{color=#000000}Notte's{/color}":
            "Sweet sassy molassy!!!  Time to break out the Notte Ball!!"
            jump notte_character_procedures

        "{color=#000000}Notte's (Gala){/color}":
            "The new and improved Notte!! Ready to help you out!!"
            jump notteG_character_procedures

        "{color=#000000}Notte's (Summer){/color}":
            "Just chillaxin' with the gang."
            jump notteS_character_procedures

        "{color=#000000}Philia's{/color}":
            "Aha!  It was fate to choose her!  It's the power of love!"
            jump philia_character_procedures

        "{color=#000000}Pia's{/color}":
            "O-Ok!  I hope you enjoy this song!"
            jump pia_character_procedures

        "{color=#000000}Ranzal's{/color}":
            "Ha ha ha!  In that case, yer on, Boss!"
            jump ranzal_character_procedures

        "{color=#000000}Thor's{/color}":
            "What do you desire of his lighting?  War?  Peace?  ...Or the end of all?"
            jump thor_character_procedures

        "{color=#000000}Zethia's{/color}":
            "Of course!  May the blessings of mana be upon you!"
            jump zethia_character_procedures

        "{color=#000000}Zodiark's{/color}":
            "As you wish; he will accompany you."
            jump zodiark_character_procedures

        "{color=#000000}No one's.{/color}":
            jump start


label npctestfiles:

    image library = "images/backgrounds/Sty_bg_0042_100_00.png"
    scene library at middle

    menu:

        "What test chapter do you want to read?"

        "{color=#000000}Heavy armored soldiers'{/color}":
            "Yes, sir!  Heavy armor units, assemble for role call!!"
            jump heavyarmor_character_procedures

        "{color=#000000}Fiends'{/color}":
            "Really?  They don't really do much, you know."
            "...You're sure?"
            "Ok, suit yourself... just don't say I didn't warn you..."
            jump fiend_character_procedures

        "{color=#000000}Satan's{/color}":
            "..."
            jump satan_character_procedures

        "{color=#000000}No one's.{/color}":
            jump start






label octestfiles:

    image library = "images/backgrounds/Sty_bg_0042_100_00.png"
    scene library at middle

    menu:

        "What test chapter do you want to read?"

        "{color=#000000}Edeline's{/color}":
            "A transfem version of the protagonist?  Pretty cool, right?"
            jump edeline_character_procedures

        "{color=#000000}No one's.{/color}":
            jump start




label othertestfiles:

    image library = "images/backgrounds/Sty_bg_0042_100_00.png"
    scene library at middle

    menu:

        "{color=#000000}Item test files.{/color}":
            "Sure.  Gotta grind all those materials!"
            jump item_procedures

        "{color=#000000}Emote test files.{/color}":
            "Sure.  Let's see if the emotes work!"
            jump emotes_procedures

        "{color=#000000}Play through all the music tracks.{/color}":
            "This is a shortcut that connects to Chapter 5 of the Tutorial.  If you want more details, be sure to read it through in its entirety!"
            jump tutorial_music_musicfiles

        "{color=#000000}Play through all the sound files.{/color}":
            "This is a shortcut that connects to Chapter 5 of the Tutorial.  If you want more details, be sure to read it through in its entirety!"
            jump tutorial_music_soundfiles

        "{color=#000000}Random test with multiple characters.{/color}":
            "I see.  Good on you for being a risktaker."
            jump chapter04

        "{color=#000000}The meme chapter.{/color}":
            "Oh.  I see you're easily pleased."
            jump chapter01

        "{color=#000000}Nothing.{/color}":
            jump start
