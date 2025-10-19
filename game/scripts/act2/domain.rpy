label domain:

    scene gate with dissolve

    play music base volume 0.3

    player "Stay alert, everyone."

    show olivia_angry1 at size_normal

    c_olivia "I can't saw nothing here. But the energy is one of the strongest I ever felt. You! [player]! Begin the process!"

    scene gatewithmachine with dissolve

    c_olivia "Decided to show up, eh? LET'S GO!"

    show frederick_angry1 at left_normal

    c_fred "Pal, good luck! We are couting with you!"

    "While you are focusing on breaking the domain, both Frederick and Olivia advances to attack the vending machine, thinking it was the Aether Creature but... the vending machine just breaks normally."

    scene gate with dissolve

    show olivia_angry1 at right_normal

    c_olivia "What?"

    "A mysterious vending machine appears behind you. You try protecing yourself but nothing happened, it just stays as a regular vending machine."
    
    hide olivia_angry1

    show aetherbasic at size_normal

    "It remains there, mysterious enough the enter the theme Mami selected."

    $ hard = 4
    menu:
        "Attack it":
            "As you attack the vending machine, it is destroyed. But something happens..."

        "Start to concentrate to break the domain":
            $ hard = 6
            "As you start to concentrate yourself to break the creature domain, something happens."

    scene domain with pixellate

    player "Where am I?"
    
    show rikumi_eyes_closed at size_normal

    c_rikumi "[player], the aether creature used a mysterious ability I never saw and everyone is inside its domain now. And we lost our elemental control. Olivia can't even move herself."
    
    player "What can we do?"

    show frederick_angry1 at left_normal

    c_fred "Damn! The creature tricked us!"

    player "I- I feel like I can still break the creature domain."

    hide frederick_angry1
    hide rikumi_eyes_closed

    show frederick_base2 at size_normal

    c_fred "Yeah? I don't even want to ask how, just do it!"

    player "Maybe because I was concentrating my energy since the time you and Olivia advanced. I will try..."

    if main_element == 'fire':
        show gaguinho at item
    elif main_element == 'earth':
        show pernalonga at item
    elif main_element == 'air':
        show ligeiro at item
    elif main_element == 'water':
        show piupiu at item

    player "AHHHHHHHHH----!!!"

    $ domain = renpy.random.randint(1, hard)

    if domain > 2:
        scene gatewithmachine
        player "I did it!"
        scene gate
    else:
        scene domain
        player "Shit! It failed! But at least I think we have our magic back!"

    
    show aetherbasic at size_normal

    "Regular Vending Machine" "-.-- --- ..- / .-- .. .-.. .-.. / -. . ...- . .-. / ... - --- .--. / --- ..- .-. / .-.. --- .-. -.. .-.-.-"

    "After everthing what happened so far, the mysterios vending machine begins to tranform itself."

    show aether2 at size_normal
    play music battle volume 0.1

    "Aether Creature" ".. / .-- .- -. - -....- -....- / -.-- --- ..- .-. / . -. . .-. --. -.-- .-.-.- / - .... . / ...- --- .. -.. .-.-.- .-.-.- .-.-.- / -- ..- ... - .-.-.- .-.-.- .-.-.- / .-. . - ..- .-. -. .-.-.-"

    jump pt1_battle

screen boss_battle:
    frame:
        ypadding 8
        xpadding 8
        vbox:
            xalign 2
            xsize 360
            text "==============="
            text "{color=#008000}Party HP:{/color} [partyhp if partyhp > 0 else 0]/[200]"
            text "==============="
            text "{color=#FFFFFF}The Quintessence Creature:{/color} [bosshp if bosshp > 0 else 0]/[300 if domain <= 2 else 260]"
            text "==============="
 

