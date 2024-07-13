
##        "{color=#000000}'My Finni Valentine.'{/color}":
##            "Excellent choice.  Android army unite!"
##            jump myfinnivalentinemenu


define everyone = Character("Everyone", callback=speaker("everyone"))

image laxi_face_sparkles:
    "images/effects/laxi face sparkles/laxi face sparkles frame1.png"
    0.08
    "images/effects/laxi face sparkles/laxi face sparkles frame2.png"
    0.08
    "images/effects/laxi face sparkles/laxi face sparkles frame3.png"
    0.08
    "images/effects/laxi face sparkles/laxi face sparkles frame4.png"
    0.08
    "images/effects/laxi face sparkles/laxi face sparkles frame5.png"
    0.08
    "images/effects/laxi face sparkles/laxi face sparkles frame6.png"
    0.08
    "images/effects/laxi face sparkles/laxi face sparkles frame7.png"
    0.08
    "images/effects/laxi face sparkles/laxi face sparkles frame8.png"
    0.08
    "images/effects/laxi face sparkles/laxi face sparkles frame9.png"
    0.08
    repeat

transform dragon_riding_pos:
    yalign 0.22
    xalign 0.65
    zoom 0.35

transform sepia:
    matrixcolor SepiaMatrix(tint=u'#ffeec2', desat=(0.2126, 0.7152, 0.0722))





label myfinnivalentinemenu:


    play music "audio/music/Kaede (Maple Leaf) - Off-Vocals loop.mp3" fadeout 1

    image finneirene = "images/backgrounds/finneirene.png"
    scene finneirene with fade

    show text "Art by abby (@vaccariia on Twitter)" at topleft
    with dissolve

    menu:
        "What chapter do you want to read?"

        "{color=#000000}Chapter 1: Worthday Fishes{/color}":
            jump my_finni_valentine

        "{color=#000000}Chapter 2: A Chocolate Crisis{/color}":
            jump my_finni_valentine2

        "{color=#000000}Chapter 3: Diverging Directives{/color}":
            jump my_finni_valentine3

        "{color=#000000}Chapter 4: Heart to Heart, Chest to Chest{/color}":
            jump my_finni_valentine4

        "{color=#000000}Chapter 5: Not Even Me{/color}":
            jump my_finni_valentine5

        "{color=#000000}Chapter 6: A Day to Remember{/color}":
            jump my_finni_valentine6

        "{color=#000000}Chapter 7: My Finni Valentine{/color}":
            jump my_finni_valentine7

        "{color=#000000}Main Menu{/color}":
            stop music fadeout 1
            jump start










# The game starts here.

label my_finni_valentine:

    # Halidom Great Hall

    play music "audio/music/BANG (Story Version B) intro.flac" fadeout 1.0
    queue music "audio/music/BANG (Story Version B).flac"

    image greathall_night = "images/backgrounds/Sty_bg_0072_300_00.png"
    scene greathall_night with fade

    play sound "audio/sound/stone steps.mp3"
    show eirene with dissolve
    hide eirene with dissolve

    play sound "audio/sound/stone steps.mp3"
    show elisanne with dissolve
    hide elisanne with dissolve

    play sound "audio/sound/stone steps.mp3"
    show finni with dissolve
    fin "Whew, I am BEAT!  I can't wait to lie down, oil up my servos and get back to painting my latest woodcarving!"
    play sound "audio/sound/note.wav"   
    show finni relaxed
    show speechright note at speechright_pos
    fin "Oh, Eirene, have I told you that I've gotten really hardcore into modelling lately?  I've made all the greatwyrms except Brunhilda!  I'm really looking forward to finishing the full set."

    hide speechright
    hide finni with dissolve
    show eirene smile1 with dissolve
    eir "That sounds nice, Finni.  I, for one, am going to continue my research into human society and relationships.  Most recently, I've been analyzing some historical texts provided to me by Elisanne."

    hide eirene with dissolve
    show elisanne frown1 surprised with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    elly "(!)"

    hide speechright
    hide elisanne with dissolve
    show eirene with dissolve
    eir "However, I don’t fully understand why such information was documented.  The report was clear that a public scandal would arise from the clandestine exchange of saliva between the prince of Jacinth and his housemaid in the duchess’s boudoir."
    eir "Additionally, only the prince and the housemaid could possibly know all these vivid sensory details, so I'm confused about why either of them would publish and disperse such information for public consumpt—"

    hide eirene with dissolve
    show elisanne blush smile2 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "AHAHAHA!  You’re such a KIDDER, Eirene!  Imagine me possessing such a clearly vapid and lurid piece of literature!  Surely such a scandal would ill befit a paladin of my position!!"
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    show elisanne flinch pout2
    elly "…Psst!  I thought we agreed we were supposed to keep the origin of those books between US?  Eirene?"

    hide speechright
    hide elisanne with dissolve
    show eirene dull with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    eir "Unless… the information was falsified, and is actually a propaganda piece published by a political rival to discredit the prince of Jacinth?"
    show speechright lightbulb
    play sound "audio/sound/inspiration.wav"
    show eirene glow_focused shout1
    eir "Fascinating.  That would recontextualize nearly everything about the text!  I'll have to factor this possibility into my analysis moving forward…"

    hide speechright
    hide eirene with dissolve
    show elisanne blush smile2 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "A-Anyway, I’ll just be glad to put some food in my stomach and take a long, relaxing bath!  …Which will DEFINITELY not be accompanied by romance novels!  Seeya!!!"

    play sound "audio/sound/grass steps armor running.mp3"
    hide speechright
    hide elisanne with dissolve
    show finni relaxed frown1 with dissolve
    fin "Whoa, Elisanne ran off REALLY fast."
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    fin "…Hey, it looks like some people are gathering over there at the end of the hall."
    hide speechright question

    play music "audio/music/Utopia.flac" fadeout 1.0 fadein 1.0

    hide finni with dissolve
    show pia_img smile1 with dissolve
    show speechright note at speechright_pos
    play sound "audio/sound/note.wav"
    pia "Happy birthday, Lathna!"

    hide speechright
    hide pia_img with dissolve
    show lathna smile1 with dissolve
    lat "Mmm… this cake is really delicious.  Thank you!"

    hide lathna with dissolve
    show curran smile1 with dissolve
    cur "Well, of course!  I worked really hard to make sure all your worthday fishes come true!  —Argh, darnit!"

    hide curran with dissolve
    show lathna closed_relaxed smile1 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    lat "Hee hee!  Yay!  He said a funny thing again!"

    hide speechright
    hide lathna with dissolve
    play sound "audio/sound/stone steps.mp3"
    show eirene with dissolve
    hide eirene with dissolve
    play sound "audio/sound/stone steps.mp3"
    show finni relaxed with dissolve
    fin "’Worthday fishes’?  It’s good to see that Curran never changes."

    hide finni with dissolve
    show eirene with dissolve
    eir "Wait a moment.  There are many human holidays which are unfamiliar to us as androids."
    eir "It may be possible that Worth Day is one such celebration, and involves sea creatures."

    hide eirene with dissolve
    show finni surprised frown1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "Oh!  You’re right!  I hadn’t thought of that.  I guess this is why you’re the smart one!"

    hide speechright
    hide finni with dissolve
    show heinwald with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos    
    hein "…No, Curran’s just tripping over his own tongue again.  The only holiday being celebrated here is Lathna’s birthday."

    hide speechright
    hide heinwald with dissolve
    show curran smile1 with dissolve
    cur "Yeah!  She was born today, and pretty soon this little miss here is going to be a full-grown lady."

    play music "audio/music/CRASHER (Story Version A) loop.mp3" fadein 2.0

    hide curran with dissolve
    show lathna frown1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    lat "Um… Everyone?  I… I just wanted to thank you for doing this."
    hide speechright
    lat "For a long time, I didn’t think my birthday was worth celebrating.  After all, the scary other me was always causing trouble for everyone."
    show lathna smile1
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    lat "But… then you guys helped me and taught me that I don’t need to worry because I’m not bad.  That people wanted to be friends with me."
    hide speechright
    lat "Back when I was alone, I never would have thought that there would be people who cared enough about me to throw me a surprise party like this with so many guests."
    lat "I mean, you all gave me such perfect gifts!  And Pia even took care of my chores today so I didn't have to worry about them!"

    hide lathna with dissolve
    show pia_img surprised smile1 with dissolve
    pia "Of course!  I didn't want you to have to work on your birthday!"
    hide pia_img with dissolve

    show lathna smile1 with dissolve
    lat "Well, it was still super nice!  Oh, and even the cake is my favorite flavor!  How did you know that I like chocolate?"

    hide lathna with dissolve
    show akasha with dissolve
    aka "Well, only the deepest of dark flavors would be appropriate for the vessel of the One who waits in blackness, no?"

    hide akasha with dissolve
    show heinwald annoyed grimace with dissolve
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    hein "Of course that’s NOT the reason, you meddlesome woman.  I merely did some detective work with Cleo’s help."
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    show heinwald surprised2 frown2
    hein "…Who invited you to this soiree, anyway?"

    hide speechright
    hide heinwald with dissolve
    show finni relaxed with dissolve
    fin "In any case, that cake DOES look really good.  I’ve heard chocolate tastes great."
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    show finni sad
    fin "…Not that I’ll ever know…  It’s a shame, I guess."

    hide speechright
    hide finni with dissolve
    show eirene with dissolve
    eir "..."

    hide eirene with dissolve
    show lathna with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    lat "Huh?  You can have some, Finni!  Here!"

    hide speechright
    hide lathna with dissolve
    show eirene sad frown1 with dissolve
    eir "I don’t want to disappoint you, Lathna, but I’m afraid it’s not that simple…"
    eir "While Eirene and I can eat in order to refuel our mana, and can identify all the chemical components in food, we simply are unable to experience flavor in the way organic beings do."
    eir "We were designed for combat, after all.  If soldiers had a preference for expensive fuels, it would very cost-ineffective."
    eir "The way we are, grass and dirt are just as viable sources of sustenance as expensive cuisine.  It does leave us unable to experience the pleasures of eating that you experience, however…"

    hide eirene with dissolve
    show pia_img surprised with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    pia "Oh no!  But Valentine’s Day is coming up!  If you can’t taste chocolate, you’ll have a sad time!"

    hide speechright
    hide pia_img with dissolve
    show finni frown2 relaxed with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    fin "...Valentine's Day?"
    hide speechright

    hide finni with dissolve
    show lathna smile1 relaxed with dissolve
    lat "Yeah, it’s a holiday where you give chocolate hearts to the people you love.  I’m gonna give some to Curran, Heinwald and Pia."

    hide lathna with dissolve
    show finni surprised frown1 with dissolve
    fin "To the people you love?"

    show finni wink smile1
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    fin "Well, that’s easy; I love Eirene!"

    hide speechright
    hide finni with dissolve
    show eirene surprised with dissolve
    eir "Love?  I suppose you ARE more important to me than anyone else in the world.  Is love the right word for that, then?"

    hide eirene with dissolve
    show curran smile1 with dissolve
    cur "It sure sounds like it!  Everyone has the ability to love, regardless of your race, gender or greed."


    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadeout 1.0

    hide curran with dissolve
    show heinwald with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    hein "(sigh) If I were you, I’d stop trying to sound impressive and focus on serving yourself a slice of birthday cake before a certain hungry sylvan makes off with it."

    hide speechright
    hide heinwald with dissolve
    show curran sweat grimace2 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    cur "H-Hey!  Luca??"

    hide speechright
    hide curran with dissolve
    show luca surprised frown5 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    luc "Eep!!  Wuh oh!!"

    hide speechright
    play sound "audio/sound/grass steps running.mp3"
    hide luca with dissolve
    show finni focused closed_mutter1 with dissolve
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos
    fin "(Hmm… Eirene has been a little distant and serious lately…  This ‘Valentine’s Day’ thing sounds like a great way to remind her how much I care about her!)"

    hide speechright
    show finni relaxed smile1
    fin "Valentine’s Day sounds like a ton of fun!  When exactly is it going to happen?"

    hide finni with dissolve
    show lathna smile1 with dissolve
    lat "Oh, it’s this Saturday.  The 14th."

    hide lathna with dissolve
    show finni relaxed with dissolve
    fin "Awesome!  That’ll give me enough time to prepare—"

    stop music fadeout 1

    show finni surprised frown2
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "…Hang on, did you say… the FOURTEENTH?  Of THIS month?"

    hide speechright
    hide finni with dissolve
    show pia_img with dissolve
    pia "Yeah, why?"

    hide pia_img with dissolve
    show eirene with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    eir "(!)"

    hide speechright
    hide eirene with dissolve
    show finni flinch closed_mutter1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "(Crap!  This is bad.  I really don’t want to give up on the idea, but… why did it have to be THAT day of all days??)"
    hide speechright
    fin "(I’ll have to handle this REALLY delicately…)"

    hide finni with dissolve

    jump myfinnivalentinemenu


