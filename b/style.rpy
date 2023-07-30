init python:
    style.mcq=Style(style.default)
    style.mcq.set_parent(style.button)
    style.mcq.color="#000000"
    style.mcq.size=84
    style.mcq.line_spacing=0
    style.mcq.outlines=((1,"#6a5431",1,1),)
    #----------------------------------- ОПИСАНИЕ КАРТЫ
    style.cinfo=Style(style.default)
    style.cinfo.xalign=.5
    style.cinfo.yalign=.5
#----------------------------------- ИМЯ КАТЫ
    style.cname=Style(style.default)
    style.cname.xalign=.5
    style.cname.yalign=.5
    style.cname.font="a/font/avanteint.ttf"
    style.cname.outlines=[(absolute(1),"#000",absolute(0),absolute(0))]
#-----------------------------------
    style.yget=Style(style.default)
    style.yget.font="a/font/avanteint.ttf"
    style.yget.outlines=[(absolute(1),"#000",absolute(0),absolute(0))]
    style.yget.color="#f9b513"
    style.yget.size=48
#-----------------------------------
    style.otxtbtn=Style(style.default)
    style.otxtbtn.font="a/font/avanteint.ttf"
    
    style.btxtbtn=Style(style.default)
    style.btxtbtn.font="a/font/avanteint.ttf"
#style word_list is button:
#    background "#FFFF00"              # Yellow 

style otxtbtn_text is text:
    size 64
    hover_color "#d87f38"             # 
    color "#ad6638"                   # 
    outlines [(absolute(1),"#000",absolute(0),absolute(0))]
style btxtbtn_text is text:
    size 64
    hover_color "#39acdc"             # 
    color "#4e83b9"                   # 
    outlines [(absolute(1),"#000",absolute(0),absolute(0))]