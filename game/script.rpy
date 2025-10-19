define c_rikumi = Character('Reiko Rikumi', color="#03a103")
define c_olivia = Character('Olivia', color="#7DF9FF")
define c_fred = Character('Frederick', color="#7DF9FF")
define player = Character("[player_name]")

transform size_normal:
    ysize 1000
    fit "contain"
    center

transform left_normal:
    ysize 1000
    fit "contain"
    left

transform right_normal:
    ysize 1000
    fit "contain"
    right

transform item:
    zoom 0.5
    truecenter

label start:

    jump introduction

    return

label character_name:

    scene black_full

    centered "31st January 2028, 8 a.m - Guardian Call HQ - London (United Kingdom)"
    
    c_rikumi "Great. Just write your name here and you will become an official member of Guardian Call."
    $ player_name = renpy.input("Name here: ", length=32)
    $ player_name = player_name.strip()

    play sound signature volume 0.3
    pause 3

    if player_name == "" or player_name == "." :
        $ player_name="Charles"

    c_rikumi "Welcome to Guardian's Call dear [player]. Like I said, starting today, I will be your boss and you will be joining the team that I take care of, which is TEAM B."

    jump news_raining