label my_finni_valentine2:

    stop music fadeout 1

    image courtyard_morning_sky = "images/backgrounds/Sty_bg_0027_100_00.png"
    image courtyard_morning_clouds = "images/backgrounds/Sty_bg_0027_100_02.png"
    image courtyard_morning = "images/backgrounds/Sty_bg_0027_100_04_front.png"

    layeredimage courtyard_day:
        always:
            "images/backgrounds/Sty_bg_0027_100_00.png"

        group clouds:

            attribute clouds1:
                "images/backgrounds/Sty_bg_0027_100_01.png"

            attribute clouds2:
                "images/backgrounds/Sty_bg_0027_100_02.png"

            attribute clouds3:
                "images/backgrounds/Sty_bg_0027_100_03.png"

        always:
            "images/backgrounds/Sty_bg_0027_100_04_front.png"


    scene courtyard_day clouds2 with fade

    "A few days later, on Valentine's Day..."

    play music "audio/music/Utopia.flac" fadeout 1 fadein 1.0

    play sound "audio/sound/grass step.mp3"
    queue sound "audio/sound/grass step.mp3"
    queue sound "audio/sound/grass step.mp3"
    show finni relaxed with dissolve
    fin "Alright, I’m all set with the chocolate, and I wrapped it up in the perfect little package!"
    show finni wink
    fin "I’m really glad I asked Cleo for help; I didn’t know the first thing about cooking or confection-making, so her directions made all the difference."
    show finni sad
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "…Granted, Eirene won’t actually be able to TASTE it, but… I wasn’t about to settle for anything less than the best for her!"
    hide speechright
    show finni relaxed grin1
    fin "Plus, it looks like my patrol duties even got cancelled for the day, so that means I'll be able to make all sorts of fun Valentine's Day plans with Eirene!"

    hide finni with dissolve
    show eirene with dissolve
    hide eirene with dissolve
    show elisanne with dissolve
    hide elisanne with dissolve

    show finni focused with dissolve
    fin "…Great, Eirene’s right over there, talking to Elisanne."
    show finni frown1
    fin "Ok, take a deep breath… and… here we go!"

    play sound "audio/sound/grass step.mp3"
    queue sound "audio/sound/grass step.mp3"
    queue sound "audio/sound/grass step.mp3"
    hide finni with dissolve
    show eirene surprised with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    eir "…Oh, hello there, Finni.  Is there any chance this could wait a moment?  I’m in the middle of an important conversation right now."

    hide speechright
    hide eirene with dissolve
    show finni surprised frown1 with dissolve
    fin "O-Oh, well, uh, I didn’t mean to bother you!  I’ll just—"
    show finni shocked frown2
    play audio "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "—Wait, no this is important!!!  I have something to give you!  Here!"
    hide speechright

    hide finni with dissolve
    show eirene focused frown1 with dissolve
    eir "A package?..."
    show eirene neutral
    eir "..."
    show eirene surprised
    eir "Oh, chocolate?"

    hide eirene with dissolve
    show finni grin1 with dissolve
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    fin "HAPPY VALENTINES’ DAY!!!"
    hide speechright

    hide finni with dissolve
    show eirene with dissolve
    eir "Oh, I see.  I suppose this is that human tradition Lathna was talking about."
    show eirene dull
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    eir "But… didn't you just say a few days ago that it was a shame that you and I can't taste it?"
    hide speechright

    hide eirene with dissolve
    show finni surprised awkward1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "W-Well, I know THAT, of course!  I was just thinking that it’s, well, the thought that counts, you know?"
    hide speechright

    hide finni with dissolve
    show eirene focused with dissolve
    eir "I see.  Thank you.  Your timing is actually shockingly perfect."

    hide eirene with dissolve
    show finni relaxed smile1 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    fin "Oh, well… that’s great!  See, I just wanted to let you know how much I care about—"
    hide speechright

    stop music fadeout 1

    hide finni with dissolve
    show eirene glow_focused frown1 with dissolve
    eir "Here, Elisanne, this should be a perfect sample for you."

    hide eirene with dissolve
    show finni shocked smile1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "Wait… what?"
    hide speechright

    play music "audio/music/CRASHER - Failure loop.mp3" fadein 1.0

    hide finni with dissolve
    show elisanne surprised frown2 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "H-Hang on, when you said you wanted to give me chocolate, I didn’t think you’d give me something from someone else… e-especially Finni!"
    hide speechright
    show elisanne flinch pout1
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    elly "And after she just gave it to you, too!  I-Isn’t that—?"
    hide speechright

    hide elisanne with dissolve
    show eirene glow_focused frown1 with dissolve
    eir "No, I would say that this is the MOST logical course of action, given these new circumstances.  Don’t you agree it’s the best way to convey my own feelings?"

    hide eirene with dissolve
    show finni surprised awkward1 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    fin "Convey… your feelings?  H-Hang on Eirene, what do you mean?"
    hide speechright

    hide finni with dissolve
    show elisanne surprised frown2 with dissolve
    elly "I-I get what you’re saying, but—isn’t this a bit of a shock to Finni in the meantime?  I think we ought to explain ourselves—"

    hide elisanne with dissolve
    show eirene focused mutter2 with dissolve
    eir "No, I’d rather not involve Finni in the details at this stage.  Besides, given what day it is, she probably already had a suspicion that I would do something like this."

    hide eirene with dissolve
    show finni surprised mutter1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "E-Eirene, what—I mean, I knew that today had a lot of significance for you, but I just figured… maybe it’s better to just give the past a rest and do something different, you know?"
    hide speechright

    hide finni with dissolve
    show eirene pained grimace1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    eir "What?  You of all people should understand why I cannot do that!  Today is such an important day for the both of us."
    hide speechright
    show eirene closed_neutral
    eir "For you to say… I should just forget about…?"
    show eirene glow_angry shout1
    eir "I would never!"

    hide eirene with dissolve
    show elisanne surprised shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "I… I think this is having the opposite result!  Maybe we should backtrack a little?"
    hide speechright

    hide elisanne with dissolve
    show eirene closed_neutral with dissolve
    eir "..."
    show eirene neutral
    eir "…I agree.  This is a counterproductive discussion.  I’m sorry, Finni.  I know you probably have your own feelings on the matter, but I’m determined not to let this day go to waste."

    hide eirene with dissolve
    show finni focused frown1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "W-Well, in that case, we still have time, right?"
    hide speechright
    show finni relaxed awkward1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "Uhh… there’s a celebration going on in the village in a half hour or so!?  I was thinking that we could maybe go together.  Doesn’t that sound nice?"
    hide speechright

    hide finni with dissolve
    show eirene pained smile1 with dissolve
    eir "It does sound nice... but I’m sorry, I currently have… other business to attend to."

    hide eirene with dissolve
    show finni pained frown1 with dissolve
    fin "Eirene..."

    hide finni with dissolve
    show eirene pained smile1 with dissolve
    eir "My apologies.  Please go and enjoy yourself while Elisanne and I discuss some more details together."

    hide eirene with dissolve
    show finni surprised awkward1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "O-Oh, really?  Y-You and… and Elly?  W-Well, I suppose I’ll be ok by myself…!"
    hide speechright

    hide finni with dissolve
    show elisanne sad frown1 with dissolve
    elly "P-Please do be patient!  I’m sure you’ll understand soon!"

    play sound "audio/sound/grass step.mp3"
    queue sound "audio/sound/grass step.mp3"
    queue sound "audio/sound/grass step.mp3"
    hide elisanne with dissolve
    show finni surprised awkward1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "Sure thing!  I… I, uh, I’ll meet back up with you later then!"
    hide speechright

    stop music fadeout 1

    hide finni with dissolve
    show finni surprised closed_awkward1 with dissolve

    fin "..."
    show finni sad
    fin "..."
    show finni focused frown1
    fin "..."

    play music "audio/music/CRASHER (Story Version C) intro.flac" fadeout 1.0
    queue music "audio/music/CRASHER (Story Version C).flac"

    show finni shocked shout1
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "OH MY GOSH, WHAT’S GOING ONNNNNNNNN?!?!?!?"
    hide speechright

    show finni surprised
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "Is… Is there something going on between her and Elly?  …No, there’s no way, right??  I mean, Eirene and I have been together for a thousand years!!!"
    hide speechright

    show finni awkward1
    fin "I mean, I get that today doesn’t have the BEST personal significance for Eirene, but… was she THAT upset about getting some chocolate?!?"

    show finni pout1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "Or maybe… Eirene has been growing distant from me for a while?!  Maybe she thinks I cause too many problems??"
    hide speechright

    play music "audio/music/CRASHER - Failure loop.mp3" fadeout 1.0 fadein 2.0

    image battlefield = "images/backgrounds/Sty_bg_0129_400_00.png"
    scene battlefield at sepia with fade

    fin "It’s true that I’m not as capable as her original Finni—THAT Finni disappeared a thousand-some years ago when Eirene implanted her damaged heart into me."
    fin "And… that happened on this exact date.  The fourteenth of the second month of the year.  The day I replaced her friend…"
    fin "It... It was selfish to try to make today about me, wasn't it?"

    scene courtyard_day clouds2 with fade

    show finni flinch frown2 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "…Ugh, Eirene was right!  I should have KNOWN this would happen!!"
    hide speechright
    show finni sad frown1
    fin "I’m… I’m such an idiot…"


    show finni surprised frown2
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    fin "But wait—even if she’s upset at ME… what does that have to do with Elisanne??"
    hide speechright
    show finni relaxed frown1
    fin "I guess it’s true that Eirene and Elisanne go on a lot of missions together…"
    show finni shocked
    fin "Maybe… Elisanne is a more trustworthy combat partner than me?  Or… maybe she’s emotionally closer to me than her now??"
    show finni surprised shout1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "AAAAAAGHHH!!!  I’m freaking out just thinking about it!!!"
    hide speechright
    show finni focused
    fin "I… I just have to show Eirene that I can still be her best partner!  That I love her more than anyone else in the world!!"
    show finni flinch
    fin "But… how do I do that?!?  I don’t even know what's going on with her!!"
    show finni frown1
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "…I’m gonna need some help…"
    hide speechright

    jump myfinnivalentinemenu







label my_finni_valentine3:

    play music "audio/music/Utopia.flac" fadeout 1 fadein 1.0

    image laboratory = "images/backgrounds/Sty_bg_0103_100_00.png"
    scene laboratory with fade

    show grace relaxed with dissolve
    gra "...and that's why you thought to approach me on the matter?  ...You do realize I am a widow, correct?"

    hide grace with dissolve
    show finni focused frown1 with dissolve
    fin "Exactly! You had the longest and most successful marriage of anyone I know here at the Halidom."

    show finni flinch closed_awkward1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "(Well... actually, I wanted Laxi and Mascula instead, but... I couldn't find them anywhere.  ...I don't think I should tell Grace she was my second pick, though...)"
    hide speechright


    show finni flinch smile2
    fin "...A-Anyway, I'm here to ask you about what kept you and your husband together for so long."

    show finni closed_focused frown1
    fin "For instance... did you two ever... fight?"
    fin "I'm... well, I don't know exactly how to put it, but... I'm feeling a rift between me and Eirene, and I want to fix it..."

    hide finni with dissolve
    show grace focused smile3 with dissolve
    gra "Hmm... well, we certainly had our share of disagreements.  My husband did have a bit of a jealous streak, for instance..."

    show grace relaxed
    gra "He once saw me having lunch with a male researcher off in private, and he swooped in and practically dragged me away…  It did bother me that his insecurities sometimes brought him to interfere with my social life…"

    show grace smile1
    gra "…Although I must admit, I was ALSO flattered that he thought I was so beautiful that I could make someone fall in love with me just by sharing a meal with them.  What a high opinion he must have had of me!"

    hide grace with dissolve
    show finni focused with dissolve
    fin "So… is that it?  You just tried to remember that your husband was doing it out of attraction to you or something?"

    play music "audio/music/CRASHER (Story Version A) loop.mp3" fadeout 1.0 fadein 2.0

    hide finni with dissolve
    show grace -smile1 -relaxed with dissolve
    gra "Well, it’s not as though that was all there was to it.  After all, we shared a host of common ideals and goals.  Medical research was very important to both of us, as well as the safety of our patients."
    gra "We cared about it so much, in fact, that we agreed to do something as risky as betraying the Syndicate to act on our mutual values."

    hide grace with dissolve
    show finni sad frown1 with dissolve
    fin "Wow, that sounds like a really important factor…"

    show finni surprised
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos
    fin "Wait, of course!  Eirene and I had been fighting for Ex Machina for thousands of years!  Now that we’ve defected, we don’t have that old common goal anymore!  That’s gotta be what happened!"
    hide speechright

    hide finni with dissolve
    show grace surprised with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    gra "Um… I suppose so?"
    hide speechright

    hide grace with dissolve
    show finni surprised smile2 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "THAT’S IT!!!  Eirene and Elisanne are both focused on their duties for the Halidom!  That’s why they’ve been clicking together so well lately!"
    hide speechright

    show finni sad mutter1
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "…And, meanwhile, I’m kind of a spaz…  Urgh…  Guess that solves the mystery of why I got taken off patrol duty today…"
    hide speechright

    show finni focused
    fin "If I want to be close to Eirene again, I need to show her that I’m committed to our NEW common goal of protecting the peace of the kingdom!"

    show finni neutral
    fin "Thank you SO much, Grace!  You’ve made everything really clear for me!!!"

    play sound "audio/sound/stone steps.mp3"
    hide finni with dissolve
    show grace surprised with dissolve
    gra "You’re… welcome?"

    show grace focused
    gra "(Oh dear… I really hope I haven’t steered Finni wrong about this…)"

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadeout 1.0 fadein 1.0

    layeredimage field_day:
        always:
            "images/backgrounds/Sty_bg_0022_100_00.png"

        group clouds:

            attribute clouds1:
                "images/backgrounds/Sty_bg_0022_100_01.png"

            attribute clouds2:
                "images/backgrounds/Sty_bg_0022_100_02.png"

            attribute clouds3:
                "images/backgrounds/Sty_bg_0022_100_03.png"

        always:
            "images/backgrounds/Sty_bg_0022_100_04_front.png"


    scene field_day with fade
    # missing clouds3 but throws error

    play sound "audio/sound/gravel step.mp3"
    queue sound "audio/sound/stone steps.mp3"
    queue sound "audio/sound/stone steps.mp3"
    show finni focused smile2 with dissolve
    fin "Take THIS, you baddie!"

    hide finni with dissolve
    show fiend with dissolve
    fie "Grawr?—"

    play sound "audio/sound/blade slice flesh.mp3"
    hide fiend with dissolve
    fie "...hurk!"

    show finni closed_focused awkward1 with dissolve
    fin "WHEW!  I got a little battered in the process, but that takes care of all the fiends in a two-mile radius of the Halidom.  Now everyone should be able to have a peaceful Valentine’s Day!"

    show finni focused smile2
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    fin "And, more IMPORTANTLY, Eirene will see that I care about fulfilling my duties just as much as she does!  She'll remember that she can trust me!"
    hide speechright

    show finni surprised smile1
    fin "Oh, perfect timing!  Here she comes now!"

    show finni shocked
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "Along with... Elisanne..."
    hide speechright

    hide finni with dissolve
    play sound "audio/sound/grass steps armor running.mp3"
    show eirene focused grimace1 with dissolve
    hide eirene with dissolve
    show elisanne surprised frown2 with dissolve

    stop music fadeout 1

    elly "There you are, Finni!  Eirene and I have been looking for you for the past hour!"

    hide elisanne with dissolve
    show eirene focused grimace1 with dissolve

    eir "You told us you would go to the village, so we searched there first, but…"
    eir "..."

    play music "audio/music/CRASHER (Story Version B) intro.flac" fadeout 1.0
    queue music "audio/music/CRASHER (Story Version B).flac"

    show eirene angry shout1
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    eir "…Finni, are you damaged??  What happened?!"
    hide speechright

    hide eirene with dissolve
    show finni wink awkward1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "O-Oh, well, you know me, I’m always working hard to protect the Halidom like you do!"
    hide speechright

    hide finni with dissolve
    show eirene injured shout1 with dissolve
    eir "Yes, but I have never been this reckless about it!  I can’t believe you would go off by yourself to fight fiends this large!"
    show eirene surprised
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    eir "And I especially didn't think you'd do so without telling anyone!  I made sure you didn't have patrol duty today, too, so if we hadn't followed the fiend corpses, we never would have found you!"
    hide speechright

    hide eirene with dissolve
    show elisanne focused shout1 with dissolve
    elly "I am inclined to agree.  If circumstances were slightly worse, you might have been in serious danger and without any reinforcements to protect you."

    hide elisanne with dissolve
    show finni focused pout1 with dissolve
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    fin "Look, I don’t need protection!  I can handle myself, ok?  I’m a reliable person!"
    hide speechright

    hide finni with dissolve
    show eirene closed_neutral grimace1 with dissolve
    eir "Tall words for someone who can’t even be relied upon to stay out of danger for ONE day."
    show eirene glow_angry
    eir "Don’t you realize why I might be particularly worried about you TODAY of all days?"

    hide eirene with dissolve
    show finni surprised mouth_slightly_open
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "(Crap!  I didn’t make the connection that getting scraped up would trigger Eirene’s past trauma from this day!  I’m such an idiot!)"
    hide speechright

    show finni closed_focused awkward1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "…Oh, uh, oh yeah… I… I didn’t think of that."
    hide speechright

    hide finni with dissolve
    show eirene closed_neutral grimace2 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    eir "(sigh)  Of course you wouldn’t.  Because once again, you're not thinking about how I feel."
    hide speechright

    hide eirene with dissolve
    show finni sad frown2 with dissolve
    fin "W-What?  Eirene, I’m… I’m sorry!..."

    hide finni with dissolve
    show eirene closed_neutral frown1 with dissolve
    eir "Finni.  Please, just… go back to the Halidom and stay there for the rest of the day.  Elly and I will take care of collecting the fiend corpses so we don’t draw more beasts to the Halidom perimeter."

    show eirene pained grimace2
    eir "Can you just do that one thing for me?  No more patrol duty, or anything else strenuous today."

    hide eirene with dissolve
    show finni surprised closed_frown1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "(Oh NO!  I thought I would impress Eirene, but this had the exact opposite effect!  Now she’s hurt, disappointed in me ...AND she’s gonna spend even MORE of Valentine's Day with Elisanne!!)"
    hide speechright

    show finni wink awkward1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "Uh, I mean… Wouldn’t it be faster to have a second android helping?  I mean, no offense, but I can move a lot faster than a flesh-and-blood human, and I’m stronger too!"
    hide speechright

    hide finni with dissolve
    show elisanne flinch shout1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    elly "Oof... I know what you’re saying is true, but that still smarts a little!"
    hide speechright

    stop music fadeout 1

    hide elisanne with dissolve
    play sound "audio/sound/grass step.mp3"
    queue sound "audio/sound/grass step.mp3"
    queue sound "audio/sound/grass step.mp3"
    show eirene glow_focused frown2 with dissolve
    eir "...Fortunately, it looks like another android has already arrived."

    hide eirene with dissolve
    show finni surprised pout1 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    fin "…Laxi??  What are YOU doing here?"
    hide speechright

    hide finni with dissolve
    show laxi with dissolve
    lax "Eirene asked me to look into a matter, so I came to report back to her.\n>>We've been looking everywhere for you!<<"
    lax "Regarding that inquiry:  we believe that Elisanne's physiology should be sufficiently compatible enough with Eirene’s neurosimulative circuits to allow for the required sensory stimulation to—"

    play music "audio/music/CRASHER (Story Version C) intro.flac" fadein 1.0
    queue music "audio/music/CRASHER (Story Version C).flac"

    hide laxi with dissolve
    show finni surprised frown2 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    fin "...Wait... WHAT?!?"
    hide speechright
    fin "What kind of 'sensory stimulation' are Elisanne and Eirene exactly going to be partaking in here???"

    hide finni with dissolve
    show laxi with dissolve
    lax ">>Um, Laxi?  I don’t think you were supposed to say that part in front of Finni...<<"

    hide laxi with dissolve
    show elisanne blush pout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "And—why did you have to PHRASE it like that?!?"
    hide speechright

    hide elisanne with dissolve
    show laxi surprised with dissolve
    lax "...I appear to have made an error in judgment.  Terminating conversational circuits."

    hide laxi with dissolve
    show finni shocked grin1 with dissolve
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    fin "No, keep talking!  I'd LOVE to hear exactly what Eirene has planned for herself and Elisanne later!  Because it really sounds like something her PARTNER should know about!"
    hide speechright

    show finni surprised shout1
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "Unless... maybe the point... IS to replace me...?"
    hide speechright

    hide finni with dissolve
    show eirene glow_angry grimace2 with dissolve
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    eir "I don't understand the conclusions you're coming to, but I think it would be better for you to go back to the castle like I asked.  Right now."
    hide speechright

    hide eirene with dissolve
    show elisanne sad shout1 with dissolve
    elly "Look, I REALLY think there’s a misunderstanding here.  Please, just listen—!"

    stop music fadeout 1.0

    hide elisanne with dissolve
    play sound "audio/sound/fiend roar.mp3"
    show fiend leader with dissolve
    fie "RROAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRR!!!!!!!!!!"

    hide fiend with dissolve
    play sound "audio/sound/exclamation.wav"
    show finni shocked mouth_slightly_open

    play music "audio/music/CRASHER (Story Bout C).flac" fadeout 1.0

    fin "!"
    fin "What—?!"

    hide finni with dissolve
    show laxi focused grimace1 with dissolve
    lax "Hostile confirmed.  Preparing for combat protocols.\n>>Oh no!!!  The scent of the fiends Finni killed wound up attracting a BOSS fiend!!<<"

    hide laxi with dissolve
    show elisanne angry shout1 with dissolve
    elly "I'll help too!"

    hide elisanne with dissolve
    show finni focused
    show finni shout1
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    fin "F-Forget it!!  This is my mess, and I'm going to show Eirene that I can take care of myself!"
    hide speechright

    play sound "audio/sound/grass steps running.mp3"
    show finni angry
    fin "HAAAAAAAAAAAAAAAAAAAAAAHHHH!!!"

    hide finni with dissolve
    show eirene glow_focused shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    eir "Finni, don't—!!!"
    hide speechright

    hide eirene with dissolve
    show fiend leader with dissolve
    play sound "audio/sound/blade slice flesh.mp3"
    show finni angry shout1 with dissolve
    fie "ROAA— *wince*"

    show finni wink smile1
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    fin "See?  I told you I could handle it!!  Now I just need to—"
    hide speechright

    play sound "audio/sound/click.mp3"
    queue sound "audio/sound/click.mp3"
    queue sound "audio/sound/click.mp3"
    show finni surprised frown2
    queue sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    fin "Wait, why can't I move my arm?...  Oh no..."
    hide speechright

    hide finni with dissolve
    hide fiend with dissolve
    show laxi angry shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    lax "Outlook deteriorating.  Hostile has exploited Finni's previous damage to break her shoulder servo.  Engaging in immediate intervention."
    hide speechright

    hide laxi with dissolve
    show eirene glow_angry grimace1 with dissolve
    eir "Finni, hold on!!!  HAAAAAAAAAAAAAAAAH!!!!"

    hide eirene
    play sound "audio/sound/fiend roar.mp3"
    show fiend leader with dissolve
    show finni flinch shout1 with dissolve
    fin "How—how did this go so wrong???"

    image field_gray = "images/backgrounds/Sty_bg_0022_400_00.png"
    scene field_gray with dissolve
    show finni flinch mutter1 with dissolve

    fin "I wanted..."
    image black = "images/backgrounds/black.png"
    scene black with dissolve
    show finni flinch mutter1 with dissolve

    fin "I just wanted..."

    show finni closed_focused
    play sound "audio/sound/grass standing up.mp3"

    stop music fadeout 2.0

    fin "..."
    hide finni with dissolve


    jump myfinnivalentinemenu


