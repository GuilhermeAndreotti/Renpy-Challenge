
label park:
    
    scene entranceseal with dissolve

    show guard2  at size_normal

    "Blue Guard" "Please show me your IDs if you are all here for the mission."

    "You, Olivia, Reiko and Frederick show the IDs, proving that you are all from Guardian Call."

    hide guard2

    show guard2 at right_normal
    show guard at left_normal

    "Kawara Norio" "Hello, Guardian Call. It's such a pleasure to meet you all. I am Kawara Norio, a member from the engo-ji clan. "

    "Kawara Norio" "Me and a few other lower-rank hunters are keeping this barrier active to avoid more creatures to enter and leave."

    "Kawara Norio" "We apologise that no high-ranking hunters of Engo-ji are here to help, but our situation is indeed complicated in Tokyo."

    "As the guard speaks english, Reiko keeps her silence, looking like she expecting you all to deal with the situation."

    default score = 10

    menu:
        "Don't worry, just keeping the barrier up is already a big help.":
            "Reiko seems happy with your response."
            "Kawara Norio" "Alright, we thank you all, good luck. I am opening the barrier for you all."

        "Damn you, just lower this dumb barrier and let us do our job.":
            "It seems Reiko didn't like the way you responded."
            hide guard
            show olivia_base1 at left_normal
            c_olivia "BUAHAHAHAHA! Even I didn't expect that coming. Good one, human."
            "The guard silently opens a part of the barrier, allowing you all to enter."
            $ score -= 1
            
        "Don't worry, my friends and I will take care of this. I trust them as we trust you!":
            "Reiko smiles, apparently it was a good response."
            "Kawara Norio" "Thank you, mister. Good luck inside."
            "The guard opens a part of the barrier, allowing you all to enter."
    
    scene entranceseal
    scene entrance with Dissolve(4)

    stop music 
    
    $ defeated = 0

    show frederick_base1 at size_normal

    c_fred "So we are here. I recommend we don't go out breaking everything. Hey boss, do we need to defeat every creature here?"

    show rikumi_base1 at left_normal

    c_rikumi "The main goal is to defeat the Aether creature. But it is also interesting to reduce the number of creatures here by its total."

    hide frederick_base1 
    hide rikumi_base1
    show olivia_base1 at size_normal

    c_olivia "YOU FOOLS TAKE TOO LONG DECIDING WHAT DO YOU. GOOD BYE. I AM GOING AFTER THE AETHER CREATURE, YOU TWO, DEFEAT THE OTHER ONES."

    hide olivia_base1
    show olivia_base2 at size_normal:
        xoffset 0
        linear 0.6 xoffset 3000

    c_olivia "BYEEEEEE!!"

    hide olivia_base1

    show frederick_base1 at size_normal

    c_fred "Hey pal, don't worry about her, she is basically an immortal. She is stupid, but she manages to get out of any situation."

    player "We should go after here, Fred. She can ended up absorbed."

    hide frederick_base1
    show frederick_base2 at size_normal

    c_fred "Well... You are right, since we are under Reiko's test, so... shit... Let's go after that walking disaster."

    jump path_save



    
