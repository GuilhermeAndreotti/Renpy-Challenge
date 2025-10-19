screen creatures_battle:
    frame:
        ypadding 8
        xpadding 8
        vbox:
            xalign 2
            xsize 360
            text "==============="
            text "{color=#008000}Party HP:{/color} [party]/[90]"
            text "==============="
            text "{color=#008000}Earth Machine:{/color} [hpearth if hpearth > 0 else 0]/30"
            text "{color=#f00}Fire Machine:{/color} [hpfire if hpfire > 0 else 0]/20"
            text "{color=#0000ff}Water Machine:{/color} [hpwater if hpwater > 0 else 0]/30"
            text "==============="
 


label path_save:

    scene park1 with pushleft

    player "She ran over there, Reiko, Fred, with me!"

    scene park1run with dissolve

    player "Olivia! Wait! Where are you?"

    scene park1 with dissolve

    "..."

    player "Fred, do you have something in mind?"

    "..."

    c_fred "BEHIND YOU!"

    player "?"

    play sound explosion volume 0.3

    show vendingtp at size_normal

    "AAAHHHHH"

    player "I must defend!"

    play sound explosion volume 0.3

    scene park1 with pixellate
    scene park2 with pixellate
    
    player "Ahhh--! Take th--. Wait?"

    show frederick_angry1 at size_normal

    player "Fred!"

    c_fred "Damn! They are stronger than I thought!"

    player "Did you see what happened, Fred?"

    hide frederick_angry1
    show frederick_base2 at size_normal

    c_fred "While we were running after Olivia, three elementals attacked us. When I was about to help you, I was teleported here."

    c_fred "I would say we're only together because Reiko defeated one of the three in time."

    c_fred "I was beliving she would have done something more to help, but she is really testing us, even with these out of the blue attacks."

    player "Let's go back to that place."

    c_fred "Yeah. But stay alert since --"

    "You hear the sound of iron coming loose from the wall."

    hide frederick_base2
    show firevending at left_normal
    show earthvending at size_normal
    show watervending at right_normal

    c_fred "Guess they dont want to play hide and seek since what happened. Be ready! We have a battle incoming!"

    "Frederick grabs his red katana, getting ready for this battle."

    play music battle1 volume 0.1

    if main_element == 'fire':
        $ amulet = 'gaguinho'
    elif main_element == 'earth':
        $ amulet = 'pernalonga'
    elif main_element == 'air':
        $ amulet = 'ligeiro'
    elif main_element == 'water':
        $ amulet = 'piupiu'

    jump battle_1_loop


