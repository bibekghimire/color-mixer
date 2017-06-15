from tkinter import Frame,Scale,Label,Button,Tk,mainloop
top=Tk()
frame=Frame(top)
red=Scale(frame,from_=0,to=255,fg='white')
green=Scale(frame,from_=0,to=255,fg='white')
blue=Scale(frame,from_=0,to=255,fg='white')

label=Label(top,font='helbetica -25 bold italic')
def set_color(x=None):
    
    a=[hex(item.get()).split('x')[1] for item in(red,green,blue)]
    for i in range(3):
        if len(a[i])<2:
            a[i]='0%s'%a[i]
    c='#%s%s%s'%(a[0],a[1],a[2])
    label['text']=c
    frame['bg']=c
    red['bg']='#%s0000'%a[0]
    green['bg']='#00%s00'%a[1]
    blue['bg']='#0000%s'%a[2]
label.pack(side='top',fill='x',expand='no')
red.pack(side='left',fill='y',expand='true')
green.pack(side='left',fill='y',expand='true')
blue.pack(side='left',fill='y',expand='true')
frame.pack(side='top',fill='both',expand='true')
red['command']=set_color
green['command']=set_color
blue['command']=set_color

mainloop()
