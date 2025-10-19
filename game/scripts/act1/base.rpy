label base:
    
    scene black_full

    centered "Upon arriving at Guardian Call, both you and Reiko have your badges inspected and then you both proceed to the location where group B is located."
    centered "It's somewhat at the corners of the building but it is still a good place."

    play sound door volume 0.3

    pause 4

    scene training1 with pushleft

    "???" "DIE!! DUMB CREATURE WITH JUST 60 PERCENT OF WATER!"
 
    play sound explosion volume 0.3

    "???" "HEY-OHH STOP! I DON'T WANT TO KILL YOU BECAUSE REIKO SAID SO, BUT YOU ARE ASKING FOR IT."

    stop sound

    show frederick_angry1 at left_normal:
        xoffset 0
        linear 0.3 xoffset 410

    show olivia_angry1 at right_normal:
        xoffset 0
        linear 0.3 xoffset -410

    play sound explosion volume 0.3

    pause 2

    show rikumi_eyes_closed at size_normal

    c_rikumi "Well... Nothing new. Let me just stop this, again."

    scene black_full

    centered "As Reiko approaches them, the ground starts shaking and a stone pillar appears in the middle of them. Stopping the fight."

    hide olivia_angry1
    hide frederick_angry1
    hide rikumi_eyes_closed
    
    scene training1 with dissolve

    show olivia_angry1 at size_normal

    "???" "BOSS! It's not my fault! HE STOLE MY DELICIOUS LEMON TASTED WATER!!"

    hide olivia_angry1
    show frederick_base2 at size_normal

    "???" "I DID NOT! Your freaking water elemental! I took your bottle out of the refrigerator to get my food but you attacked me the moment I took it out! Damn."

    hide frederick_base2

    player "Oh. Hello Frederick, Hello Olivia."

    show frederick_base1 at size_normal

    c_fred "Hello boy. Good to see another regular person like me here."

    hide frederick_base1
    show olivia_base2 at size_normal
    c_olivia "LOW RANK HUMAN. Kill this person while he sleeps, It's a order from your superior."

    hide olivia_base2
    show rikumi_base1 at size_normal

    c_rikumi "So, everyone, time to stop. I need you all to pay attettion to me. The HQ sent us a new mission, in fact, the first outside United Kingdom."

    player "Outside?"

    hide rikumi_base1
    show olivia_base1 at size_normal

    c_olivia "OPEN SEAS?!"

    hide olivia_base1
    show rikumi_base2 at size_normal

    c_rikumi "No. No. The mission will be in partnership with the Engo-ji Elemental Hunter Organization. So, it will be at my birth country, Japan."

    scene training1

    show rikumi_base2 at size_normal

    c_rikumi "Engo-ji asked Guardian Call to undertake this mission as a way of showing other groups that good relations between organizations are possible."
    c_rikumi "So... The mission itself. You all know that elementals possess both creatures and objects."
    c_rikumi "In this case, we will be dealing with the possession of objects, in particular, machines."

    hide rikumi_base1
    show rikumi_base2 at size_normal

    c_rikumi "But, before that, I want you all to do something."

    if afraid == 1:
        c_rikumi "I heard that sometimes I scare you all. So I'm going to do things differently."
    else:
        c_rikumi "I want to try something new for this mission."

    c_rikumi "[player], I want you to choose Frederick or Olivia to go with you to buy me an iced coffe at the entrance with this money, but from the vending machine with only drinks, and I want the group to tell me a vending machine characteristic after."

    c_rikumi "The other one will help me getting the amulets."

    hide rikumi_base2
    show olivia_base2 at size_normal

    c_olivia "Huh? You are just being lazy, BOSS."

    hide olivia_base2
    show rikumi_base1 at size_normal

    c_rikumi "Trust me. I am not."

    hide rikumi_base1
    show olivia_base2 at size_normal

    c_olivia "Whoa, calm down."

    hide olivia_base2

    menu:
        "Hey Fred. Let's go":
            $ path = 'Fred'
            show frederick_base1 at size_normal
            c_fred "Sure buddy. At least I will stay away a while from this freaking elemental."
            jump machine_fred
        "Mister Waterson. Let's go there?":
            $ path = 'Olivia'
            show olivia_base1 at size_normal
            c_olivia "Alright human, BUT I AM leading the way."   
            jump machine_olivia


