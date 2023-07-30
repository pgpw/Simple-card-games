define e = Character('ИГРОК',color="#c8ffc8")
label start:
    pass
label chosecardgame:
    menu:
        "В какую игру будем играть?"
        "В 21":
            $play21()
            $oldcardgame=0
            $kolodatip=52
        "Дурак 52 карты":
            $playdurak()
            $oldcardgame=1
            $kolodatip=52
        "Дурак 36 карт":
            $playdurak(36)
            $oldcardgame=1
            $kolodatip=36
        "Пьяница":
            $play21()
            $oldcardgame=2
            $kolodatip=52
label chosecardgame2:
    if iwin21:
        if iwin21 is 2:
            $dia="Ничья!"
        else:
            $dia="Я победил!"
    else:
        $dia="Я проиграл..."
    menu:
        e "[dia]"
        "Cыграем ещё раз":
            $[play21,playdurak,play21][oldcardgame](kolodatip)
        "Давай в другую игру":
            jump chosecardgame
        "Хватит":
            return
    jump chosecardgame2
