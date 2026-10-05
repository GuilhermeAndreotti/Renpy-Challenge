label news_raining:
    scene black_full

    play music street_rain volume 0.5

    centered "2028, Thursday, 1 p.m - London (United Kingdom)"

    scene london_1

    "Unlike the crowd around you who walks their way to their work, the rain catches you unprepared."

    "To avoid the rain, you stop at small coffee store nearby."

    play sound door_bell volume 0.3

    scene coffe_1 with dissolve

    "After ordering a coffee, you think to yourself how you will avoid being late this time if the rain doesn't stop in the next 30 minutes."

    "Accepting the fate that the rain will not stop so soon, your attention turns to the television near you."

    "Presenter" "Yesterday we marked the last day of the 36th anniversary event of Guardian's Call! One of the first organizations to rise and fight against the elemental beasts that returned during the Cold War."
    "Presenter" "I remind you once again that if it weren't for Guardian Call, and all others organizations that were created to confront such atrocities, we wouldn't have lasted another year after the rifts were reopened and all the elemental danger returned to our world."
    "Presenter" "From the powers of the creatures, we are able to defeat the monsters, even after the destruction of all the temples."
    "Presenter" "If you get yourself in danger or spot any evil beast, remember to call the emergency number. Members will come as fast as possible to aid you."

    scene black_full

    centered "You keep your attention on what comes next. It's a show with various elemental powers and in the middle of the stage is Abo, a famous Japanese singer, whom you like a lot. "
    centered "The music in fact reminds you about a Japanese person you see almost every day, in this case, your very own boss, Reiko Rikumi. The one who offered you a position as an elemental hunter intern inside Guardian Call HQ when she discovered your affinity for elemental powers."

    scene coffe_1 with dissolve
    play sound door_bell volume 0.3
    $ afraid = 0

    menu:
        "She is so beautiful":
            "???" "Am I? Well... I am glad you think so, [player]."
            show rikumi_base2 at size_normal
            player "Reiko! Sorry! I thought aloud without realizing it."
            c_rikumi "Don't worry. I like a compliment."

        "Reiko is quite serious, sometimes I feel afraid.":
            "???" "Really? I am really sorry, I will consider this next time."
            show rikumi_serious2 at size_normal
            $ afraid = 1
            player "I am sorry Miss Reiko! Please forget what I said."
            c_rikumi "Don't worry. I like listening to my employees' feedback"

        "It's time to go... Avoiding being late is not an option anymore.":
            "???" "Oh! What a finding."
            show rikumi_base1 at size_normal

    
    show rikumi_serious2 at size_normal
    c_rikumi "Oh. It's already 1:32 PM. I see you are somewhat late. Something happened?"

    hide rikumi_base1 
    hide rikumi_base2 
    hide rikumi_serious2
    show rikumi_base1 at size_normal

    player "Well... The sky was so beautiful this morning that raining never crossed my mind, sorry."

    c_rikumi "Since it is your first time being late, I will let it slide."
    
    hide rikumi_base1
    show rikumi_base2 at size_normal
   
    c_rikumi "Come with me, I can give you a ride. Just let me grab a coffee and here, take this umbrella for you, it's a gift."

    scene black_full

    centered "Your boss's good self-esteem helps you go to work today."

    play sound door_bell volume 0.3

    scene car1 with dissolve

    c_rikumi "My car is over there."

    show rikumi_eyes_closed at size_normal

    c_rikumi "Let's see if those two didn't destroy anything. It turns into a mess every time they are alone."

    show rikumi_base1 at size_normal

    c_rikumi "Oh.. Just to spoil it for you a little, today you will be having your first RANK A mission."

    hide rikumi_base1

    play music car1 volume 0.4

    scene path1 with dissolve

    pause 2.0

    scene path2 with pushleft

    pause 2.0

    stop music

    scene black_full with dissolve

    centered "The path to work is reasonably close."

    centered "However, the silence is still awkward. But it is quickly interrupted by a question from your boss."

    scene insidecar1 with dissolve

    c_rikumi "So, we still haven't discovered your main affinity, and on your last mission, you were using a fire amulet, but my question is, do you have any element that interests you more?"

    menu:
        "I really liked fire, so yeah. I would pick it again.":
            $ main_element = 'fire'
            c_rikumi "Really? Mister Frederick can teach you a few things then."
       
        "To be honest, I would like to try Earth. I'm kind of a fan of Toph myself.":
            $ main_element = 'earth'
            c_rikumi "Earth can be both defensive and offensive, if that is your choice, I can teach you a few tricks after the mission."

        "We still don't have an air user, so it would be cool to try.":
            $ main_element = 'air'
            c_rikumi "Good choice. It would be a great help since we still don't have an air user for TEAM B."

        "Probably water. I like how it can both heal and attack.":
            $ main_element = 'water'
            c_rikumi "I was about to say that Olivia could help you but to be honest, I am pretty sure it will be somewhat complicated."

    c_rikumi "Well... if [main_element] is your choice. I have something in mind."

    play music car1 volume 0.3

    stop music

    scene black_full with dissolve

    centered "Some minutes after."

    scene hq1 with dissolve

    c_rikumi "And we arrived. We are 18 minutes late already."

    jump base