label mission:
    scene training1 with dissolve

    show rikumi_base2 at size_normal

    c_rikumi "Wellcome back, we already selected the amulets for this mission, what about you two?"

    player "Here your iced coffe, Miss Reiko."

    hide rikumi_base2
    show rikumi_base1 at size_normal

    c_rikumi "Thank you, [player]! So go on, tell me what you two noticed there."

    if path == 'Fred':
        show frederick_base1 at left_normal
        c_fred "Huh. You asked for the iced coffe.. so..."
        menu:
            "Fred and I noticed the [keyword_fred] types of vending machines. It can be even further than just the two we saw. But they all share the money part in common.":
                $ success = 1
            "The beverage machine is focused on beverages.":
                $ success = 0
            "Vending machines are strategically placed to attract attention and encourage spending.":
                $ success = 0
    else:
        show olivia_base1 at left_normal
        c_olivia "Human, answer her."
        menu:
            "The snack vending machine is smaller because the beverage vending machine attracts more attention.":
                $ success = 0
            "The money [keyword_olivia] can work like its heart. It can have some functions before but will only complete the process after that.":
                $ success = 1
            "Vending machines are strategically placed to attract attention and encourage spending.":
                $ success = 0

    hide olivia_base1
    hide frederick_base1
    hide rikumi_base1
    
    if success == 1:
        show rikumi_base1 at size_normal
        c_rikumi "Oh! Congratulations! I'm glad to hear that. What you said will be important for the mission."
    else:
        show rikumi_eyes_closed at size_normal
        c_rikumi "What you said makes sense, but unfortunately it doesn't matter much for the mission"

    scene training1 
    show rikumi_base1 at size_normal

    c_rikumi "Well. I asked this because the place we are going in Japan is Sagamihara's city. Specially the Sagamihara Retoro Jihanki, which translates for Sagamihara Vending Machine Park."
    c_rikumi "Recently, locals have begun to disappear after visiting the park, with some being found either very weak or even near death."
    c_rikumi "The police closed the area, and some hunters from Engo-ji noticed elemental traces of almost every kind, like earth, water, lightning, air and even..."

    hide rikumi_base1
    show rikumi_eyes_closed at size_normal

    c_rikumi "And even a unique signature of the aether, or the quintessence."

    hide rikumi_eyes_closed
    show rikumi_serious2 at size_normal

    c_rikumi "Engo-ji was about to send its powerful members on this mission, but due to the initial partnership between the United Kingdom and Japan, Guardian Call decided to take on this mission to strengthen the good relationship."

    c_rikumi "Since most members are dealing with a strong creature in Tokyo, called Sukura."

    hide rikumi_serious2
    show rikumi_base1 at size_normal

    c_rikumi "Team A was supposed to get this mission completly but after some events, the mission fell into our hands with Team A being there if necessary."

    hide rikumi_base1
    show rikumi_serious2 at size_normal

    c_rikumi "Both the void and the aether element are in fact rare signatures we don't see often. So that is why the mission is qualified as RANK A."

    hide rikumi_serious2
    show frederick_base2 at size_normal
    c_fred "You said all the inforamtion and that it's happening inside that park, but my question is, where are the elementals in that park? Don't tell me..."

    hide frederick_base2
    show rikumi_base2 at size_normal
    c_rikumi "Yes. Mostly possed the vending machines there. And since the place gained new vending machines corridors after 2024, it's not that small anymore."

    player "Am I really included for this mission, boss? I can't even fight that well. Both Olivia and Fred are way stronger than me."

    c_rikumi "You are quite good with the mage fighting style and you recently trained a lot, I trust you. And of course, both Frederick and Olivia are going together."

    hide rikumi_base2
    show rikumi_base1 at size_normal

    c_rikumi "So as do I. You all need a translator, right?"

    hide rikumi_base1
    show olivia_base1 at size_normal

    c_olivia "BOSS I am ready to kill my siblings since I kinda like this new life style BUT-- this weaklings humans are with their dumb amulets off, what can they do?"

    hide olivia_base1
    show rikumi_base2 at size_normal

    c_rikumi "Fortunately, Guardian Call's superiors gave me a recent addition of amulets containing very powerful elemental creatures. Due to the level of the mission, we will use them."

    c_rikumi "To start. Since you are all related to fire, Mister Frederick, I am giving you the Fire Duck."

    show patolino at item

    show frederick_base1 at left_normal
    c_fred "A duck with fire powers? That is different. Well. Thank you."

    hide patolino
    hide rikumi_base2
    show rikumi_serious2 at size_normal
    c_rikumi "And I must advice you, Mister Frederick. Just use your white katana as a last resource."
    c_fred "Aye captain, I know that well."

    scene training1 

    show rikumi_base1 at size_normal

    c_rikumi "As for you [player], as you picked before, I have this one for you."

    if main_element == 'fire':
        show gaguinho at item
    elif main_element == 'earth':
        show pernalonga at item
    elif main_element == 'air':
        show ligeiro at item
    elif main_element == 'water':
        show piupiu at item

    c_rikumi "A amulet related with the [main_element]. Hope you use it well."

    player "I am glad Miss Reiko. I will try my best!"

    scene training1 
    show olivia_base1 at size_normal

    c_olivia "You all need weird ANIMALS to have power while The powerful WATERSON can do it ALONE MUHAUHAUHA."
    hide olivia_base1

    show rikumi_base1 at size_normal
    c_rikumi "Well. Stay ready everyone, train a little, we are departing in the next 2 hours."

    scene black_full
    stop music

    centered "You, Frederick, and Olivia train under Reiko's supervision, learning some new skills from the amulets."

    if main_element == 'fire':
        centered "Frederick teaches you some strategies for using fire, even though your style is way different from his."
    elif main_element == 'earth':
        centered "Reiko teaches you how to create earth shields, one of the basic tricks any earth user can do."
    elif main_element == 'air':
        centered "Being the first air user, you try yourself doing some things and as you notice, you are quite good controlling this element."
    elif main_element == 'water':
        centered "You try asking Olivia's help, she then says a bunch of nonsense, which makes you even more confused, but at least you notice that water is very versatile."

    centered "ACT 1 - DONE. VERY OBRIGADO."

    jump travel
