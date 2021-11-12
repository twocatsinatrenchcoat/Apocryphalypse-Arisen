label ch01:

    $ prns = random.choice(persistent.prns) 
    $ contactname = "arsenicCatnip"

    pchum "{color=#000}--- {color=#416600}arsenicCatnip{/color} started pestering{/color} [persistent.chumhandle] {color=#000}at 15:37 ---{/color}"
    ac ":33 < *the meowghty lioness pounces in!*{nw}"
    menu (nvl=True):
        "*[persistent.chumabbrev] plays along!*":
            python:
                renpy.say(player, "{cps=15}"+quirk("yeah")+"{/cps}")
        "*[persistent.chumabbrev] tells AC it's urgent!*":
            python:
                renpy.say(player, "{cps=15}"+quirk("*[persistent.chumabbrev] says [prns[0]] is very sorry!*")+"{/cps}")
                renpy.say(player, "{cps=15}"+quirk("*but there isn't any time for roleplay right now!*")+"{/cps}")
                renpy.say(player, "{cps=15}"+quirk("*however, [prns[0]] offers to roleplay with AC sometime later!*")+"{/cps}")
            ac ":33 < nyaww thats a shame..."
            ac ":33 < *but AC will definitely take that offer!*"
            ac ":33 < anyway what did mew want to talk ameowt?"
        "Please stop.":
            python:
                renpy.say(player, "{cps=15}"+quirk("Look, I don't have time for your games.")+"{/cps}")
                renpy.say(player, "{cps=15}"+quirk("This needs to be taken seriously.")+"{/cps}")
            ac ":33 < well if mew want to be a buzzkill >://"
    
    jump end