label pt1_battle:
    
    show screen boss_battle

    $ partyhp = 200
    $ bosshp = 300 if domain <= 2 else 260
    $ aether_damage = 0
    $ negate_damage = 0
    $ party_damage = 0
    $ special_cd = 0
    $ boss_special = 0
    $ shield = 0
    $ chosen = 'nothing'
    $ fred_cd = 0
    $ olivia_cd = 0
    $ transformed = 0
    $ rikumi_cd = 0

    show olivia_base1 at left_normal
    c_olivia "Common you all! We already faced stronger creaturees! This one is nothing!"
    hide olivia_base1

    show rikumi_base1 at right_normal
    c_rikumi "An advice, this creature is being able to resist one element at time, I noticed when Frederick and Olivia attacked at the beginning."
    hide rikumi_base1

    while (partyhp > 0) and (bosshp > 0):   

        if boss_special > 0:
            "The aether creature is currectly immune to {color=#FFFFFF}[chosen]{/color}"
            $ boss_special -= 1
        
        if special_cd > 0:
            $ special_cd -= 1
        
        if fred_cd > 0:
            $ fred_cd -= 1
        
        if olivia_cd > 0:
            $ olivia_cd -= 1
        
        menu:
            "Attack with your {color=#FFFFFF}[main_element]{/color} ability!":
                
                if chosen == main_element:
                    "But the creature is immune!"
                    $ party_damage = 0
                else:
                    $ party_damage = renpy.random.randint(4, 12)
                    "Your attack deals [party_damage] damage!"

            "Attack with Frederick":
                
                show frederick_angry1 at left_normal
                c_fred "Take this, aether monster! You are dying today."
                play sound slash volume 0.2
                hide frederick_angry1

                if chosen == 'fire':
                    "But the creature is immune!"
                    $ party_damage = 0
                else:
                    $ party_damage = renpy.random.randint(4, 15)
                    "Your attack deals [party_damage] damage!"

            "Attack with Olivia":

                show olivia_angry1 at left_normal
                c_olivia "I AM SORRY BUT I NEED TO BECOME THE STROGEST ELEMENTAL ALIVE, SO YOU MUST DIE MUHAUHAUHAUHA"
                play sound water volume 0.2
                hide olivia_angry1

                if chosen == 'water':
                    "But the creature is immune!"
                    $ party_damage = 0
                else:
                    $ party_damage = renpy.random.randint(4, 15)
                    "Your attack deals [party_damage] damage!"

            "Use a weaker regular attack, without any elemental power.":
                $ party_damage = renpy.random.randint(2, 6)
                "Your attack deals [party_damage] damage!"

            "Create a shield for youself and your allies!" if main_element == 'earth' and special_cd == 0:
                $ shield = 1
                $ special_cd = 2
            
            "Blast burn the creature" if main_element == 'fire' and special_cd == 0:
                $ party_damage = 15
                "Your attack deals [party_damage] damage!"
                $ special_cd = 2

            "Create a freezing shield" if main_element == 'water' and special_cd == 0:
                $ shield = 1
                $ special_cd = 2

            "Use the wind to make a quick attack!" if main_element == 'air' and special_cd == 0:
                $ party_damage = renpy.random.randint(2, 6) + 10
                "Your attack deals [party_damage] damage!"
                $ special_cd = 2

            "{color=#5ad9f9}Special Olivia{/color}: Healing abitilies or extra HP" if olivia_cd == 0:
                $ olivia_cd = 3
                $ partyhp += 20
                show olivia_angry1 at left_normal
                c_olivia "Don't expect I like you all for doing this!"
                play sound water volume 0.2
                hide olivia_angry1

            "{color=#ff0000}Special Frederick{/color}: Fire Flaming Slash" if fred_cd == 0:
                $ fred_cd = 3
                show frederick_base2 at left_normal
                c_fred "Time to use my magnus explosion!"
                play sound explosion volume 0.2
                hide frederick_base2
                
                if chosen == 'fire':
                    "But the creature is immune!"
                    $ party_damage = 0
                else:
                    $ party_damage = 25
                    "Your attack deals [party_damage] damage!"

        $ bosshp -= party_damage



        if boss_special == 0:
            $ chosen = 'nothing'
        
        if bosshp > 0:
            $ aether_damage = renpy.random.randint(5, 25)    
           
            if aether_damage >= 10:
                $ boss_special = 1
                $ elements = ['earth', main_element, 'fire', 'water']
                $ chosen = renpy.random.choice(elements)

                "the creature begins to sintonize into one of the elements present in the battlefield"
                "Take care using [chosen] for the next turn!"
                if domain <= 2:
                    $ boss_special = 2
                    "The domain enchance the effect! So take care for the next two turns!"

        if transformed == 1 and bosshp > 0:
            show rikumi_base1 at left_normal
            $ damage = renpy.random.randint(2, 6) + 2
            "Reiko attacks by manipulating the metal around her dealing [damage] damage!"
            hide rikumi_base1
            $ bosshp -= damage
            
        if bosshp <= 0:
            jump ending1

        if partyhp <= 0 and bosshp > 0:
            jump ending2

        $ partyhp -= 0 if shield == 1 else aether_damage
        $ phrases = ['The quintessence creature fires a barrage of all the elements combined at once.', 'The creatures punches you with its combined elements' if transformed == 1 else 'The creature fires a item from its vending machine', 'The combined energy advances at you']
        $ chosenp = renpy.random.choice(phrases)
        
        "[chosenp] (dealing [aether_damage] at you and your allies!)"

        if shield == 1:
            "But the shields protects TEAM B!" 
        
        $ shield = 0

        if bosshp <= 80 and transformed == 0:
            $ domain = 3
            $ transformed = 1
            "As death approaches, the creature begins to scream, as if unable to bear maintaining that form, until..."
            scene black_full with dissolve
            scene gate with dissolve
            show finalform at size_normal
            $ bosshp = 120

            c_rikumi "Test is over, you all fought well, it's time to join the battle."

            "Rikumi rises stones shields around everyone."
            $ partyhp += 40
            $ shield = 1



