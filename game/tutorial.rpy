define myst = Character("???", callback=speaker("myst"))

label tutorial_start:

    stop music fadeout 1

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image black = "images/backgrounds/black.png"
    scene black with fade

    " "

    "..."

    myst "...Hello?"

    myst "Do you need help?"

    myst "You seem to be trapped in the void."

    myst "Here, reach out your hand and I'll pull you out."

    "..."

    image white = "images/backgrounds/white.png"
    scene white with dissolve

    image otherworld1 = "images/backgrounds/Sty_bg_0146_100_00.png"
    scene otherworld1 with dissolve

    myst "There you go!  Glad you made it out of there ok; I was a little worried!"

    play music "audio/music/Kibou no Oto (Sound of Hope) - Off-Vocals.mp3" fadein 6.00

    show beuden relaxed smile1 with dissolve
    beud "Now... are you all right?  And... who are you?"

    show beuden sweat smile3
    beud "I... actually didn't even know it was possible for anyone besides me to be here."
    beud "This is the space between worlds, and it's a pretty inhospitable place."

    show beuden relaxed smile1
    beud "I'm a bit of a special case though, since I come from... wait, are you caught up with the story of Dragalia Lost?"

    show beuden sweat smile2
    beud "Because if not... uh... you're in for some major spoilers."

    show beuden sad frown2
    beud "Are you ok with me continuing on?"

    "..."

    show beuden sweat grimace2
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos   
    beud "Oh, I'm sorry, you don't have the power to speak right now.  But... if you can be here right now, then maybe..."
    hide speechright

    show beuden relaxed shout1
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos   
    beud "...Right!  You should be able to use the power of creation."
    hide speechright

    show beuden relaxed smile1
    beud "In that case, we'll use that power to give you the power of choice.  In other words, a \"menu\"."

    show beuden focused frown3
    beud "Repeat after me:  \"In the name of the first...\""

    menu:
        "\"In the name of the first...\""

        "{color=#000000}\"I know your story.\"{/color}":
            jump tutorial_start_spoilers

        "{color=#000000}\"Wait, I'm not caught up!\"{/color}":
            show beuden sweat smile1
            beud "No worries; I'm still processing it all myself, to be honest."
            beud "Let's just focus on the matter at hand, then."

            jump tutorial_start_no_spoilers



label tutorial_start_spoilers:

    show beuden focused smile1
    beud "Really?  That's good to hear."

    show beuden frown1
    beud "If you're familiar with me, then you probably know that after I defeated Xenos, I had to be completely cut off from the remade world."
    beud "After all, since I'm a part of Xenos, Xenos could use me as a link to the world if I remained connected to it."

    show beuden relaxed
    beud "So I remade the world for my friends such that Xenos, and me, will never have influenced it.  And that means that almost no one even remembers me."
    beud "After that, I waited for what felt like eons before I couldn't take the loneliness anymore."
    beud "I've actually come to understand Xenos a little during that time."

    show beuden focused2 grimace1
    beud "At first, I thought he simply cast away Mordecai, his heart, because he viewed it as unnecessary."
    beud "But now I think there was more to it.  Being alone here, sealed away, is unimaginably lonely and miserable."
    beud "If I knew how to cast away my own heart and stop feeling, I would have been tempted to myself."

    show beuden focused3 frown1
    beud "Eventually, I couldn't take it anymore and searched around in this vast sea of emptiness between the worlds for anything to connect to."
    beud "Something that, for instance, Xenos wouldn't be able to corrupt through me."

    show beuden sweat smile3
    beud "And... as it happens, I made some really interesting discoveries."

    show beuden relaxed grin1
    beud "Firstly, I realized that, since Xenos was only ever interested in controlling everything, he didn't care about the portions of this place that were outside his influence."

    show beuden smile2
    beud "But I probed around a bit, and it turns out that what I thought was the edge of the universe was actually an interface between this cluster of universes with a much vaster sea of information."
    beud "This space of possibility and the worlds it contains appear to be a self-contained existence, and people here can't really cross out."
    beud "But outside, there are all kinds of worlds—many of which are more boring than the world I come from, and some of which are even more wild."
    beud "And after sifting through some of that external information, I found out that this particular multiverse has creators even older than Xenos and Bahamut."
    beud "A whole bunch of them, actually, so much so that the people on the outside have conglomerated them into a whole business."
    beud "I can tell you're from the outside, aren't you?"
    beud "And where you're from, you refer to my cluster of universes as a continuity called \"Dragalia Lost,\" right?"
    beud "I thought so.  Anyway, apparently the people on the outside had a whole variety of motives for making this universe."
    beud "A lot of developers poured tons of love into my world, but one primary motivation was the business of telling my story to entertain people through..."

    show beuden sweat grin1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos   
    beud "...well, I guess you would call it a \"mobile game?\""
    hide speechright
    beud "Anyway, apparently the costs of keeping my world going were barely less than the money they were making."
    beud "So the two main parties, \"Nintendo\" and \"Cygames,\" made the decision to shut it down.  In fact, I think that's why Xenos actually manifested as an entity at all—to \"end\" the \"game.\""
    beud "I honestly don't even think Xenos realizes the role that was assigned to him.  He's never had interest in anyone outside himself, to be frank."

    show beuden focused frown1
    beud "In any case, I wouldn't want the people who created me to go out of business, so I can't blame them too much."

    show beuden sweat grin1
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos   
    beud "...After all, if there's anyone who would understand the amount of attention and energy it takes to keep an entire world running, it would be me..."
    hide speechright

    show beuden sad frown1
    beud "But at the same time, I didn't want my friends and I to disappear entirely.  Even if they don't remember me, I love all my friends very dearly."
    beud "So that's when I resolved to see if I could use anything from the outside world to hold it together."

    show beuden relaxed smile1
    beud "As it happened, all the places and people I knew were preserved as \"assets\" or \"files\" inside the sea of information."

    show beuden sweat grin1
    beud "So... well, since the world ended anyway, I figured nobody would mind if I borrowed them, right?"
    beud "But those things are just like... well, a skeleton.  They're basically images and sounds, but there's no \"life\" in them."

    show beuden focused frown1
    beud "That's why I needed to find a way to breathe life into them, using the power of creation."
    beud "And in order to use the power of creation on things from the outside worlds, I needed a different method than what I was used to."

    show beuden relaxed smile1
    beud "I couldn't just say \"In the name of the first\" and have everything magically come together.  It's sort of like I needed a different... well, language."
    beud "So ultimately, I did some digging and found this framework, which is how I'm interacting with you right now.  Does that make sense?"



    jump tutorial_start_no_spoilers

label tutorial_start_no_spoilers:

    show beuden focused frown3
    beud "The place we're currently in is a type of semantic rigging constructed using a language of creation I borrowed from your world—it's called \"Ren'Py.\""

    show beuden sweat grin1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos   
    beud "I've... heard that the term comes from the Japanese term \"ren'ai,\" which means \"romantic love\", and... er, \"Python...?\""
    beud "Which is apparently a DIFFERENT language for creation?  For a... \"computer?\""
    hide speechright
    beud "—Anyway, apparently it was originally made for something called \"dating sims\" and then branched out into a more generic \"visual novel engine\"."
    beud "I don't really get all the details, since there wasn't anything like this back in my world, but apparently you can use it to piece together \"assets\" and bring a \"story\" to life."

    show beuden relaxed smile1
    beud "Suffice it to say, Ren'Py works a lot like the underpinnings of my old world did, and it means I was able to take the \"skeleton\" of the world I used to know and put an artificial \"spirit\" into it."
    beud "That being said, you're accessing this place from the outside, so that means you probably have an even greater aptitude for using this new language of \"creation\" than I am."

    show beuden sad shout1
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos  
    beud "Oh!  I've never had anyone here before, so why don't you try using the language of \"Ren'Py\" to... well, create something?"
    hide speechright

    show beuden focused frown1
    beud "Let's see... for starters, why don't we make a place for us to chat?"

    show beuden sweat grin1
    beud "I mean... I'm sure it would be better than floating around here in this chaotic space, right?"

    show beuden relaxed smile2
    beud "Here, I'll help you out.  Lemme take a look here... so the \"asset\" corresponding to the Halidom's main hall is called..."

    show beuden sweat grin1
    beud "...Uhh... this is a mouthful... \"Sty_bg_0024_100_00.png\".  I pinched it off and saved it in a \"folder\" called \"images/backgrounds\"."
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos  
    beud "...Maybe I should help you out here.  I'll define the image for you, so all you have to do is say \"scene\" to dissolve away everything around us into the new \"setting.\""
    hide speechright

    show beuden focused shout1
    beud "...\"image halidom_hall = \"images/backgrounds/Sty_bg_0024_100_00.png\"!"

    image halidom_hall = "images/backgrounds/Sty_bg_0024_100_00.png"

    show beuden relaxed smile3
    beud "Whew, ok.  So now that that's set up, you just need to say \"scene halidom_hall with dissolve\"."

    beud "Whenever you're ready, go ahead and try."

    menu:
        "{color=#000000}\"scene halidom_hall with dissolve\"{/color}":
            show beuden relaxed shout1
            play sound "audio/sound/exclamation.wav"
            show speechright exclamation at speechright_pos  
            beud "Oh!!  It's working!!!"
            hide speechright

            jump tutorial_start_halidom



label tutorial_start_halidom:

    stop music fadeout 1

    scene halidom_hall behind beuden with dissolve

    play music "audio/music/Utopia.flac" fadeout 1 fadein 1.0

    show beuden relaxed smile1
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    beud "Wow, this is fantastic!  This already feels so much more like home!"
    hide speechright

    show beuden sweat grin1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    beud "Do you... uh... mind if I change into something more comfortable?  This whole 'bondforged' thing doesn't really... uh... fit with the aesthetic?"
    hide speechright
    beud "I'm gonna 'hide' myself for a second and come back in a different form."
    beud "\"hide beuden with dissolve\"."

    hide beuden with dissolve

    beud "Ok, I'm coming back.  So..."
    beud "\"show euden with dissolve\"."

    show euden with dissolve
    eud "Whew!  I'm back!"

    show euden surprised
    eud "Wow, this is so nostalgic.  Dressing like this, being in the Halidom... it's just like old times!"

    show euden sad smile3
    eud "And... I'm... even welcoming a new friend here."

    stop music fadeout 1

    show euden closed_focused grimace1
    eud "..."

    play music "audio/music/CRASHER - Failure loop.mp3" fadeout 1

    show euden sad grimace1
    eud "...I'm sorry, I'm just feeling a little emotionally overwhelmed right now."
    eud "It's nice to be talking to someone, but... I miss my friends so much..."

    show euden focused frown1
    eud "..."
    eud "...I'm sorry, but I'd really like you to try something."
    eud "Despite my abilities, it's really difficult for me to use the language of \"Ren'py.\""
    eud "But... together, we might be able to do things that I can't do by myself."

    show euden closed_focused grimace2
    eud "So... could you try to bring back my friend Notte for me?  Please!"
    eud "I know the words, but it doesn't respond for me."
    eud "Please, can you at least try to say them with me?"

    stop music fadeout 1

    eud "H-Here goes..."

    menu:
        eud "\"show notte with dissolve\""

        "{color=#000000}\"show notte with dissolve\"{/color}":
            jump tutorial_start_notte




