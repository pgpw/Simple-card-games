init python:
    import time
    import random
    UIC=ui.callsinnewcontext
    UIC2=renpy.call_in_new_context
    rand,ranc,rant,ransh,ranu,rans=random.randint,random.choice,random.triangular,random.shuffle,random.uniform,random.sample
    pauza=renpy.pause
    remusplay=renpy.music.play
    style.mcq=Style(style.default)
    style.mcq.set_parent(style.button)
    style.mcq.color="#000000"
    style.mcq.size=84
    style.mcq.line_spacing=0
    style.mcq.outlines=((1,"#6a5431",1,1),)
    class Karta(object):#======================== КЛАСС КАРТ =======================================
        __slots__ ="num","img"
        def __init__(self,num=0,img="b/0.png"):
            self.num=num #НОМЕР
            self.img=img #КАРТИНКА
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
    def start21():#============================== ЗАПУСКАЮЩАЯ ИГРУ ФУНКЦИЯ ==============================
        start21a()
        renpy.call("card78")
    def start21a():#============================== ПЕРЕМЕШИВАНИЕ И РАЗДАЧА КАРТ =========================
        global iwin21,btnn,cpucards,playercards,cpupoint,ipoint,zerocard,intergames,koloda52
        iwin21=0
        btnn=2
        zerocard=Karta(0,"b/0.png")
        zerocardkrb=Karta(0,"b/k.jpg")
        koloda52=[Karta(2,"b/102.jpg"),Karta(3,"b/103.jpg"),Karta(4,"b/104.jpg"),Karta(5,"b/105.jpg"),Karta(6,"b/106.jpg"),Karta(7,"b/107.jpg"),Karta(8,"b/108.jpg"),Karta(9,"b/109.jpg"),
            Karta(10,"b/110.jpg"),Karta(10,"b/110a.jpg"),Karta(10,"b/110b.jpg"),Karta(10,"b/110c.jpg"),Karta(11,"b/111.jpg"),
            Karta(2,"b/202.jpg"),Karta(3,"b/203.jpg"),Karta(4,"b/204.jpg"),Karta(5,"b/205.jpg"),Karta(6,"b/206.jpg"),Karta(7,"b/207.jpg"),Karta(8,"b/208.jpg"),Karta(9,"b/209.jpg"),
            Karta(10,"b/210.jpg"),Karta(10,"b/210a.jpg"),Karta(10,"b/210b.jpg"),Karta(10,"b/210c.jpg"),Karta(11,"b/211.jpg"),
            Karta(2,"b/302.jpg"),Karta(3,"b/303.jpg"),Karta(4,"b/304.jpg"),Karta(5,"b/305.jpg"),Karta(6,"b/306.jpg"),Karta(7,"b/307.jpg"),Karta(8,"b/308.jpg"),Karta(9,"b/309.jpg"),
            Karta(10,"b/310.jpg"),Karta(10,"b/310a.jpg"),Karta(10,"b/310b.jpg"),Karta(10,"b/310c.jpg"),Karta(11,"b/311.jpg"),
            Karta(2,"b/402.jpg"),Karta(3,"b/403.jpg"),Karta(4,"b/404.jpg"),Karta(5,"b/405.jpg"),Karta(6,"b/406.jpg"),Karta(7,"b/407.jpg"),Karta(8,"b/408.jpg"),Karta(9,"b/409.jpg"),
            Karta(10,"b/410.jpg"),Karta(10,"b/410a.jpg"),Karta(10,"b/410b.jpg"),Karta(10,"b/410c.jpg"),Karta(11,"b/411.jpg")]
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
    if iwin21 is 2:
        $start21a()
        jump card78
    return