label my_finni_valentine4:

    play music "audio/music/CRASHER - Failure loop.mp3" fadeout 1

    image bedroom = "images/backgrounds/Sty_bg_0049_100_00.png"
    scene bedroom with fade

    show finni closed_focused mutter1 with dissolve
    fin "...(sigh)..."

    show finni sad
    fin "...In the end, I was completely useless, and Eirene had to team up with Elisanne again to drive off the fiend...  I guess that's what I deserve for acting stupid..."

    show finni flinch frown1
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "On top of that, it took Laxi, Mascula and Chelle three hours of working together just to replace my bum arm’s servo.  This really couldn’t be any worse..."
    hide speechright

    show finni pained
    fin "And... what was Laxi really talking about with Eirene and Elisanne’s \"sensory compatibility\"?  She wouldn’t give me a straight answer the whole time she was helping with the repair job..."

    show finni closed_focused pout1
    fin "(sigh) Well, I guess there isn’t anything else to do but wait for this lousy day to be over..."

    hide finni with dissolve

    play sound "audio/sound/door knock.mp3"
    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadeout 1

    play sound "audio/sound/heart.wav"
    vchel "Ohhh, Luccyyy!  Where are youuuu?"

    show finni surprised frown1 with dissolve
    fin "Hm?"

    hide finni with dissolve
    queue sound "audio/sound/door open.mp3"
    show vchelsea focused smile4 with dissolve
    vchel "Hey, Finni.  Have you seen my Luccy around anywhere?"

    show vchelsea relaxed frown1
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    vchel "Our date was going so well, but... then when I tried to fetch Hildegarde so she could marry us, he suddenly vanished!"
    hide speechright

    hide vchelsea with dissolve
    show finni wink mutter1 with dissolve
    fin "Nope.  Nobody in here but plain ol’ me."

    hide finni with dissolve
    show vchelsea wide pout1 with dissolve
    vchel "Aw... I was really hoping he’d be here..."

    stop music fadeout 1

    hide vchelsea with dissolve
    show finni neutral mutter1 with dissolve
    fin "...Hey, you and Luca are kind of an item, right?"

    hide finni with dissolve
    show vchelsea with dissolve
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    vchel "Well, YEAH!  We're totally soulmates!!"
    hide speechright

    hide vchelsea with dissolve
    show finni neutral mutter1 with dissolve
    fin "...Well, uh... what would you do if... Luca moved on to someone else?"

    play music "audio/music/Yumemiteta no Atashi (Story Version A) intro.flac" fadeout 1.0
    queue music "audio/music/Yumemiteta no Atashi (Story Version A).flac"

    hide finni with dissolve
    show vchelsea surprised frown2 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    vchel "...Moved on?"
    hide speechright

    show vchelsea neutral smile3
    vchel "...I don't think that would ever happen."

    hide vchelsea with dissolve
    show finni shocked frown2 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "Surely that's just being overly optimistic, though?  People don't stay the same forever.  And... sometimes they outgrow people."
    hide speechright

    hide finni with dissolve
    show vchelsea focused_closed smile5 with dissolve
    vchel "That’s true, but I’m not worried.  Nobody knows Luca better than I do!"

    hide vchelsea with dissolve
    show finni surprised frown1 with dissolve
    fin "What do you mean?"

    hide finni with dissolve
    show vchelsea serious smile1 with dissolve
    vchel "Even before Luca knew about me, I was watching him from afar.  And when we started dating, I was paying attention to him every second of the day.  And recording everything in my heart."

    show vchelsea focused smile5
    vchel "I know everything about him, from his favorite food to his ideal vacation spots to his ultimate dream of making a place where all kinds of people can live in harmony."

    show vchelsea relaxed smile2
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    vchel "Most people think that I just like Luca because he’s a hunk, but… it’s actually his heart that I love the most.  Luca saved me when I thought I was going to disappear.  He’s my hero."
    hide speechright

    hide vchelsea with dissolve
    show finni shocked mouth_slightly_open with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "(Wow.  I thought that Chelsea was just a crazy stalker, but what she's saying right now is... actually sort of resonating with me!!)"
    hide speechright

    hide finni with dissolve
    show vchelsea focused smile5 with dissolve
    vchel "I'm confident that Luca won't fall for anyone else, because… he wants someone who loves him for who he is, and, well... there's nobody who knows about his own heart than me."

    hide vchelsea with dissolve
    show finni surprised frown2 with dissolve
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos
    fin "You know what?  You're RIGHT!!"
    hide speechright

    hide finni with dissolve
    show vchelsea with dissolve
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    vchel "Duhh, of course!  I'm the #1 Luccy expert."
    hide speechright

    hide vchelsea with dissolve
    show finni flinch with dissolve
    fin "N-No, not about your Luca stuff.  What I mean is that Eirene and I have a thousand years' worth of history!!  It's literally impossible for anyone to be closer to her than me!"

    hide finni with dissolve
    show vchelsea surprised frown1 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    vchel "Uh... what are you talking about?  Weren't you asking about Luccy and my compatibility?"
    hide speechright

    hide vchelsea with dissolve
    show finni focused frown1 with dissolve
    fin "I've been going about this all wrong from the beginning.  Instead of trying to make myself more like Elly, I should think about how EIRENE feels, just like she's been asking me to!"

    show finni closed_focused frown1
    fin "Think... why would Eirene be upset about all the stuff I've been doing today?  Hmmmm...  I need to... 'consider her feelings'...  'Stay safe'...  And she took me off patrol duty..."

    hide finni with dissolve
    show vchelsea surprised frown1 with dissolve
    vchel "Uh... Earth to Finni?  Hello?"

    hide vchelsea with dissolve
    show finni shocked frown1 with dissolve
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos
    fin "Oh!  Of course!  All my unusual behavior must be making her think I'm malfunctioning!!!  This day DOES bring up those sorts of memories for her!"
    fin "So... she's been consulting Laxi, since she helped last time I went berserk!  She wants to make sure my sensory functions aren't glitched."
    hide speechright

    show finni surprised smile2
    fin "Of COURSE she wouldn't want to confront ME about it; if I got upset, it could accelerate the 'corruption' process!  So she's been confiding in Elly, who's a close work associate!"
    fin "So... all I need to do is talk to Eirene and check in with her so she knows that I've just been feeling insecure, not glitched.  One system check later, and all her worries will disappear!"

    show finni relaxed smile1
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    fin "Thanks, Chelsea, I feel SO much better now!  I'm gonna go talk to Eirene right now!!"
    hide speechright

    play sound "audio/sound/grass steps armor running.mp3"
    hide finni with dissolve
    show vchelsea surprised smile2 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    vchel "Oh, well, uh... I'm glad I was able to help?—"
    hide speechright

    stop music fadeout 1

    show vchelsea relaxed
    vchel "—Aaaaand she's gone.  Man, some people sure can be crazy when it comes to love."

    show vchelsea serious frown1
    vchel "Well, I'd better go find Luccy while I still have the caterer around—"

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadeout 1

    hide vchelsea with dissolve
    show luca sweat with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    luc "Pssst!  Finni, are you in there?  Chelsea's trying to marry me and I really need somewhere to hide out for the next—"
    hide speechright

    show luca surprised frown5
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    luc "—WAAAAAAAAHHH!!!!"
    hide speechright

    hide luca with dissolve
    show vchelsea blush drool2 with dissolve
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    vchel "LUCCCYY!!!  THERE YOU ARE, MY DARLING!!!"
    hide speechright

    hide vchelsea with dissolve
    show luca surprised sweat with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    luc "A-Ah, whoops!!  I just remembered, there's somewhere I need to be!!!"
    hide speechright

    hide luca with dissolve
    show vchelsea cry shout1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    vchel "Where are you going, Luccy?!  Take me with youuuuuu!!!"
    hide speechright

    stop music fadeout 1


    image halidom_hallway = "images/backgrounds/Sty_bg_0050_100_00.png"
    scene halidom_hallway with fade

    show finni sad shout1 with dissolve
    fin "Eirene?  Are you around here?  I wanted to apologize for earlier—"
    hide finni with dissolve

    elly "—and you're still sure you want to go through with this?"

    show finni pained mutter1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "Ugh, that's Elly in her room.  Maybe I should apologize to HER too... I was pretty passive-aggressive earlier..."
    hide speechright
    hide finni with dissolve

    eir "Of course.  At this point, it's the only way to set things right after everything that happened."

    show finni surprised closed_awkward1 with dissolve
    fin "(Wait... is that Eirene?  Is she having some kind of meeting with Elisanne?)"
    hide finni with dissolve

    elly "I understand your reasons, but… perhaps you should check in on Finni first?"

    show finni pained mouth_slightly_open with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "(Should I interrupt them?  I don't wanna eavesdrop, but—  I mean… they're talking about me…)"
    hide speechright
    hide finni with dissolve

    eir "…It will probably be better for me to stay away from Finni for now.  Not until I have something to offer her."

    elly "Very well.  But… are all these… erm, 'preparations' really necessary?  Why am I dressed like this?"

    show finni surprised mouth_slightly_open with dissolve
    fin "(Aaaaaa!  I need to know what’s happening!  A quick peek won’t hurt anyone, right?!)"

    show finni shocked
    fin "(If I just look through the keyhole… wh…. What am I…?!)"

    play music "audio/music/24h (Story Version) intro.flac" fadein 6.0
    queue music "audio/music/24h (Story Version).flac"

    image elly_bedroom = "images/backgrounds/Sty_bg_0049_101_00.png"
    scene elly_bedroom with fade

    show selisanne blush pout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    selly "I feel so embarrassed… These clothes are fairly… revealing, aren’t they?"
    hide speechright
    hide selisanne with dissolve

    show eirene with dissolve
    eir "That is the idea, is it not?  I need access to as much of your bare skin as possible."
    hide eirene with dissolve

    show selisanne blush pout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    selly "Wh-When you put it like that, it sounds…!"
    hide speechright
    hide selisanne with dissolve

    show eirene relaxed mutter2 with dissolve
    eir "Shh… Don't make such a fuss, or people will come knocking.  If you simply open your mouth, then I'll take care of the rest…"
    hide eirene with dissolve

    show selisanne closed_blush pout1 with dissolve
    selly "O-Ok… I suppose I have no choice…"

    scene halidom_hallway with fade

    show finni shocked open_awkward1 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    fin "(Wh… What am I looking at?!?!  Why is Elisanne in her bathing suit?  Why is she lying down on her bed like that?)"
    hide speechright
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "(Wait, is—is Eirene getting on TOP OF ELISANNE?!?  Don’t tell me—!)"
    hide speechright

    scene elly_bedroom with fade

    show selisanneSTR closed_blush pout1 at selisanneSTRpos_embrace
    show eirene behind selisanneSTR with dissolve

    selly "Oh my… this is quite… ticklish…!"

    eir "I apologize; I'm attempting to be gentle.  In any case, prepare your senses, because here it comes…"

    show eirene glow_focused

    show selisanneSTR smile1
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    selly "Oh… Ohhhh, wow!  This…  This is AMAZING!!"
    selly "To think that an android could produce something this exceptional!"
    hide speechright

    show eirene smile1
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    eir "You should expect no less, since it comes from an exceptional android."
    hide speechright

    show selisanneSTR smile2
    selly "W-Well, in any case, as strange as this felt initially, I feel fortunate that you chose me as your subject for this!"

    eir "And I you.  This pleasure data is exactly what I was looking for.  But I want to be extra thorough, so prepare yourself for a second taste..."

    scene halidom_hallway with fade

    stop music fadeout 1.0

    show finni surprised open_shout1 with dissolve
    fin "…"
    show finni shocked
    fin "…"
    show finni angry
    fin "…"

    play music "audio/music/CRASHER (Story Bout C).flac" fadeout 1.0

    show finni angry shout1
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    fin "THAT SPEAR-TOTING HUSSY!!!"
    fin "WHO DOES THAT FILTHY FLESHBAG THINK SHE IS???"
    hide speechright

    show finni shocked pout1
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    fin "I don’t even get this… why would Eirene…?  And after all this time…?"
    hide speechright

    show finni closed_focused frown1
    fin "…It’s ok.  This is fine.  I'm sure there's a perfectly reasonable explanation for this."

    stop music fadeout 1.0

    show finni_crop closed_focused closed_grin1 at finni_crop_pos
    hide finni
    show finni_crop at finni_crop_shake
    fin "…"

    play music "audio/music/CRASHER (Story Version C) intro.flac" fadeout 1.0
    queue music "audio/music/CRASHER (Story Version C).flac"

    show finni_crop angry grin1
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    fin "…A perfectly reasonable explanation that I'm gonna BEAT OUT OF ELLY WITH MY BARE FISTS!!!"
    hide speechright

    show alex_back angry frown1 at alex_back_ambush_pos behind finni_crop with fade
    show finni_crop surprised shout1 at finni_crop_pos

    stop music fadeout 1.0

    ale "If you so much as lay a finger on Elisanne, I will personally slice every single wire out of your chassis until even Chelle can’t put you back together again."

    show finni_crop at finni_crop_leap_right
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_upperrightpos
    fin "B-BAH!?  Alex?!?  Where did you come from?!?  How long have you even been there?!?"
    hide speechright

    play music "audio/music/CRASHER - Failure loop.mp3" fadein 2.0

    show alex_back focused
    ale "Long enough to know that you’re making a big mistake."

    show finni_crop shocked pout1
    fin "A mistake?!  Are you even seeing what's going ON in there?!"

    show alex_back closed_focused
    ale "(sigh) As cliché as I'm sure this sounds, it's actually not what it looks like."
    ale "Just… calm down for a second.  Put away the hydraulics and let's talk this out."

    show finni_crop closed_angry closed_frown1
    fin "…"

    show finni_crop angry frown1
    fin "…I'll give you twenty seconds, and if I don't like what I hear by then, I start smashing."

    hide finni_crop with dissolve
    show alex_back at alex_back_ambush_to_regular
    ale "Great.  I'll get right to the point, then."

    hide alex_back
    show alex focused frown1

    ale "First of all, you’re completely misunderstanding the situation between Elisanne and your precious Eirene."

    show alex askance

    ale "This isn't a tryst.  Just like you, Eirene is a combat android, so you should already know that she isn't designed to require… that sort of thing."
    ale "(sigh) I shouldn't even be telling you this, but, in fact, Eirene's doing this entirely for your sake."

    hide alex with dissolve

    show finni surprised pout1 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    fin "F… For my—?  What?"
    hide speechright

    hide finni with dissolve

    show alex askance mutter1 with dissolve

    ale "It would be a breach of confidence to tell you more, but I would urge you to be patient in this matter."

    show alex focused frown1

    ale "Secondly, I know with complete certainty that Elisanne has no interest in Eirene from a romantic perspective."

    show alex askance grimace1
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    ale "As far as I can tell, she only has eyes for the prince.  And I’m not sure if even she herself realizes THAT much."
    hide speechright

    hide alex with dissolve
    show finni focused pout1 with dissolve

    fin "Oh, is that so?  And what makes you such an expert on the subject, huh?"

    hide finni with dissolve
    show alex sad smile1

    play music "audio/music/CRASHER (Story Version A) loop.mp3" fadeout 1.0 fadein 2.0

    ale "Because... I only have eyes for Elisanne.  I love her completely.  In fact, I probably know her better than she knows herself."

    show alex focused frown1

    ale "And if YOU love Eirene as much as you profess, you should know understand HER heart as well."

    show alex closed_focused

    ale "However, I can tell that you’re feeling unworthy, and afraid of being abandoned.  I think that’s getting in your way.  Trust me, I'm speaking from firsthand experience."

    hide alex with dissolve
    show finni pained shout1 with dissolve
    fin "So what?  I should just… throw my hands up and say 'whatever?!'  I’m… I’m nothing without Eirene.  She’s everything to me!  And if she starts getting all cosy with Elisanne—"

    hide finni with dissolve
    show alex with dissolve

    ale "It’s not about giving up, it’s about trusting in Eirene’s judgment and accepting her choices."

    hide alex with dissolve
    show finni surprised mutter1 with dissolve

    fin "What?"

    hide finni with dissolve
    show alex focused frown1 with dissolve

    ale "If you love Eirene, you should also want her to achieve her goals and live the life she wants to live."
    ale "Being possessive of her just to satisfy your own insecurities isn’t helping her, it’s hurting her AND you."

    hide alex with dissolve
    show finni surprised mutter1 with dissolve

    fin "Wait, that's like..."


    show laboratory at sepia with fade


    show grace at sepia with dissolve

    gra "He once saw me having lunch with a male researcher off in private, and he swooped in and practically dragged me away…  It did bother me that his insecurities sometimes brought him to interfere with my social life…"


    scene halidom_hallway with fade

    show finni shocked pout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "…Crap, have I seriously spent the whole day being a possessive girlfriend???  Ughhh, why didn’t I realize it sooner???"
    hide speechright

    hide finni with dissolve
    show alex askance smile1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    ale "Well, maybe a little.  That being said, this particular (ahem) {i}scenario{/i} is almost DISTURBINGLY easy to misinterpret.  Talk about tactless on Eirene's part to not even warn you..."
    hide speechright

    hide alex with dissolve
    show finni pained smile1 with dissolve

    fin "...Tell me about it..."

    show finni surprised frown1
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "But wait... isn't this scenario even worse for YOU?  I mean, Elly isn't even interested in you, right?"
    hide speechright

    hide finni with dissolve

    show alex askance grimace1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    ale "Yeah... she's lowkey… (ahem) kind of homophobic.  In a really cringy way."
    hide speechright

    show alex askance smile1

    ale "…But I love her anyway, and that means I accept her in spite of her flaws, and regardless of who she loves.  If the Prince will make her happy, then I want that for Elly as well."

    show alex closed_focused grimace1

    ale "I... I owe my life to Elisanne, and that means that I’ll support her no matter what.  ...My feelings exist for her sake, not my own..."

    hide alex with dissolve
    show finni pained frown1 with dissolve

    fin "Still… that’s such a hard way to live…  I never would have guessed you have it even tougher than I do."

    hide finni with dissolve

    show alex surprised pout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    ale "…Really??  I’m an orphan who lost my parents as a child, then became an assassin who was raised by a heartless sect of priests, being told that murder was the only path for a sinner like me…"
    ale "…and THEN became a hunted target when I defied an order to kill my only friend in the world… and THIS is what made you think I have a hard life?"
    hide speechright

    hide alex with dissolve
    show finni surprised awkward1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "Oh… oh yeah… now that you mention it…"
    hide speechright

    hide finni with dissolve
    show alex closed_focused grimace1 with dissolve

    ale "(sigh) Anyway, let’s say that at this point, I’ve learned to bury my emotions pretty deep…"
    ale "…Which is good, since later this evening, I get to look forward to watching Elly give Euden the chocolate she made by hand…"

    hide alex with dissolve
    show finni pained pout1 with dissolve

    fin "Yeesh…  I’m sorry…"

    hide finni with dissolve
    show alex askance smile1 with dissolve

    ale "W-Well, as things are now, I’m able to atone in part for my past while also standing by the side of the one I love.  I couldn’t ask for anything more..."

    hide alex with dissolve
    show finni surprised mutter1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "Uh, well, I suppose that’s very... erm, noble of you.  What with the 'suffering in silence' bit and all..."
    hide speechright

    hide finni with dissolve

    stop music fadeout 1.0

    elly "Ah!  You want ANOTHER?  This isn’t overly unpleasant, but I had no idea that this would be so… prolonged!"

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3"

    eir "It’s imperative for me to collect data on the aftereffects as well.  This time, let me focus on the legs and feet..."

    elly "Eek!  Your hands are so cold!  Aaaaah!  And ticklish!!"

    show alex closed_blush grimace1 with dissolve
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    ale "...Tsk..."

    hide alex
    show alex_back closed_blush grimace1 at alex_back_pos

    ale "…That being said, I can’t say I like this particular 'arrangement' any more than you do…"
    hide speechright

    hide alex_back with dissolve
    show finni closed_angry mutter1 with dissolve
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    fin "Y...Yeah...  Obviously it's not right to smash Elly's face in, so maybe I'll use that new statue of Prince Emile as a stand-in."
    hide speechright
    fin "You know, the gaudy bronze one he installed without permission yesterday in the middle of the third-floor hallway?  You can't even walk around it, so the prince said it needs to go anyway."

    hide finni with dissolve

    elly "Oh!!  Eirene!!!"

    show alex_back closed_blush grimace1 with dissolve
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    ale "…Let me know when you’re done; I've been meaning to test how well my new dagger cuts through bronze…"
    hide speechright

    hide alex_back with dissolve