label battle_1_loop:
    
    show screen creatures_battle

    $ hpearth = 30
    $ hpfire = 20
    $ hpwater = 30
    $ party = 90
    $ earth_damage = 0
    $ fire_damage = 0
    $ water_damage = 0
    $ fred_used = 0
    $ shield = 0  

    while (party > 0) and ((hpearth > 0) or (hpfire > 0) or (hpwater > 0)):    
        menu:
            "Atack the fire creature with your [main_element]!" if hpfire > 0:
                "With your [main_element] spellcaster abilities, you cast a magical sphere towards the enemy!"

                if shield == 1 and hpfire > 0:
                    $ hpfire -= 0
                    "BUT! The Earth Elemental uses its shield to protect its friend."
                else:
                    if main_element == 'fire':
                        "Oh no! The Fire elemental absorbed your attack!"
                    else:
                        $ hpfire -= renpy.random.randint(2, 6)
                            
            "Attack the earth creature with your [main_element]!" if hpearth > 0:
                    player "Take this!"
                    if main_element == 'earth':
                        "Oh no! The Earth elemental absorbed your attack!"
                    else:
                        $ hpearth -= renpy.random.randint(2, 6)

            "Attack the water creature with your [main_element]!" if hpearth > 0:
                player "Take this!"
                if shield == 1 and hpwater > 0:
                    $ hpwater -= 0
                    "BUT! The Earth Elemental uses its shield to protect its friend."
                else:
                    if main_element == 'water':
                        "Oh no! The Water elemental absorbed your attack!"
                    else:
                        $ hpfire -= renpy.random.randint(2, 6)

            "Protect yourself and your ally" if (main_element == 'water' or main_element == 'air') and party < 61:
                if main_element == 'air':
                    "You use the wind around you to create a barrier for both you and Fred!"
                else:
                    "You heal yourself and Fred! Dispite not liking to use water that way."   
                $ party += 5
                             
            "Use your knowledge you learned before and attack its weak spots!" if success == 1 and hpearth > 0 and hpfire > 0 and hpwater > 0:
                jump special_event

         
        if hpfire > 0:
            $ fire_damage = renpy.random.randint(2, 8)
        if hpearth > 0:
            $ earth_damage = renpy.random.randint(1, 4)
        if hpwater > 0:
            $ water_damage = renpy.random.randint(1, 2)
        
        if earth_damage == 1 and hpearth > 0:
            $ shield = 1
            $ earth_damage = 1
        
        if water_damage == 2 and hpwater > 0:
            "The water elemental heals everyone, expect its enemy, he is not that dumb. But he is happy, in fact."
            if hpfire > 0 and hpfire < 15:
                $ hpfire += renpy.random.randint(1, 4)
            if hpearth > 0 and hpearth < 20:
                $ hpearth += renpy.random.randint(1, 4)

        $ party -= fire_damage
        $ party -= earth_damage
        $ party -= water_damage
        
        "Rrrrrrrrr! {i}*They attacks you*{/i} (damage dealt - [fire_damage + earth_damage + water_damage]hp)"
   
        $ hpearth -= renpy.random.randint(4, 6)
        $ hpfire -= 0 if shield == 1 else renpy.random.randint(1, 4)
        $ hpwater -= 0 if shield == 1 else renpy.random.randint(3, 8)

        "Frederick uses his abilities, he quickly switches between slashes with fire, mist and even ordinary ones."

        $ shield = 0
        if hpfire <= 0:
            hide firevending
        
        if hpearth <= 0:
            hide earthvending

        if hpwater <= 0:
            hide watervending

        if hpwater > 0 and hpfire <= 0 and hpearth <= 0:
            hide watervending
            show sadwatervending at size_normal
            "After seeing both of its friends dying, the water vending machine decided to kill itself, good bye."
            jump continue_story
        
        if party <= 0:
            "It was suppossed to be impossible to reach this place, congrats."
            c_fred "Damn!"
            play sound explosion volume 0.2
            play sound slash volume 0.3
            "Fred charges a massive fire blast which kills the creatures but it also destroys the surrounding area a little"
            $ fred_used = 1
            jump continue_story
    
        if hpfire <= 0 and hpearth <= 0 and hpwater <= 0:
            jump continue_story

label special_event:
    hide screen creatures_battle
    scene black_full with dissolve
    scene training1 with dissolve

    show rikumi_base1 at size_normal

    if path == 'Fred':
        player "Fred and I noticed the different types of vending machines. It can be even further than just the two we saw."       
    else:
        player "The money compartment works like its heart. It can have some functions before but will only complete the process after that."

    hide rikumi_base1
    scene black_full with dissolve 
    centered "You attack its weak spot, aiming to what is common to both machines, which is the money compartment, its core."

    play sound explosion volume 0.2

    scene park2 with dissolve

    show frederick_base1 at size_normal

    c_fred "My Friend! That was impressive! No kidding! The moment I noticed what you did, I tried following your plan."
    c_fred "It worked perfectly and we defeat them easily. You remembered the boss lesson!"

    jump continue_story
    

