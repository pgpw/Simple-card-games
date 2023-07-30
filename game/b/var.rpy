init python:
    import time
    import random
    from copy import deepcopy
    from itertools import chain
    UIC=ui.callsinnewcontext
    UIC2=renpy.call_in_new_context
    rand,ranc,rant,ransh,ranu,rans=random.randint,random.choice,random.triangular,random.shuffle,random.uniform,random.sample
    pauza=renpy.pause
    remusplay=renpy.music.play
    class Karta(object):#======================== КЛАСС КАРТ =======================================
        __slots__ ="num","img"
        def __init__(self,num=0,img="b/0.png",suit=1):
            self.num=num   #НОМЕР
            self.img=img   #КАРТИНКА
            self.suit=suit #МАСТЬ
    #================================================================================================
    base_koloda_21=[Karta(2,"b/102.jpg",1),Karta(3,"b/103.jpg",1),Karta(4,"b/104.jpg",1),Karta(5,"b/105.jpg",1),Karta(6,"b/106.jpg",1),Karta(7,"b/107.jpg",1),Karta(8,"b/108.jpg",1),Karta(9,"b/109.jpg",1),
            Karta(10,"b/110.jpg",1),Karta(10,"b/110a.jpg",1),Karta(10,"b/110b.jpg",1),Karta(10,"b/110c.jpg",1),Karta(11,"b/111.jpg",1),
            Karta(2,"b/202.jpg",2),Karta(3,"b/203.jpg",2),Karta(4,"b/204.jpg",2),Karta(5,"b/205.jpg",2),Karta(6,"b/206.jpg",2),Karta(7,"b/207.jpg",2),Karta(8,"b/208.jpg",2),Karta(9,"b/209.jpg",2),
            Karta(10,"b/210.jpg",2),Karta(10,"b/210a.jpg",2),Karta(10,"b/210b.jpg",2),Karta(10,"b/210c.jpg",2),Karta(11,"b/211.jpg",2),
            Karta(2,"b/302.jpg",3),Karta(3,"b/303.jpg",3),Karta(4,"b/304.jpg",3),Karta(5,"b/305.jpg",3),Karta(6,"b/306.jpg",3),Karta(7,"b/307.jpg",3),Karta(8,"b/308.jpg",3),Karta(9,"b/309.jpg",3),
            Karta(10,"b/310.jpg",3),Karta(10,"b/310a.jpg",3),Karta(10,"b/310b.jpg",3),Karta(10,"b/310c.jpg",3),Karta(11,"b/311.jpg",3),
            Karta(2,"b/402.jpg",4),Karta(3,"b/403.jpg",4),Karta(4,"b/404.jpg",4),Karta(5,"b/405.jpg",4),Karta(6,"b/406.jpg",4),Karta(7,"b/407.jpg",4),Karta(8,"b/408.jpg",4),Karta(9,"b/409.jpg",4),
            Karta(10,"b/410.jpg",4),Karta(10,"b/410a.jpg",4),Karta(10,"b/410b.jpg",4),Karta(10,"b/410c.jpg",4),Karta(11,"b/411.jpg",4)]
    base_koloda_durak=[Karta(2,"b/102.jpg",1),Karta(3,"b/103.jpg",1),Karta(4,"b/104.jpg",1),Karta(5,"b/105.jpg",1),Karta(6,"b/106.jpg",1),Karta(7,"b/107.jpg",1),Karta(8,"b/108.jpg",1),Karta(9,"b/109.jpg",1),
            Karta(10,"b/110.jpg",1),Karta(11,"b/110a.jpg",1),Karta(12,"b/110b.jpg",1),Karta(13,"b/110c.jpg",1),Karta(14,"b/111.jpg",1),
            Karta(2,"b/202.jpg",2),Karta(3,"b/203.jpg",2),Karta(4,"b/204.jpg",2),Karta(5,"b/205.jpg",2),Karta(6,"b/206.jpg",2),Karta(7,"b/207.jpg",2),Karta(8,"b/208.jpg",2),Karta(9,"b/209.jpg",2),
            Karta(10,"b/210.jpg",2),Karta(11,"b/210a.jpg",2),Karta(12,"b/210b.jpg",2),Karta(13,"b/210c.jpg",2),Karta(14,"b/211.jpg",2),
            Karta(2,"b/302.jpg",3),Karta(3,"b/303.jpg",3),Karta(4,"b/304.jpg",3),Karta(5,"b/305.jpg",3),Karta(6,"b/306.jpg",3),Karta(7,"b/307.jpg",3),Karta(8,"b/308.jpg",3),Karta(9,"b/309.jpg",3),
            Karta(10,"b/310.jpg",3),Karta(11,"b/310a.jpg",3),Karta(12,"b/310b.jpg",3),Karta(13,"b/310c.jpg",3),Karta(14,"b/311.jpg",3),
            Karta(2,"b/402.jpg",4),Karta(3,"b/403.jpg",4),Karta(4,"b/404.jpg",4),Karta(5,"b/405.jpg",4),Karta(6,"b/406.jpg",4),Karta(7,"b/407.jpg",4),Karta(8,"b/408.jpg",4),Karta(9,"b/409.jpg",4),
            Karta(10,"b/410.jpg",4),Karta(11,"b/410a.jpg",4),Karta(12,"b/410b.jpg",4),Karta(13,"b/410c.jpg",4),Karta(14,"b/411.jpg",4)]
    base_koloda_durak36=[Karta(6,"b/106.jpg",1),Karta(7,"b/107.jpg",1),Karta(8,"b/108.jpg",1),Karta(9,"b/109.jpg",1),
            Karta(10,"b/110.jpg",1),Karta(11,"b/110a.jpg",1),Karta(12,"b/110b.jpg",1),Karta(13,"b/110c.jpg",1),Karta(14,"b/111.jpg",1),
            Karta(6,"b/206.jpg",2),Karta(7,"b/207.jpg",2),Karta(8,"b/208.jpg",2),Karta(9,"b/209.jpg",2),
            Karta(10,"b/210.jpg",2),Karta(11,"b/210a.jpg",2),Karta(12,"b/210b.jpg",2),Karta(13,"b/210c.jpg",2),Karta(14,"b/211.jpg",2),
            Karta(6,"b/306.jpg",3),Karta(7,"b/307.jpg",3),Karta(8,"b/308.jpg",3),Karta(9,"b/309.jpg",3),
            Karta(10,"b/310.jpg",3),Karta(11,"b/310a.jpg",3),Karta(12,"b/310b.jpg",3),Karta(13,"b/310c.jpg",3),Karta(14,"b/311.jpg",3),
            Karta(6,"b/406.jpg",4),Karta(7,"b/407.jpg",4),Karta(8,"b/408.jpg",4),Karta(9,"b/409.jpg",4),
            Karta(10,"b/410.jpg",4),Karta(11,"b/410a.jpg",4),Karta(12,"b/410b.jpg",4),Karta(13,"b/410c.jpg",4),Karta(14,"b/411.jpg",4)]