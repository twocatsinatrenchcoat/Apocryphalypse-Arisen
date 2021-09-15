init offset = -1

init python:
    import re

    if persistent.bloodclr == None:
        persistent.bloodclr = "#626262"
        
    if persistent.bloodclr_string == None:
        persistent.bloodclr_string = "None"
        
    if persistent.quirklist == None:
        persistent.quirklist = [] 

    def quirk(text):
        modstr = text
        for x in persistent.quirklist:
            try:
                re.sub(x[0],x[1],modstr,0,flags=re.IGNORECASE)
            except:
                modstr = text + "(Quirk error - Invalid replace)"
                break
            modstr = re.sub(x[0],x[1],modstr,0,flags=re.IGNORECASE)
            if r"\U" in modstr:
                for x in range(0,len(modstr)-2):
                    if modstr[x:x+2] == r"\U":
                        try:
                            modstr.replace(modstr[x:x+3], modstr[x+2].upper())
                        except:
                            modstr = text + "(Quirk error - Lookup string too short to capitalize)"
                            break
                        else:
                            modstr = modstr.replace(modstr[x:x+3], modstr[x+2].upper())
            if r"\l" in modstr:
                for x in range(0,len(modstr)-2):
                    if modstr[x:x+2] == r"\l":
                        try:
                            modstr.replace(modstr[x:x+3], modstr[x+2].lower())
                        except:
                            modstr = text + "(Quirk error - Lookup string too short to decapitalize)"
                            break
                        else:
                            modstr = modstr.replace(modstr[x:x+3], modstr[x+2].lower())
        return modstr

    def quirkadd(lkup,rplc):
        persistent.quirklist.append([str(lkup),str(rplc)])
        lkup = ""
        rplc = ""

    def quirkrem(rem):
        del persistent.quirklist[rem]

    focusnumber = -1
    quirktemp1 = "Lookup"
    quirktemp2 = "Replace"

    if persistent.name == None:
        persistent.name = "None"

    if persistent.chumhandle == None:
        persistent.chumhandle = "anonymousChum"
        persistent.chumabbrev = "AC"
        
    namevar = persistent.name
    chumvar = persistent.chumhandle

