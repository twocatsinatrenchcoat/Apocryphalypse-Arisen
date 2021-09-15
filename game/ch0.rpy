define vriska = Character("Vriska",color="#005682")
define aa = Character("",what_color="#a30000",what_prefix="AA: ",kind=nvl)
define player = Character("",what_color=persistent.bloodclr,what_prefix="[persistent.chumabbrev]: ",kind=nvl)
define pchum= Character("",what_color=persistent.bloodclr,kind=nvl)

label ch0:

    $ contactname = "apocalypseArisen"

    pchum "{color=#000}--- {color=#a30000}apocalypseArisen{/color} started pestering{/color} [persistent.chumhandle] {color=#000}at 15:37 ---{/color}"
    aa "hi h0w are y0u d0ing"
    aa "this is a test 0f the pesterl0g system"
    aa "i need t0 kn0w h0w many lines fit 0n the screen"
    aa "s0 i'll just keep 0n blathering f0r n0w"
    aa "can y0u hear me?{nw}"
    menu (nvl=True):
        "yeah":
            python:
                renpy.say(player, "{cps=10}"+quirk("yeah")+"{/cps}")
        "yep":
            python:
                renpy.say(player, "{cps=10}"+quirk("yep")+"{/cps}")
        "yes":
            python:
                renpy.say(player, "{cps=10}"+quirk("yes")+"{/cps}")
    aa "0h nice"
    aa "what's y0ur fav0rite pangram?{nw}"
    menu (nvl=True):
        "The quick brown fox...":
            python:
                renpy.say(player, "{cps=15}"+quirk("The quick brown fox jumped over the lazy dog.")+"{/cps}")
        "Sphinx of black quartz...":
            python:
                renpy.say(player, "{cps=15}"+quirk("Sphinx of black quartz, judge my vow.")+"{/cps}")
        "Pack my box with...":
            python:
                renpy.say(player, "{cps=15}"+quirk("Pack my box with five dozen liquor jugs.")+"{/cps}")
    aa "i als0 like that 0ne"
    aa "anyway here c0mes vriska"

    show pir8ship:
     size(1280,720)

    play music "mega-lowfi-nia_.ogg"

    "You spot a spidergirl on the dock."

    show vriska_placeholder at center with dissolve

    vriska "Wh8 the f8ck are you doing here?"

    menu:
        
        "I'm looking for a game":
            jump player
            
        "I'm a dev testing this game":
            jump dev
            
label player:

    vriska "Well, this game 8n't ready yet, dum8ass!"
    
    vriska "Come 8ack l8er and there m8 be something here!"

    jump end

label dev:

    vriska "Fair enough. Get on with it, then!"
    
    jump end

label end:
    
    window hide
    
    $ quick_menu = False

    show voidending with dissolve:
     size(1280,720)

    pause
    
    $ quick_menu = True
    $renpy.full_restart()
