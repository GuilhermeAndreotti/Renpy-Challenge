define c_rikumi = Character('Reiko Rikumi', color="#03a103")
define player = Character("[player_name]")

transform size_normal:
    ysize 1000
    fit "contain"
    center

label start:

    jump introduction

    return

label character_name:

    scene black_full

    centered "31st January 2028, 8 a.m - Guardian Call HQ - London (United Kingdom)"
    
    c_rikumi "So. The last thing you need to do to start working with us. Just write your name here."
    $ player_name = renpy.input("Name here", length=32)
    $ player_name = player_name.strip()

    play sound signature volume 0.3
    pause 3

    c_rikumi "Welcome to Guardian's Call [player]. Starting today, I will be your boss and you will join the group that I take care of, which is TEAM B. Dont fell bad about it, we are quite strong."

    if player_name == "" or player_name == "." :
        $ player_name="Charles"

    jump news_raining