label continue_story:

    scene park2
    hide screen creatures_battle

    show frederick_base1 at size_normal

    if fred_used == 1:
        c_fred "On the way, we must find everyone."
    else:
        c_fred "You are way stronger than the last mission, let's go eat something here in Japan after the mission to celebrate, Olivia may like japanese food."
        player "Thank you! Let's keep going, we must find Olivia and Reiko."

    c_fred "Let's keep this following this path. It's like the only way."

    scene black_full with dissolve
    scene park2

    show earthvending at right_normal
    show firevending at left_normal
    show watervending at size_normal

    c_fred "I can't even get something to drink and they attack us! Goddman!"

    c_fred "Die you all, I hate this freaking creatures."
    
    play sound slash volume 1

    scene black_full

    centered "After a while"

    scene park2

    show frederick_base2 at size_normal

    c_fred "Phew... That was the last one."

    c_fred "I was expecting something more in the investigative to be honest. Look."

    scene entrance with dissolve

    show rikumi_eyes_closed at size_normal

    c_rikumi "My my..."

    player "Reiko! We are back!"

    hide rikumi_eyes_closed
    show rikumi_base2 at size_normal

    c_rikumi "Glad to see you are both back, I was right at trusting you two."

    show frederick_angry1 at left_normal

    c_fred "Boss, any news about Olivia?"

    hide rikumi_base2
    show rikumi_eyes_closed at size_normal

    c_rikumi "Take a look by yourself just there."

    scene lotmonsters

    show olivia_angry1 at left_normal:
        xoffset 0
        linear 0.6 xoffset 3000

    c_olivia "DIEEEEE!!!!!!!!!!"

    play sound water volume 0.3

    show olivia_angry1 at right_normal:
        xoffset 0
        linear 0.6 xoffset -3000

    c_olivia "TAKE THISSSSS"

    scene entrance with dissolve

    show rikumi_serious2 at size_normal

    c_rikumi "Due to the great event Olivia caused, some elementals went after her to try absorbing her."

    show frederick_base2 at left_normal
    
    c_fred "Let's save her."

    c_rikumi "I must help this time, it's necessary."

    player "Of course!"

    scene park1 with dissolve

    show olivia_angry1 at size_normal

    c_olivia "I DIDN'T ASK ANY HELP, THE GREATEST WATER GODDESS CAN DEAL WITH IT ALONE."

    show frederick_base2 at left_normal

    c_fred "Common not here, even I was worried about you."

    c_olivia "Fine... boss is judging me by her eyes, so okay."

    scene lotmonsters

    show olivia_angry1 at left_normal:
        xoffset 0
        linear 0.6 xoffset 600

    show earthvending at right_normal:
        xoffset 0
        linear 0.6 xoffset -600

    c_olivia "DIEEEEE!!!!!!!!!!"

    scene entrance with dissolve

    show firevending at left_normal
    show watervending at right_normal

    show rikumi_base1 at size_normal

    c_rikumi "Are you two sure about doing this?"

    hide firevending 
    hide watervending

    show sadfirevending at left_normal:
        xoffset 0
        linear 0.6 xoffset -900
    show sadwatervending at right_normal:
        xoffset 0
        linear 0.6 xoffset 900

    hide rikumi_base1
    show rikumi_eyes_closed at size_normal
    c_rikumi "Too late."

    play sound explosion volume 0.3

    pause 2

    scene entrance with dissolve

    if main_element == 'fire':
        show vendingtp at size_normal
        show gaguinho at item
        player "FIREBALL!!!!!!!!!!!!!!!!!!!"
    elif main_element == 'earth':
        show firevending at size_normal
        show pernalonga at item
        "You envelops your hands in stone and attack the creature!"
    elif main_element == 'air':
        show firevending at size_normal
        show ligeiro at item
        "With your great air abilities, you destroy the elemental creature!"
    elif main_element == 'water':
        show earthvending at size_normal
        show piupiu at item
        "You cast several ray of frost until the earth elemental dies."

    scene black_full

    stop music

    centered "After some time fighting..."

    scene entrance with dissolve

    show frederick_angry1 at left_normal

    c_fred "Next time, remember to think ONLY A LITTLE, especially if we are under Reiko's test."

    show olivia_angry1 at right_normal

    c_olivia "ALRIGHT ALRIGHT, THANKS FOR SAVING ME."

    player "Are you okay, Olivia? Damaged somehow?"

    hide frederick_angry1
    hide olivia_angry1
    show olivia_base1 at size_normal

    c_olivia "I am healing myself right now. It will take a while but I discovered something."

    c_olivia "The machines possessed by elementals are reacting to energy, not only from humans, but also from elementals outside this domain."

    c_olivia "When I was attacked by some of these elementals we all defeated, I felt my energy not being absorbed by them, but rather going towards the top of that hill."

    scene gate with fade

    c_olivia "There."

    scene entrance with fade
    
    show rikumi_serious2 at size_normal

    c_rikumi "It's a domain the aether creature created to absorb magic."

    hide rikumi_serious2

    show frederick_base2 at size_normal

    c_fred "I got it. Since Olivia is a well strong water elemental by its core."

    c_fred "The aether creature wanted this energy as quickly as possible, so it made it easier to extract it."

    c_fred "Since aether elementals can consume both souls and elemental magic to survive."

    c_fred "Still I can't understand why others creatures are obeing this alpha one. Since I am quite sure we are not facing smarts elementals who can talk."

    hide frederick_base2
    show rikumi_base2 at size_normal

    c_rikumi "Quite impressive, mister Frederick. You're all right."

    c_rikumi "You answered your own question, the aether one is the alpha creature, so the other ones are basically obeying a strong creature to survive."

    player "Boss, If I am not wrong, we can break that domain, right? It will make the creature weaker if we do so."

    c_rikumi "You're right. But its barrier will work with the same properties as the Aether Element, so it could be harder."

    hide rikumi_base2
    show frederick_base1 at size_normal

    c_fred "Let's go there, I protect you from the creature while you try breaking the domain. You are our mage, so good luck, hehe."
    
    hide frederick_base1
    show olivia_base2 at size_normal

    c_olivia "Protecting someone means fighting, sooooo I AM DOWN!"

    jump domain

