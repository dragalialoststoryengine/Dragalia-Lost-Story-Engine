
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

    play music "audio/music/Utopia loop.mp3" fadein 1.0

    image greathall_night = "images/backgrounds/Sty_bg_0072_300_00.png"
    scene greathall_night with fade

    show cleo at walk_in_left
    cle "I was told that I needed to make a fresh pot of stew, but I just put out the first tureen not fifteen minutes ago.  Who could possibly...?"

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
    ranz "Oh, of course, NOW you step in with that herbal tidbit!  Thanks for letting me struggle back there!"
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
    elly "Oh?  What, pray tell, is your proposal?"
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

    show elisanne focused frown2 at disagree_shake with dissolve
    elly "Th-That's right!  Surely it would be more mature to let the matter rest."
    hide elisanne with dissolve

    show luca askance grin1 with dissolve
    luc "Well, ok, if you say so..."
    show luca frown1_closed
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
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"
    show ranzal frown1 at disagree_shake
    ranz "...Ok, to hell with being mature, we've gotta get to the bottom of this."
    hide speechright
    hide ranzal with dissolve

    show cleo focused at appear_left
    show elisanne closed_neutral frown1 at appear_right
    show luca with dissolve
    elly "I agree, Ilia forgive me but I simply must know."
    cle "Thank goodness, I thought I was the only one who was desperate for answers."
    luc "Yeah, I couldn't even buy the words as they were coming out of my MOUTH."
    show elisanne at disappear_right
    show cleo at disappear_left
    hide luca with dissolve
    hide elisanne
    hide cleo

    show ranzal frown1 with dissolve
    show speechright lightbulb at speechright_pos
    play sound "audio/sound/inspiration.wav"
    ranz "As it happens, I actually have an idea that might have a shot."
    hide speechright
    ranz "Here's the plan..."
    hide ranzal with dissolve


    # play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadeout 1.0
    play music "audio/music/BANG (Story Version B) intro.flac" fadeout 1.0
    queue music "audio/music/BANG (Story Version B).flac"


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
    ranz "Well, about that... I'm really just cashing in a favor from my ol' pal Kagutsuchi over there."
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
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    ranz "What, you think I have some motive other than helping one of my best buds?"
    hide speechright
    hide sranzal with dissolve



    image woods_night = "images/backgrounds/Sty_bg_0021_300_00.png"
    scene woods_night with fade


    show elisanne blush pout1 with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    elly "Ohh... this feels really wrong...  Ought we truly to stoop to the level of base voyeurs hiding in bushes?"
    elly "They're about to bathe, for the Goddess's sake!"
    hide speechright
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
    show berserker neutral
    bers "Still, I generally prefer to bathe in my quarters.  Is this dragon-bath truly something special?"
    hide berserker with dissolve

    show sranzal with dissolve
    ranz "It's the best, I'm tellin' ya!  It soothes injuries, reduces aches... it's all-around invigoratin'!"
    show sranzal closed_neutral
    show speechright note at speechright_pos
    play sound "audio/sound/note.wav"
    ranz "Plus, afterwards, when you're all warmed up, you can have some cold milk, and... whew, man, it's tops!"
    hide speechright
    hide sranzal with dissolve

    show berserker askance with dissolve
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"
    bers "Hmm... I am embarrassed to admit, but milk does not actually agree with me..."
    bers "I do apprecate the gesture, but perhaps I should simply retire early..."
    hide speechright
    hide berserker with dissolve

    show sranzal surprised mutter1_closed with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    ranz "(Drat!  I'm losin' him!  Time to bring out the big guns...)"
    # show speechright lightbulb at speechright_pos
    # play sound "audio/sound/inspiration.wav"
    show sranzal closed_neutral grin1
    hide speechright
    ranz "Oh, well.  If you're sure.  Maybe it's for the best."
    show speechright note at speechright_pos
    play sound "audio/sound/note.wav"
    show sranzal focused
    ranz "After all, facing the heat of a dragon can be a little... intense."
    hide speechright
    hide sranzal with dissolve

    show berserker surprised with dissolve
    show speechright exclamation at speechright_pos
    play sound "audio/sound/exclamation.wav"
    bers "...!"
    hide speechright
    hide berserker with dissolve

    show sranzal focused grin1 with dissolve
    ranz "Yeah, when it comes to the power of flame, Kagutsuchi's no pushover."
    show sranzal closed_neutral
    show sranzal at sink_down
    play sound "audio/sound/splash small.mp3"
    ranz "Yyyyup, even just his ambient heat in the water can be a little extreme for some people."
    ranz "So if it's not your cup 'o tea, I totally get—"
    hide sranzal with dissolve

    show berserker with dissolve
    show berserker burn
    bers "Very well, allow me to join you after all!"
    stop music fadeout 1.0
    play sound "audio/sound/splash big.mp3"
    show berserker at jump_down
    bers "Ha ha ha!!!"
    hide berserker with dissolve

    show sranzal shocked shout1 with dissolve
    show speechright exclamation at speechright_pos
    play sound "audio/sound/exclamation.wav"
    ranz "(splutter) Wh-Whoa, man!  You're really gonna do this in full plate armor—?!"
    hide speechright
    hide sranzal with dissolve

    play music "audio/music/CRASHER (Story Version C) intro.flac" fadeout 1.0
    queue music "audio/music/CRASHER (Story Version C).flac"

    show berserker burn with dissolve
    bers "Come, dragon!  Are the waters stoked by your flames truly so tepid?!"
    show berserker burn2
    bers "Only a brilliant heat can warm these frigid bones of mine!!"
    hide berserker with dissolve

    show kagutsuchi with dissolve
    show speechright anger at speechright_upperrightpos
    play sound "audio/sound/anger.wav"
    kagut "Hmph.  As you wish."
    hide speechright
    hide kagutsuchi with dissolve

    show sranzal surprised frown1 with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    ranz "Uhh... for the record, I don't have any issue with the current temperature, guys..."
    hide speechright
    show sranzal shocked frown1
    ranz "—Hey, it's getting a little hot in here..."
    show sranzal shout1
    show speechright exclamation at speechright_pos
    play sound "audio/sound/exclamation.wav"
    play sound "audio/sound/steam.mp3"
    image fog = "images/effects/fog.png"
    show fog zorder 99 with dissolve
    ranz "OW!  OW!  Seriously?!?  We're gonna boil at this rate!!!"
    hide speechright
    hide sranzal with dissolve

    show berserker burn2 with dissolve
    show berserker at laugh_bob
    bers "Wa-hahaha!!!  That's more like it!  Shall we see who can stay in the longest, Ranzal?!"
    hide berserker with dissolve

    
    scene woods_night with fade

    show cleo frown1 at appear_left
    show elisanne frown1 at appear_right
    show luca frown1 with dissolve

    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"

    luc "Well... That was a bust.  Shoulda known, it was a Ranzal plan after all."
    luc "Even IF Berserker took off his armor at this point, I can't see anything through all that steam."
    hide speechright
    elly "Poor Ranzal... Cleo, are you perchance able to heal him?"
    cle "Not from this vantage point; we'd be spotted!"

    show luca surprised
    show elisanne surprised
    show cleo surprised

    ranz "SOMEONE HELP!!  THE SIDES ARE TOO HOT TO CLIMB OUT!!!"
    ranz "I'M TRAPPED IN BOILING WATER WITH A MANIAC!!!  COME ON, GUYS!!!"

    elly "...We should leave, lest he implicate us in this fiasco."
    show elisanne at disappear_right

    cle "I rather thought this matter needed a woman's touch, anyway."
    show cleo at disappear_left

    luc "...Yup, let's bail before Ranzal blows our cover."
    hide luca with dissolve

    bers "HAHAHAHA!!!  I FEEL ALIVE!!!"

    ranz "WELL, I FEEL LIKE I'M DYING!!!  SOMEBODY SAVE ME!!!"

    stop music fadeout 1.0

    image greathall_morning = "images/backgrounds/Sty_bg_0072_100_00.png"
    scene greathall_morning with fade

    play music "audio/music/Utopia loop.mp3"

    show luca relaxed_closed mutter1 at walk_in_right
    luc "(Yawn) Good morning, Cleo.  Anything good for breakfast?"
    hide luca with dissolve

    show cleo focused2 with dissolve
    cle "Ah, look who finally decided to wake up."
    show cleo focused
    cle "Here, we have a spread of oatmeal, Hinamotoan rice porridge, applesauce, orange juice, coffee, tea..."
    hide cleo with dissolve

    show luca surprised frown1 with dissolve
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"
    luc "...Uh... is there anything less... liquid-y?"
    hide speechright
    hide luca with dissolve

    show elisanne pained frown1 with dissolve
    elly "Luca!  Don't tell me you've already forgotten the plan."
    hide elisanne with dissolve

    show luca surprised mutter1 with dissolve
    show speechright lightbulb at speechright_pos
    play sound "audio/sound/inspiration.wav"
    luc "Ohhh, right, my bad!  Which reminds me, where is..."
    hide speechright
    hide luca with dissolve

    show ranzal angry closed_frown1 at walk_in_right
    play sound "audio/sound/steam.mp3"
    image fog = "images/effects/fog.png"
    show fog zorder 99 with dissolve
    hide fog with dissolve
    ranz "..."
    hide ranzal with dissolve

    show luca shocked frown2 with dissolve
    luc "Oh man, you look like a lobster!"
    hide luca with dissolve
    
    show ranzal angry grimace1 with dissolve
    show speechright anger at speechright_pos
    play sound "audio/sound/anger.wav"
    ranz "Why, I oughta clobber you!"
    ranz "I can't believe you guys bailed on me after I put myself in the literal hot seat for you."
    ranz "My skin's gonna be peeling for weeks!!"
    hide speechright
    hide ranzal with dissolve

    show elisanne focused pout1 with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    elly "Well, how, praytell, were we supposed to explain the fact that we were spying on your bath?"
    hide speechright
    show elisanne surprised
    elly "—Shh!  He's coming!  We're moving forward with Cleo's plan next!"
    hide elisanne with dissolve

    show berserker surprised at walk_in_right
    show speechright note at speechright_pos
    play sound "audio/sound/note.wav"
    bers "Ah, good morning, my compatriots!"
    show berserker at laugh_bob
    bers "Ha ha, Ranzal, you genius!  Your dragon-heated steam bath was absolutely brilliant!  I've never slept better!"
    bers "Might we partake in another after our hunt today?"
    hide speechright
    hide berserker with dissolve

    show ranzal closed_neutral grimace1 with dissolve
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"
    ranz "Ah, right, I almost forgot that I have to go trudging through the woods all day like this."
    ranz "Thanks for that, Cleo..."
    hide speechright
    hide ranzal with dissolve

    show berserker surprised with dissolve
    show speechright question at speechright_pos
    play sound "audio/sound/question.wav"
    bers "My, Cleo, today's breakfast seems different than your usual.  I was rather looking forward to your scrambled eggs and bacon."
    hide speechright
    hide berserker with dissolve

    show cleo zorder 50 with dissolve
    show speechright sweat zorder 51 at speechright_pos
    play sound "audio/sound/sweat.wav"
    cle "Ah, well, I did tell you yesterday evening that I was running low on ingredients..."
    hide speechright

    image black = "images/backgrounds/black.png"
    show black zorder 00 with dissolve
    show cleo focused2 mutter1_closed
    cle "(But mostly, if I put out solid food, you could potentially push it underneath your helmet and eat it that way!)"
    cle "(I won't let you get away that easily!)"

    hide black with dissolve
    show cleo closed_focused smile1
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    cle "So, only porridge today, unfortunately."
    cle "In fact, I may join you boys on your hunt this afternoon to do some foraging, ha ha..."
    hide speechright
    hide cleo with dissolve

    show berserker with dissolve
    bers "Hmm... and only one bowl and spoon left.  Well, I suppose I should help myself."
    show berserker at bigger_dip
    bers "Thank you for the meal; I shall take this to my room and return my dishes later."
    hide berserker with dissolve

    show cleo surprised with dissolve
    cle "Are you certain?  Surely it would be more enjoyable while it's still piping hot."
    hide cleo with dissolve

    show lowen at run_in_right
    low "Miss Cleo!  Am I too late for breakfast?"
    hide lowen with dissolve

    show cleo with dissolve
    show cleo at disagree_shake
    cle "I'm sorry, Lowen, but the last bowl was just taken.  You'll need to wait until someone turns theirs in."
    hide cleo with dissolve

    show lowen sad frown2 with dissolve
    low "Aw..."
    show lowen surprised smile2
    low "Hi, Berserker!  Please finish up fast, ok?  That way I can eat too!"
    hide lowen with dissolve

    show cleo with dissolve
    cle "Well, Berserker was just about to take his food to his room, actually, so it may take a while."
    hide cleo with dissolve

    show lowen sad frown2 zorder 50 with dissolve
    low "Aw... but that might take forever..."

    show black zorder 00 with dissolve
    show lowen focused closed_smile1
    show speechright note zorder 52 at speechright_pos
    play sound "audio/sound/note.wav"
    low "(I followed Miss Cleo's instructions to the letter!  This plan is so good!)"
    show lowen closed_neutral
    low "(I also wanna know what Berserker looks like, hee hee hee!!!)"
    hide speechright
    hide lowen with dissolve

    show cleo focused2 mutter1_closed with dissolve
    cle "(Berserker has a soft spot for children.  Roping Lowen into this was the right move.)"
    cle "(Now Berserker has pressure to eat here, and this food is too watery to shove underneath his helmet.)"
    show cleo angry
    cle "(Which means... he'll have to take his helmet off!)"
    
    hide black with dissolve
    hide cleo with dissolve

    show berserker surprised with dissolve
    bers "Well... under the present circumstances, I suppose the solution is obvious..."
    show berserker at bigger_dip
    bers "Here, Lowen, you may have my food instead.  I'll wait until more bowls become available."
    hide berserker with dissolve

    show cleo focused2 mutter1_closed zorder 50 with dissolve
    show black with dissolve
    cle "(Aha, I thought you might try to wiggle out of my trap this way!  Which is why I also coached Lowen to say...)"
    hide black with dissolve
    hide cleo with dissolve

    show lowen sad mutter1 with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    low "W...Well, I'm trying to be more adult, so I need to own up to the fact that I came to breakfast late."
    hide speechright
    hide lowen with dissolve

    show ranzal zorder 50 with dissolve
    ranz "Good on ya, kid.  Sounds like you're on your way to manhood already!"
    show ranzal shocked closed_frown1
    show black with dissolve
    show speechright exclamation zorder 51 at speechright_pos
    play sound "audio/sound/exclamation.wav"
    ranz "(Holy crap!  Cleo's thought of everything!  This might actually work!)"
    hide speechright
    hide black with dissolve
    show ranzal neutral smile1
    ranz "If ya wanna do the kid a favor, big guy, then just hurry up and eat so Cleo can wash your bowl."
    hide ranzal with dissolve

    show berserker askance with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    bers "Well... I wouldn't want to put a stumbling block in the path of Lowen's road to maturity..."
    hide speechright
    stop music fadeout 1.0
    show berserker glint
    bers "Very well!  I shall finish this porridge right here and now!"
    hide berserker with dissolve

    show black with dissolve

    show cleo focused2 mutter1_closed with dissolve
    show speechright exclamation at speechright_pos
    play sound "audio/sound/exclamation.wav"
    play music "audio/sound/heartbeat.mp3" volume 10.0 # ShidenBeatsMusic
    cle "(He's going to do it!)"
    hide speechright
    hide cleo with dissolve

    show ranzal shocked closed_frown1 with dissolve
    ranz "(He's actually gonna do it!)"
    hide ranzal with dissolve

    show elisanne surprised frown1_closed
    elly "(Come on...)"
    hide elisanne with dissolve

    show luca shocked frown1_closed
    luc "(Show me the embarrassing birthmark!  No, no, snaggletooth city, here we come!!!!)"
    hide luca with dissolve

    show lowen focused closed_frown1
    low "(Any second now...)"
    hide lowen with dissolve

    show berserker with dissolve
    hide black with dissolve
    stop music fadeout 1.0
    pause 1.0
    bers "..."

    show berserker downcast
    play sound "audio/sound/straw slurp.mp3"
    pause 6.0

    hide berserker with dissolve

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadeout 1.0

    show cleo shocked pout1 with dissolve
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"
    cle "Y—You just carry a straw around with you at all times?!"
    hide speechright
    hide cleo with dissolve

    show berserker surprised with dissolve
    show speechright question at speechright_pos
    play sound "audio/sound/question.wav"
    bers "What?  I thought everyone wanted me to eat it as fast as possible."
    hide speechright
    hide berserker with dissolve

    show elisanne flinch pout2 with dissolve
    elly "He... He really drank an entire bowl of porridge with a straw..."
    hide elisanne with dissolve

    show luca askance grin2 with dissolve
    luc "I don't know whether to be disgusted or impressed..."
    hide luca with dissolve

    show berserker surprised with dissolve
    bers "...I'm very confused.  Everyone here seems to be so disappointed."
    show berserker neutral at bigger_dip
    bers "Here, Cleo, if you wash this bowl out, Lowen should be able to eat."
    hide berserker with dissolve

    show cleo shocked with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    cle "O-Oh, thank you...  I'll... get right on it..."
    hide speechright
    show cleo at walk_out_left
    pause 1.0

    show lowen flinch frown1 with dissolve
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"
    low "Actually... After seeing that, I'm... not really hungry anymore..."
    hide speechright
    show lowen at walk_out_right
    pause 1.0

    show ranzal closed_neutral grimace1 with dissolve
    ranz "...Honestly?  I don't blame ya, kid..."
    hide ranzal with dissolve

    show berserker surprised with dissolve
    show speechright question at speechright_pos
    play sound "audio/sound/question.wav"
    bers "...What did I do?"
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"
    show berserker downcast
    bers "(sigh) And people wonder why I eat in private..."
    hide speechright
    hide berserker with dissolve

    stop music fadeout 1.0

    image woods_day = "images/backgrounds/Sty_bg_0073_100_00.png"
    scene woods_day with fade

    play music "audio/music/Utopia.flac" fadeout 1.0

    show berserker with dissolve
    bers "..."
    show berserker downcast at searching_on_ground
    play sound "audio/sound/grass standing up.mp3"
    bers "...Aha."
    show berserker neutral
    bers "They're faint, but I see boar tracks in this brush.  Our quarry went in this direction."
    show berserker surprised
    show speechright question at speechright_pos
    play sound "audio/sound/question.wav"
    bers "...Hm?"
    hide speechright
    hide berserker with dissolve

    show luca askance mutter1 with dissolve
    luc "Psst.  Maybe what we could try is..."
    hide luca with dissolve
    
    show ranzal focused mutter1 with dissolve
    ranz "Nah, that would never work.  But what if..."
    hide ranzal with dissolve

    show berserker with dissolve
    bers "My friends, the boars lie this way.  Let us proceed with all haste."
    hide berserker with dissolve

    show luca relaxed frown1 with dissolve
    luc "Oh, uh, great!"
    show luca askance mutter1
    luc "So anyway..."
    hide luca with dissolve

    show berserker downcast with dissolve
    bers "..."
    show berserker neutral
    bers "...Afterwards, I was thinking we could duel to the death over our spoils.  How does that sound?"
    hide berserker with dissolve

    show ranzal relaxed smile2 with dissolve
    ranz "—Huh?  Yeah, I'm ok with that."
    show ranzal focused mutter1
    ranz "But Luca, we've gotta..."
    hide ranzal with dissolve

    show berserker closed_neutral with dissolve
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"
    bers "(Sigh)"
    show berserker neutral
    bers "When I agreed to go on a hunt with you, I was expecting at least Ranzal to take this seriously."
    bers "But all you've been doing is whispering amongst yourselves this entire time while I do all the tracking."
    bers "I am first and foremost a mercenary.  My time should be spent fighting, not supervising you lot."
    show berserker surprised
    show speechright question at speechright_pos
    play sound "audio/sound/question.wav"
    bers "And speaking of supervising... Cleo said she was foraging, but why has Elisanne accompanied us as well?"
    hide speechright
    hide berserker with dissolve

    show elisanne surprised pout1 with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    elly "Oh, well, that is because... um... "
    hide speechright
    hide elisanne with dissolve

    show fcleo surprised pout1 with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    cle "...because... Elisanne is joining me in foraging!"
    cle "Yes, she wants to... learn more survival tips for long missions, where rations could run out."
    hide speechright
    hide fcleo with dissolve

    show elisanne surprised smile1 with dissolve
    elly "Y-Yes, exactly!!"
    elly "And, on that subject, I have questions for you, Berserker."
    hide elisanne with dissolve

    show berserker surprised with dissolve
    bers "Oh?  Such as?"
    hide berserker with dissolve

    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    show elisanne flinch smile1 with dissolve
    elly "S-Such as... do you not find hunting in full plate armor difficult?"
    elly "A-After all, I imagine that the rattling of steel might alert your quarry."
    hide speechright
    hide elisanne with dissolve

    show berserker with dissolve
    bers "Hmm... I suppose so, but I tend not to rely on stealth to hunt."
    show berserker glint at laugh_bob
    bers "I prefer to confront my prey head-on!  Hahahaha!"
    show berserker neutral
    bers "...Or, if that doesn't work, I'll set up a snare or trap."
    hide berserker with dissolve

    show elisanne flinch smile1 with dissolve
    elly "A-Ah, I see..."
    show elisanne focused frown1_closed
    elly "..."
    show elisanne surprised pout1
    elly "Oh, um, Berserker!  Your helmet appears to have some... uh... leaves stuck to it!"
    hide elisanne with dissolve

    show berserker surprised with dissolve
    bers "Hm..."
    show berserker at bigger_dip
    bers "Did I get them?"
    hide berserker with dissolve

    show elisanne surprised pout1 with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    elly "N-No...  Um... well..."
    elly "...Perhaps you could... take the helmet off?  It would be easier to clean that way."
    hide speechright
    hide elisanne with dissolve

    show luca askance grin2 with dissolve
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"
    luc "Yeesh, this is painful to watch..."
    hide speechright
    hide luca with dissolve

    show berserker askance with dissolve
    bers "Ah, you worry too much, Elisanne.  A few leaves shan't stop me from swinging my sword!"
    hide berserker with dissolve

    show elisanne flinch smile1 with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    elly "I... suppose not, ha ha... ha..."
    hide speechright
    elly "But... um... surely you'll need to take off your gloves to do the delicate work of tying knots for the snares?"
    hide elisanne with dissolve

    show berserker surprised with dissolve
    bers "Well, I assume Luca would be much more proficient than me in that regard anyway."
    bers "I had planned to leave the trapping to him for this outing..."
    hide berserker with dissolve

    stop music fadeout 2.0

    show luca angry frown1 with dissolve
    luc "Ok, Elly had her turn.  It's time for me to step in, everyone."
    hide luca with dissolve

    show fcleo surprised shout1 with dissolve
    show speechright exclamation at speechright_pos
    play sound "audio/sound/exclamation.wav"
    cle "Luca, wait, you can't simply—"
    hide speechright
    hide fcleo with dissolve

    play music "audio/music/Story Bout B intro.flac"
    queue music "audio/music/Story Bout B.flac"

    show berserker zorder 2 with dissolve
    luc "Alley-oop!"
    show luca zorder 1 at lunge_in_left_to_leftpos
    show speechright exclamation zorder 3 at speechright_pos
    play sound "audio/sound/exclamation.wav"    
    bers "What—?! Luca, have you taken leave of your senses?!"
    hide speechright
    show luca angry shout1 at rapid_shake_left
    show berserker at rapid_shake
    luc "I'm... taking... your helmet... off!!!"
    luc "Geez, this thing is really stuck on!"
    show speechright sweat zorder 3 at speechright_pos
    play sound "audio/sound/sweat.wav"        
    bers "Cease this jackanapery at once!"
    hide speechright
    hide berserker
    show berserker glint
    play sound "audio/sound/punch.mp3"
    show luca at lunge_out_left_from_leftpos
    luc "Ow!! ...Ooof!"
    show berserker downcast
    hide luca
    bers "Hmph.  A just punishment for leaping upon me for no reason."
    show berserker askance
    show speechright question zorder 3 at speechright_pos
    play sound "audio/sound/question.wav"
    bers "Hm?  What is this fluid on my helmet?"
    bers "(Sniff) It smells citrusy sweet as well..."
    hide speechright
    hide berserker with dissolve

    show luca with dissolve
    show luca at disagree_shake
    luc "That's right.  That's because it's my backup plan!"
    luc "How do you like my bee balm nectar?  Pollinating insects go crazy for the stuff."
    show luca focused2 grin2
    luc "Which means..."
    hide luca with dissolve

    show berserker with dissolve
    bers "Hold a moment... did you say... BEE balm nectar?"
    play audio "audio/sound/bee swarm.mp3"
    show berserker surprised at disagree_shake
    bers "By Elysium, they're EVERYWHERE!!!"
    hide berserker with dissolve

    show luca with dissolve
    show speechright note at speechright_pos
    play sound "audio/sound/note.wav"
    luc "Yup!  And the only way to get rid of them is to ditch the helmet!"
    hide speechright
    hide luca with dissolve

    show berserker surprised with dissolve
    show speechright anger at speechright_pos
    play sound "audio/sound/anger.wav"
    bers "What?!  Why would you—?!  Argh, you will answer for this later!"
    hide speechright
    show berserker at rapid_shake
    play audio "audio/sound/bee swarm.mp3"
    bers "In any case, I must— OW!  Off me at once, you creatures!!  OW!!!"
    bers "Augh!  My helmet is stuck!!!  I need to unfasten—"
    show speechright exclamation at speechright_pos
    play sound "audio/sound/exclamation.wav"
    queue sound "audio/sound/bee swarm.mp3"    
    bers "—OW!!  OH, GOD, THIS IS HELLISH!"
    bers "—NOOOO!!!  MY EYES!!!  THE BEES ARE IN MY EYES!!!"
    bers "WHY DOES THIS KEEP HAPPENING TO MEEEEE?!?"
    hide speechright
    play sound "audio/sound/grass steps armor running.mp3"
    show berserker at lunge_out_right
    pause 1.0
    hide berserker

    show luca shocked frown1 with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"    
    luc "I... uh... pictured this going differently in my head..."
    hide speechright
    hide luca with dissolve

    show ranzal shocked shout1 with dissolve
    ranz "No KIDDING, moron!!!  We have to help him!!"
    ranz "Berserker, I'm coming, buddy!!!"
    hide ranzal with dissolve

    play sound "audio/sound/grass steps armor running.mp3"
    queue sound "audio/sound/grass steps armor running.mp3"
    show berserker surprised at lunge_in_left
    pause 0.75
    show berserker surprised at lunge_out_right
    bers "AAAAAAHHHHH!!!!"
    show ranzal shocked shout1 at lunge_in_left_to_leftpos
    ranz "Just hold still, big guy—!"
    play sound "audio/sound/grass steps armor running.mp3"
    show berserker surprised at lunge_in_right
    pause 0.5
    play sound "audio/sound/punch.mp3"
    show berserker at rapid_shake
    show ranzal at lunge_out_left_from_leftpos
    ranz "—OOOF!!!"
    show berserker at lunge_out_left
    pause 0.5
    hide ranzal
    hide berserker

    show elisanne surprised shout1 with dissolve
    elly "Never fear!  I will chase the bees away with my spear attacks!"
    hide elisanne with dissolve

    show fcleo surprised shout1 with dissolve
    show speechright exclamation at speechright_pos
    play sound "audio/sound/exclamation.wav"    
    cle "No, Elisanne, that will simply—!!!"
    hide speechright
    hide fcleo with dissolve

    show berserker surprised at rapid_shake with dissolve
    play sound "audio/sound/bee swarm.mp3"      
    bers "Auuugggh, make it stop!!!"
    show elisanne angry shout1 at lunge_in_left_to_leftpos
    pause 0.25
    play sound "audio/sound/blade slice flesh.mp3"
    hide berserker
    show berserker zorder 1
    elly "Hiyaaaaa!!!"
    bers "Urrrggghhh...."
    show berserker at fall_down
    pause 0.5
    show elisanne surprised frown1
    show woods_day at bg_jitter
    play sound "audio/sound/grass standing up.mp3"
    elly "...Berserker?  Oh dear..."
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"  
    bers "Why... me..."
    hide speechright
    bers "..."
    hide elisanne with dissolve

    show fcleo closed_angry closed_frown1 with dissolve
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"
    cle "(Sigh)"
    show fcleo focused frown1
    hide speechright
    cle "At least now he won't have to be conscious for the rest of this ordeal."
    show fcleo shout1
    cle "Luca!  Make smoke to drive away the bees!  I'll focus on healing him!!"
    hide fcleo with dissolve

    show luca shocked frown1 with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"    
    luc "R-Right..."
    hide speechright
    hide luca with dissolve

    stop music fadeout 1.0

    image halidom_bedroom = "images/backgrounds/Sty_bg_0049_100_00.png"
    scene halidom_bedroom with fade

    play music "audio/music/Yumemiteta no Atashi (Story Version A) intro.flac"
    queue music "audio/music/Yumemiteta no Atashi (Story Version A).flac"

    show berserker downcast with dissolve
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"    
    bers "Urghhh... I think I may be more bee-sting than man at this point..."
    hide speechright
    hide berserker with dissolve

    show fcleo pained frown1 with dissolve
    cle "Yes... On the bright side, because the bees were lured out of their hive, I was able to collect honey to make a salve."
    show fcleo sad
    cle "If you apply this to the stings, it should help to reduce the swelling and inflammation."
    hide fcleo with dissolve

    show berserker askance with dissolve    
    show berserker at disagree_shake
    bers "Ah, you have my gratitude... However... my head is so swollen I cannot even remove my helmet to apply it."
    hide berserker with dissolve

    show ranzal flinch grimace1 with dissolve
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"    
    ranz "Oof... I'm so sorry, buddy..."
    hide speechright
    hide ranzal with dissolve

    show berserker with dissolve
    show speechright question at speechright_pos
    play sound "audio/sound/question.wav"    
    bers "So all of this happened merely because you wanted to see my face?"
    hide speechright
    bers "If this comes up in the future, just ask me directly.  It would have saved me much grief..."
    hide berserker with dissolve

    show luca sad sweat with dissolve
    luc "Y-Yeah, you're right...  It got built up as this big forbidden mystery..."
    luc "...but we all took it way too far.  Sorry."
    hide luca with dissolve

    show elisanne angry frown1 with dissolve
    show speechright anger at speechright_pos
    play sound "audio/sound/anger.wav"  
    elly "What do you mean, 'we ALL took it way too far?'  YOU were the one who assaulted him with bees!!!"
    hide speechright
    hide elisanne with dissolve

    show luca shocked sweat with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    luc "H-Hey, I just said I was sorry for that!"
    hide speechright
    hide luca with dissolve

    show fcleo closed_angry frown1 with dissolve
    cle "...No, we're all somewhat at fault for this.  I for one should have had more sense than to pry."
    cle "Instead, I orchestrated a whole plot involving oatmeal and put Berserker on the spot."
    show fcleo pained
    cle "As it was, Ranzal was the only one who actually did anything NICE for him."
    hide fcleo with dissolve

    show berserker surprised with dissolve
    show berserker at laugh_bob
    bers "Heh... At some level, I should be flattered that you all were so intrigued by me."
    show berserker at disagree_shake
    bers "However, my appearance isn't some big secret.  To be frank, I have a rather plain-looking face."
    bers "If I had to explain why I wear my armor at all times... I suppose it's because I want to leave the past in the past."
    show berserker askance
    bers "Before I donned this armor, I didn't lead a life that I was proud of.  I made a lot of mistakes."
    bers "When I became a mercenary, I decided that I wanted to put my past to rest and start a new life."
    show berserker neutral
    stop music fadeout 2.0
    queue music "audio/music/CRASHER (Story Version A) loop.mp3" fadein 3.0
    bers "So I took on a new identity.  I wanted my armor to become a symbol of my resolve to fight, and my desire to face strong foes."
    bers "And I've found a lot of joy in my new life.  Deadly struggles allow me, however briefly, to experience a burning zeal for life pulsing through my veins."
    bers "And it also was under this identity that I came to join the Halidom and found a new reason to wield my sword."
    bers "A cause that was not just worth dying for, but worth LIVING for."
    show berserker surprised
    bers "So... I've decided that I want to BECOME this armor of mine.  To be reborn not as a man, but as a symbol of valor and righteous battle."
    show berserker askance at laugh_bob
    bers "Although... heh, I suppose there are more mundane reasons as well.  I would be lying if I said I wasn't proud of my armor."
    bers "It's gotten me through many a battle, and I can't deny that the awe, fear and respect that it inspires in others is... enjoyable."
    show berserker neutral
    bers  "So fret not.  I suppose that, in a way, my current predicament is merely the price of my own vanity."
    hide berserker with dissolve

    show ranzal grin1 with dissolve
    ranz "Well, as far as my vote goes, it's a damn fine suit of armor.  For a damn fine warrior.  It suits you, buddy."
    hide ranzal with dissolve

    show berserker surprised at laugh_bob with dissolve
    show speechright note at speechright_pos
    play sound "audio/sound/note.wav"
    bers "Heh... You have my gratitude, friend."
    hide speechright
    hide berserker with dissolve

    show luca sad frown1 with dissolve
    luc "Still... I feel really bad leaving things like this.  I was definitely way out of line."
    luc "Are you sure there isn't anything I can do to make it up to you?"
    hide luca with dissolve

    show berserker askance with dissolve
    bers "Hmmm..."
    show berserker neutral
    bers "In that case, I would simply ask that you accompany me the next time I go hunting."
    show berserker at laugh_bob
    bers "Our hunting trip today was cut short prematurely, after all."
    hide berserker with dissolve

    show luca relaxed_closed grin1 with dissolve
    show speechright note at speechright_pos
    play sound "audio/sound/note.wav"
    luc "Heh, is that all?  Sure, no sweat!"
    show luca relaxed
    luc "You've got yourself a deal, man!"
    hide speechright
    hide luca with dissolve

    stop music fadeout 2.5
    show ranzal shocked closed_frown1 with dissolve
    ranz "..."
    hide ranzal with dissolve
    show elisanne surprised frown1_closed
    elly "..."
    hide elisanne with dissolve
    show fcleo focused frown1 with dissolve
    cle "..."
    show fcleo closed_angry mutter1
    show speechright bad at speechright_pos
    play sound "audio/sound/bad.wav"
    cle "...I'll have the medical supplies ready for when you return..."
    hide speechright
    hide fcleo with dissolve

    show luca surprised mutter1 with dissolve
    show speechright question at speechright_pos
    play sound "audio/sound/question.wav"
    luc "...What's with you guys?  The mood got so somber all of a sudden."
    luc "Like Berserker said, we're just gonna go out hunting.  No biggie."
    hide speechright
    hide luca with dissolve

    image cliff_storm = "images/backgrounds/Sty_bg_0038_400_00.png"
    scene cliff_storm with fade

    show luca shocked sweat with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    luc "TH... THIS is what you're hunting?!?"
    hide speechright
    hide luca with dissolve

    play music "audio/music/Legend of Flight Fatalis intro.mp3" fadein 2.0
    queue music "audio/music/Legend of Flight Fatalis.mp3"

    show dreadking_rathalos at trudge_in_left
    pause 0.75
    show cliff_storm at bg_jitter
    pause 0.8
    show cliff_storm at bg_jitter
    pause 0.8
    show cliff_storm at bg_jitter
    play sound "audio/sound/dreadking rathalos roar.mp3" volume 0.45
    show cliff_storm at bg_jitter_long
    dkr "ROAAAAAAAAAAAAAAAAAAR!!!!"
    hide dreadking_rathalos with dissolve

    show hberserker at laugh_bob with dissolve
    pause 0.6
    show hberserker at laugh_bob
    pause 0.6
    show hberserker at laugh_bob
    bers "Hahaha.... HAHAHAHAHA!!!  Can't you feel the beast's roar reverberate through your entire BODY?!?"
    show hberserker glint
    bers "That's how you know he's a FEISTY one!!!  Good, good!!!  GOOD!!!"
    hide hberserker with dissolve

    show luca flinch_closed shout1 at disagree_shake with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    luc "Bad, bad, BAD!!!  This is BAD!!!  We're gonna die!!!  We're totally gonna die!!!"
    hide speechright
    hide luca with dissolve

    show hberserker glint with dissolve
    show speechright note at speechright_pos
    play sound "audio/sound/note.wav"
    bers "Perhaps!  And if so, it will be an honor to die gloriously with you, my friend!!!"
    hide speechright
    hide hberserker with dissolve
    play sound "audio/sound/blade swing.mp3"
    show hberserker_sword with dissolve
    bers "But let us attempt to carve out a future for ourselves with blade and bow!!!"
    show hberserker_sword glint
    bers "Now ready yourself!!!  This fight will take every ounce of strength we have!!!"
    hide hberserker_sword with dissolve

    show luca flinch_closed shout1 at disagree_shake with dissolve
    show speechright sweat at speechright_pos
    play sound "audio/sound/sweat.wav"
    luc "Literally NO amount of preparation could POSSIBLY make me ready for this!!!"
    luc "Is this still because of the bees?  I'm SO sorry, man!!  I'M SORRY!!!  PLEASE!!!"
    hide speechright
    hide luca with dissolve

    show hberserker_sword glint at rapid_shake with dissolve
    bers "My pulse races!!!  My body trembles!!!  The heat of the beast's dread breath washes over me!!!"
    bers "YES!!  TRULY, THIS IS WHAT IT MEANS TO BE ALIVE!!!"
    show hberserker_sword at laugh_bob
    pause 0.6
    show hberserker_sword at laugh_bob
    pause 0.6
    show hberserker_sword at laugh_bob
    bers "HAHAHAHAHAAHAHAAHAHAHAHA!!!  HOLD NOTHING BACK, MY FOE!!!  LET US SAVOR THIS FATAL DANCE!!!"

    show hberserker_sword at big_swing_counterclockwise
    play sound "audio/sound/axe swing.mp3"
    pause 0.5
    queue sound "audio/sound/axe swing.mp3" #floraphonic on pixabay
    pause 2.0
    show hberserker_sword at thrust_forward
    play sound "audio/sound/blade slice flesh.mp3"
    queue sound "audio/sound/blade slice flesh.mp3" volume 1.3
    queue sound "audio/sound/blade slice flesh.mp3" volume 1.6
    queue sound "audio/sound/dreadking rathalos roar.mp3" volume 0.45
    pause 1.0
    show cliff_storm at bg_jitter_long
    dkr "ROAAAAAAAAAAAAAAAAAAR!!!!"
    hide hberserker_sword with dissolve


    scene black with fade
    show text "{color=ffffff}{i}The End...?{/i}{/color}" at middle with dissolve
    pause 20.0

    jump newcastlestoriesmenu