#    ale "In order to complete her intended surprise, Elisanne requires neurological data that Elly's volunteered to provide.  What you're observing is a body scan."

#    fin "Well, it's definitely a SURPRISE, all right!  If she's supposedly doing this… 'SCAN' for me, then wouldn't she should have asked first?"

#    ale "I'm inclined to agree with you.  This is a considerably more… (ahem) intimite process than I was initially led to believe."

#    ale "But that doesn't change the fact that



    jump myfinnivalentinemenu


label my_finni_valentine5:

    play music "audio/music/Yumemiteta no Atashi (Story Version A) intro.flac" fadeout 1.0
    queue music "audio/music/Yumemiteta no Atashi (Story Version A).flac"

    image courtyard_sunset = "images/backgrounds/Sty_bg_0027_200_00.png"
    scene courtyard_sunset with fade

    show finni closed_pained mutter1 with dissolve

    fin "(sigh) What am I going to do?"

    show finni pained

    fin "Things are such a mess between me and Eirene now, and… on top of that, I’m also feeling hurt myself…"

    scene field_day at sepia with fade
    # I deleted the clouds3 clause
    show eirene closed_neutral grimace2 at sepia with dissolve
    eir "(sigh)  Of course you wouldn’t.  Because once again, you're not thinking about how I feel."

    scene courtyard_sunset with fade
    show finni pained frown1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "I did a bunch of stuff because I wanted to prove to Eirene that I was good enough to be her partner, but instead I just made everything worse."
    hide speechright

    show finni closed_focused
    fin "I know that I’m being a little selfish, and I shouldn’t make my problems Eirene’s…"

    show finni pained pout1
    fin "…But…"

    scene bedroom at sepia with fade
    show vchelsea relaxed smile2 at sepia with dissolve
    vchel "Most people think that I just like Luca because he’s a hunk, but… it’s actually his heart that I love the most.  Luca saved me when I thought I was going to disappear.  He’s my hero."

    scene courtyard_sunset with fade
    show finni pained shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "…my feelings haven’t changed, either!  Eirene is MY hero!  She’s everything to me!  But..."
    hide speechright

    scene halidom_hallway at sepia with fade
    eir "…It will probably be better for me to stay away from Finni for now.  Not until I have something to offer her."

    scene courtyard_sunset with fade
    show finni closed_angry shout1 with dissolve
    fin "But... I also don't want to be a burden to her, either!  It's at the point where she feels like she can't even tell me what's wrong!"

    fin "What am I supposed to do here?  What are WE supposed to do??"

    scene halidom_hallway at sepia with fade
    show alex closed_focused grimace1 at sepia with dissolve
    ale "I... I owe my life to Elisanne, and that means that I’ll support her no matter what.  ...My feelings exist for her sake, not my own..."

    scene courtyard_sunset with fade
    show finni_crop sad mouth_slightly_open at finni_crop_right with dissolve
    fin "..."

    stop music fadeout 1.0

    show eirene_crop sad behind finni_crop at left with dissolve
    eir "...Hello, Finni."

    show finni_crop surprised shout1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_upperrightpos
    fin "—E-Eirene!  I… um…!!"
    hide speechright

    show eirene_crop surprised frown1
    eir "I was hoping I could take you aside for a few minutes.  But... first, are you feeling any better?"

    show finni_crop shocked awkward1
    fin "Y-Yeah, I’m doing a lot b—"

    show finni_crop neutral mouth_slightly_open
    fin "..."

    play music "audio/music/New Alberia.flac" fadein 3

    show finni_crop closed_focused frown1
    fin "...No, I'm through with putting on a front to try to impress you.  I’ve been feeling really awful and scared lately."

    hide finni_crop with dissolve
    show eirene_crop closed_neutral mutter2
    eir "...I thought that might be the case.  Thanks for finally telling me."

    hide eirene_crop with dissolve
    show finni sad frown1 with dissolve
    fin "Y-Yeah... Thanks to everything going on, I've been really scared.  Feeling like I'm not good enough.  Scared that you've... given up on me."

    show finni closed_focused mutter1
    fin "I… I saw what you and Elisanne were doing this afternoon."

    hide finni with dissolve
    show eirene surprised frown2 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    eir "I.. I see.  That's... unfortunate.  I hope you will understand once I give you the results."
    hide speechright

    hide eirene with dissolve
    show finni closed_angry shout1 with dissolve
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    fin "Well, I don't know HOW I'm supposed to understand!  I don't know what's going on with you anymore!"
    hide speechright

    show finni sad mutter1
    fin "But... Elly seems to know.  I can tell you two have been... really close lately.  And... that actually hurt me a lot, if I'm being honest."

    hide finni with dissolve
    show eirene pained grimace2 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    eir "Finni... I had no idea..."
    hide speechright

    hide eirene with dissolve
    show finni shocked pout1
    fin "Augh, will you stop looking at me like that!  I'm so sick of making you upset and worried all the time!"

    show finni closed_focused pout1
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "Argh, this isn't going at all how I wanted it to—I'm, I'm sorry, ok!!"
    hide speechright

    show finni closed_angry pout1
    fin "I'm sorry for being selfish, and defective, and useless!  I just... I just feel so bad ALL THE TIME!  I KNOW my heart is defective and bugged, and has a million instabilities!!"

    hide finni with dissolve
    show eirene surprised grimace1 with dissolve
    eir "Is... Is THAT what you think this is about?  Finni, I'm so sorry, I thought we'd already talked through that, I don't think—!"

    hide eirene with dissolve
    show finni closed_angry pout1
    fin "Yeah, yeah, I KNOW, ok?  \"You're nothing like the original Finni, and that's ok!  I don't think you're defective, it's ok that you have these freakouts!\"  I get it!  You've already been more than accomodating with me."

    show finni pained pout1
    fin "It's not like you're not being SUPPORTIVE enough!  It's not YOUR fault I feel this way!  But... when I see you all scared, and going out of your way to protet my feelings all the time... I just..."

    show finni closed_pained shout1
    fin "...I just... I just think that... if you'd never lost your original Finni, then you wouldn't even need to be having these kinds of conversations all the time!  I wouldn't constantly be holding you back!"

    hide finni with dissolve
    show eirene pained shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    eir "Finni... Oh dear... please wait!   That's not how I feel at all!"
    hide speechright

    hide eirene with dissolve
    show finni pained smile1 with dissolve
    fin "It's... It's ok, Eirene, you don't have to pretend that you're not hurting.  I saw how you reacted when I said I wanted to celebrate today."
    fin "And... I understand now why you were so upset when I was damaged.  Especially on the day you lost your friend."
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "I mean... heck, you even took me off patrol duty to PREVENT that exact scenario, and I STILL screwed it up!!"
    hide speechright
    fin "Let's face it, I'm kind of the resident QUEEN of bringing up painful memories for you."
    fin "It... It must be like living with a walking corpse."

    hide finni with dissolve
    show eirene closed_injured grimace1 with dissolve
    eir "Oh, F-Finni...!!  Finni, I...!!"

    hide eirene with dissolve
    show finni closed_angry pout1 with dissolve
    fin "And... I'm scared all the time too.  Scared of losing you.  Scared that you didn’t want to have to have me around as a reminder anymore."
    fin "So I grabbed on tighter.  I tried to impress you.  I wanted to be better."

    show finni closed_focused mutter1
    fin "But in doing so, I just drove you further away this Valentine's Day and right into Elisanne’s arms…"

    hide finni with dissolve
    show eirene dull mutter1 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    eir "...Uh...that's not really..."
    hide speechright

    hide eirene with dissolve
    show finni wink awkward1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "No, I know, you don't have anything romantic going on between you.  I know that."
    hide speechright

    show finni sad smile1
    fin "But… it made me realize that there could be a future where I’m no longer the person who’s most important to you…"

    show finni closed_focused mutter1
    fin "…And that terrified me."

    hide finni with dissolve
    show eirene pained grimace1 with dissolve
    eir "Oh, Finni… I’m so sorry… this is all my fault…  I've been acting so stupid…"

    hide eirene with dissolve
    show finni surprised smile1 with dissolve
    fin "B-But, it’s ok, you know?!  I got some good advice from some great people!  And I realized… I’ve been being selfish this whole time."

    fin "I thought I was looking out for you and trying to take care of YOUR needs… but I was really just feeding my OWN insecurities.  I was trying to use you to prop MYSELF up."

    show finni shocked smile1
    fin "But… I don’t want my feelings for you to be about ME!  I want them to be about YOU!  You’re the most important person in the world to me!  I love you forever and ever!!!"

    show finni closed_pained grin1
    fin "S-So, even if you don’t want me to be your 'number one' anymore, I... I can accept that, you know!  Because if that’s what you want, then I want that for you, too!"

    show finni closed_pained mutter1
    fin "For the rest of my service life, all I want is to make you happy.  As long as I can see you smiling sometimes—even just from a distance—that’s all I really care about."

    hide finni
    show finni_crop shout1 at finni_crop_shake
    fin "We… We promised to always be together, until the day we both broke down… But..."

    show finni_crop pained
    fin "…I’ve… I’ve decided to release you from that promise, Eirene!  You don't have to stay with me anymore!"
    fin "Because I don’t want ANYTHING to get in the way of your happiness!  Not even me!"

    stop music fadeout 1.0

    hide finni_crop with dissolve
    show eirene surprised grimace1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    eir "!"
    hide speechright

    show eirene closed_injured
    show eirene_crop closed_injured grimace1 at eirene_crop_shake
    hide eirene with dissolve
    eir "Finni… you idiot…"

    hide eirene_crop with dissolve
    show finni pained mouth_slightly_open with dissolve
    fin "…"

    play music "audio/music/CRASHER (Story Version A) loop.mp3" fadein 3.0

    hide finni with dissolve
    show eirene_crop closed_injured shout1 at eirene_crop_shake
    eir "I could NEVER be happy without you!!!"


    hide eirene_crop with dissolve
    show finni surprised closed_frown1 with dissolve
    fin "???"

    hide finni with dissolve
    show eirene_crop injured shout1 at eirene_crop_shake
    eir "Why can’t you see… Do you still think that all I see when I look at you is that original combat android?"
    eir "No matter how many times I tell you, you always feel like you're a disappointment to me!  But..."
    eir "...Finni, you’re the only reason I have for going on!!!  I forsook everything else just to be with you!!!"
    eir "And... now you want me to leave you?!?  Why can't I just make you understand how much I love you, and want to spend the rest of forever with you??"

    hide eirene_crop with dissolve
    show finni surprised awkward1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "H-Hey, Eirene, I wasn't saying we HAVE to go our separate ways or anything!!  I-I just wanted to let you know the OPTION was there!!"
    hide speechright
    fin "I obviously wanna stay with you, I just, well, didn't want you to feel TRAPPED, is all!  ...Geez..."

    show finni sad grin1
    fin "...Let's, uh, just forget all about it, ok?  It was just me being stupid like usual!  Talking out of my chassis without thinking!  \"Stupid Finni,\" right?  Ahaha..."

    hide finni with dissolve

    show eirene_crop closed_injured at eirene_crop_pos
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    eir "…No, there's absolutely nothing wrong with you, Finni; this is all my fault!  All day I was so focused on preparing things, but…"
    hide speechright

    show eirene_crop sad grimace1
    eir "…But… I left you all alone because I thought I was supposed to take care of things behind the scenes for you today."
    eir "But... that just made you think I hated being around you!"

    show eirene_crop closed_injured shout1 at eirene_crop_shake
    eir "I'M the stupid one, Finni!  I should have just celebrated that \"Valentine's Day\" that you wanted us to instead of… making such a mess of everything!"
    eir "You didn't need me to give you a break from patrol duties, or treat you any differently from normal…"

    hide eirene_crop with dissolve
    show finni shocked pout1 with dissolve
    fin "E-Eirene?  Oh man, I'm sorry I said anything... look at you, you're leaking coolant!"

    hide finni with dissolve
    show eirene_crop closed_injured shout1 at eirene_crop_shake with dissolve

    show hyper_bolt at item_pos with dissolve
    eir "And… if I caused you to feel even slightly less loved in order to make it... this data drive may as well just be a piece of trash!"

    hide eirene_crop with dissolve
    show finni surprised pout1 with dissolve
    fin "N-No, if you took the time to make it, of course I wanna see this, uh...!"
    fin "...\"Data drive?\"  Now that you mention it, Alex and Laxi both said something about data you were collecting."

    hide hyper_bolt with dissolve
    play sound "audio/sound/click.mp3"
    fin "Let's, see... (click)  Uh, is this... an update to my parasympathetic simulation protocol software package?"

    show finni flinch grin1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "Uh... Thanks, I guess?  I suppose this might help with the servo readjustments after my accident... I think...?"
    hide speechright

    hide finni with dissolve
    show eirene closed_neutral mutter2 with dissolve
    eir "It's not for that, it's supposed to... (sigh) Never mind, I think we should both just forget about it and go somewhere quiet together for a while."

    show eirene sad smile1
    eir "...You know, just the two of us spending time together?  ...Is that an appropriate thing to do for \"Valentine's Day?\""

    hide eirene with dissolve
    show finni surprised mutter1
    fin "Hmm... I dunno, actually?  All I heard about was the \"giving out chocolate\" thing..."


    show finni sad grin1 with dissolve
    fin "...Haha... You know what?  Who cares about what we're 'supposed' to do?  I think I obsessed too much about it anyway."
    fin "Let's just wing it.  That's how we wound up together in the first place, right?"

    show finni relaxed
    fin "So... let's start, well, \"winging.\"  ...Wanna go up the hill and watch the sunset together?"

    hide finni with dissolve
    show eirene relaxed smile1 with dissolve
    eir "...That sounds perfect."

    stop music fadeout 2.0

    hide eirene with dissolve

    play sound "audio/sound/grass step.mp3"
    pause 0.35
    play sound "audio/sound/grass step.mp3"
    pause 0.35
    play sound "audio/sound/grass step.mp3"
    show elisanne neutral frown1 with dissolve
    elly "Eirene?  Are you ready yet?  Everyone's waiting."

    hide elisanne with dissolve

    show finni surprised closed_awkward1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "..."
    hide speechright
    hide finni with dissolve

    show eirene dull with dissolve
    eir "...Oh.  Right.  I should..."
    hide eirene with dissolve

    show finni sad closed_frown1 with dissolve
    fin "..."
    hide finni with dissolve

    play music "audio/music/24h (Story Version) intro.flac" fadein 10.0
    queue music "audio/music/24h (Story Version).flac"

    show eirene relaxed smile1 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    eir "...Actually, I'm sorry, Elly, I'm calling it off.  Finni and I have somewhere more important to be right now."
    hide speechright
    eir "Isn't that right, Finni?"

    hide eirene with dissolve
    show finni surprised frown1 with dissolve
    pause 0.75
    show finni wink grin1 with dissolve
    fin "Hehe, yeah!  That sunset isn't gonna watch itself!"

    hide finni with dissolve
    show elisanne surprised pout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "Wait... What?  But what am I supposed to tell—?!"
    hide speechright

    hide elisanne with dissolve
    show eirene relaxed smile1 with dissolve
    eir "Tell them thanks, but that I realized that all the plans were unnecessary.  Nothing's more important than spending Valentine's Day with the person I love."


    show eirene focused
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    eir "...Anyway, hurry up, Finni!  We've got to move at maximum speed if we want to make it up the hill in time!"
    hide speechright

    play sound "audio/sound/grass steps armor running.mp3"
    hide eirene with dissolve
    show finni grin1 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    fin "Hey, wait for me, hee hee hee!!!  Don't tell me you're just trying to ditch me again!"
    hide speechright

    play sound "audio/sound/grass steps armor running.mp3"
    hide finni with dissolve
    show elisanne surprised shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "Wait, Eirene, hold up!!!  Wait a second, you haven't explained—!?"
    hide speechright

    show elisanne closed_neutral pout1
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    elly "...Augh, the cake's gonna be coming out any minute now!  Geez!!!  What am I supposed to do now!?"
    hide speechright

    hide elisanne with dissolve


    jump myfinnivalentinemenu