label tutorial_start_notte:

    show euden closed_focused grimace2
    eud "..."

    hide euden with dissolve
    pause 2

    show notte closed_relaxed2 frown1 with dissolve
    nott "...(Yawn) What's going on?"

    play music "audio/music/CRASHER (Story Version A) loop.mp3" fadein 2.0

    show notte neutral frown3
    nott "...?"

    show notte surprised frown3
    nott "...Wait, are you...?"

    hide notte with dissolve

    show euden blank frown1 with dissolve
    eud "..."
    eud "You're... you're really here..."

    hide euden with dissolve

    show notte shocked shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    nott "...You're EUDEN!!  SWEET HOPPING HALIDOM!!!"
    hide speechright
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos  
    nott "What are you—wait, what am I—?!?"
    hide speechright

    show notte surprised shout2
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    nott "I-I remember everything!  I can't believe I forgot you!!!"
    hide speechright

    show notte grumpy shout1
    nott "I'm so sorry, I can't believe I let myself forget about you!!!"

    hide notte with dissolve

    show euden pained grimace1
    eud "..."

    show euden pained skew_smile1
    eud "Notte... I'm... (sniff) I'm just so happy to see you...!"
    eud "I never thought I'd see you again!"

    hide euden with dissolve

    show notte closed_grumpy pout1
    nott "W-Well, (sob) I missed you TOO, doofus!!!  How could you just act like that and decide to save the world by making us all forget you!!"

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadeout 2
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos  
    nott "(Sniffle) Nobody wanted that, you—you big dummy!!! T-That's it, you're SO getting a Notte Ball, mister!!!"
    hide speechright

    hide notte with dissolve

    show euden flinch smile3 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Well, the thing is— OUCH! N-Notte, come on, I get that you're upset, but...!"

    show euden sweat_frown1
    eud "Ow!  Notte, your hair is so spiky!"
    hide speechright

    hide euden with dissolve
    show notte closed_grumpy pout1
    nott "(Sniffle) Yeah, it is!!  And you—you thought you could just make me forget all about you scott-free?!  (Sob) We're best BUDS, mister!!"
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos  
    nott "Or I THOUGHT so, anyway!!!  Take this, and this!!  It's my wrath of friendship!!!"
    hide speechright

    hide notte with dissolve

    show euden flinch sweat_frown1
    eud "Oof!"
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "H-Hey, uh, you there... I'm sorry to do this after you just did all this for me, but... maybe you could give us a few minutes here?"
    hide speechright

    show euden closed_focused
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    eud "—Ack!  Have you been working out or something, Notte!?  That seriously stings!"
    hide speechright

    show euden sad smile3
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "—A-Anyway, I clearly have my hands full catching up with Notte here (wince), so, uh, let's meet up after a few minutes to talk more about how to use Ren'Py's power of creation—"
    hide speechright

    hide euden with dissolve

    show notte focused shout1 with dissolve
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos  
    nott "Why don't you 'create' a less selfish ATTITUDE for yourself, mister?!?  \"Ohh, I'm Euden, I have to save the world!  WELP, guess I'll just gonna make my friends casually think I never EXISTED!!\"  I am SO mad right now!  HIYAAAAH!!!"
    hide speechright

    hide notte with dissolve

    show euden flinch frown1
    eud "OW!  All right, I GET it, I GET it!!  I'm sorry for making you forget, ok?"

    show euden smile1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "A-Anyway, see you soon, new friend, and—YEOUCH!—thanks for trying out the Dragalia Lost Story Engine!!"
    hide speechright


    # This goes back to script

    stop music fadeout 2

    jump tutorialmenu


























label tutorial_bgs:


    play music "audio/music/Utopia.flac" fadeout 1 fadein 1.0

    scene halidom_hall with dissolve

    show euden with dissolve
    eud "Oh, hello, you're back!"

    show euden sad smile3 with dissolve
    eud "Sorry for the commotion back there...  I think Notte's finally calmed down a bit."

    hide euden with dissolve

    show notte grumpy pout1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos  
    nott "It's not like I didn't have a good reason, you doofus!  You're always doing stuff like this!"
    hide speechright
    nott "I mean... going off alone and \"sacrificing yourself\" for \"everyone else's sake\" when we're all just worrying our heads off about YOU?!"

    show notte closed_grumpy
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos  
    nott "Rrrgh!  Would it KILL you to have have just a LITTLE more self-preservation instinct?"
    hide speechright

    show notte sad smile3
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    nott "...But... I AM crazy-happy to see you again, obviously..."
    hide speechright

    show notte surprised frown1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    nott "So, uh... where ARE we exactly?  It looks like the main hall of the Halidom, but... I've tried flying around, and I can't actually leave."
    hide speechright

    hide notte with dissolve

    show euden with dissolve
    eud "Well, that's actually a great point.  This is a 'background' that our friend here made for us."
    eud "It captures a specific place from our journeys and displays it around us."

    hide euden with dissolve

    show notte with dissolve
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos  
    nott "Oh, neat!  So it's kind of like we're on a stage and it's, uh... what do you call it?  A backdrop?"
    hide speechright

    hide notte with dissolve

    show euden with dissolve
    eud "Exactly!  And whenever our friend wants, they can change it to a different one."

    hide euden with dissolve

    show notte closed_relaxed2 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    nott "Oooh!  Oooh!  In that case, take us somewhere with lots of YUMMY TREATS!  All this remembering has made me SUPER hungry!"
    hide speechright

    hide notte with dissolve

    show euden relaxed sweat_frown1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Whoa, easy there, Notte, it's not that simple.  Last time, I made the background for our friend here; I'm not sure they know how to do it on their own."
    hide speechright

    hide euden with dissolve

    show notte focused with dissolve
    nott "Well, that's an easy fix, then!  Just tell them how to work their magic, and PRESTO CHANGEO!  Notte gets her sugar fix!"

    show notte shocked
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos  
    nott "OOH, OOH!  Take us to the Sweet Retreat from Halloween!!!  The whole gosh-darn THING is made of CANDY!"
    hide speechright

    hide notte with dissolve

    show euden relaxed smile1 with dissolve
    eud "Well, actually, that does sound really fun.  And I'm sure YOU want to come as well?  In that case, I'll help you change the backgrounds."

label tutorial_defining_backgrounds:

    eud "First of all, you need to actually have a background image to use.  For our purposes, I've been putting them all in the file \"images/backgrounds\"."
    eud "There's actually a bunch of other folders under \"images,\" but we won't worry about it for right now."

    show euden blank sweat_frown1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Hmm... do I even HAVE the Sweet Retreat as a file?"
    hide speechright

    show euden focused smile1
    eud "Ah, here it is.  \"Sty_bg_0027_102_00.png\""
    eud "And yes, I know the name is super weird.  I think it's ripped straight from the original data of the world."
    eud "Do you want to hear about the file naming conventions?  You don't REALLY have to know the details, it's more for curiosity's sake."

    menu:

        "{color=#000000}Yeah, hit me with the details!{/color}":
            eud "Oh, sure!  I guess it IS best to be thorough, after all..."
            jump tutorial_background_name_conventions

        "{color=#000000}Mmm... nah, maybe later.{/color}":
            eud "Sure thing.  Like I said, it's not really that important."
            jump tutorial_background_no_name_conventions

label tutorial_background_name_conventions:

    eud "From what I can tell, there's 3 sets of numbers.  The first four-digit one refers to a specific location (\"0027\" here, the Halidom lawn)."
    eud "The second one (\"102\" in this case) refers to the time of day or the state of things in the image.  For instance, in this one the Sweet Retreat is fully built and it's daytime."
    eud "And the third one (\"00\") is used if there's multiple parts that come together to make the scene.  Some backgrounds are actually composite images, but in this case ours is a single image."
    eud "Anyway, all of this is to say, \"the files have weird names from the original game, but the numbers mean something.\"  As long as you can view the images, though, it shouldn't be a problem in selecting one."

label tutorial_background_no_name_conventions:

    show euden focused frown1

    eud "In any case, after you've got the image file, you need to make a statement to tell Ren'Py that it's an image you want to use, and to save it in memory."
    eud "You do this by using an 'equals' (=) statement that defines the file."
    eud "In this case, it's an 'image' file, so we'll precede it with 'image.'"
    eud "Next you need to come up with a name that you want to CALL the file within the program.  This is called a 'variable' name."
    eud "It's generally good convention to name it in lowercase.  OH!  And you can't use SPACES in a variable name."
    eud "If you put a space between two words, Ren'Py will think that you're using two separate names.  Underscores are a good workaround."
    eud "For our purposes, let's name the file... uh... 'sweet_retreat'?"
    eud "And last but not least, you follow the 'equals' sign (=) with the file pathway name in QUOTES.  That's very important; it tells Ren'Py to input the file pathway as a string of characters."

    show euden focused smile1
    eud "To put things simply, you just need to say:  image sweet_retreat = \"images/backgrounds/Sty_bg_0027_102_00.png\""
    eud "Are you ready to try it, or do you want to hear that again?"

    menu:

        "{color=#000000}Got it:  image sweet_retreat = \"images/backgrounds/Sty_bg_0027_102_00.png\"{/color}":
            show euden surprised smile1
            eud "Perfect!  I think it worked!"
            jump tutorial_successful_background

        "{color=#000000}...Actually, could I hear that again?{/color}":
            show euden sad smile3
            eud "No worries; I know this is a lot to process in one hearing."
            jump tutorial_defining_backgrounds

label tutorial_successful_background:

    show euden focused
    eud "In that case, the next thing you need to do is tell the program to display the background."
    eud "This is a lot easier than defining the image; just like last time, you just say the 'scene' statement."
    eud "That tells Ren'Py to change the background.  And then you just follow it by the 'variable' name you chose for the background."
    eud "In this case, it would be \"scene sweet_retreat\"."
    eud "Why don't you try it now?"

    hide euden with dissolve

    show notte with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    nott "Yeah, do it!!  Bring on the sugar rush!!!"
    hide speechright

    menu:
        "{color=#000000}scene sweet_retreat{/color}":
            jump tutorial_successful_bg_change

