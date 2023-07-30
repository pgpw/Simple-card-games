init python:
    def sum21(x):#======================== CУММА КАРТ===============================================
        z=0
        for i in x:
            z+=i.num
        return z
    def getcard21(x):#======================== БЕРЕМ ЕЩЁ КАРТУ =======================================
        for n,i in enumerate(x):
            if not i.num:
                x[n]=koloda52.pop()
                break
    def cpui():#=============================== ХОД =================================================
        global cpupoint,ipoint,btnn
        btnn+=1
        getcard21(playercards)
        if cpupoint<16:
            getcard21(cpucards)
        cpupoint=sum21(cpucards)
        ipoint=sum21(playercards)
        if cpupoint>21:
            if cpucards[0].num==11:
                kart1=1
            elif cpucards[1].num==11:
                kart2=1
            elif cpucards[3].num==11:
                cpucards[3].num=1
            elif cpucards[3].num==11:
                cpucards[3].num=1
            elif cpucards[4].num==11:
                cpucards[4].num=1
            cpupoint=sum21(cpucards)
        if ipoint>21:
            if cpucards[0].num==11:
                kart1=1
            elif cpucards[1].num==11:
                kart2=1
            elif cpucards[3].num==11:
                cpucards[3].num=1
            elif cpucards[3].num==11:
                cpucards[3].num=1
            elif cpucards[4].num==11:
                cpucards[4].num=1
            cpupoint=sum21(cpucards)
    def cstand():#============================= ОПРЕДЕЛЯЕМ ПОБЕДИТЕЛЯ ===============================
        global iwin21,intergames,bgresult,cpupoint,ipoint
        intergames=0
        cpupoint=sum21(cpucards)
        ipoint=sum21(playercards)
        if ipoint>21:
            bgresult="b/l.png"
            if cpupoint>21:#Ничья
                iwin21=2
                bgresult="b/d.png"
        elif cpupoint>21:
            iwin21=1
            bgresult="b/w.png"
        elif ipoint is cpupoint:#Ничья
            iwin21=2
            bgresult="b/d.png"
        elif ipoint>cpupoint:
            if cpupoint<16:
                if not cpucards[1].num or not cpucards[2].num or not cpucards[3].num:
                    getcard21(cpucards)
                    cstand()
            else:
                iwin21=1
                bgresult="b/w.png"
        else:
            bgresult="b/l.png"
    def play21(kolodatip=52):#============================== ЗАПУСКАЮЩАЯ ИГРУ ФУНКЦИЯ ==============================
        global quick_menu
        start21a(kolodatip)
        quick_menu=False
        renpy.choice_for_skipping()
        renpy.call("card78")
        quick_menu=True
    def start21a(kolodatip=52):#============================== ПЕРЕМЕШИВАНИЕ И РАЗДАЧА КАРТ =========================
        global iwin21,btnn,cpucards,playercards,cpupoint,ipoint,zerocard,intergames,koloda52
        iwin21=0
        btnn=2
        zerocard=Karta(0,"b/0.png")
        zerocardkrb=Karta(0,"b/k.jpg")
        if kolodatip is 52:
            koloda52=deepcopy(base_koloda_21)
        elif kolodatip is 36:
            koloda52=deepcopy(base_koloda_21)
        ransh(koloda52)
        cpucards=[koloda52.pop(),zerocardkrb,zerocard,zerocard,zerocard]
        playercards=[koloda52.pop(),koloda52.pop(),zerocard,zerocard,zerocard]
        cpupoint=sum21(cpucards)
        ipoint=sum21(playercards)
        intergames=1
screen key_off():#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    key"game_menu"action NullAction()
    key"rollback"action NullAction()
    key"viewport_wheelup"action NullAction()
    key"viewport_wheeldown"action NullAction()
    key"viewport_up"action NullAction()
    key"viewport_down"action NullAction()
    key"hide_windows"action NullAction()
    key"skip"action NullAction()
    key"stop_skipping"action NullAction()
    key"toggle_skip"action NullAction()
    key"fast_skip"action NullAction()
    key"accessibility"action NullAction()
screen c78a():#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    use key_off
    add"b/tb.jpg"
    add"b/s.png"pos(1608,66)
    imagebutton idle"b/deal.png"pos(800,909)action Return()
screen c78():#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    use key_off
    add"b/tb.jpg"
    add"b/s.png"pos(1608,66)
    hbox pos(412,66):
        spacing 12
        for i in cpucards:
            add i.img
    hbox pos(412,681):
        spacing 12
        for i in playercards:
            add i.img
    if intergames:
        if btnn<5:
            imagebutton idle"b/hit.png"pos(52,953)action Function(cpui)
        imagebutton idle"b/stand.png"pos(1614,953)action Function(cstand)
        text"[ipoint]"pos(106,770)style"mcq"
    else:
        imagebutton idle bgresult action Return()
label card78:################################################################################################
    call screen c78a
    call screen c78
    return