label ending2:
    hide screen boss_battle
    scene gate 
    show finalform at size_normal

    "Aether Creature" "..-. .-. .- -.-. --- ... .-.-.- / -- --- .-. .-. .- -- .-.-.-"

    hide finalform
    show frederick_base2 at size_normal

    c_fred "Boss! I am sorry. But I will use it."

    show rikumi_eyes_closed at right_normal

    c_rikumi "You should not. It will drain half of your soul if you do so. We haven't yet discovered a way around this."

    c_fred "Shit! I know! But if I don't do so, what else can we do?"

    hide rikumi_eyes_closed
    hide frederick_base2

    show rikumi_serious2 at size_normal

    c_rikumi "Remember what I said about Team A? So..."

    scene black_full

    centered "At the same time, Reiko creates a huge stone barrier that protects you all, and then activates something on her phone."

    centered "A few hours later."

    scene plane2 with dissolve

    show olivia_angry1 at size_normal

    c_olivia "AHHHHHHHHHHH! I CAN'T BELIEVE WE FAILED AND THAT DUMB AIR ELEMENTAL FROM TEAM A STOOD OUT AGAIN, I WANT TO KILL HER EVEN MORE NOW"

    show frederick_base1 at left_normal

    c_fred "I am sorry, pal. We didn't pass Reiko's test this time but at least we are alive."

    player "It's okay, don't worry, we will have another chances."

    c_fred "I also think so, my late wife used to say that defeats only make future victories sweeter, so never surrender, pal."

    hide frederick_base1
    hide olivia_angry1

    show rikumi_base1 at size_normal

    c_rikumi "So. It's time to go back to London. But before that I have something to say."

    c_rikumi "You all fought well, even though we didn't win the battle. I liked that you all worked as a team."
    c_rikumi "So I am still promoting you all. However, unfortunately, I won't be able to keep the amulets I gave you as I had said, because they now belong to Team A."

    show frederick_base2 at left_normal
    
    c_fred "Boss..."

    show frederick_base1 at left_normal
    
    c_fred "You are the best!"

    scene black_full

    centered "Thanks for playing... maybe just reading this. I had plans to make it way longer and with multiples endings... but it didn't happen."
    centered "Still. Hope you enjoyed the story."
    centered "..."
    centered "..."
    centered "What about DMing this world? Huh?"
    centered "END"

    centered "..."
    
    return

label ending1:
    hide screen boss_battle
    scene gate 
    "After countless attacks from Team B, the elemental begins to enter a state of complete elemental absorption..."

    show rikumi_base1 at left_normal
    c_rikumi "Team B. Let's overcharge the creature. Due to previous attacks, I believe this will be the best option."

    show frederick_base1 at right_normal

    c_fred "Aye!"

    show olivia_base1 at size_normal

    "HAHAHAHAHAH WE WILL WIIIIIIIIIIIIIN!"

    player "Sure! We will!"

    show itemcharge at item

    play sound charge volume 0.5

    pause 3

    "Team B" "FIREEEE!!!!!!"

    scene gate

    show finalform at size_normal

    "Aether Creature" "..."

    play sound explosion volume 0.5

    "Aether Creature" "- .... . / .-.. --- .-. -.. / .-- .. .-.. .-.. / .-. . - ..- .-. -. .-.-.- / .. / .-- .- ... / --- -. .-.. -.-- / .. - ... / -- .. -. .. --- -. .-.-.-"

    stop music

    hide finalform

    player "We... We did it!"

    show rikumi_base1 at size_normal

    c_rikumi "Congratulations you all! It was indeed a great battle."

    scene black_full

    "After this battle, you and your group spend some time defeating the remaining elementals, until you return to the guards."

    scene entranceseal with dissolve

    show guard2 at size_normal

    "Kawara Norio" "Thank you, everyone! You all saved Sagamihara city!"

    player "We are glad we managed to defeat the creature there. It was a honour to help the Engo-ji."

    scene plane2 with dissolve

    show frederick_base1 at right_normal

    c_fred "Hey boss, I know we are still in Japan but I need to ask, did we pass the test?"

    show rikumi_base2 at left_normal

    if score == 9:
        c_rikumi "Despite the fact [player] was rude with the guard that time."
    
    c_rikumi "Of course. You all passed, even with Olivia doing some mistakes, she paid off in the end."

    show olivia_base1 at size_normal

    c_olivia "Of cour---"

    scene plane2

    show guard2 at size_normal
    "Kawara Norio" "Hey! I'm glad I got here in time... Leader Shumi would like to talk to you all!"

    scene black_full

    centered "Thanks for playing... maybe just reading this. I had plans to make it way longer and with multiples endings... but it didn't happen."
    centered "Still. Hope you enjoyed the story."
    centered "..."
    centered "..."
    centered "What about DMing this world? Huh?"
    centered "END"

    return