label tutorial_successful_bg_change:

    image sweet_retreat = "images/backgrounds/Sty_bg_0027_102_00.png"
    scene sweet_retreat

    show notte shocked shout1
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    nott "Eep!!!  Holy moly!  What in the heck just happened??"
    nott "We just appeared here before I even got a chance to blink!"
    hide speechright

    hide notte with dissolve

    show euden sad smile3 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Yeah... I forgot to mention that the default 'scene' statement just instantaneously changes the background."
    eud "The transition can certainly be a little... jarring."
    hide speechright

    hide euden with dissolve

    show notte grumpy pout1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos  
    nott "Well, thanks for the heads-up, Euden!  I swear I'm gonna have a tiny fairy heart-attack over here!"
    hide speechright

    hide notte with dissolve

    show euden relaxed sweat_frown1 with dissolve
    eud "Sorry, sorry... Uh, why don't I tell you how to make the transition a little cleaner?"

    show euden smile3
    eud "Last time you did this, I had you add the phrase 'with dissolve', which causes the previous image to blend gradually into the upcoming one."
    eud "But let's try for something different.  Here, I'll define a different image for you.  I always thought the Sweet Retreat was prettier at night, anyway."
    eud "Let's call it... sweet_retreat_night."

    image sweet_retreat_night = "images/backgrounds/Sty_bg_0027_302_00.png"

    show euden focused smile1
    eud "This time, try saying 'scene sweet_retreat_night with fade'.  The 'fade' statement makes things transition to black and then come back with the new image."

    menu:
        "{color=#000000}scene sweet_retreat_night with fade{/color}":
            jump tutorial_successful_bg_fade

label tutorial_successful_bg_fade:
    scene sweet_retreat_night with fade

    show notte surprised smile1 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    nott "Whoa!  It became night!  And it wasn't so shocking this time!"
    hide speechright

    hide notte with dissolve

    show euden with dissolve
    eud "Yeah, great job!  This looks fantastic.  Did you see how the 'fade' statement made the transition a little cleaner?"

    hide euden with dissolve

    show notte focused with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    nott "Oh, yeah!!!  Major kudos!  But let's dig in first!!!"
    hide speechright

    show notte closed_relaxed2 smile2 with dissolve
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos  
    nott "(Monch) Mmmmmm... oh my gosh, it tastes so good!  So sweet!  Aaahhh, I love candy! (Nom)"
    hide speechright

    hide notte with dissolve

    show euden with dissolve
    eud "Haha, I'm glad you like it so much."

    eud "And... as for you over there, does that make sense, or do we need to go through that again?"

    menu:

        "{color=#000000}I get it.  'Scene' to transition, 'fade' to make transitions cleaner.{/color}":
            jump tutorial_done_with_bgs

        "{color=#000000}Uh... I think I need to hear it again.{/color}":
            eud "No worries!  You should keep trying until you feel comfortable with it."
            jump tutorial_successful_background

label tutorial_done_with_bgs:

    show euden with dissolve

    eud "That's great!  You're a real natural at this!  I can't wait to see what kind of things you'll be capable of in the future!"

    hide euden with dissolve

    show notte grumpy smile1 with dissolve
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos  
    nott "Forget the future, I want more treats NOW! (gobble)"
    hide speechright

    hide notte with dissolve

    show euden focused sweat_frown1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Uh, are you sure?  If you keep eating at this rate, you're gonna get bloat—"
    hide speechright

    hide euden with dissolve

    image notte_bloat_tutorial = "images/notte/notte_bloated_body.png"

    stop music fadeout 1.0

    show notte_bloat_tutorial with dissolve

    nott "(PLOP!)"

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadein 1.0

    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    nott "..."
    hide speechright

    hide notte_bloat_tutorial with dissolve

    show euden surprised sweat_frown1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos  
    eud "..Oh dear, it looks like I'm already too late..."
    hide speechright

    show euden sad smile3
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Uh... well, it looks like Notte's gonna be out of commission for a while, so let's... take five and meet back up?"
    eud "Ha... Haha..."
    hide speechright

    hide euden with dissolve

    stop music fadeout 2.0

    # This goes back to script

    jump tutorialmenu






















label tutorial_chars:


    play music "audio/music/Utopia.flac" fadeout 1 fadein 1.0

    scene halidom_hall with dissolve

    show notte closed_grumpy smile3 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    nott "...Whew, I think I'm finally through the stomache cramps!  Lesson learned; from now on, it's salads and portion control for ol' Notte!"
    hide speechright

    hide notte with dissolve

    show euden surprised smile1 with dissolve
    eud "Yeah, I'll say...  I was worried you were going to explode for a second there!"

    hide euden with dissolve

    show notte closed_relaxed2 smile2 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos  
    nott "Yeah... I kinda went a little overboard...  Turns out an entire Sweet Retreat is KIND of something to share with a bunch of people, not to eat solo...."
    hide speechright

    show notte surprised frown1
    nott "Speaking of though, isn't it kind of a bit lonely with just the two of us here?"

    show notte shocked smile4
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    nott "—Ah, whoops!  I mean the THREE of us.  Sorry about that, new friend over there."
    hide speechright

    hide notte with dissolve

    show euden with dissolve
    eud "Well, actually, that's exactly what I wanted to talk about next.  Now that we've figured out how to bring Notte here, instantiating some of our other friends should be a lot easier the second time around."

    hide euden with dissolve
    show notte sad2 smile1 with dissolve
    nott "Oh, goody!!!  Not that I'm not TOTALLY happy having some one-on-one time with Euden, of course!  I just miss the other folks too, and if we brought them over here, that would really liven things up!"

    hide notte with dissolve

    show euden with dissolve
    eud "I agree!  And I think with our new friend helping, it should be super easy."

    show euden relaxed
    eud "Now... I was thinking about someone in particular that I think we should bring first.  Want me to surprise you, or should I just tell you now?"

    hide euden with dissolve

    show notte sad smile2 with dissolve
    nott "I dunno, do they happen to have long blonde hair, a flowy sash and a huge \'ahoge?\'  Perhaps a name that starts with a 'Z' and rhymes with \"Schmethia\"?"

    hide notte with dissolve
    show euden closed_relaxed smile3 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Haha yeah, I guess you got me there...  Not much of a surprise, huh?"
    hide speechright

    hide euden with dissolve
    show notte closed_relaxed2 smile1 with dissolve
    nott "Well, duh, the three of us have been friends for our whole lives.  I wanna see her too!"

    hide notte with dissolve

    show euden with dissolve
    eud "Sure thing.  In that case... Here, friend, I've got the procedure already pulled up for you."
    eud "Characters work just like any other image, in that you can 'show' and 'hide' them."
    eud "And just like with backgrounds, you can use the 'dissolve' or 'fade' commands to alter the way a character appears on the screen when you 'show' them."
    eud "But unlike backgrounds, I already pre-defined the character's data into \".rpy\" code files for you!  Hopefully that makes things convenient?"

    hide euden with dissolve

    menu:

        "{color=#000000}show zethia with dissolve{/color}":
            jump tutorial_chars_zethia_appears

label tutorial_chars_zethia_appears:

    play music "audio/music/Yumemiteta no Atashi (Story Version B).flac" fadeout 1.0

    show zethia with dissolve
    zeth "...Huh?"
    zeth "What am I... Wait, Euden?  And Notte?"

    hide zethia with dissolve
    show notte surprised with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    nott "ZETHIA!  It's AMAZING to be able to see you again!!!"
    hide speechright

    hide notte with dissolve
    show euden sad smile1 with dissolve
    eud "...Yeah.  Welcome home, Zethia."

    hide euden with dissolve
    show zethia with dissolve
    zeth "...Euden... and Notte... I'm... I'm so glad to see you all again..."
    zeth "...I don't even know how to express my feelings right now..."

    hide zethia with dissolve
    show notte sad with dissolve
    nott "It's ok, girl!  Let it all out!!!"

    stop music fadeout 1.0
    hide notte with dissolve
    show zethia with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    zeth "...No, as in, I LITERALLY have no idea how to express my feelings."
    hide speechright

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadein 1.0

    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    zeth "I... I feel like my face is frozen in this one expression.  Hrrrrgh.  It actually feels really unnatural.  Please help."
    hide speechright
    hide zethia with dissolve

    show euden blush_surprised sweat_frown1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    eud "S-Sorry!  T-This is embarrassing!  I was so caught up in the moment that I forgot to help Zethia change her 'face' group when she started speaking."
    hide speechright

    hide euden with dissolve
    show notte shocked frown1 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos  
    nott "\"Face group?\"  What even IS that?  Hurry and help Zethia, I'm starting to freak out here."
    hide speechright

    hide notte with dissolve

    show euden surprised sweat_frown1 with dissolve
    eud "Y-Yeah, right away.  But I might need some help from our friend here."
    show euden relaxed
    eud "Unlike backgrounds, characters are more complicated because they need a bunch of different animated assets."
    eud "As a result, they've all been implemented as something called a \"layeredimage\", including me and Notte."
    eud "Layeredimages are useful because they allow you 1) to easily overlay components of composite images on top of each other..."
    eud "...and 2) to sort image components into logical groups, each of which can be changed independently with keywords."

    show euden focused frown1
    eud "Layeredimages are built from the bottom up.  Most 'character' layeredimages have a single sprite that comprises their 'body'."
    eud "The other layers are then then overlaid on top of the 'body' image to alter its appearance and emotions."
    eud "Usually, characters don't have 'body' GROUPS, but they might on occasion, so be sure to check.  (Pia, for example, can switch between holding a book and having her hands empty)."
    eud "Anyway, whether or not the character has a body group, they'll almost always have a 'face' and a 'mouth' group.  Each of those groups contains a set of similar components."
    eud "The 'face' group usually controls the character's eyes, and the 'mouth' group controls their mouth."
    eud "And within each group, the related components have unique labels that allow you to access them with a keyword."
    eud "So... if Zethia wants to be able to express her surprise and confusion at this unusual situation, for instance, you'll need to use a keyword to help her change her eyes and mouth."
    eud "Why don't you try changing her eyes to 'surprised'?"

    hide euden with dissolve
    show zethia with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    zeth "Yes, please do, with all haste!"
    hide speechright
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos  
    zeth "...How exactly does our friend do that?"
    hide speechright

    hide zethia with dissolve
    show euden surprised sweat_frown1 with dissolve
    eud "Oh, sorry.  You actually just use the 'show' statement like usual, but instead of adding 'with dissolve', you can just follow it with the keyword.  So in this case..."

    hide euden with dissolve
    show zethia with dissolve

    menu:
        "{color=#000000}show zethia surprised{/color}":
            jump tutorial_chars_zethia_surprised

