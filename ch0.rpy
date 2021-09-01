define v = Character("Vriska",color="#005682")

label ch0:

    show pir8ship:
     size(1280,720)

    play music "mega-lowfi-nia_.ogg"

    "You spot a spidergirl on the dock."

    show vriska_placeholder at center with dissolve

    v "Wh8 the f8ck are you doing here?"

    menu:
        
        "I'm looking for a game":
            jump player
            
        "I'm a dev testing this game":
            jump dev
            
label player:

    v "Well, this game 8n't ready yet, dum8ass!"
    
    v "Come 8ack l8er and there m8 be something here!"

    jump end

label dev:

    v "Fair enough. Get on with it, then!"
    
    jump end

label end:
    
    window hide
    
    $ quick_menu = False

    show voidending with dissolve:
     size(1280,720)

    pause
    
    $ quick_menu = True
    $renpy.full_restart()