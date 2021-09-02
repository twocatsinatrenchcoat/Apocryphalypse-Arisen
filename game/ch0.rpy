define vriska = Character("Vriska",color="#005682")
define aa = Character("",what_color="#a30000",what_prefix="AA: ",kind=nvl)
define player = Character("",what_color="#000",what_prefix="You: ",kind=nvl)
define pchum = Character("",what_color="#000",kind=nvl)

label ch0:

    $ contactname = "apocalypseArisen"

    pchum "--- {color=#a30000}apocalypseArisen{/color} started pestering You at 15:37 ---"
    aa "hi h0w are y0u d0ing"
    aa "this is a test 0f the pesterl0g system"
    aa "i need t0 kn0w h0w many lines fit 0n the screen"
    aa "s0 i'll just keep 0n blathering f0r n0w"
    aa "can y0u hear me?{nw}"
    menu (nvl=True):
        "yeah":
            player "{cps=5}yeah{/cps}"
        "yep":
            player "{cps=5}yep{/cps}"
        "yes":
            player "{cps=5}yes{/cps}"
    aa "0h nice"
    aa "8 lines"
    aa "wuh0h i sh0uldn't have said that here she c0mes"

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
