init python:
    import re

    if persistent.quirklist == None:
        persistent.quirklist = []
    templist = []

    def quirk(text):
        modstr = text
        for x in persistent.quirklist:
            modstr = re.sub(x[0],x[1],modstr,0,flags=re.IGNORECASE)
            if r"\U" in modstr:
                for x in range(0,len(modstr)-2):
                    if modstr[x:x+2] == r"\U":
                        modstr = modstr.replace(modstr[x:x+3], modstr[x+2].upper())
            if r"\l" in modstr:
                for x in range(0,len(modstr)-2):
                    if modstr[x:x+2] == r"\l":
                        modstr = modstr.replace(modstr[x:x+3], modstr[x+2].lower())
        return modstr

    def quirkadd(lkup,rplc):
        persistent.quirklist.append([str(lkup),str(rplc)])
        lkup = ""
        rplc = ""

    def quirkrem(rem):
        persistent.quirklist.remove(rem)

    if persistent.name == None:
        persistent.name = "None"

screen charcreate():
    tag menu
    
    default castecreate = Tooltip(persistent.bloodclr)
    
    default aprnc_tab = Tooltip(1)

    default namefield = Tooltip(persistent.name)

    default quirktemp1 = "Lookup"
    default quirktemp2 = "Replace"

    use game_menu(_("Character creation"), scroll="viewport"):
        style_prefix "about"
        
        vbox:
            xfill True
            spacing 10
            
            hbox:
                ysize 550
                spacing 10
                
                frame:
                    yfill True
                    vbox:
                        xsize 100
                        spacing 10
                        
                        text "CASTE:" color castecreate.value xalign .5 size 24 ypos 5
                        frame:
                            background Solid(castecreate.value)
                            xsize 70
                            ysize 30
                            xalign .5
                            text "CURRENT" xalign .5 yalign .5 size 12 color "#000"
                            
                        null height 10
                        
                        button background Solid("#a30000") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#a30000"),SetVariable("persistent.bloodclr","#a30000")]
                        
                        button background Solid("#a25203") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#a25203"),SetVariable("persistent.bloodclr","#a25203")]
                        
                        button background Solid("#a1a100") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#a1a100"),SetVariable("persistent.bloodclr","#a1a100")]
                        
                        button background Solid("#ff0000") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#ff0000"),SetVariable("persistent.bloodclr","#ff0000")]
                        
                        button background Solid("#416600") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#416600"),SetVariable("persistent.bloodclr","#416600")]
                        
                        button background Solid("#078446") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#078446"),SetVariable("persistent.bloodclr","#078446")]
                        
                        button background Solid("#008282") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#008282"),SetVariable("persistent.bloodclr","#008282")]
                        
                        button background Solid("#004182") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#004182"),SetVariable("persistent.bloodclr","#004182")]
                        
                        button background Solid("#0021cb") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#0021cb"),SetVariable("persistent.bloodclr","#0021cb")]
                        
                        button background Solid("#440a7f") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#440a7f"),SetVariable("persistent.bloodclr","#440a7f")]
                        
                        button background Solid("#6a006a") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#6a006a"),SetVariable("persistent.bloodclr","#6a006a")]
                
                vbox:
                    frame:
                        hbox:
                            xfill True
                            yfill True
                            vbox:
                                xsize 450
                                yfill True
                                frame:
                                    background Solid(castecreate.value)
                                    xfill True
                                    ysize 450   
                                    text "Image Placeholder" color "#000" xalign .5 yalign .5 size 15
                                hbox:
                                    frame:
                                        xsize 90
                                        yfill True
                                        button:
                                            text "Layer 1"
                                            action aprnc_tab.Action(1)
                                            
                                    frame:
                                        xsize 90
                                        yfill True
                                        button:
                                            text "Layer 2"
                                            action aprnc_tab.Action(2)
                                            
                                    frame:
                                        xsize 90
                                        yfill True
                                        button:
                                            text "Layer 3"
                                            action aprnc_tab.Action(3)
                                            
                                    frame:
                                        xsize 90
                                        yfill True
                                        button:
                                            text "Layer 4"
                                            action aprnc_tab.Action(4)
                                            
                                    frame:
                                        xsize 90
                                        yfill True
                                        button:
                                            text "Layer 5"
                                            action aprnc_tab.Action(5)
                            vbox:
                                frame:
                                    xfill True
                                    padding (10,10)
                                    vbox:
                                        text "NAME:" size 15
                                        hbox: 
                                            text namefield.value size 40
                                            textbutton u"\u270E"text_size 40 text_font "DejaVuSans.ttf" text_color "#fff"
                                hbox:
                                    xalign .5
                                    xoffset -2
                                    ypos 3
                                    box_wrap True
                                    spacing 10
                                    box_wrap_spacing 10
                                
                                    if aprnc_tab.value == 1:
                                        button:
                                            xysize(75,75)
                                            background Frame("gui/window_icon.png", 0, 0)
                                    
                                    if aprnc_tab.value == 2:
                                        button:
                                            xysize(75,75)
                                            background Frame("gui/window_icon.png", 0, 0)
                                    
                                    if aprnc_tab.value == 3:
                                        button:
                                            xysize(75,75)
                                            background Frame("gui/window_icon.png", 0, 0)
                                    
                                    if aprnc_tab.value == 4:
                                        button:
                                            xysize(75,75)
                                            background Frame("gui/window_icon.png", 0, 0)
                                    
                                    if aprnc_tab.value == 5:
                                        button:
                                            xysize(75,75)
                                            background Frame("gui/window_icon.png", 0, 0)
                                    for x in range(0,4): ## placeholder, remove if all tabs have four or more items
                                        frame:
                                            xysize (75,75)
                                            background Solid("#fff")
                                        
            frame:
                padding (10,5)
                vbox:
                    spacing 5
                    xfill True
                    text quirk("Quirk:") size 30 color castecreate.value
                    frame:
                        ysize 3
                        background Solid(castecreate.value)
                        xfill True
                   
                    text quirk("Examples:") size 15
                   
                    text quirk("The quick brown fox jumped over the lazy dog.") size 15
                   
                    text quirk("Sphinx of black quartz, judge my vow.") size 15
                   
                    text quirk("Pack my box with five dozen liquor jugs.") size 15

                    text quirk("Tip: Put two slashes followed by either an uppercase U or lowercase l before a matched regex group for upper- and lowercase text, respectively.") size 15
                    
                    frame:
                        ysize 3
                        background Solid(castecreate.value)
                        xfill True
                    
                    for x in persistent.quirklist:
                        $ i = persistent.quirklist.index(x)
                        hbox:
                            spacing 12
                            text str(i+1)+"." size 20

                            button:
                                xysize (250,20)
                                background Solid("#333")
                                text x[0] size 16 yalign .5
                                action Function(renpy.call_in_new_context,"inpt",*str(i)+"0")
                            text "=" size 20
                            button:
                                xysize (250,20)
                                background Solid("#333")
                                text x[1] size 16 yalign .5
                                action Function(renpy.call_in_new_context,"inpt",*str(i)+"1")
                            button:
                                xysize (20,20)
                                text "-" size 20 yalign .5
                                background Solid("#a30000")
                                action Function(quirkrem,x)
                            
                
                    hbox:
                        spacing 12
                        text str(len(persistent.quirklist)+1)+"." size 20

                        button:
                            xysize (250,20)
                            background Solid("#333")
                            text quirktemp1 size 16 yalign .5
                            action Function(renpy.call_in_new_context,"inpt",*[quirktemp1])
                        text "=" size 20
                        button:
                            xysize (250,20)
                            background Solid("#333")
                            text quirktemp2 size 16 yalign .5
                            action Function(renpy.call_in_new_context,"inpt",*[quirktemp2])
                        button:
                            xysize (20,20)
                            text "+" size 20 yalign .5
                            background Solid("#658200")
                            action Function(quirkadd,quirktemp1,quirktemp2)

label inpt(var,var2="-1"):

    python:
        inptv = renpy.input('Input:')
        if var2.isdigit() and var2 > 0:
            persistent.quirklist[int(var)][int(var2)] = inptv
        else:
            globals()[var] = inptv
        renpy.pause()
