label machine_fred:
    
    $ keyword_fred = 'different types'

    scene corridor1 with dissolve

    show frederick_base2 at size_normal

    c_fred "Boss told us to pay attention to details but I wonder which details."

    player "Maybe how it works?"

    c_fred "Yeah. It could be."

    hide frederick_base2
    show frederick_base1 at size_normal

    c_fred "Well. Let's go there first before thinking about the details."

    scene vending1 with dissolve

    show frederick_base2 at size_normal

    c_fred "Well, I don't see anything special, just two machines, one for drinks and the small one for snacks. For now, just insert the money, pal."

    player "Sure thing."

    "As you put the money, you grab the iced coffee Reiko asked for."

    hide frederick_base2
    show frederick_base1 at size_normal
    
    c_fred "I was wondering with myself, she asked for the iced coffee, this one is just for drinks. So... the fact that there are {color=#f00}different {/color}types of vending machine is something she wants to hear."

    jump mission