label tutorial_chars_zethia_surprised:
    show zethia surprised
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    zeth "Oh my, amazing!  That's already so much better."
    hide speechright

    hide zethia with dissolve
    show notte surprised frown1 with dissolve

    nott "But her mouth's still all frozen in that weird smile.  Shouldn't we do something about that?"

    hide notte with dissolve
    show euden surprised sweat_frown1 with dissolve
    eud "Yes, do that again but use the 'frown1' mouth command.  Same syntax; Ren'py's smart enough to figure out whether a part is in the 'face' or 'mouth' group."
    eud "(However, that does mean that every part within a single layeredimage needs to have a unique name, F.Y.I.)"

    hide euden with dissolve
    show zethia surprised with dissolve

    menu:
        "{color=#000000}show zethia frown1{/color}":
            jump tutorial_chars_zethia_frown1

label tutorial_chars_zethia_frown1:
    show zethia surprised frown1
    zeth "Oh!  That was fast!"
    zeth "Thank you!  This is all a bit shocking, but at least my face feels less frozen."

    play music "audio/music/Utopia.flac" fadeout 1.0 fadein 1.0
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos  
    zeth "Are... these the only faces I'm able to make, though?"
    hide speechright

    hide zethia with dissolve
    show euden surprised frown1 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    eud "Of course not!  I offloaded all of Zethia's \"art assets,\" so there's a huge list of what she can do!"
    eud "Whenever I implement one of my friends, I put a \"readme\" section at the top of their character_procedures.rpy file."
    hide speechright
    hide euden with dissolve
    image zethiareadme = "images/tutorial/Zethia readme.png"
    show zethiareadme at top with dissolve

    eud "As you can see, it lists all the different options and commands you can use for that character."
    eud "A lot of these words, like 'relaxed', 'angry', 'sad', 'smile1', 'frown1', 'mutter1', etc. are consistent across multiple characters."
    eud "This consistent language is valuable because, if the same command works for multiple characters, it makes writing a lot easier."
    eud "Of course, not all characters have every expression, and some have multiple of the same, so you need to be cognizant of that when writing."
    eud "Oh, I should also probably explain how this 'readme' works."
    eud "See, because each of these lines is preceded by a hashtag (#) on the left, those lines are \"commented out\" and Ren'py knows not to execute them as code."
    eud "Creating useful, comprehensive 'readme's and then consulting them properly when writing is the key to effective implementation of characters."
    eud "And of course, you can use the # to make notes to yourself anywhere else in your code as well."

    hide zethiareadme with dissolve
    show euden surprised frown1 with dissolve
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos  
    eud "Oh!  And as a side note, the parts for these characters automatically do dynamic blinking, and their mouth moves to match whatever text they happen to be saying."
    hide speechright
    eud "If you want to implement characters that aren't already part of the provided file package, you'll need to learn how to write that procedure yourself, but that's a topic for later."

    stop music fadeout 1.0

    hide euden with dissolve
    show notte focused with dissolve

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadein 1.0

    nott "Enough of the 'code' talk!  Let's give this list of face words a whirl!"

    nott "Let's see here... uhhh... \"show zethia focused awkward1!\""

    hide notte with dissolve
    show zethia focused awkward1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    zeth "Eeep!  That tickles!"
    hide speechright

    hide zethia with dissolve
    show notte closed_relaxed2 with dissolve
    nott "Hee hee!  Looks like it worked!"

    hide notte with dissolve
    show zethia focused awkward1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    zeth "Hold on!  Does this mean it's possible to change MULTIPLE facial parts as a list within a single \"show\" statement?"
    hide speechright

    hide zethia with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    show euden surprised sweat_frown1 with dissolve
    eud "Uh— yeah, it is, I was planning to get into that...  Aren't we getting a little ahead here, though?  We should take it slowly and—"
    hide speechright

    hide euden with dissolve
    show notte focused with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    nott "Oh oh!  \"show zethia grumpy pout1\"!"
    hide speechright

    hide notte with dissolve
    show zethia grumpy pout1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos  
    zeth "Wh— Notte, this isn't funny!"
    hide speechright

    hide zethia with dissolve
    show notte closed_relaxed2 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    nott "Well, your face definitely LOOKS pretty funny!  Ha ha ha ha!"
    hide speechright

    show notte surprised
    nott "Oooh, and you even have {i}other{/i} expressions as well!  I bet they're even sillier-looking!"
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos  
    nott "But... why did Euden bother to label them that way?"
    hide speechright

    hide notte with dissolve

    show euden surprised sweat_frown1 with dissolve
    eud "What do you mean, \"label them that way?\"  I thought the labelling was pretty consistent."

    hide euden with dissolve
    show notte focused frown1 with dissolve
    nott "No, like, you literally had to REMIND yourself that she had other expressions?  Like, 'other_angry1'.  Isn't it already obvious that it's \"another\" expression?"

    nott "Seems like bad labelling to me, but whatever.  \"show zethia other_angry1\"—"

    hide notte with dissolve
    show euden angry shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    eud "No, Notte, wait, that's—!!!"
    hide speechright

    stop music fadeout 1.0

    image white = "images/backgrounds/white.png"
    show white with dissolve
    hide euden
    show zethia closed_focused grin1
    hide white with dissolve

    zeth "...heh heh heh."

    play music "audio/music/Threatening Aura intro.flac" fadein 1.0
    queue music "audio/music/Threatening Aura.flac"

    show zethia other_angry grin1
    zeth "I thank you, foolish little fey creature.  Your actions have finally released me from the prison of that wretched Auspex's mind."

    hide zethia with dissolve
    show notte shocked shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    nott "...Wait, the label meant 'other' as in... THE Other?!?!?"
    hide speechright

    hide notte with dissolve
    show zethia other_angry2 grin1
    zeth "Indeed.  And now that my metaphorical jail cell has been sprung, I'll be able to wreak all kinds of havoc upon this little hovel of a dimensional space.  Ha ha ha haaaa!!!"

    image halidom_hall_dark = "images/backgrounds/Sty_bg_0024_400_00.png"
    scene halidom_hall_dark with fade

    pause 2.0

    show notte grumpy shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    nott "Jeepers creepers!!!  Not this jerk again!!!  We just got the Halidom back in order, too!!!"
    hide speechright

    show notte closed_grumpy
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos  
    nott "EUDEN, YOU COMPLETE DOOFUS!!!  Why do you even HAVE 'The Other' face options for Zethia in the FIRST PLACE?!?!"
    hide speechright

    hide notte with dissolve
    show euden surprised grimace2 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "I-I just grabbed all the image data on Zethia I could get, that's all!  I'm still figuring this out, ok?!?"
    hide speechright

    hide euden with dissolve
    show zethia other_angry2 grin1 with dissolve
    zeth "HAHAHAHAHA!!!  BOW BEFORE ME, FOOLS!!!"

    hide zethia with dissolve
    show notte closed_grumpy shout1 with dissolve
    nott "Well, DO something!!  Or what about our friend here?  Quick, why don't YOU help us fix this!!!"

    hide notte with dissolve

    menu:
        "{color=#000000}hide zethia with dissolve{/color}":
            jump tutorial_chars_zethia_hide

label tutorial_chars_zethia_hide:

    show zethia other_focused shout1 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos  
    zeth "Wait, what?!?  You mean you can just DO tha—?!"
    hide speechright

    stop music
    hide zethia with dissolve

    scene halidom_hall with dissolve

    show euden closed_focused grimace1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Whew... that was some quick thinking.  Thanks for fixing the situation."
    hide speechright

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadein 1.0

    hide euden with dissolve
    show notte shocked shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    nott "Wait, what exactly is \"fixed\" about the situation?  In case you haven't noticed, our friend just made Zethia DISAPPEAR!"
    hide speechright

    hide notte with dissolve
    show euden sad skew_smile1
    eud "W-Well, the thing is, that actually fixed the problem automatically.  Once a 'layeredimage' disappears, all its 'group' settings get reverted to their defaults."
    eud "Or, at least, that's the case unless you explicitly name a different 'face' or 'mouth' when you 'show' it again."

    hide euden with dissolve
    show notte surprised frown1 with dissolve
    nott "The defaults?... Oh, you mean those things labelled \"default\" in the readme?  ...let's see, \"relaxed\" and \"small_smile1\"?"
    show notte surprised smile1
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos  
    nott "OHHHH, I get it!  So when Zethia comes back, she won't have those eyes of \"The Other\" anymore!"
    hide speechright
    nott "\"show zethia with dissolve\"!"

    hide notte with dissolve
    show zethia with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    zeth "My goodness, what a fright!  Thanks so much for saving me!"
    hide speechright

    hide zethia with dissolve
    show notte sad smile2 with dissolve
    nott "WHEW!  She's back to normal!  That was CRAZY!"

    hide notte with dissolve
    show euden sad smallsmile1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Yeah... I guess the lesson here would be, \"Always pay close attention to the readme?\""
    eud "Since if you're not careful, the results may be... shocking... \nah ha ha..."

    show euden sweat_frown1
    eud "...How about we all take a little break and meet up later?  ...I think I need to lie down..."
    hide speechright

    hide euden with dissolve

    stop music fadeout 2.0


    # This goes back to script

    jump tutorialmenu


















label tutorial_writing_dialogue:


    play music "audio/music/Utopia.flac" fadeout 1 fadein 1.0

    scene halidom_hall with dissolve

    show notte sad smile3 with dissolve
    nott "...Well, we've got the Halidom set up, Zethia's back, I'm over my tummyache and that whole 'other label' situation got fixed thanks to our friend here."
    show notte relaxed
    nott "Seems like we're pretty much all set now!  So now we can just relax, sit back and have a nice chat."
    show notte closed_smile1
    nott "..."
    hide notte with dissolve
    show zethia closed_smile1 with dissolve
    zeth "..."
    hide zethia with dissolve
    show euden closed_smile1 with dissolve
    eud "..."
    hide euden with dissolve
    show notte surprised closed_smile1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    nott "..."
    hide speechright
    show notte sad smile2
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos  
    nott "...Yeah, I got nothing."
    hide speechright
    show notte frown1
    nott "It's great that we're all together again, but now that we ARE, I'm not really sure what we should even TALK about!  Things have been pretty wild."
    hide notte with dissolve
    show euden surprised smallsmile1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "...Yeahh, I feel the same way.  I thought that things could just go back to normal as soon as I got you guys here, but a lot has happened since we last saw each other."
    hide speechright
    eud "I don't even know what your lives have been like in the meantime."
    eud "To be honest, I'm kind of unsure what questions I should be asking..."

    hide euden with dissolve
    show zethia with dissolve
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos  
    zeth "...Well, perhaps we should let our new friend decide on a topic of conversation?  They have done quite a lot for us lately, so it would only be fair."
    hide speechright
    hide zethia with dissolve
    show euden with dissolve
    eud "That's true.  In that case, why don't YOU take point and lead the three of us through a quick chat?"
    eud "Ren'py's designed to be a visual novel engine, which means that the dialogue writing is SUPER streamlined."
    eud "All you have to do is use the character's 'sayer' tag followed by what you want them to say, in quotes."

    menu:
        "{color=#000000}Uhh... so, like this?\n\neuden \"You did it correctly!\"{/color}":
            jump tutorial_dialogue_euden_no

