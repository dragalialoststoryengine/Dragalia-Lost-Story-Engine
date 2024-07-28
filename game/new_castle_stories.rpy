
transform sepia:
    matrixcolor SepiaMatrix(tint=u'#ffeec2', desat=(0.2126, 0.7152, 0.0722))





label newcastlestoriesmenu:


    play music "audio/music/Utopia loop.mp3" fadeout 1

    image wagabondpupper_bg = "images/backgrounds/wagabondpupperbg.png"
    scene wagabondpupper_bg with fade

    menu:
        "What short do you want to read?"

        "{color=#000000}001 - Gotta See!  Gotta Know!  Berserker's True Face!{/color}":
            jump berserkerstrueface


        "{color=#000000}Main Menu{/color}":
            stop music fadeout 1.0
            jump start










# The game starts here.
label berserkerstrueface:

    play music "audio/music/Utopia loop.mp3" fadeout 1.0

    image greathall_night = "images/backgrounds/Sty_bg_0072_300_00.png"
    scene greathall_night with fade

    show cleo at walk_in_left
    cle "I was told that I needed to make a fresh pot of stew, but I put out the first tureen less than fifteen minutes ago.  Who could possibly...?"

    show cleo glare pout1
    show speechright anger at speechright_pos
    play sound "audio/sound/anger.wav"
    cle "...Oh, of course.  It's you two."
    hide speechright
    hide cleo with dissolve

    show luca sad sweat with dissolve
    luc "H-Heyyy, Cleo...  Guess we went overboard again..."
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    show luca relaxed_closed
    luc "...Uhhhh... it was just so delicious, we couldn't stop eating...?"
    hide speechright
    hide luca with dissolve

    show ranzal wink with dissolve
    ranz "Y-You got that right, this might be yer best work yet.  You really made the magic happen with that..."
    show ranzal surprised mutter1
    ranz "...uh... sage you added."
    hide ranzal with dissolve

    show cleo glare with dissolve
    cle "Wrong."
    hide cleo with dissolve
    
    show ranzal flinch grimace1 with dissolve
    ranz "...O-Of course not, I meant to say... basil?"
    hide ranzal with dissolve
    
    show cleo closed_focused with dissolve
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"
    cle "Even more wrong.  Clearly you shovelled it down so fast you didn't stop to taste it properly."
    hide speechright
    show cleo glare
    cle "When you overeat, everyone in the Halidom suffers. The two of you had better hunt down some choice game tomorrow to make up for this."
    hide cleo with dissolve

    show ranzal shocked grimace1 with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    ranz "Hang on, in case yer math is off, there's four of us at the table here.  Why are Elly and Berserker magically exempt from this?"
    hide speechright
    hide ranzal with dissolve

    show elisanne closed_neutral frown1 with dissolve
    show elisanne at disagree_shake
    elly "That is because Cleo knows I eat in proper proportion to my needs."
    hide elisanne with dissolve

    show berserker askance with dissolve
    bers "And I was merely stopping by to be polite.  I'm actually returning the empty bowl of stew I ate earlier."
    show berserker neutral at bigger_dip
    bers "Excellent as always, Cleo.  The rosemary added some wonderful flavor."
    hide berserker with dissolve

    show ranzal flinch shout1 with dissolve
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"
    ranz "Oh, of course, NOW you step in with that tidbit!  Thanks for letting me struggle back there!"
    hide speechright
    hide ranzal with dissolve

    show berserker with dissolve
    show berserker at laugh_bob
    bers "Heh heh!  My apologies.  Fear not, it would be my pleasure to join you on the hunt tomorrow."
    show berserker glint
    bers "Let us take down a beast large and fierce enough that we may boast uproariously tomorrow!"
    show berserker downcast
    bers "But for now, I must adjourn.  Today's march home has left me quite spent."
    show berserker at walk_out_left
    pause 1.5

    show luca focused frown1 with dissolve
    luc "...Hmm... You know, I don't think I've ever seen Berserker eat or drink before."
    show luca relaxed_closed
    show speechright question at speechright_pos
    play sound "audio/sound/question.wav"
    luc "For that matter, I've never even seen him with his helmet off.  Have you guys?"
    hide speechright
    hide luca with dissolve

    show cleo surprised with dissolve
    cle "...Now that you mention it, he's complimented me for the food, but he always eats in private and returns the dishes."
    show cleo sad
    cle "He seems to enjoy my cooking, but it suppose it would be nice to witness him enjoying it firsthand."
    hide cleo with dissolve

    show elisanne surprised frown1 with dissolve
    show speechright exclamation at speechright_pos
    play sound "audio/sound/exclamation.wav"
    elly "Come to think of it, I have likewise never seen him in anything save his full plate mail!"
    hide speechright
    show elisanne neutral
    elly "Ranzal, I believe you knew him during your stint as a mercenary.  What does Berserker look like underneath his armor?"
    hide elisanne with dissolve

    show ranzal neutral mutter1 with dissolve
    pause 0.5
    show ranzal at disagree_shake
    ranz "Yer guess is as good as mine.  For someone who's got guts like crazy on the battlefield, he's weirdly shy about showing some skin."
    show ranzal closed_neutral
    ranz "But then again, being a merc's a hard life; almost everybody picks up some quirks and habits after a while."
    show ranzal squint grimace2
    ranz "Man's probably got some nasty scars he's too polite to show.  Heck, given how he fights, he's probably covered in gashes."
    show ranzal focused mutter1 at agree_dip
    ranz "I'm sure he's just looking out for squeamish folks, or else he's avoiding pity glances for his war wounds."
    hide ranzal with dissolve

    show cleo with dissolve
    cle "But that's just your opinion, yes?  So we don't know for sure."
    cle "Off the battlefield, he's a proper gentleman.  It's equally likely he could be beguilingly handsome."
    show cleo blush_askance shout1
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    show cleo at disagree_shake
    cle "...Not that I'm interested in him that way!  He's much too war-crazy for my taste."
    hide speechright
    show cleo mutter1
    cle "I'm just inclined to envision him as more attractive than a human pincushion."
    hide cleo with dissolve

    show elisanne blush pout1 with dissolve
    show speechright exclamation at speechright_pos
    play sound "audio/sound/exclamation.wav"
    elly "Oh, so you think he's that rugged, stoic sort of handsome?"
    show elisanne smile1
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    elly "I-It's also not my place to comment on such things, but I must admit that the mystery has piqued my curiosity a little..."
    hide speechright
    hide elisanne with dissolve

    show ranzal squint mutter1 with dissolve
    ranz "Oh, come on, there's no way he's that attractive.  I'm confident that the guy looks like swiss cheese, so cool it, ladies."
    hide ranzal with dissolve

    show cleo relaxed smile1 with dissolve
    show cleo at laugh_bob
    cle "Hm hm, do I detect a hint of jealousy in your tone?  Maybe you're worried he's more handsome than you."
    hide cleo with dissolve

    show ranzal squint shout1 with dissolve
    show speechright anger at speechright_pos
    play sound "audio/sound/anger.wav"
    ranz "L-Like hell I am!"
    hide speechright
    hide ranzal with dissolve

    show luca relaxed_closed frown1 with dissolve
    luc "No way, nobody hides their face that religiously unless they've got something to hide."
    show luca neutral luca_grin1
    show speechright note at speechright_pos
    play sound "audio/sound/note.wav"
    show luca at laugh_bob
    luc "I bet he's got a really embarrassing birthmark on his face.  Or a snaggle tooth!"
    hide speechright
    hide luca with dissolve

    show elisanne focused pout1 with dissolve
    elly "Oh, come now, Luca!  That's not nice to say!"
    show elisanne closed_neutral at disagree_shake
    elly "I bet he's just really pale, so he covers up to avoid getting sunburnt."
    hide elisanne with dissolve

    show ranzal angry frown1 with dissolve
    ranz "Ya gotta be kidding.  A guy that takes severe beatings on the regular, afraid of a little sunburn?  That theory's just plain dumb."
    hide ranzal with dissolve

    show cleo angry frown1 with dissolve
    cle "Well, it's not like your theory makes any more sense!  The man's obsessed with battle, wouldn't he be PROUD of his scars?"
    hide cleo with dissolve

    show luca relaxed_closed grin1 with dissolve
    show luca at laugh_bob
    luc "Guys, guys, calm down.  There's an easy way to solve this argument."
    hide luca with dissolve

    show elisanne surprised frown1 with dissolve
    show speechright question at speechright_pos
    play sound "audio/sound/question.wav"
    elly "Oh?  What, praytell, is your proposal?"
    hide speechright
    hide elisanne with dissolve

    show luca relaxed grin1 with dissolve
    luc "Easy.  We just have to get Berserker to take his helmet off."
    hide luca with dissolve

    show ranzal neutral grin1 with dissolve
    show ranzal at laugh_bob
    ranz "Ha!  Good luck with that.  I've known him for years and I still don't even know the color of his skin."
    hide ranzal with dissolve

    show cleo with dissolve
    cle "And is this even something we ought to be prying into?  I'm sure he has reasons to maintain his privacy."
    hide cleo with dissolve

    show elisanne focused frown2 with dissolve
    pause 0.5
    show elisanne at disagree_shake
    elly "Th-That's right!  Surely it would be more mature to let the matter rest."
    hide elisanne with dissolve

    show luca askance grin1 with dissolve
    luc "Well, ok, if you say so..."
    show luca grin1_closed
    luc "..."
    hide luca with dissolve

    show cleo sad mutter1_closed with dissolve
    cle "..."
    hide cleo with dissolve

    show elisanne frown1_closed with dissolve
    elly "..."
    hide elisanne with dissolve

    show ranzal closed_frown1 with dissolve
    ranz "..."
    show ranzal frown1 at disagree_shake
    ranz "...Ok, to hell with being mature, we've gotta get to the bottom of this."
    hide ranzal with dissolve

    show cleo focused at appear_left
    show elisanne closed_neutral frown1 at appear_right
    show luca with dissolve
    elly "I agree, Ilia forgive me but I simply must know."
    cle "Thank goodness, it's not just me."
    luc "I couldn't even buy the words as they were coming out of my mouth."
    show elisanne at disappear_right
    show cleo at disappear_left
    hide luca with dissolve
    hide elisanne
    hide cleo

    show ranzal frown1 with dissolve
    ranz "As it happens, I actually have an idea that might have a shot.  Here's the plan..."
    hide ranzal with dissolve



    image foreststream_night = "images/backgrounds/Sty_bg_0074_300_00.png"
    scene foreststream_night with fade


    show berserker at walk_in_right
    pause 1.0
    show speechright question at speechright_pos
    play sound "audio/sound/question.wav"
    bers "...Is there a particular reason you've brought me here in your swimming trunks?"
    hide speechright
    hide berserker with dissolve

    show sranzal at walk_in_right
    ranz "Well, of course.  You said you were worn out earlier, and as yer buddy, I couldn't just ignore that, now, could I?"
    ranz "So I figured I'd treat you to one of my new favorite passtimes:  a hot springs bath!"
    hide sranzal with dissolve

    show berserker surprised with dissolve
    bers "Hot springs?  I was unaware that the Halidom had such amenities.  And is this not just a regular pond?"
    hide berserker with dissolve

    show sranzal relaxed smile1 with dissolve
    ranz "Well, about that... I'm really just cashing in a favor from my big ol' pal Kagutsuchi over there."
    hide sranzal with dissolve

    show kagutsuchi with dissolve
    kagut "Ah, hello, Ranzal!  Come in, the water is clean and pure!"
    hide kagutsuchi with dissolve

    show berserker with dissolve
    bers "Ah, I see.  The dragon's heat warms the surrounding water."
    show berserker surprised
    bers "But... is that really all there is to this invitation?"
    hide berserker with dissolve

    show sranzal surprised grin2 with dissolve
    ranz "What, you think I have some motive other than helping one of my best buds?"
    hide sranzal with dissolve



    image woods_night = "images/backgrounds/Sty_bg_0021_300_00.png"
    scene woods_night with fade

    show elisanne blush pout1 with dissolve
    elly "Ohh... this feels really wrong...  Ought we truly to stoop to the level of base voyeurs hiding in bushes?"
    hide elisanne with dissolve

    show luca askance mutter1 with dissolve
    luc "Do you want to find out what Berserker looks like or not?  Now shhh!  He'll hear us if you're too loud!"
    hide luca with dissolve

    show cleo focused with dissolve
    cle "Agreed.  There's no reason to feel abashed, we'll simply leave as soon as he takes off his helmet."
    hide cleo with dissolve



    scene foreststream_night with fade

    show berserker with dissolve
    bers "Surely this invitation isn't a comment on my personal hygiene, is it?"
    hide berserker with dissolve
    
    show sranzal closed_neutral with dissolve
    show sranzal at laugh_bob
    ranz "Hehe, no, of course not.  I just figured you'd appreciate a good soak.  I always find this the best way to relieve tension."
    hide sranzal with dissolve

    show berserker askance with dissolve
    bers "Hmm... I suppose I do need to be rested and refreshed for tomorrow's outing..."
    show berserker 
    bers "Still, I generally prefer to bathe in my quarters.  Is this dragon-bath truly something special?"
    hide berserker with dissolve

    show sranzal with dissolve
    ranz ""







    scene black with fade
    show text "{color=ffffff}{i}The End{/i}{/color}" at middle with dissolve
    pause 20.0

    jump newcastlestoriesmenu