label my_finni_valentine6:

    play music "audio/music/gentle dawn temp intro.flac" fadeout 1.0
    queue music "audio/music/gentle dawn temp.flac"

    image hill_sunset = "images/backgrounds/Sty_bg_0029_200_00.png"
    scene hill_sunset with fade

    show finni surprised smile1 with dissolve
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    fin "Wow, we made it up the hill in time!  And it's so beautiful!"
    hide speechright

    hide finni with dissolve
    show eirene smile1 with dissolve
    eir "Indeed.  It's quite remarkable, even though it results from basic light diffusion phenomena."
    eir "You know, back when we were employed by Ex Machina, downtime and detours were always minimized for us.  It was seen as a waste of time."
    eir "But being away from that environment, and observing how humans live their lives, has made me appreciate the value of these kinds of excusrions."
    eir "Even if they don't have an obvious 'purpose,' they still feel... meaningful."
    hide eirene with dissolve

    show finni relaxed with dissolve
    fin "Yeah.  Especially if you do these things with someone else."
    fin "There's a lot to be said for shared experiences, I guess.  They tie people together."

    stop music fadeout 2.0

    show finni sad mutter1
    fin "..."

    play music "audio/music/Yumemiteta no Atashi (Story Version A) intro.flac" fadein 3.0
    queue music "audio/music/Yumemiteta no Atashi (Story Version A).flac"

    fin "Hey, I wanted to apologize again for acting so awkward all day.  I think the only reason I was pushing Valentine's Day so hard is because I wanted to have a new experience with you."

    show finni flinch smile1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "But... uh... maybe next time we should just get hyped about a DIFFERENT holiday?"
    hide speechright
    fin "This day's got some pretty negative undertones for you, and I should have factored that in more.  My bad."
    hide finni with dissolve
    show eirene surprised with dissolve
    eir "Well... regarding that, I think I may have been giving off the wrong impression."
    eir "This day's very significant for me, but ...in reality, I haven't associated it with negative connotations for many centures now."

    hide eirene with dissolve
    show finni shocked shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "...Wait, WHAT?!  No way!"
    hide speechright

    hide finni with dissolve
    show eirene pained smile1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    eir "Y-Yeah.  That's what I meant when I got upset and said, \"You're not thinking about how I feel.\"  ...And I'm sorry again for saying that, by the way."
    hide speechright
    eir "See, you get flustered whenever the concept of the original Finni gets involved, but..."
    eir "...as I try to keep reminding you, I'm thankful for you the way you are."
    eir "And, additionally, the original Finni's damage was the main catalyst for your creation."
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    eir "So, without disrespect for the original Finni, I feel partly... thankful for that day."
    hide speechright

    show eirene frown1
    eir "But I know that it's something you've deeply internalized, of course.  Those feelings of inadequacy won't go away overnight."

    hide eirene with dissolve
    show finni pained frown1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    fin "Yeah... I'm sorry for being such a mess..."
    hide speechright

    hide finni with dissolve
    show eirene surprised shout1 with dissolve
    eir "No, no, that's what I want to emphasize!  I don't MIND it when you need reminders that I value you!"
    eir "You're extremely important to me, and assisting you adds VALUE to my life!"

    show eirene pained grimace1
    eir "Does that make sense?  Even in your percieved 'worst' moments, you're still an enormous net positive to my happiness."
    eir "So please, don't read negativity into my feelings that isn't there!"

    hide eirene with dissolve
    show finni surprised mutter1 with dissolve
    fin "Wow... I guess it makes sense when you put it that way, but... I don't think you've ever said that to me before."

    hide finni with dissolve
    show eirene sad smile1 with dissolve
    eir "Yes, well... I'm sorry I haven't been able to convey that until now.  Interacting with humans has made me realize that I'm... not the best at conveying emotional content."
    eir "And that's why, today, I was hyper-focused on—"

    stop music fadeout 1.0

    hide eirene with dissolve
    lax ">>Laxi, Elly TOLD us not to interrupt them—!  Stop—!<<"

    show finni surprised frown1 with dissolve
    fin "Wait, is that Laxi coming up the hill...?!"

    play music "audio/music/BANG (Story Version B) intro.flac" fadein 2.5
    queue music "audio/music/BANG (Story Version B).flac"

    hide finni with dissolve
    play sound "audio/sound/grass steps armor running.mp3"
    show laxi focused frown1 with dissolve
    lax "Overruled.  Organizing and then cancelling this event was illogical, as well as a misuse of our time."
    lax "I demand the opportunity to present the results of my preparation."

    show laxi flinch shout1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos   
    lax ">>Ngh...!  I'm not gonna let you get away with this!<<\n\nI hardly think... the manner in which I give it to her... is pertinent to you!  Applying override to Mascula's control!"
    hide speechright

    show laxi focused frown1
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos   
    lax ">>H-Hey!!!  That's it!  The second my remote body gets here, I'm putting a stop to this!<<\n\nTry it then, if you think you have the capacity to do so."
    hide speechright

    hide laxi with dissolve
    show finni closed_focused mutter1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos   
    fin "Tch... and just when we finally had a minute alone... (sigh)"
    hide speechright

    hide finni with dissolve
    show eirene pained frown1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos   
    eir "Ah, my apologies.  Once again, I think I may be responsible for this..."
    hide speechright

    hide eirene with dissolve
    show laxi with dissolve
    lax "Greetings, Finni.  Eirene has issued a contradictory set of instructions.  I have, therefore, defaulted to an individual intervention."
    lax "I insist that you accept this token of my goodwill."

    show laxi frown1
    lax ">>Tsk, that's hardly a way to give someone a—<<\n\nI apologize for Mascula's intrusion into this matter.\n\n>>YOU'RE the one who's... ARGH!!!<<"

    hide laxi with dissolve
    show finni surprised awkward1 with dissolve
    show dragonyule_present at item_pos with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos   
    fin "Er... thanks?  I've always wanted an... ornate... paper and fabric cube...?"
    hide speechright

    hide finni with dissolve
    show laxi with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos   
    lax "I thank you for acknowledging my wrapping talents.  However, the contents are far more valuable than their container.  I will remain here while you open it."
    hide speechright

    hide laxi with dissolve
    show finni surprised frown1 with dissolve
    fin "Huh... Uh, well, ok, I guess...?"
    play sound "audio/sound/paper rustling.mp3"
    hide dragonyule_present with dissolve
    show finni surprised smile1
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos   
    fin "...Oh!  Is this some kind of mechanical oil?  But... it looks kinda pearlescent, too!"
    hide speechright

    hide finni with dissolve
    show laxi with dissolve
    lax "Precisely.  This facial joint oil was specially formulated by Zardin to enhance both the lubrication and natural beauty of the android form."
    lax "I have been making use of it for several weeks, and wanted to share my secret."

    show laxi_face_sparkles at laxi_face_pos
    lax "Now you can be just as radiant as me."

    hide laxi_face_sparkles with dissolve
    hide laxi with dissolve

    show finni surprised mutter1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos   
    fin "Wow, that's REALLY radiant..."
    hide speechright

    show finni smile1
    fin "Anyway, uh, this is a really nice surprise!  Thank you so much!"

    show finni surprised grin1
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos   
    fin "But... uh... why are you giving this to me out of the blue—?"
    hide speechright

    hide finni with dissolve
    show mascula angry shout1 with dissolve
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos   
    masc "AHA!!  I've got you NOW, Laxi!!!  Shame on you for bothering Finni and Eirene right now!"
    hide speechright

    hide mascula with dissolve
    show laxi focused smile1 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos   
    lax "You are too late, Mascula.  My mission was already successful.  Heh heh."
    hide speechright

    hide laxi with dissolve
    show mascula closed_neutral mutter1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos   
    masc "Sigh... Laxi, you're so selfish sometimes..."
    hide speechright

    show mascula sad smile1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos   
    masc "...Well, since she's already ruined the mood, I may as well give you MY gift..."
    hide speechright

    hide mascula with dissolve
    show finni surprised mutter1 with dissolve
    fin "Wait, YOU have something for me too?"

    hide finni with dissolve
    show mascula smile1 with dissolve
    masc "Well, yeah.  It's probably not as good as Laxi's, but I got you a new whetstone for your axe."
    masc "It's... well, it's not much, but it should last a while.  And I laser-engraved your name on it!"

    show mascula surprised mutter1
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos   
    masc "...Oh!  And Chelle had somewhere else she needed to be, but... she said I should give this to you, too."
    hide speechright
    masc "Apparently it's a module that can apply extra torque to your wheel engines for ascending steep slopes."

    hide mascula with dissolve
    show finni surprised grin1
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos   
    fin "Whoa, this is really cool!  And my old whetstone's been a dud for ages; I really needed this!  Thanks!"
    hide speechright

    show finni shout1
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos   
    fin "...Wait, hold up!  Why is everybody suddenly giving me stuff??"
    hide speechright

    hide finni with dissolve
    show mascula surprised frown1 with dissolve
    masc "Wait, Eirene, you still haven't told her?  I assumed that you cancelled because she didn't like it for some reason."

    show mascula angry shout1
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos   
    masc "...Urgh, Laxi!!  Look what you've done now!  Earlier you almost ruined Eirene's present, and now THIS!"
    hide speechright

    hide mascula with dissolve
    show laxi surprised mutter1 with dissolve
    lax "...But under the circumstances, I believe YOUR present is what led to the current line of questioning, affirmative?"

    hide laxi with dissolve
    show mascula closed_neutral grimace1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos   
    masc "...Arghh!!!  You're right!!!  I'm sorry, Eirene!"
    hide speechright

    show mascula angry shout1
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos   
    masc "...Hey, wait!  You're just trying to distract me from how mad I am at you!  Laxi!!!"
    masc "I mean, do you see anyone ELSE running up the hill to deliver presents?"
    hide speechright

    play music "audio/music/BANG (Story Version A) intro.flac" fadeout 1.0
    queue music "audio/music/BANG (Story Version A).flac"

    hide mascula with dissolve
    play sound "audio/sound/grass steps armor running.mp3"
    show karl with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos   
    kar "AHA!!!  So you and Eirene were hiding out here!!!  Thank goodness my dogged pursuit of justice has heightened my senses!!!"
    hide speechright

    hide karl with dissolve
    show mascula closed_neutral grimace1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos   
    masc "...I stand corrected..."
    hide speechright

    hide mascula with dissolve
    show karl closed_focused grimace1 with dissolve
    kar "You see, when the party was cancelled, I was quite distraught."
    kar "Not being able to reward a member of the Elite Justice Search on her special day would be a miscarriage of JUSTICE!!!"

    hide karl with dissolve
    show mascula surprised grimace1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos   
    masc "Psst!  Karl!  'ix-nay' on the 'arty-pay!'  ...Karl?!"
    hide speechright

    hide mascula with dissolve
    show karl focused grin1 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos   
    kar "So I decided that, in order for justice to prevail, I would simply have to bring the celebration to her!!!  The others are already on their way!!!"
    hide speechright

    hide karl with dissolve
    show eirene surprised shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos   
    eir "Oh, no, please tell me you didn't!  I thought I said...!"
    hide speechright

    show eirene closed_injured grimace1
    eir "...Urgh, I'm sorry Finni, I KNOW you wanted alone time with me, so I tried to call things off..."
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos   
    eir "...but it looks like my earlier actions are catching up with me... I'm so embarrassed..."
    hide speechright

    hide eirene with dissolve
    show finni surprised shout1
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos   
    fin "Hang on, I'm REALLY confused now!!  What the heck is going on, and why does everybody keep giving me gifts and mentioning some kind of \"party?\""
    hide speechright

    hide finni with dissolve
    play sound "audio/sound/grass step.mp3"
    pause 0.45
    play sound "audio/sound/grass step.mp3"
    pause 0.45
    play sound "audio/sound/grass step.mp3"
    show linus with dissolve
    linu "Hey guys, hope I'm not late or anything.  I really got thrown for a loop when Karl told me the party was moved."
    hide linus with dissolve
    play sound "audio/sound/grass step.mp3"
    pause 0.35
    play sound "audio/sound/grass step.mp3"
    pause 0.35
    play sound "audio/sound/grass step.mp3"
    show luca with dissolve
    luc "Hey, Mascula!  Thanks for inviting me to this!  Come to think of it, I should throw one of these for YOU next year!"
    show luca sad
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos   
    luc "Plus, with more notice, I'll be able to get a better gift than apples..."
    hide speechright
    hide luca with dissolve
    show vchelsea with dissolve
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos   
    vchel "As far as I'm concerned, your presence ALONE is already enough of a gift, my sweet Luccy!!!"
    hide speechright
    hide vchelsea with dissolve

    play sound "audio/sound/grass steps armor running.mp3"
    show elisanne pained shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos   
    elly "(pant) I'm SO sorry, Eirene!  (pant) I EXPLICITLY told everyone NOT to bother you guys, but they all immediately dashed off!!  (pant)"
    hide speechright
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos   
    elly "It was a foolhardly mistake to tell them where you were going... (sigh)"
    hide speechright

    hide elisanne with dissolve
    show alex surprised with dissolve
    ale "...Hey, Finni.  Sorry to intrude."
    hide alex with dissolve

    show eirene sad grimace1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    eir "Don't worry, Elly, you were a lot of help earlier.  I'm just reaping what I sowed..."
    hide speechright
    eir "Although I'm sad Finni's the one who had to pay the cost... Back then, I didn't realize she just wanted time alone with me, and so the plans fell apart."
    hide eirene with dissolve

    show finni frown1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "Uhhh, Eirene?  Can you PLEASE explain what's going on??  Why did you get all these people together?"
    hide speechright
    fin "I thought Valentine's Day was supposed to be a 'one-on-one' sort of deal!  But this is more like..."

    stop music fadeout 2.0

    scene greathall_night at sepia with fade
    show lathna smile1 at sepia with dissolve
    lat "Back when I was alone, I never would have thought that there would be people who cared enough about me to throw me a surprise party like this with so many guests."
    scene hill_sunset with fade

    show finni surprised mouth_slightly_open with dissolve
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos
    fin "(!)"
    hide speechright

    hide finni with dissolve

    show eirene sad smile1 with dissolve
    eir "Ah, yes.  Well... I can't keep it a secret any longer, I suppose."

    play music "audio/music/CRASHER (Story Version A) loop.mp3" fadein 2.5

    eir "Finni, I'm sorry I didn't realize how important Valentine's Day was to you.  I was shortsighted, and I clearly caused you a lot of worry..."

    show eirene surprised smile1
    eir "...But... well, it was all because, in my mind, there was something even more important to celebrate today."
    eir "It's... well... the day I put that damaged core into your chassis, and you first came into existence as YOU."

    image battlefield = "images/backgrounds/Sty_bg_0129_400_00.png"
    scene battlefield at sepia with fade

    fin "It’s true that I’m not as capable as her original Finni—THAT Finni disappeared a thousand-some years ago when Eirene implanted her damaged heart into me."
    fin "And… that happened on this exact date.  The fourteenth of the second month of the year.  The day I replaced her friend…"

    scene hill_sunset with fade

    show finni shocked frown1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "Wait!  So that means..."
    hide speechright
    hide finni with dissolve

    show karl with dissolve
    kar "Well, I think we have enough people here, so let's all say it on the count of three, everyone!  One...!"
    hide karl with dissolve

    show finni shocked frown1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "...OH!  Hang on, so when you took me off patrol duty today—!"
    hide speechright

    scene greathall_night at sepia with fade
    show lathna smile1 at sepia with dissolve
    lat "I mean, you all gave me such perfect gifts!  And Pia even took care of my chores today so I didn't have to worry about them!"
    scene hill_sunset with fade

    show vchelsea smile1 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    vchel "...Two..!"
    hide speechright
    hide vchelsea with dissolve

    show eirene smile1 with dissolve
    eir "See... that one time, Lathna said she didn't feel like she was someone worth celebrating before."
    eir "But, according to her, having a party with all her friends helped her realize she was valued.  And..."
    show eirene surprised
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    eir "...well, there's nobody who deserves to be celebrated more than you, Finni!  And I'm SO glad you're here with me!"
    hide speechright
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    eir "So, well...!"
    hide speechright

    hide eirene with dissolve
    show laxi smile1 with dissolve
    lax "...Three!"

    hide laxi with dissolve
    everyone "HAPPY BIRTHDAY, FINNI!!!"

    stop music fadeout 1.0

    show finni surprised open_shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "(!)"
    hide speechright

    show finni_crop closed_pained closed_frown1 at finni_crop_pos
    hide finni
    fin "..."

    show finni_crop closed_awkward1 at finni_crop_shake
    fin "..."

    play music "audio/music/Yumemiteta no Atashi (Story Version B).flac" fadein 3.0

    show finni_crop awkward1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "I... I don't know what to say..."
    hide speechright
    fin "...Thank you, Eirene!  Thank you everyone!!!"
    show finni_crop pained grin1
    fin "I... I'm gonna start bawling here, but... I've never had anybody throw a big celebration for me like this before!"
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "I... Wow, I didn't know you all cared about me this much!  Uh... I feel so overwhelmed!!!  I have no clue what to say here!"
    hide speechright

    show finni_crop at finni_crop_move_right
    show eirene_crop relaxed smile1 behind finni_crop at left with dissolve
    eir "You don't NEED to say anything!  Or do anything!  We're here for YOU, Finni, just the way you are!"

    show finni_crop relaxed smile1
    fin "...Thanks so much for doing this for me, Eirene."
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_upperrightpos
    fin "...Man, I was REALLY confused, though!"
    hide speechright

    hide eirene_crop with dissolve
    hide finni_crop with dissolve

    show elisanne sad smile1 with dissolve
    elly "Well, it looks like everything worked out in the end after all!"
    show elisanne surprised frown1
    elly "...Although I can't help but feel like we're still forgetting something..."

    stop music fadeout 1.0

    hide elisanne with dissolve
    cle "THERE YOU ARE, YOU HOOLIGANS!!!"

    show eirene surprised mutter1 with dissolve
    eir "...Oh dear..."

    play music "audio/music/BANG (Story Version B) intro.flac" fadein 1.0
    queue music "audio/music/BANG (Story Version B).flac"

    hide eirene with dissolve
    show cleo glare shout1 with dissolve
    show dragonyule_cake at item_pos
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    cle "I SPENT TWO HOURS PAINSTAKINGLY BAKING AND ICING THIS CAKE, AND THEN YOU ALL CANCEL AT THE LAST MINUTE?!?"
    cle "I DON'T THINK SO!!!  FINNI IS GETTING THIS CAKE WHETHER SHE WANTS IT OR NOT!!!"
    hide speechright

    hide cleo with dissolve
    show finni surprised shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "Uh oh, Cleo, watch where you're waving that fork—!"
    hide speechright

    play music "audio/music/BANG (Story Version A) intro.flac" fadeout 1.0 fadein 1.0
    queue music "audio/music/BANG (Story Version A).flac"

    show finni closed_frown1
    hide dragonyule_cake with dissolve
    fin "(!)"

    image sky_night = "images/backgrounds/Sty_bg_0029_301_00.png"
    show sky_night behind finni with dissolve

    show finni shocked
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "(!!!!!!)"
    hide speechright


    show finni grin1
    show laxi_face_sparkles at topleft
    show laxi_face_sparkles as laxi_face_sparkles2 at topright
    show laxi_face_sparkles as laxi_face_sparkles3 at top
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    fin "“—HOLY CIRCUIT BOARDS, I CAN {u}TASTE{/u} IT!!!  AND IT’S AMAZING!!!"

    hide sky_night with dissolve
    fin "OH MY GOSH, WHAT *IS* THIS?!?  IT’S LIKE MY CHEMICAL ANALYSIS PALETTE IS RIDING ALONG THE SURFACE OF A MANDELBROT RAINBOW WRAPPED IN PUPPIES AND ROLLER SKATES!!!"
    hide speechright

    hide laxi_face_sparkles
    hide laxi_face_sparkles2
    hide laxi_face_sparkles3

    hide finni with dissolve
    show elisanne focused smile1 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    elly "THAT is what chocolate tastes like.  …Or, more specifically, how I experienced it about an hour ago."
    hide speechright

    hide elisanne with dissolve
    show eirene sad smile1 with dissolve
    eir "Maybe you forgot about it because it was just an offhand comment, but... I wanted to make your wish come true for your birthday..."

    scene greathall_night at sepia with fade
    show finni relaxed at sepia with dissolve
    fin "In any case, that cake DOES look really good.  I’ve heard chocolate tastes great."
    show finni sad
    fin "…Not that I’ll ever know…  It’s a shame, I guess."
    scene hill_sunset with fade

    show cleo focused triangle1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    cle "Yes, and with the late notice Eirene gave me, you're lucky it even happened at all!  Hmph!"
    show cleo closed_focused
    cle "To think you would make me bake an entire cake on rush order, and then completely abandon it... so rude!"
    hide speechright
    show cleo blush_askance
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    cle "...But it's the first time I've baked for an android, so that was... still a rewarding challenge, in its own right..."
    cle "...And... I suppose that Finni DID recieve it in the end, so there's no harm done..."
    hide speechright

    hide cleo with dissolve
    show finni surprised shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "...Wait... So... So THAT'S what you and Eirene were doing earlier with all the talk of 'tasting'?!"
    fin "And... that body contact in the bedroom?!?  You were recording her physiological responses!"
    hide speechright
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos
    show finni shocked
    fin "OH MY GOSH, EVERYTHING MAKES SENSE NOW!!!  SHE GAVE YOU {u}MY{/u} CHOCOLATE SO YOU COULD RECORD THE FLAVOR FOR {u}ME{/u}!!!"
    hide speechright

    hide finni with dissolve
    show elisanne blush shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    elly "Wait, you SAW US?!?!?  OH, BY THE GODDESS, I'M GOING TO DIE OF EMBARRASSMENT!!!"
    hide speechright
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "W-Was there anyone else watching!?!  Did—Did you see anyone in the hallway!?!"
    hide speechright
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    elly "A holy paladin in a state of undress with… another WOMAN on top of her!  I can’t even imagine what VILE things people would assume about me!"
    hide speechright

    hide elisanne with dissolve
    show alex shock grimace1 with dissolve
    ale "Yes… (cough) that… would be… very… UNFORTUNATE… (ahem)!"

    stop music fadeout 10.0

    hide alex with dissolve
    show elisanne blush shout1 with dissolve
    elly "For truth!  Now, if you’ll excuse me, I simply must go find the Prince!"
    show elisanne surprised
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "I have… (ahem) something I need to deliver to him by the end of the day, and it is already quite late!..."
    hide speechright
    hide elisanne with dissolve

    show alex sad mutter1 with dissolve
    ale "(sigh) ...Indeed.  Come, I will accompany you..."
    hide alex with dissolve

    pause 0.5

    play sound "audio/sound/grass steps armor running.mp3"
    show ranzal angry grimace1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    ranz "Bad news, everyone!  We've got serious trouble!!!"
    hide speechright
    ranz "The boss just fled the castle on Midgardsormr's back!!!"

    hide ranzal with dissolve

    jump myfinnivalentinemenu