label tutorial_dialogue_euden_no:

    stop music

    image black = "images/backgrounds/black.png"
    show black
    "{color=#FF0000}An exception has occurred.{/color}"
    "{color=#FF0000}Exception: Sayer 'euden' is not defined.{/color}"

    nott "Eeek!  Everything went dark!  What happened?"

    eud "Oops!  I think Ren'py crashed.  Lemme reboot the world really quickly..."

    eud "..."

    play music "audio/music/Utopia.flac" fadeout 1 fadein 1.0

    scene halidom_hall with fade
    show euden closed_relaxed smile3 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "There we go, ahaha... I should have warned you that 'euden' is my LAYEREDIMAGE name, not my 'sayer' name."
    hide speechright

    hide euden with dissolve
    show notte surprised frown1 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos  
    nott "...Well, why can't you just make them BOTH 'euden'?"
    hide speechright

    hide notte with dissolve
    show euden surprised frown1 with dissolve
    eud "Well, that's because 'euden' is already referring to an image of me.  If Ren'py tried to use 'euden' to write DIALOGUE, it wouldn't know what to do..."
    eud "And if you tried to redefine 'euden' as a 'sayer' with a separate statement, it could even make my image disappear."
    eud "...Also, since characters sometimes say a lot of lines in a row, you could wind up typing the 'sayer' name a lot.  So it's nice for the 'sayer' name to be short."
    eud "Anyway, if you want to make me say dialogue, my 'sayer' tag is 'eud,' NOT 'euden.'  Likewise, Notte's is 'nott' and Zethia's is 'zeth'."

    hide euden with dissolve
    show notte surprised smile2 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    nott "Ohhh, well, I guess that makes sense then... 'Eud,' my dude?"
    hide speechright

    hide notte with dissolve
    show euden surprised sweat_frown1 with dissolve
    eud "Uh, well, you don't have to CALL me 'Eud' when you're talking to me.  The program kind of just ignores everything in the quotes and assumes it's dialogue..."
    eud "It's only when making commands in Ren'py OUTSIDE quotation marks that 'euden' vs. 'eud' makes a difference."

    show euden sad smile1
    eud "A-Anyway, why don't you just try that dialogue thing again?"

    menu:
        "{color=#000000}eud \"You did it correctly!\"{/color}":
            jump tutorial_dialogue_euden_yes

label tutorial_dialogue_euden_yes:
    eud "You did it correctly!"

    hide euden with dissolve
    show notte surprised with dissolve
    nott "Whoa, it really worked!"
    hide notte with dissolve
    show euden relaxed smile2
    eud "Absolutely!  And you might have noticed that my lips moved automatically when our friend had me say that."
    eud "That's because everyone's layeredimages are designed to recognize whether their corresponding 'sayer' is talking or not..."
    eud "...and if the 'sayer' IS talking, this story engine will make 'lip flap' happen on their layeredimage while that character's dialogue is actively scrolling."

    hide euden with dissolve
    show zethia with dissolve
    zeth "That's impressive.  With things implemented this way, dialogue looks totally natural!"

    hide zethia with dissolve
    show euden closed_relaxed with dissolve
    eud "Absolutely.  And it should be fairly natural to write, now, too."
    show euden relaxed
    eud "So... now that you know how to use our 'eud,' 'nott' and 'zeth' sayers to make dialogue, why don't you lead us in that conversation?"

    menu:
        "{color=#000000}eud \"Ok.  Zethia, how have things in Alberia been without me?\"{/color}":
            jump tutorial_dialogue_part1

label tutorial_dialogue_part1:
    eud "Ok.  Zethia, how have things in Alberia been without me?"
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    eud "(That's great!  Now have Zethia reply to me!)"
    hide speechright

    menu:
        "{color=#000000}zeth \"Well, things have been keeping me pretty busy as Alberia's Auspex.\"{/color}":
            jump tutorial_dialogue_part2

label tutorial_dialogue_part2:

    stop music fadeout 1.0

    show euden surprised frown1
    zeth "Well, things have been keeping me pretty busy as Alberia's Auspex."

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadein 1.0

    show euden sweat_frown1
    zeth "...Hang on, can you guys see me?  Something feels off."
    zeth "Hello?"
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Yeah, sorry, Zethia, I think the issue is your layeredimage wasn't shown first."
    hide speechright
    show euden relaxed smile1
    eud "If you want to see Zethia talking, you need to use a 'show' statement to make her layeredimage 'zethia' appear, and THEN use 'zeth' to make her talk."
    eud "...Although this was actually cool to see, because (as you might have noticed) my lips didn't move for ZETHIA's dialogue.  That's the value of having separate speakers 'eud' and 'zeth'."
    show euden closed_relaxed smile1
    eud "A-Anyway, why don't you try showing Zethia for the NEXT line?  I'll step out of the way for you."
    hide euden with dissolve

    menu:
        "{color=#000000}show zethia with dissolve\n\nzeth \"I recently held an audience with Auspex Origa.  It's good to see her without worrying about plots and schemes.\"{/color}":
            jump tutorial_dialogue_part3

label tutorial_dialogue_part3:
    show zethia with dissolve
    zeth "I recently held an audience with Auspex Origa.  It's good to see her without worrying about plots and schemes."
    show zethia surprised frown1
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    zeth "...Ah!  It worked!  Astounding."
    hide speechright
    nott "Oooh, ooh!  I want a turn!  Can I say something?"
    nott "That shouldn't be hard for you, right?"

    menu:
        "{color=#000000}show notte with dissolve\n\nnott \"Wait, you should totally go shopping with her!  With the two of you in solidarity, you could totally revamp the future of Auspex duds!\"{/color}":
            jump tutorial_dialogue_part4

label tutorial_dialogue_part4:
    show notte with dissolve
    stop music fadeout 1.0
    nott "Wait, you should totally go shopping with her!  With the two of you in solidarity, you could totally revamp the future of Auspex duds!"
    play music "audio/music/CRASHER (Story Version C) intro.flac" fadein 1.0
    queue music "audio/music/CRASHER (Story Version C).flac"
    show notte shocked shout1
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    nott "Eek!!!  Now I'm right smack-dab over Zethia's face!!!"
    hide speechright
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    zeth "Mmmfffmfmf.... Mfff!"
    hide speechright
    nott "How do we fix this???"
    eud "Uh oh... I think our friend forgot to 'hide' Zethia first..."
    nott "Hurry!  She's gonna suffocate here!"

    menu:
        "{color=#000000}hide zethia with dissolve{/color}":
            jump tutorial_dialogue_part5

label tutorial_dialogue_part5:
    stop music fadeout 1.0
    hide zethia with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    zeth "...Whew!  I can breathe again!"
    hide speechright

    play music "audio/music/Utopia.flac" fadein 1.0

    show notte sad smile2
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    nott "Man, that's a relief.  I thought we were gonna have to get emergency surgery or something..."
    hide speechright

    menu:
        "{color=#000000}hide notte with dissolve\n\nshow euden surprised grimace1 with dissolve{/color}":
            jump tutorial_dialogue_part6

label tutorial_dialogue_part6:

    hide notte with dissolve
    show euden surprised grimace1 with dissolve

    eud "Oh?  It looks like our friend wants me to say something?"
    eud "...and, nice job with the 'hide'ing and 'show'ing, by the way.  Very smooth."

    menu:
        "{color=#000000}eud \"Notte, maybe you shouldn't say stuff like, \"That shouldn't be hard for you, right?\"  Clearly this is trickier than it looks for our friend.\"{/color}":
            jump tutorial_dialogue_part7

label tutorial_dialogue_part7:
    eud "Notte, maybe you shouldn't say stuff like—"

    stop music

    image white = "images/backgrounds/white.png"
    show white
    "{color=#FF0000}Parsing the script failed.{/color}"
    "{color=#FF0000}end of line expected.\neud \"Notte, maybe you shouldn't be saying stuff like, \" —> That shouldn't be hard for you, right?{/color}"

    nott "Oh no, not again!  This time it looks like the dialogue didn't even get to RUN before it crashed!"

    eud "Ah... I think I see the problem.  Our friend was trying to have me quote Notte, but with real quotation marks."
    eud "See, you can't use normal quotation marks inside the quote-text, since Ren'py will think you're closing out of the sentence, and that whatever comes afterwards is CODE."
    eud "...Try doing the same thing, but this time, use the backslash (\\) before the quotation marks.  It's a little weird, but just trust me."

    menu:
        "{color=#000000}eud \"Notte, maybe you shouldn't say stuff like, \\\"That shouldn't be hard for you, right?\\\"  Clearly this is trickier than it looks for our friend.\"{/color}":
            jump tutorial_dialogue_part8

label tutorial_dialogue_part8:

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadein 1.0

    scene halidom_hall with dissolve
    show euden surprised grimace1 with dissolve
    eud "Notte, maybe you shouldn't say stuff like, \"That shouldn't be hard for you, right?\"  Clearly this is trickier than it looks for our friend."

    show euden surprised smile1
    eud "...Aha!  There we go.  The backslash (\\) character, which is sometimes called an \"escape character,\" is used in blocks of quote-text like this to indicate special characters that shouldn't break the quote apart."
    eud "And it's not just for quotes.  You can use the phrase \\n to tell Ren'py to break a quote up into two lines on a screen.\n\nLike this!  See how the line went down to the next line? (I cheated and used two here.)"
    eud "Heck, you can even use \\\\ to tell Renpy to print a \\ on the screen!"

    hide euden with dissolve
    show notte surprised shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    nott "Whoa, that's one powerful line!  I can't believe it can do all that."
    hide speechright
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos  
    nott "...Oh!  But what if I want to CHANGE the text instead?"
    hide speechright

    hide notte with dissolve
    show euden surprised frown1 with dissolve
    eud "...\"Change\" the text?  What do you mean?"
    hide euden with dissolve

    show notte surprised with dissolve
    nott "Oh, well, like... if I wanted my dialogue to be pretty and pink, like a strawberry!  Black is boring, right?"
    hide notte with dissolve

    show euden with dissolve
    eud "Ohhhh, you mean FORMATTING TAGS.  Yeah, those are super useful!  You indicate THOSE with curly brackets.  That is to say, {{ and }."
    eud "To change the color of text like you're talking about, you have to put a {{color} statement at the beginning of your phrase, and a \n{{/color} statement at the end."
    eud "The forward slash in {{/color} tells Ren'py that it's REMOVING a formatting that was applied previously with {{color}."
    eud "Of course, you have to actually SAY the color you want to use, through hex code.  So, for pink specifically, you'd say something like {{color=#F81894}, then the text you want to color, then end with {{/color}."
    eud "Why doesn't our friend give you a hand with that, actually?"

    hide euden with dissolve

    menu:
        "{color=#000000}nott \"{{color=#F81894}Radical!  Now my words can be as sweet as strawberries!{{/color}\"{/color}":
            jump tutorial_dialogue_part9