screen charcreate():
    tag menu
    
    default castecreate = Tooltip(persistent.bloodclr)
    
    default aprnc_tab = Tooltip(1)


    use game_menu(_("Character creation"), scroll="viewport"):
        style_prefix "about"
        
        key "K_RETURN" action SetVariable("focusnumber",-1)
        
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
                            
                        null height 7.5
                        
                        if persistent.ee_candyred_unlocked:
                            button background Solid("#ff0000") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#ff0000"),SetVariable("persistent.bloodclr","#ff0000"),SetVariable("persistent.bloodclr_string","Candy-Red")]
                        else:
                            frame:
                                xysize (60,30) 
                                xalign .5
                                background Solid("#626262")
                                add "padlock.png" xalign .5 yalign .5 size (23,23)
                        
                        button background Solid("#a30000") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#a30000"),SetVariable("persistent.bloodclr","#a30000"),SetVariable("persistent.bloodclr_string","Rust")]
                        
                        button background Solid("#a25203") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#a25203"),SetVariable("persistent.bloodclr","#a25203"),SetVariable("persistent.bloodclr_string","Bronze")]
                        
                        button background Solid("#a1a100") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#a1a100"),SetVariable("persistent.bloodclr","#a1a100"),SetVariable("persistent.bloodclr_string","Gold")]
                        
                        button background Solid("#416600") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#416600"),SetVariable("persistent.bloodclr","#416600"),SetVariable("persistent.bloodclr_string","Olive")]
                        
                        button background Solid("#078446") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#078446"),SetVariable("persistent.bloodclr","#078446"),SetVariable("persistent.bloodclr_string","Jade")]
                        
                        button background Solid("#008282") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#008282"),SetVariable("persistent.bloodclr","#008282"),SetVariable("persistent.bloodclr_string","Teal")]
                        
                        button background Solid("#004182") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#004182"),SetVariable("persistent.bloodclr","#004182"),SetVariable("persistent.bloodclr_string","Cerulean")]
                        
                        button background Solid("#0021cb") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#0021cb"),SetVariable("persistent.bloodclr","#0021cb"),SetVariable("persistent.bloodclr_string","Indigo")]
                        
                        button background Solid("#440a7f") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#440a7f"),SetVariable("persistent.bloodclr","#440a7f"),SetVariable("persistent.bloodclr_string","Purple")]
                        
                        button background Solid("#6a006a") xsize 60 ysize 30 xalign .5 action [castecreate.Action("#6a006a"),SetVariable("persistent.bloodclr","#6a006a"),SetVariable("persistent.bloodclr_string","Violet")]
                
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
                                            if focusnumber == 2:
                                                window:
                                                    xsize 290
                                                    ysize 40
                                                    background Solid("#444")
                                                    input value VariableInputValue("namevar") copypaste True length 13 size 37 color "#fff"
                                                $ persistent.name = namevar
                                            else:
                                                text persistent.name size 37
                                                textbutton u"\u270E" text_size 37 text_font "DejaVuSans.ttf" text_color "#fff" action SetVariable("focusnumber",2)
                                        if focusnumber == 2:
                                            null height 12
                                        text "CHUMHANDLE:" size 15
                                        hbox: 
                                            if focusnumber == 3:
                                                window:
                                                    xsize 290
                                                    ysize 23
                                                    background Solid("#444")
                                                    input value VariableInputValue("chumvar") copypaste True length 20 size 20 color persistent.bloodclr
                                                $ persistent.chumhandle = chumvar
                                                $ persistent.chumabbrev = re.sub(r"(\w)\w*([A-Z])\w*", "\\1\\2", chumvar).upper()
                                                if len(persistent.chumabbrev) > 2:
                                                    $ persistent.chumabbrev = persistent.chumabbrev[0:2]
                                            else:
                                                text "[[" + persistent.chumabbrev +"] " + persistent.chumhandle size 20 color persistent.bloodclr
                                                textbutton u"\u270E" text_size 20 text_font "DejaVuSans.ttf" text_color persistent.bloodclr action SetVariable("focusnumber",3)
                                        if focusnumber == 3:
                                            null height 9
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

                            if focusnumber == 2*i+4:
                                window:
                                    background Solid("#444")
                                    input value DictInputValue(persistent.quirklist[i],0) copypaste True
                                    xysize (250,20)
                                    yalign .5
                            else:
                                textbutton "%s" % (x[0]) action SetVariable("focusnumber",2*i+4) xysize (250,20) background Solid("#333") text_size 20 text_yalign .5
                            text "=" size 20
                            if focusnumber == 2*i+5:
                                window:
                                    background Solid("#444")
                                    input value DictInputValue(persistent.quirklist[i],1) copypaste True
                                    xysize (250,20)
                                    yalign .5
                            else:
                                textbutton "%s" % (x[1]) action SetVariable("focusnumber",2*i+5) xysize (250,20) background Solid("#333") text_size 20 text_yalign .5
                            button:
                                xysize (20,20)
                                text "-" size 20 yalign .5
                                background Solid("#a30000")
                                action Function(quirkrem,i)
                
                    hbox:
                        spacing 12
                        text str(len(persistent.quirklist)+1)+"." size 20

                        if focusnumber == 0:
                            window:
                                background Solid("#444")
                                input value VariableInputValue("quirktemp1") copypaste True
                                xysize (250,20)
                                yalign .5
                        else:
                            textbutton "[quirktemp1]" action SetVariable("focusnumber",0) xysize (250,20) background Solid("#333") text_size 20 text_yalign .5
                        text "=" size 20
                        if focusnumber == 1:
                            window:
                                background Solid("#444")
                                input value VariableInputValue("quirktemp2") copypaste True
                                xysize (250,20)
                                yalign .5
                        else:
                            textbutton "[quirktemp2]" action SetVariable("focusnumber",1) xysize (250,20) background Solid("#333") text_size 20 text_yalign .5
                        button:
                            xysize (20,20)
                            text "+" size 20 yalign .5
                            background Solid("#658200")
                            action Function(quirkadd,quirktemp1,quirktemp2)