label my_finni_valentine7:

    stop music fadeout 1.0

    image hill_sunset = "images/backgrounds/Sty_bg_0029_200_00.png"
    scene hill_sunset with fade

    play music "audio/music/CRASHER (Story Version C) intro.flac" fadein 5.0
    queue music "audio/music/CRASHER (Story Version C).flac"

    show ranzal angry grimace1 with dissolve
    ranz "The boss just fled the castle on Midgardsormr's back!!!"

    hide ranzal with dissolve

    show elisanne surprised shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    elly "Wait... WHAT?!?"
    hide speechright
    hide elisanne with dissolve

    show alex focused grimace1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    ale "Is the prince in danger??"
    hide speechright
    hide alex with dissolve

    show ranzal surprised grimace2 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    ranz "Well, emotional danger, at least!  See, I dunno how this coulda happened, but..."
    hide speechright

    image main_hall_sunset = "images/backgrounds/Sty_bg_0024_200_00.png"
    show main_hall_sunset at sepia with dissolve
    show mym_img blush smile1 at sepia with dissolve

    ranz "Ol' Mym went absolutely nuts after reading some love letter.  And... she said it was from the boss!"
    hide mym_img with dissolve
    hide main_hall_sunset with dissolve
    show ranzal flinch
    ranz "She's all hot-and-bothered now... and not just because she's the Flamewyrm!"

    hide ranzal with dissolve
    show elisanne surprised open_shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    elly "(!)"
    hide speechright
    hide elisanne with dissolve

    show ranzal surprised grimace1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    ranz "A-Anyway, she started chasin' him down, and... well, one thing led to another, and Euden had to beg Midgardsormr for an emergency getaway!"
    hide speechright
    ranz "They’re probably already a mile south o' here, with Brunhilda in hot pursuit—literally!!"
    hide ranzal with dissolve

    show elisanne focused shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "But… that’s crazy!!!  We all know His Highness would never write a love letter to ANYONE!!!"
    hide speechright
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "W-Was this a prank or something??  That's it, it's gotta be a prank!!"
    hide speechright
    hide elisanne with dissolve

    show finni neutral smile1 with dissolve
    fin "No kidding?!  Wow, that’s SUPER weird!"
    hide finni with dissolve

    show ranzal angry grimace1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    ranz "I dunno—it’s in his handwriting, though!  Look right here!  It's got his signature and everythin'!!"
    hide speechright
    ranz "You’d need, like, MACHINE-level precision to make a forgery THIS convincin'!"
    hide ranzal with dissolve

    stop music fadeout 1.0

    show alex surprised closed_mutter1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    ale "(!)"
    hide speechright
    hide alex with dissolve

    show elisanne angry shout1 with dissolve
    elly "L-Let me see that letter!!!"

    play music "audio/music/Cinderella Step (Story Version A) loop.mp3" fadeout 1.0

    pause 0.75
    show elisanne surprised shout1
    pause 0.75
    show elisanne blush open_shout1
    pause 0.75
    show elisanne pout2
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    elly "Th...This is HORRIBLE!!! I-I refuse to believe this!  The Prince would NEVER..."
    hide speechright
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    elly "But... this is undeniably in his hand!!!  He must have..."
    hide speechright
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    show elisanne pout1
    elly "B-But the contents of this letter are so...!!"
    hide speechright
    show elisanne closed_blush
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    elly "OHHH, BY THE GODDESS, THIS IS TOO MUCH!!!  There's NO WAY His Highness's hand could have ever penned such... shameless... b-brazen...!!!"
    hide speechright
    show elisanne shout1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "I... and I was planning to give him...  But if he truly feels this way... AUGHHH!!  WHAT'S GOING ON!?!?!?"
    hide speechright
    hide elisanne with dissolve

    show finni neutral with dissolve
    fin "Well, that's unfortunate.  At this rate, it sounds like Euden'll be tied up for… approximately the rest of the evening, if I had to guess?"
    fin "Total bummer...  I suppose Elly’s gonna have to figure out some OTHER way to spend the rest of her Valentine’s Day, then…"
    pause 0.5
    show finni wink
    pause 0.3
    show finni neutral
    pause 0.5
    hide finni with dissolve

    show alex surprised closed_mutter1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    ale "(Don't tell me... after our conversation, she...!)"
    hide speechright
    hide alex with dissolve

    show eirene pained grimace1 with dissolve
    eir "Oh dear... Elisanne, you look agitated and unwell.  This must be a shock, especially after you did so much to help with Finni's birthday."
    eir "Perhaps you should go sit down somewhere and rest.  You've certainly earned a break..."
    hide eirene with dissolve

    show elisanne closed_neutral pout1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    elly "Yes, I… That sounds like a splendid idea…"
    hide speechright
    hide elisanne with dissolve

    show alex focused closed_mutter1 with dissolve
    ale "..."
    show alex askance smile1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    ale "…Allow me to accompany you, Elly.  Someone should be there to… ensure your safety."
    hide speechright
    hide alex with dissolve

    show ranzal surprised frown1 with dissolve
    ranz "Uh... don't you guys think we should do something about the boss?  I certainly wouldn't wanna be in his position..."
    hide ranzal with dissolve

    show luca sad sweat with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    luc "Uh, well... it's not like any of us can fly, right?  It's kind of out of our hands at this point."
    hide speechright
    luc "Plus... Midgardsormr's probably the fastest dragon around.  So... I'm sure he has it covered, right...?  Ahaha..."
    luc "And... Mym cares about Euden more than life itself.  It's not like she'd actually hurt him..."
    show luca askance
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    luc "...probably..."
    hide speechright

    stop music fadeout 1.0

    show luca relaxed smile1
    luc "So, er... I think Euden probably wouldn't want us to stress at this point.  He can handle it."
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    luc "...Oh!  Speaking of... Here, have some cake and relax, big guy!  It's Finni's birthday today, after all!"
    hide speechright
    hide luca with dissolve

    show ranzal closed_neutral closed_frown1 with dissolve
    pause 1.0

    play music "audio/music/24h (Story Version) intro.flac" fadein 12.0
    queue music "audio/music/24h (Story Version).flac"

    show ranzal surprised grin1
    ranz "...Yeah, yer probably right.  Plus, negotiatin' with the fairer sex is just one o' the rungs on the ladder to manhood."
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    ranz "Heh, the boss sure is growin' up fast...  Hope he has more luck in love than I did."
    hide speechright
    show ranzal wink
    ranz "Plus, this cake looks mighty tasty...  Don't mind if I do—"
    hide ranzal with dissolve

    show cleo glare frown1 with dissolve
    cle "ONE slice.  You get ONE slice, Ranzal.  ...And the same goes for you, Luca."
    hide cleo with dissolve

    show ranzal flinch grimace1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    ranz "Ugh, yeah, yeah...  —Hey!  You call that a \"slice?\"  It's practically paper-thin!"
    hide speechright
    hide ranzal with dissolve

    show luca frown1 with dissolve
    luc "Yeah, Cleo, we're growing guys who need some calories!  Cut us some slack!"
    hide luca with dissolve

    show vchelsea focused frown1
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    vchel "No way, you CAN'T, Luccy! I've portioned out your food today to make sure you'll fit in the wedding tuxedo I picked out!"
    hide speechright
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    show vchelsea angry
    vchel "And where is Hildegarde?!?  She said she'd be here so we could get married right on the hilltop!!"
    hide speechright
    hide vchelsea with dissolve

    show luca sad sweat with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    luc "Oh, geez...  Hey, Chelsea, I hate to break it to you, but..."
    hide speechright
    hide luca with dissolve

    show linus with dissolve
    pause 0.5
    show linus closed_focused
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    pause 0.5
    hide speechright
    show linus relaxed
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    pause 0.5
    hide speechright
    hide linus with dissolve

    show karl with dissolve
    pause 0.5
    show karl grin1
    pause 0.5
    show karl gloom shout1
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    pause 0.5
    hide speechright
    hide karl with dissolve

    show eirene smile1 with dissolve
    eir "Well... it's a lot livelier than you were probably hoping, but... is this a decent birthday party?"
    hide eirene with dissolve

    show finni surprised shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "O-Of course!!!  Are you kidding?!  I just wish I'd known what was going on.  If you'd told me, I wouldn't have been acting all paranoid today!"
    hide speechright
    hide finni with dissolve

    show eirene sad frown1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    eir "Well... I thought birthday parties were supposed to be surprises.  And... if you hadn't been acting all paranoid, I wouldn't have worried so much about you!"
    hide speechright
    hide eirene with dissolve

    show finni focused shout1 with dissolve
    fin "Well, if you weren't so WORRIED, I wouldn't have been trying to IMPRESS you so hard—!"
    show finni closed_focused smile1
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "—Pfft!"
    hide speechright
    show finni grin1

    fin "...BAHAHAHAHA!!!"
    hide finni with dissolve

    show eirene surprised frown1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    eir "Finni?  What are you suddenly laughing about?"
    hide speechright
    hide eirene with dissolve

    show finni relaxed grin1 with dissolve
    fin "Because, I just realized—our insecurities spin out of control because they totally feed INTO each other!!!"
    show finni closed_focused
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    fin "In other words, we're a pair of supercomputers (snicker)... who didn't notice a basic NEGATIVE FEEDBACK LOOP!  BAHAHAHA!!"
    hide speechright
    hide finni with dissolve

    show eirene surprised shout1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    eir "I-I fail to see what's so funny about that!"
    hide speechright
    hide eirene with dissolve

    show finni surprised grin1 with dissolve
    fin "Well, I guess I have a different opinion, because I happen to think it's hilarious!"
    show finni wink
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    fin "And YOU'RE the one who said I need to stop chasing your approval on everything, so... I'm starting with my sense of humor!"
    hide speechright

    play music "audio/music/Kaede (Maple Leaf) - Off-Vocals loop.mp3" fadeout 3.0 fadein 3.0

    show finni sad smile1
    fin "And... well at least now we know something we can work on together, right?"
    fin "I'll try to curb my inferiority complex.  You clearly have tons of love for me, so that means I don't have to run myself ragged trying to earn it."
    show finni focused grin1
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    fin "BUT, that means YOU'VE gotta stop worrying about me as much!"
    hide speechright
    hide finni with dissolve

    show eirene surprised shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    eir "B-But I care about you so much!  It's not like I can just STOP worrying about you!"
    hide speechright
    show eirene closed_neutral frown1
    eir "...But... I suppose if you're taking better care of yourself, I don't mind stepping back a little..."
    show eirene relaxed smile1
    eir "You ARE my super-capable partner after all.  ...I love you, Finni."
    hide eirene with dissolve

    show finni neutral smile1 with dissolve
    fin "And I love you too!  Which means there's only one thing we still have to resolve."
    hide finni with dissolve

    show eirene surprised frown1 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    eir "Huh?  What's that?"
    hide speechright
    hide eirene with dissolve

    show finni surprised shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    fin "I've gotta figure out what to do for YOUR birthday celebration!"
    hide speechright
    hide finni with dissolve

    show eirene surprised frown1 with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    eir "...But from an ontological perspective, what would that even BE for me?  My assembly?  That process took weeks...  Maybe my first bootup?"
    hide speechright
    eir "...And even if so, those events happened in the middle of summer, so we have multiple months.  Surely we can wait to figure the details out?"
    hide eirene with dissolve

    show finni shocked shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    fin "NUH-UH!  I've gotta make this perfect to show you how much I love YOU back!!!"
    hide speechright
    fin "Which MEANS... I need to start planning, like, YESTERDAY!"
    fin "It'll be the summer, so... I guess that's beach weather?!  Maybe we could make it a whole beach outing!  With surfing, and snorkeling!"
    show finni grin1
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos
    fin "And I could make a giant sand sculpture in the shape of your head!!  Yeah, that'd work!"
    hide speechright
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    fin "And not just for your birthday, we've gotta have ourselves a totally hot android summer together!!!!"
    hide speechright
    show finni shout1
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos
    fin "OH!!! AND ANOTHER THING—!!!"
    hide speechright
    hide finni with dissolve

    show eirene surprised smile1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    eir "...Hahahaha.... what on earth have I unleashed?  Oh dear..."
    hide speechright
    hide eirene with dissolve



    image sky_sunset = "images/backgrounds/Sty_bg_0029_201_00.png"
    scene sky_sunset with fade

    show euden surprised shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    eud "H-Hurry, Midgardsormr, she's gaining on us!"
    hide speechright
    hide euden with dissolve

    show midgardsormr with dissolve
    show euden surprised shout1 at dragon_riding_pos behind midgardsormr with dissolve

    eud "At this rate, she'll overtake us before we can even reach the edge of the forest!"
    mids "Hmmm... yes, the Flamewyrm's current persistence is indeed formidable."

    hide euden with dissolve
    hide midgardsormr with dissolve

    show brunhilda surprised wide1 with dissolve
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    brun "DAAAAAARLING!!!  I'M COMING!!!!"
    hide speechright
    hide brunhilda with dissolve

    show euden focused shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    eud "Mym, please LISTEN!!!  Whoever left you that letter, it wasn't ME!!!"
    hide speechright
    hide euden with dissolve

    show brunhilda wide1 with dissolve
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    brun "There's no need to be so coy, darling!!!  After all, only YOUR words could inflame my heart so!!!"
    hide speechright
    show brunhilda closed
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    brun "Ah... but to think you would be interested in... THAT!  I'm so embarrassed, I didn't realize you appreciated the physical aspects of things so much!"
    hide speechright
    show brunhilda surprised
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    brun "But... if you're ready for THAT step of our relationship, then I am too!!!  Come, darling, and we'll take our romance to the next level!!!"
    hide speechright
    hide brunhilda with dissolve

    show midgardsormr closed with dissolve
    show euden surprised shout1 at dragon_riding_pos behind midgardsormr with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    mids "Hmmm... I may have to reevaluate my opinion of you, Euden.  I know humans must act decisively and boldly, but toying with the heart of a dragon is quite reckless..."
    hide speechright

    show euden blush_surprised
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    eud "I'm TELLING you, I have NO idea what she's talking about, Midgardsormr!!!  I'm being framed!!!"
    hide speechright

    show midgardsormr normal open1
    mids "Yes, yes, I merely tease... but the truth may not matter in this situation."
    mids "It would seem the Flamewyrm has taken full leave of her senses by now."

    hide euden with dissolve
    hide midgardsormr with dissolve

    show brunhilda surprised wide1 with dissolve
    brun "Aaaah!  I can't wait any longer!!  My heart feels like a furnace!!"

    hide brunhilda with dissolve
    show brunhilda0 with dissolve
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    brun "I'm ALL YOURS, darling!!!  Get ready, because I'm about to give you ALL THE LOVE A DRAGON CAN GIVE!!!"
    hide speechright

    hide brunhilda0 with dissolve
    show euden surprised shout1
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    eud "Mym, stop, you're going Primal!!!"
    hide speechright

    brun "Someone's about to get a FULL-SIZED DRAGON KISS, MY SHY DARLING!!!"
    show euden blush_surprised
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    eud "WH-WHAT?!?  Calm down, can't we just talk about this?!?  MYM?!?"
    hide speechright





    image hill_sunset = "images/backgrounds/Sty_bg_0029_200_00.png"
    scene hill_sunset with fade

    show vchelsea surprised smile5 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    vchel "...Why didn't you just SAY so?  Of COURSE we should postpone the wedding if you're not ready!"
    hide speechright
    hide vchelsea with dissolve

    show luca surprised sweat with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    luc "Wait, what?  Trust me, I'm glad, but... I didn't think you'd just drop the matter that fast!"
    hide speechright
    hide luca with dissolve

    show vchelsea smile1 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    vchel "Well, obviously it wouldn't be the dream wedding I imagined if you're a mopey mess the whole time, now would it?"
    hide speechright
    vchel "You're the star of the show, so you need to be just as happy as me!"
    vchel "Plus, we have the rest of our lives.  There's no need to rush into stuff when we can do it the right way at our own pace."
    hide vchelsea with dissolve

    show luca sad smile1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    luc "...WHEW...  I'm glad that's something we can agree on!"
    hide speechright
    hide luca with dissolve

    show vchelsea surprised shout1 with dissolve
    vchel "Besides, this test run had WAYYYY too many snafus!"
    vchel "I've got a whole TIDAL WAVE'S worth of problems to iron out for next time!!"
    show vchelsea focused
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    vchel "First of all, Hildegarde was a TOTAL no-show!  How's somebody that wishy-washy supposed to bind you and me together in eternal love?!"
    hide speechright
    show vchelsea surprised frown1
    vchel "And I DID actually like the hill for a venue, but unless we set up some kind of barricade, we'll just get a bunch of party crashers like Finni and Eirene did."
    show vchelsea focused mutter1
    vchel "Hmm... maybe if I dug some pit traps around the perimeter, and filled them with bamboo spikes?  That could work."
    show vchelsea drool2
    play sound "audio/sound/heart.wav"
    show speechright heart at speechright_pos
    vchel "Or... I could always just set the surroundings on FIRE instead!  The glow of the firelight would be so ROMANTIC!"
    hide speechright
    hide vchelsea with dissolve

    show luca surprised sweat with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    luc "Uh... um... Chelsea?  You're... uh... starting to say some REALLY worrying things again...!!"
    hide speechright
    show luca shocked sweat
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    luc "...Ch-Chelsea...?!?"
    hide speechright
    hide luca with dissolve




    image halidom_hallway_sunset = "images/backgrounds/Sty_bg_0050_100_00 sunset edit.png"
    scene halidom_hallway_sunset with fade

    show saboa with dissolve
    sabo "...Yes, Your Highness, I'm overjoyed at the opportunity to lay eyes on your latest masterpiece!"
    sabo "Given the size of the mold you crafted for it, it must be positively awe-inspiring!"
    hide saboa with dissolve

    show gemile angry grimace1 with dissolve
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    emil "Tch!  Well, of COURSE it is!  Not only was it made by yours truly, the Great Muse Emperor, but I spent five whole days crafting it without pause!"
    hide speechright
    emil "I only slept when my hands were too shaky to hold the chisel, and skipped meals out of pure artistic zeal!"
    show gemile neutral smile1
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    emil "It's not even an overstatement when I say that this was my most ambitious masterwork to date!"
    hide speechright
    emil "Once the materials are in order, I'll mass-produce these statues and place them on every street in the Empire!"
    hide gemile with dissolve

    show saboa with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    sabo "...HRRK!  THIS... THIS IS...!!"
    hide speechright
    hide saboa with dissolve

    show gemile closed_neutral with dissolve
    emil "Heh heh heh, Saboa... Normally I care not for the ramblings of a lickspittle like you, but your enthralled gasp is quite a welcome sound..."
    emil "Has my artistic genius striken you speechless, or are you awestruck from its sheer scale and grandeur?"
    show gemile neutral closed_frown1 with dissolve
    emil "..."
    show gemile shocked shout1
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    emil "...MY STATUE!!!  IT'S BEEN UTTERLY RUINED!!!"
    hide speechright
    show gemile pout1
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    emil "NO, IT'S EVEN WORSE!!!  Wh-Why, it was positively beaten into a crumpled heap... and THEN sliced to ribbons in a SECOND act of spite?!?"
    hide speechright
    show gemile cry grimace1
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    emil "AUUUUGH, MY MASTERPIECE HAS BEEN UTTERLY BESMIRCHED!!!!  WHOEVER DID THIS WILL PAY!!!"
    hide speechright
    hide gemile with dissolve

    show saboa with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    sabo "Y-Your Highness, do not fear, the mold yet remains!  I will send away to have the bronze recast immediately!!"
    hide speechright
    hide saboa with dissolve

    show gemile closed_cry grimace1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    emil "No, you don't understand!  Even if I made another copy, now it would just remind me of the vandalism of the original and leave a sour taste in my mouth!"
    emil "It would be a psychological stain on my pride as an artist!"
    hide speechright
    show gemile focused grimace2
    emil "...Tsk, it can't be helped!!  I will have to craft a new statue with an entirely different design..."
    show gemile closed_cry sweat_grimace1
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    emil "...But (sniffle) I've spent all the willpower to do so... I need to cleanse my artistic pallette with something else..."
    hide speechright
    hide gemile with dissolve

    show saboa with dissolve
    sabo "...I see.  Very well.  Do not fear, Your Highness!!"
    sabo "I shall call a carriage at once to take you to your mountainside retreat, wherein you may refresh your noble soul!"
    hide saboa with dissolve

    show gemile shocked shout1 with dissolve
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos
    emil "...WAIT!!!  DON'T MOVE A MUSCLE!!!"
    hide speechright
    hide gemile with dissolve

    show saboa with dissolve
    play sound "audio/sound/question.wav"
    show speechright question at speechright_pos
    sabo "Um... Your Highness?..."
    hide speechright
    hide saboa with dissolve

    show gemile focused mutter1 with dissolve
    emil "...That earnest salute... the adoration in those eyes... the lighting... that composition..."
    show gemile angry smile2 with dissolve
    play sound "audio/sound/inspiration.wav"
    show speechright lightbulb at speechright_pos
    emil "...YES!  I'm a GENIUS!!!  Rejoice, peon, for your visage will be immortalized by the great Emperor Emile!"
    hide speechright
    hide gemile with dissolve

    show saboa with dissolve
    sabo "Y-Your Highness?!  Do you mean..."
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    sabo "...You wish for ME to be the model for your next work?!?"
    hide speechright
    sabo "Th-This is an astounding honor, Your Highness!!  (sniff) You don't know how long I've dreamed of something like thi..."
    hide saboa with dissolve

    show gemile focused frown1 with dissolve
    emil "Yes, yes, I'm very magnanimous, and your tiny peon brain could never imagine such an honor.  Blast it all, where did I put my brush and paints?!?"
    show gemile angry pout1
    emil "I NEED to capture this before the lighting fades!!  That model of worship and servitude is exactly how I wish EVERYONE in the Empire to look at me!!"
    show gemile smile2
    emil "Making statues of myself was heavy-handed from the start.  INSTEAD, I will instill the values of respect, obedience and adoration in their hearts by EXAMPLE!"
    show gemile closed_neutral
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    emil "Soon, all in the land will see that I am supremely loveable and deserving of ABSOLUTE LOYALTY!!!  AHAHAHA!  I'm a GENIUS!!!"
    hide speechright
    hide gemile

    show saboa with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    sabo "...(sigh) I suppose some things never change..."
    hide speechright
    hide saboa with dissolve

    show gemile angry frown1 with dissolve
    play sound "audio/sound/anger.wav"
    show speechright anger at speechright_pos
    emil "Excuse me?  What did you just say, you cur?"
    hide speechright
    hide gemile with dissolve

    show saboa with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    sabo "...I-I said, this artistic endeavor will bring such change, Your Highness...!"
    hide speechright
    hide saboa with dissolve

    show gemile focused smile1 with dissolve
    emil "Hmph, that's right.  Now, quit your babbling!!!  You must hold absolutely still so I can capture this moment."
    show gemile mutter1
    emil "You can hold your breath for the next hour, right?"
    hide gemile with dissolve

    show saboa with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    sabo "(Ha ha ha... I'm unsure of whether to feel flattered or terrified...)"
    hide speechright
    hide saboa with dissolve




    image church_sunset = "images/backgrounds/Sty_bg_0013_200_00.png"
    scene church_sunset with fade

    show grace closed_neutral with dissolve
    gra "...This marks my second Valentine's Day without you..."
    gra "It's still so lonely living in a world you're not a part of, dear.  Sometimes, all I can think about is joining you."
    gra "But... you needn't worry so much about me.  I've resolved to keep thwarting the machinations of the Syndicate."
    show grace closed_neutral smile1
    gra "Talking to that android today reminded me of something, after all."
    gra "A part of you will always remain here.  So long as I carry on your dream..."
    gra "...No, OUR dream."
    gra "With the sword you left me, I'll take back the hope of our patients."
    gra "And... that means I have quite a lot to do before I can afford to leave this world."
    gra "So, for now, I'll just say... Happy Valentine's Day, dear."




    image courtyard_sunset = "images/backgrounds/Sty_bg_0027_200_00.png"
    scene courtyard_sunset with fade

    show elisanne closed_neutral frown1 with dissolve
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    elly "Ohh... what am I going to DO?!"
    elly "I wanted to give Euden this chocolate I made, because... because..."
    hide speechright
    show elisanne closed_blush pout1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "...well, I-I respect him so much for all he does to keep the Halidom and this nation safe!"
    elly "H-He deserves to receive proper gratitude from a paladin of the church such as myself!"
    elly "A-And, that's definitely all there is to it!"
    hide speechright
    hide elisanne with dissolve

    show alex closed_sad smile1 with dissolve
    ale "(sigh...)"
    ale "Yes, I understand, Elly.  His Highness has done so much for me, and for you."
    ale "Our lives both changed enormously for the better because of his help."
    ale "So regardless of any... personal feelings that may exist, we both owe him an enormous debt of gratitude."
    show alex frown1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    ale "And... I'm sorry that this evening didn't go the way you want.  I... (ahem)... highly suspect that Euden didn't write that letter, either..."
    hide speechright
    show alex closed_focused
    play sound "audio/sound/bad.wav"
    show speechright bad at speechright_pos
    ale "...I should track down the culprit later, and give them a stern talking-to about this little \"prank\" of theirs... erm, whoever they are..."
    hide speechright
    hide alex with dissolve

    show elisanne with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    elly "Oh, you think it was a forgery?!  Whew, that would be such a relief...!"
    hide speechright
    show elisanne closed_blush shout1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "...I-I mean, but it's not like I have a stake in who wrote that letter!!"
    elly "If the prince wants to rendezvous with that... buxom lizard, th-that's none of MY concern!"
    hide speechright
    hide elisanne with dissolve

    show alex focused duchenne1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    ale "...If you say so...  ha ha..."
    hide speechright
    hide alex with dissolve

    show elisanne sad frown1 with dissolve
    elly "...Hey, Alex?  I think I've been taking it for granted lately, but... this conversation just now reminded me..."
    show elisanne sad smile1 with dissolve
    elly "Speaking of debts... I may owe His Highness a lot, but... I've only been at his side for a few years."
    elly "And... well, we've been friends since forever."
    show elisanne focused
    elly "So... I want to thank YOU for everything YOU'VE done for me, too."
    hide elisanne with dissolve

    show alex surprised mutter1
    ale "Elly..."
    show alex askance smile1
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    ale "No, really, it's ok, if anything, I'm the one who..."
    hide speechright
    hide alex with dissolve

    show elisanne sad with dissolve
    elly "No, please don't shrug it off!  Even when you were working for Leonidas, you still cared enough about me to defy your orders, right?  That was so brave!"
    elly "You tend to hide yourself in the background and downplay your deeds all the time."
    elly "But I also know it's only because you want other people to shine in your place."
    elly "And... that has to be really lonely, right?"
    hide elisanne with dissolve

    show alex sad mutter1 with dissolve
    ale "...Well..."
    show alex askance
    ale "...Maybe a little... but—"
    hide alex with dissolve

    show elisanne focused shout1 with dissolve
    play sound "audio/sound/exclamation.wav"
    show speechright exclamation at speechright_pos
    elly "No \"buts\" about it!  You're my friend, you can't hide it from me!"
    elly "You absolutely deserve to be appreciated, so I want to show you all my gratitude and lov—"
    hide speechright
    show elisanne blush pout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "—I mean, I would \"love\" to help you feel appreciated!"
    hide speechright
    hide elisanne with dissolve

    show alex surprised frown1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    ale "N-No, really, it's ok, Elly!  I-I just want to stay by your side, that's all I need!"
    hide speechright
    hide alex with dissolve

    show elisanne focused shout1 with dissolve
    elly "But you deserve more than just a place in the shadows!"
    elly "...In fact, I've made up my mind!  Here, you're the one who deserves to have THIS!"
    hide elisanne with dissolve

    show alex surprised mutter1 with dissolve
    ale "...Wait, your chocolate for Euden?!  I-I couldn't possibly accept!"
    hide alex with dissolve

    show elisanne sad smile1 with dissolve
    elly "...Oh, don't be silly, Alex!  It's just chocolate, right?"
    elly "Besides, it'll be better when it's fresh.  At this point, it'll be better to make the Prince another batch of chocolate tomorrow."
    hide elisanne with dissolve

    show alex blush shout1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    ale "...W-Well, that's not the only issue, either!  I don't have anything to give YOU!"
    hide speechright
    show alex askance frown1
    ale "I-I didn't make chocolate for you; I thought it would... complicate things..."
    hide alex with dissolve

    show elisanne relaxed smile1 with dissolve
    play sound "audio/sound/note.wav"
    show speechright note at speechright_pos
    elly "Well, that's easy to fix!  Just give me half back then, and we'll eat it together!"
    hide speechright
    show elisanne closed_neutral smile1
    elly "It wouldn't be the FIRST regifted chocolate someone gave me today, after all."
    hide elisanne with dissolve

    show alex askance mutter1 with dissolve
    ale "...Elly..."
    show alex sad smile1
    ale "...Thank you.  This means more to me than I can even express."
    ale "In that case.... (snap) here, I'll share my heart with you.  Happy Valentine's Day, Elly."
    hide alex with dissolve

    show elisanne closed_blush smile1 with dissolve
    play sound "audio/sound/sweat.wav"
    show speechright sweat at speechright_pos
    elly "Eek!  Alex, don't say it like THAT!"
    hide speechright
    elly "But... Happy Valentine's Day..."
    hide elisanne with dissolve


    image finneirene_bg = "images/backgrounds/finneirene ending.png"
    scene finneirene_bg with fade
    show text "{size=-3}{color=#B0B0B0}Art by abby (@vaccariia on Twitter){/color}{/size}" at topleft with dissolve

    fin "(I know that I have a lot of work to do on myself before I can truly hold my head up high as Eirene’s partner.)"
    fin "(I’m not going to be able to change the way I think about myself overnight.)"
    fin "(And it won’t be easy for Eirene to let go of the past either, OR stop being afraid for me.)"
    fin "(And... we're definitely gonna have a lot more fights, for sure.  But...)"
    fin "(The thing is, I have someone who loves me in spite of all that.)"
    fin "(Someone who loves me no matter what.)"
    fin "(And I feel the same way about her, too!)"
    fin "(So... I think we're going to be alright.)"
    fin "(Because, as long as we fight for each other and face the future together...)"
    fin "(...then our story isn't over.  Not by a long shot.)"

    scene black with fade
    show text "{color=ffffff}{i}The End{/i}{/color}" at middle with dissolve
    pause 20.0

    jump myfinnivalentinemenu