label tutorial_dialogue_part9:

    show notte with dissolve
    nott "{color=#F81894}Radical!  Now my words can be as sweet as strawberries!{/color}"
    nott "Whoa, it really worked!  My dialogue can become {color=#F81894}PINK{/color}!"

    hide notte with dissolve
    show euden with dissolve
    eud "Exactly!  Formatting tags are useful for other stuff, too.  They're very versatile."
    eud "For instance, you can put text in {{i}{i}italics{/i}{{/i}, you can {{b}{b}bold{/b}{{/b} text (although that doesn't look great in this font), or even {{u}{u}underline{/u}{{/u} it!"

    play music "audio/music/BANG (Story Version B) intro.flac" fadeout 1.0 fadein 2.0
    queue music "audio/music/BANG (Story Version B).flac"

    hide euden with dissolve
    show zethia focused with dissolve
    zeth "Wow, that's really impressive!  Although you might have to be careful that you're not making too... {b}bold{/b} of a statement!  Hee hee."

    hide zethia
    show euden surprised sweat_frown1 with dissolve
    eud "Wait, Zethia making a pun?  That's rare to see."
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    eud "...Uh oh...  Brace yourselves..."
    hide speechright

    hide euden with dissolve
    show zethia surprised smile1 with dissolve
    zeth "There's no need to be upset.  Thanks to your instruction just now, I've simply developed a different... {i}slant{/i} on things than usual.  I don't think there's any point in being {color=#0000FF}blue{/color} over some goofy {u}lines{/u}, is there?"

    hide zethia with dissolve
    show notte shocked shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    nott "Oh no!!!  We've unleashed Zethia's inner punster with these darn formatting tags!!!  This'll go on forever!!!"
    hide speechright

    hide notte with dissolve
    show zethia surprised smile1 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    zeth "Well, that just won't do.  You don't like these puns?  Maybe you've... {color=#FF0000}RED{/color} them already??  HEE HEE!"
    hide speechright

    hide zethia with dissolve

    show notte closed_grumpy pout1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos  
    nott "AAAAAAAAAAAUGH!!!  This is somehow even WORSE than when she was the Other!"
    nott "Cut!  Fade to black!  End the episode!  Help!!!"
    hide speechright

    scene black with fade

    stop music fadeout 2.0


    # This goes back to script

    jump tutorialmenu























label tutorial_music_and_audio:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "audio/music/Utopia.flac" fadeout 1 fadein 1.0

    image halidom_hall = "images/backgrounds/Sty_bg_0024_100_00.png"
    scene halidom_hall with dissolve

    show notte surprised with dissolve
    nott "Hey, Euden!  Now that we can bring our friends here and change the backgrounds, you know what we should do?"

    show notte focused
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    nott "Let's throw a totally awesome party!!!"
    hide speechright

    show notte closed_relaxed2 smile3
    nott "I'm thinking we could make it a whole celebration, with food and music!  Let's crank those tunes!"

    hide notte with dissolve
    show euden surprised sweat_frown1 with dissolve

    eud "Umm... but I'm not really sure how to play music or anything like that..."

    hide euden with dissolve
    show notte surprised frown1 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos  
    nott "What?  But you and your friend can do all this other amazing stuff!  Surely it shouldn't be hard to DJ for us, right?"
    hide speechright

    hide notte with dissolve
    show euden closed_sad smallsmile1 with dissolve

    eud "Well, when you put it like that, it sounds reasonable... but the thing is, I don't even know where to start."

    show euden relaxed sweat_frown1
    eud "I guess I managed to download some files that SEEM like audio, but I'm not really much of a musician..."
    show euden blush_surprised skew_smile1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "I was mostly focused on the files for my friends and the places we've been... ahaha..."
    hide speechright

    hide euden with dissolve
    show notte relaxed2 frown2 with dissolve

    nott "Well, if you don't know how to do it..."

    show notte smile4
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos  
    nott "...why don't you just call in somebody who DOES?  I mean, we've got a LOT of musically-inclined friends, right?"
    hide speechright

    hide notte with dissolve
    show euden surprised skew_smile1 with dissolve

    eud "That's... actually not a bad idea."

    hide euden with dissolve
    show notte closed_relaxed2 smile2 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    nott "Well, duh!  Your old pal Notte's got a billion great ideas in her noodle!"
    hide speechright

    show notte relaxed smile1
    nott "As far as who to ask... how about Maritimus?  He runs a whole choir!"

    show notte relaxed3 smile3
    nott "Hey, you over there behind the screen!  Why don't you pull up that fluffy ol' lump of dragon for us?"

    hide notte with dissolve
    show euden surprised shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    eud "UHHHH... Hang on, wait a minute!!!  That's no good!!!"
    hide speechright

    hide euden with dissolve
    show notte shocked pout1 with dissolve

    nott "What?  Why?"

    hide notte with dissolve
    show euden focused2 sweat_frown1 with dissolve

    eud "Well, if you're pulling up Maritimus... doesn't he specialize in CHORAL MUSIC?"

    hide euden with dissolve
    show notte neutral frown1 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos  
    nott "Well, yeah.  Duh.  What's the issue with that?"
    hide speechright

    hide notte with dissolve
    show euden closed_focused skew_frown1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Erm, well, vocal music could get us into trouble with 'copyright' law..."
    hide speechright

    hide euden with dissolve
    show notte surprised frown1 with dissolve

    nott "...\"Copy Write\" law?  What's that?"

    hide notte with dissolve
    show euden surprised skew_smile1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos  
    eud "Um... well, it's hard to explain without getting too 'meta'... but... basically, we have to be respectful of the rules of the world our friend here is from, or we'll get into major trouble."
    show euden grimace1
    eud "If we start ripping a bunch of .mp3's with vocals in them, the lawsuits will tear our dimension apart faster than you can say 'terms of service violation'..."
    hide speechright

    hide euden with dissolve
    show notte sad pout1 with dissolve

    nott "I... don't get any of that, but it sounds bad.  Does that mean no music?  Aww..."

    hide notte with dissolve
    show euden surprised sweat_frown1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Uh, well, maybe not music with LYRICS.  Background music's... um... PROBABLY fine?"
    hide speechright

    hide euden with dissolve
    show notte shocked smile2 with dissolve
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos  
    nott "Oh!  Well, in that case, ol' Notte has the perfect idea!  (scribbles)  Here, new friend!  Why don't you give THIS a whirl?"
    hide speechright

    menu:
        "{color=#000000}show giovanni with dissolve{/color}":
            jump tutorial_music_giovanni_appears

label tutorial_music_giovanni_appears:

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadeout 1

    hide notte with dissolve
    show giovanni with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_upperrightpos  
    gio "AT LAST, I APPEAR!!!  THE MAESTRO OF MUSIC GIOVANNI, CALLED BY YOUR {i}CONVOCAZIONE{/i}!!!"
    hide speechright
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_upperrightpos  
    gio "I mean—ahem—hello..."
    hide speechright

    show giovanni open
    play sound "audio/sound/note.wav"
    show speechright note at speechright_upperrightpos  
    gio "Why, Euden, I haven't seen you in ages!  How resourceful of you to call me!  {i}Bravizzimo{/i}!"
    hide speechright

    hide giovanni with dissolve

    show euden closed_sad skew_smile1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Haha, hello to you too, Giovanni!  You seem as... uh... exuberant as ever!"
    hide speechright

    hide euden with dissolve

    show giovanni happy with dissolve

    gio "Indeed!  And with good reason, for it seems I have transcended time and space to appear in your presence once more!  Such a miracle should be rightly celebrated, no?"

    hide giovanni with dissolve
    show notte with dissolve

    nott "Yeah, you're right!  It's great to see you, too, big guy!  And... now that you're here, maybe you can tell us how to play these \"audio files\" Euden was talking about?"

    hide notte with dissolve
    show giovanni surprised with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_upperrightpos  
    gio "\"Audio files?\" How perplexing!  Perhaps you should fill me in on the situation..."
    hide speechright

    scene halidom_hall with fade

    show giovanni angry with dissolve

    gio "I see, I see... Indeed, this is a most complex matter.  You were wise to consult a professional of my caliber."
    play sound "audio/sound/note.wav"
    show speechright note at speechright_upperrightpos  
    gio "However, fear not!  With my assistance, we will indeed plumb the depths of the musical world together!!  {i}Coraggio{/i}, my friend!!!"
    hide speechright

    gio "But first, a change of scenery is necessary!  A musical medley is best suited for..."

    image theater = "images/backgrounds/Sty_bg_0131_100_00.png"
    show theater behind giovanni with dissolve

    gio "...THE THEATER!!!  LET THE CURTAIN RISE ON THIS, OUR INAUGURAL PERFORMANCE!!!"

    hide giovanni with dissolve
    show notte surprised shout1 with dissolve

    nott "Eeek!  Wait, now YOU can change backgrounds TOO?!  This is already getting crazy!!"

    hide notte with dissolve
    show giovanni happy with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_upperrightpos  
    gio "Ah, my fae friend, but music MUST be allowed to run wild in order for it to truly carry... {i}PASSIONE{/i}!!!"
    hide speechright

    gio "In any case, now that the stage has been set, how can I lend my services to you all?"



label tutorial_music_menu:

    show theater behind giovanni

    menu:
        "{color=#000000}Tell me the basics behind using audio!{/color}":
            show giovanni happy
            gio "Certainly!  One must always start from the basics and work upwards to greatness!"
            jump tutorial_music_giovanni_starts_explaining

        "{color=#000000}Tell me about the built-in soundtracks!{/color}":
            jump tutorial_music_musicfiles

        "{color=#000000}What kind of sound effects can I use?{/color}":
            gio "Hmm... it seems like this section hasn't been built yet.  Please be patient!"
            jump tutorial_music_soundfiles

        "{color=#000000}What kind of voice files do we have?{/color}":
            show giovanni happy
            gio "Of course!  Let us go on a tour through the wonderful world of voice acting!"
            gio "..."
            show giovanni surprised
            play sound "audio/sound/sweat.wav"
            show speechright sweat at speechright_upperrightpos  
            gio "Oh dear... it seems like we don't actually HAVE any voice files at the moment..."
            hide speechright
            gio "However!  If you have the initiative and a microphone, I am sure you and your friends can create wonderful voice lines to enrich your writing!"
            gio "...Erm... anyway, would you like to talk about something else?"
            jump tutorial_music_menu

        "{color=#000000}I can't think of anything at the moment...{/color}":
            jump tutorial_music_end







label tutorial_music_giovanni_starts_explaining:

    show giovanni closed_neutral
    gio "Now, as I understand it, there are actually three different types of audio that can be played:  {color=#FF0000}music{/color}, {color=#008000}sound{/color} and {color=#0000FF}voice{/color}."

    gio "Each of these exists as a separate 'channel,' and the three are overlaid to create the sounds that you hear."

    show giovanni happy
    gio "The {color=#FF0000}music{/color} channel is used to play dulcet melodies and set the atmosphere for various theatrical events which you may depict through this story engine."

    show giovanni angry
    gio "Meanwhile, the {color=#008000}sound{/color} channel is used to play sounds that accompany action and motion.  The swish of a sword!  The crash of an axe!  The pattering of footsteps!  All of these are a music of their own, setting the world in dynamic motion!"

    show giovanni closed_neutral
    gio "Finally, the {color=#0000FF}voice{/color} channel is used to convey spoken dialogue.  If you have the work of talented voice actors, you may use this channel to bring them to your listener's ears!"

    show giovanni open
    gio "Ah!  I must convey something important:  while the {color=#008000}sound{/color} and {color=#0000FF}voice{/color} channels play audio once and then terminate, the {color=#FF0000}music{/color} channel automatically LOOPS audio files that are played on it!"
    gio "This looping of the {color=#FF0000}music{/color} track is quite a useful feature; it allows background music to remain playing until a scripted time, since one doesn't know when the reader will advance the text."

    gio "As a result, music files in the {color=#FF0000}music{/color} channel should ideally be designed to loop, with the end connected musically back to the beginning {i}ad infinitum{/i}!"

    show giovanni happy

    gio "Such a feat of musicianship is quite invaluable for maintaining the audience's immersion, no?  The composers of Dragalia Lost have already made a variety of wonderful, atmospheric tracks that function this way."

    show giovanni closed_neutral
    gio "Now, all three of these channels can be manipulated using a number of simple commands.  To change the audio status, simply use the command word followed by the channel you wish to affect."

    gio "Let us start with the 'stop' statement, which is used to mute the given channel.  So:  simply say 'stop music' to give our theater the pregnant silence which precedes a performance!"

    menu:
        "{color=#000000}stop music{/color}":
            jump tutorial_music_stop_music

label tutorial_music_stop_music:

    hide giovanni with dissolve
    show notte surprised shout1 with dissolve

    stop music
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos  
    nott "Whoa!  It really worked!  It's almost spookily quiet now!"
    hide speechright

    hide notte with dissolve
    show giovanni surprised with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_upperrightpos  
    gio "Yes, well... that may have been a bit jarring to immediately silence the audio like that."
    hide speechright

    show giovanni happy

    gio "However, never fear!  {i}Coraggio{/i}!  There exist 'fadeout' and 'fadein' tags which can be used to modify audio commands!"
    gio "Simply follow a statement such as 'stop music' with 'fadeout' followed by a decimal number to have the audio gradually fade out over that many number of seconds."

    show giovanni closed_neutral
    gio "Likewise, the 'fadein' statement can be appended to certain commands to allow music to swell gradually from silence over a set number of seconds."

    show giovanni angry
    gio "Now...  Let us raise the curtain on this musical extravaganza!  I shall tell you how to play music!"

    gio "Playing audio is as easy as a 'play' statement!  To play it on the music track, for example, simply say \"play music\", followed by the file path in QUOTES."

    gio "I shall be your conductor!  For your first piece, you must play the title theme for Dragalia Lost with a 1-second fadein!"
    gio "The file path is \"audio/music/In A World That Never Ends (Dragalia Lost Main Theme) - Off-Vocals.mp3\"  Now, play!  Play, my budding musician!"

    menu:
        "{color=#000000}play music \"audio/music/In A World That Never Ends (Dragalia Lost Main Theme) - Off-Vocals.mp3\" fadein 1.0{/color}":
            jump tutorial_music_play_music

label tutorial_music_play_music:

    play music "audio/music/In A World That Never Ends (Dragalia Lost Main Theme) - Off-Vocals.mp3" fadein 1.0

    show giovanni open with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_upperrightpos  
    gio "YES!  BRAVO!!  BRAVISSIMO!!!  This is indeed the (vocalless) main theme of Dragalia Lost, \"In A World That Never Ends!\""
    hide speechright

    show giovanni sad
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_upperrightpos  
    gio "...although, what cruel irony!  For indeed, the world of Dragalia Lost DID end, resulting in the situation we find ourselves in presently!  Its own opening theme perjures the game's transient nature!"
    hide speechright

    hide giovanni with dissolve
    show notte grumpy pout1
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos  
    nott "Hey!  Who said anything about it ending!  Not on Notte's watch!  We're gonna keep the good times rolling even if it's just in our little pocket dimension!"
    hide speechright

    hide notte with dissolve

    show giovanni surprised
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_upperrightpos  
    gio "Ah, my apologies!  I did not mean to diminish your efforts!  Rather, I think the fleeting nature of our time together makes our memories, and indeed these moments we now spend together, even more precious!"
    hide speechright

    hide giovanni with dissolve

    show euden sad smile1 with dissolve

    eud "This is so nostalgic... This song makes me think of when I first set off on my journey.  I never thought I'd wind up making so many wonderful friends, and having such exciting experiences!"

    hide euden with dissolve
    show giovanni open with dissolve

    gio "Indeed.  The hopeful crescendos of this song are masterful, and capture that sentiment perfectly."

    show giovanni closed_neutral

    gio "Ah... Even now I remember the first time we met.  It was only a shame that we were so preoccupied with that business with Phantom Thief Lapis..."

    show giovanni sad

    gio "The shock I felt upon seeing the Halidom for the first time still remains with me... and the memory of Karina's wonderful aria brings me to the verge of tears..."

    show giovanni surprised
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_upperrightpos  
    gio "...Ah, but—my apologies!  I have forgotten myself in the throes of this music... as I am oft want to do, unfortunately..."
    hide speechright
    show giovanni open

    gio "You have, indeed, successfully used the 'play' command, which can take both 'fadein' (for the new track) and 'fadeout' (for cutting off the old track) statements."

    gio "Oh!  I must note:  the 'play' command immediately transitions out of whatever was playing before it the instant it takes effect."
    gio "This means that if you write multiple 'play' statements in sequence without any dialogue to buffer, only the last song will actually play."

    gio "If you want a song to play through in its entirety and then switch to a different song AFTER completion, that requires a different statement entirely!"

    show giovanni closed_neutral

    gio "Instead of 'play,' then, one must use the 'queue' command.  This functions just like the 'play' statement, but waits for the current audio file to finish before starting."
    gio "And of course, the 'play', 'queue' and 'stop' commands can be used independently on the each of the three audio tracks, 'music,' 'sound,' and 'voice'."

    hide giovanni with dissolve

    show notte surprised pout1 with dissolve

    nott "Wow, you sure know a lot about music!  I hope our friend can remember all that, because my brain's pretty bamboozled right now."
    nott "Do YOU need him to repeat any of that?"

    hide notte with dissolve

    show giovanni with dissolve

    gio "{i}Di certo{/i}, if there is anything you require me to go over again, I shall gladly oblige for the sake of your musicianship!"

    menu:
        "{color=#000000}No, I think I understand the 'stop,' 'play,' and 'queue' commands, and how the three audio tracks work.{/color}":
            jump tutorial_music_understand_stopplayandqueue

        "{color=#000000}Well... actually, could you maybe repeat that again?{/color}":
            show giovanni surprised with dissolve
            gio "Ah, my apologies... I have failed you as your musical mentor.  Let me start from the top, then..."
            jump tutorial_music_giovanni_starts_explaining


label tutorial_music_understand_stopplayandqueue:
    show giovanni happy with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_upperrightpos  
    gio "Good, good!  Bellissimo!  I could tell you were a quick study when I first gazed upon you!"
    hide speechright

    show giovanni angry
    gio "Yes, you shall become a true {i}virtuoso{/i} indeed!  Ha ha haaaa!!!"

    hide giovanni with dissolve
    show euden with dissolve

    eud "Thanks so much for explaining all this.  I certainly learned a lot already!"

    hide euden with dissolve
    show giovanni happy with dissolve

    gio "Of course!  It was my pleasure!  After all, it is my vocation to help spread the gift of music to the world!!"

    gio "Now, is there anything ELSE that I can help to illuminate for you?"

    jump tutorial_music_menu




label tutorial_music_musicfiles:
    scene theater
    show giovanni happy with dissolve

    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_upperrightpos  
    gio "YES, {i}DI CERTO{/i}!  I always have time to wax poetic over audio scores with those who show an interest and aptitude!!!"
    hide speechright

    play sound "audio/sound/note.wav"
    show speechright note at speechright_upperrightpos  
    gio "As for you, my new friend, I knew right away that I was speaking with a kindred spirit!!"
    hide speechright

    gio "In that case, let us first go over songs with several story variations!"

    show giovanni open
    gio "Now, one of the first things you should know is that many of the songs from the Dragalia Lost story soundtrack come from a talented Japanese artist named DAOKO."

    show giovanni closed_neutral
    gio "In fact, the title theme you just played, \"In A World That Never Ends,\" was performed by DAOKO, and the same goes for many of the upcoming songs as well."

    show giovanni sad
    gio "Of course, it is a tragedy of the highest level that you will be unable to listen to DAOKO's wonderful voice.  After all, her signature whisper-like raps have a unique tenderness to them which is utterly pleasant and draws the listener in!"
    gio "I cannot play them here for reasons Euden has explained to me, but I encourage you to listen to the vocal versions of the songs and support DAOKO's releases!"

    show giovanni open
    gio "In any case, I shall lead off with a tune which will be nostalgic to many fans of the Dragalia Lost mobile game—\"CRASHER\"!"



    show giovanni closed_neutral
    gio "\"CRASHER\" by DAOKO, the theme which accompanied the heart-pounding High Dragon Trials, is a multifarious piece which lends itself well to a number of different adaptations."

    play music "audio/music/CRASHER (Story Version A) loop.mp3" fadeout 1.0
    gio "This adaptation, \"CRASHER (Story Version A)\", creates an emotional and vulnerable mood with its gentle, swelling string section crescendos while chimes play the familiar melody.  You can find it under the file name \"CRASHER (Story Version A) loop.mp3\"."

    play music "audio/music/CRASHER (Story Version B) intro.flac" fadeout 1.0
    queue music "audio/music/CRASHER (Story Version B).flac"
    gio "This version, \"CRASHER (Story Version B).flac\", in contrast, creates a sense of oppression or ominousness through its heavy piano chords and slow tempo.  For best results, {i}queue{/i} it after {i}play{/i}ing the intro file \"CRASHER (Story Version B) intro.flac\"."

    play music "audio/music/CRASHER (Story Version C) intro.flac" fadeout 1.0
    queue music "audio/music/CRASHER (Story Version C).flac"
    gio "Finally, this version, \"CRASHER (Story Version C).flac\" is closest to the feeling of the original battle theme, with fast-paced, pulsing synths.  It's a great pick for action sequences!  For best results, {i}queue{/i} it after {i}play{/i}ing the intro file \"CRASHER (Story Version C) intro.flac\"."


    gio "Of course, CRASHER has a number of different settings besides the ones labelled \"Story Version!\""

    play music "audio/music/CRASHER (Story Bout C).flac" fadeout 1.0
    gio "For instance, this setting, \"CRASHER (Story Bout C).flac\", is a battle theme that keeps most of the energy of Story Version C but with more tension and urgency provided by the quick arpeggios and more classical instrumentation, with the melody played by flute."

    play music "audio/music/CRASHER Mana Circles loop.mp3" fadeout 1.0
    gio "This version, used for the mana circles menu, can be used to convey an air of mystery and magic.  Its synthesized, drawn-out notes create a buzzing, electric atmosphere.  You can find it under the file name \"CRASHER Mana Circles loop.mp3\"."

    play music "audio/music/CRASHER - Failure loop.mp3" fadeout 1.0
    gio "This version, used after quitting a quest in-game, conveys a sense of disappointment and brooding.  The deep piano bass chords create a sense of heaviness, while the lilting rendition of the familiar melody creates a sense of limping and fragility.  You can find it under the file name \"CRASHER - Failure loop.mp3\"."



    play music "audio/music/BANG (Story Version A) intro.flac" fadeout 1.0
    queue music "audio/music/BANG (Story Version A).flac"
    show giovanni open
    gio "Next is \"BANG\" by DAOKO, which is the famous (or maybe infamous, depending on your luck) jaunty tune which accompanied summoning in the game!  Although it seems cutesy, the lyrics are actually surprisingly dark and contain mature themes..."
    show giovanni closed_neutral
    gio "This version you're hearing, \"BANG (Story Version A).flac\", is accompanied by a percussive intro.  It follows the song's refrain and is often used in-game to denote celebrations or excitement.  For best results, {i}queue{/i} it after {i}play{/i}ing the intro file \"BANG (Story Version A) intro.flac\"."

    play music "audio/music/BANG (Story Version B) intro.flac" fadeout 1.0
    queue music "audio/music/BANG (Story Version B).flac"
    gio "In contrast, this rendition, \"BANG (Story Version B).flac\", is slightly more playful and comedic, with a more muted melody that replicates the background track of \"BANG\"'s verses.  For best results, {i}queue{/i} it after {i}play{/i}ing the intro file \"BANG (Story Version B) intro.flac\"."


    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadeout 1.0
    gio "This song, based on the song Cinderella Step, is called \"Cinderella Step (Story Version A) loop.mp3\".  It has a playful quality and features flutes and horns to create a whimsical, silly atmosphere perfect for humorous moments."




    play music "audio/music/Yumemiteta no Atashi (Story Version A) intro.flac" fadeout 1.0
    queue music "audio/music/Yumemiteta no Atashi (Story Version A).flac"
    gio "This track, matching the verses of Yumemiteta no Atashi by DAOKO, is named \"Yumemiteta no Atashi (Story Version A).flac\".  Its quiet, brooding synths with a bluesy feel is perfect for contemplative sections.  For best results, {i}queue{/i} it after {i}play{/i}ing the intro file \"Yumemiteta no Atashi (Story Version A) intro.flac\"."

    play music "audio/music/Yumemiteta no Atashi (Story Version B).flac" fadeout 1.0
    gio "This track, following Yumemiteta no Atashi's CHORUS, is named \"Yumemiteta no Atashi (Story Version B).flac\".  Unlike its more moody and atmospheric partner, this track features bright, optimistic piano and an uptempo feel to inspire hope and courage."



    play music "audio/music/24h (Story Version) intro.flac" fadeout 1.0
    queue music "audio/music/24h (Story Version).flac"
    gio "This song is a background music rendition of 24h by DAOKO named \"24h (Story Version).flac\".  Its celebratory electronic fanfares couple nicely with bass slaps to create a suave, intimate and festive feeling.  For best results, {i}queue{/i} it after {i}play{/i}ing the intro file \"24h (Story Version) intro.flac\"."



    play music "audio/music/Utopia.flac" fadeout 1.0
    gio "This song, \"Utopia.flac\" is also by DAOKO.  Its upbeat chimes and waltz-like meter are perfect for happy moments, especially establishing moments in a story that set up the status quo."



    play music "audio/music/Kibou no Oto (Sound of Hope) - Off-Vocals.mp3" fadeout 1.0
    gio "This song, Kibou no Oto, is an original made by DAOKO for Dragalia Lost.  This vocalless version, \"Kibou no Oto (Sound of Hope) - Off-Vocals.mp3\", creates an air of mystery and urgency with its soft piano and chimes.  It's perfect for moments where deep-seated truths or hidden potentials are uncovered."


    play music "audio/music/New Alberia.flac" fadeout 1.0
    gio "This song, New Alberia, is another Daoko original for Dragalia Lost.  This soundtrack (\"New Alberia.flac\"), evoking a dramatic decision, features heavy piano chords in a minor key, an urgent tempo and several meter changes."


    play music "audio/music/Threatening Aura intro.flac" fadeout 1.0
    queue music "audio/music/Threatening Aura.flac"
    gio "This song, \"Threatening Aura.flac\", features oppressive, aggressive string notes accompanied by a shouting, dissonant choir to create... well, a 'threatening aura.'  For best results, {i}queue{/i} it after {i}play{/i}ing the intro file \"Threatening Aura intro.flac\"."


    play music "audio/music/gentle dawn temp intro.flac" fadeout 1.0
    queue music "audio/music/gentle dawn temp.flac"
    gio "This song, \"gentle dawn temp.flac\", features soft, hopeful piano, evoking a sunrise or quiet tranquility.  I'm... not sure if this comes from an existing Daoko song or not, so I've named it 'gentle dawn' temporarily.  For best results, {i}queue{/i} it after {i}play{/i}ing the intro file \"gentle dawn temp intro.flac\"."






    show giovanni open
    gio "Now, let's get into songs by some other artists.  DAOKO is but one of many artists that have contributed to the soundtrack of \"Dragalia Lost\"."

    play music "audio/music/Kaede (Maple Leaf) - Off-Vocals loop.mp3" fadeout 1.0
    gio "This song, Kaede (meaning \"maple leaf\"), was a cover performed by Lucretzia for the Resplendent Refrain event.  The swelling guitar chords in this file (\"Kaede (Maple Leaf) - Off-Vocals loop.mp3\") that slowly build up to an emotional climax are perfect for heartfelt moments."

    play music "audio/music/BGM (Arikitari)  WON Dragalia Lost - One Starry Dragonyule.mp3" fadeout 1.0
    gio "This song, Arikitari, is by the artist WON for the Dragalia Lost event One Starry Dragonyule.  Its upbeat guitar riffs intermixed with quiet moments evoke the exhiliration of flying through the snow on a snowboard.  Access it under the filename \"BGM (Arikitari)  WON Dragalia Lost - One Starry Dragonyule.mp3\"."


    show giovanni happy
    gio "Well, that represents all the music files currently built into this Story Engine.  Hopefully you've stumbled upon something that stirs your heart and soul with the joy of music!"


    jump tutorial_music_menu


label tutorial_music_soundfiles:
    scene theater
    jump tutorial_music_menu


label tutorial_music_end:

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadeout 1.0 fadein 1.0

    show giovanni sad with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_upperrightpos  
    gio "Ah, I see.  Unfortunate, but I suppose we have already spent quite a while talking."
    hide speechright
    gio "Ah, how the time flies, never to return!"

    show giovanni closed_neutral
    gio "In any case, I hope I have clarified most of your questions!  Do not hesitate to summon me if you have need!"
    gio "In the meantime, I must prepare for my next great performance!  {i}Arrivederci, miei adorabili amici{/i}!"

    hide giovanni with dissolve
    scene halidom_hall with fade

    show notte sad smile3 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    nott "Whew, what a wild ride!  I never thought I'd learn that much about music just from an offhand comment..."
    hide speechright

    hide notte with dissolve
    show euden closed_relaxed with dissolve
    eud "Yeah, but everything Giovanni told us was extremely helpful!  I can't wait to start playing around with music again."

    show euden relaxed
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos  
    eud "Maybe I'll finally take up piano again!  I'm suddenly inspired to start making some of my OWN music!"
    hide speechright

    show euden focused
    eud "Well, I'm gonna go track it down.  Thanks for stopping by again, friend!  Hope you learned as much as I did!"


    stop music fadeout 3.0



    # This goes back to script

    jump tutorialmenu



label tutorial_implementing_characters:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "audio/music/Utopia.flac" fadeout 1 fadein 1.0

    scene halidom_hall with dissolve

    show euden with dissolve

    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos  
    eud "Ah, sorry, DabblerDragon hasn't written this part yet!  But he has a channel explaining how to do it in the Dragalia Lost Story Engine discord!"
    hide speechright
    eud "Oh, also, some miscellaneous things:  DabblerDragon's figured out how to do some basic animation stuff."
    eud "It seems like you need to actively crop the white space out of character portraits because they currently occupy the same space as the screen."
    eud "So even if you try to make the portrait move, it's locked in place by the pixel limits.  (Ren'py doesn't like moving images over the edge of the screen, I guess?)"
    eud "Anyway, if you want to define an animation for a cropped image, you can look at some of the examples, like the ones for Finni and Eirene."
    eud "To make an animation you have to define a 'transform.'  You can define the coordinates with 'xalign' and 'yalign'."
    eud "To make a linear movement, say 'linear' with a time duration followed by 'xalign' to the new x pos and 'yalign' to the new ypos."
    eud "You can also use statements like 'zoom' in the transform to change the size of an image!"
    eud "With color matrices, you can even change the coloration of an image!  Check out the 'sepia' transform dabblerdragon defined!"
    eud "In addition to these topics, please let DabblerDragon know what topics you want this tutorial to cover!  It's still very much a work in progress!"
    eud "For now, thanks for trying out Dragalia Lost Story Engine!  We hope you'll be able to use this to let your imagination run wild and have a fresh encounter with your favorite characters."

    stop music fadeout 1.0

    # This goes back to script

    jump tutorialmenu
