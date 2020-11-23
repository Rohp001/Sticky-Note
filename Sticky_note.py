from tkinter import *
import tkinter as tk
from tkinter import ttk

# the main function from where the sticky_notes are made
def sticky():
    # function to return the color of the note selected by the user
    def note(event):
        return note_color.get()

    # function to return the color of the text selected by the user
    def text(event):
        return text_color.get()

    # function to return the size of the font selected by the user
    def size(event):
        return font_size.get()

    #function to return the style of the text selected by the user
    def style(event):
        return text_style.get()

    # function to display the main sticky notes
    def sticky_notes():
        root = Tk()
        root.title('Sticky Notes')
        root.geometry('300x300')
        root.configure(bg='black')
        text1 = Text(root,font=(style('<<ComboboxSelected>>'),int(size('<<ComboboxSelected>>'))), fg=text('<<ComboboxSelected>>'),
                      bg=note('<<ComboboxSelected>>'),cursor='pirate')
        text1.pack(expand=True,padx=12,pady=10)

        root.attributes('-topmost',True) #This helps to keep the window always at the top

        root.attributes('-toolwindow',True) #This disables the minimize/maximize button
        root.mainloop()

    # our opening window
    master= Tk()
    master.title('Sticky Notes')
    master.configure(bg='black')
    master.geometry('850x150')

    ttk.Label(master,text='Select the size of your text',foreground='red',background='black',font=('Comic Sans MS',12,'bold')).grid(row=0,column=8)
    ttk.Label(master, text='Select the colour of your note', foreground='red',background='black',font=('Comic Sans MS',12,'bold')).grid(row=0,column=0)
    ttk.Label(master, text='Select the colour of your text', foreground='yellow',background='black',font=('Comic Sans MS',12,'bold')).grid(row=4,column=8)
    ttk.Label(master,text='Select the style of your text',foreground='yellow',background='black',font=('Comic Sans MS',12,'bold')).grid(row=4,column=0)

    # creating a combobox where the user only gets the select from the choices available
    n= tk.StringVar()
    note_color= ttk.Combobox(master,width=24,textvariable=n)

    t= tk.StringVar()
    text_color= ttk.Combobox(master,width=24,textvariable=t)

    s= tk.StringVar()
    font_size= ttk.Combobox(master,width=24,textvariable=s)

    st= tk.StringVar()
    text_style= ttk.Combobox(master,width=24,textvariable=st)

    # assinging the options for the two comboboxes
    text_color['values']=('red','green','yellow','white',
                          'black','orange','pink','blue')

    note_color['values']=('red','green','yellow','white',
                          'black','orange','pink','blue')

    font_size['values']=('1','2','3','4','5','6','7','8','9','10','11','12','13',
                          '14','15','16','17','18','19','20','21','22','23','24','25')



    text_style['values']=('Albertus Extra Bold','Albertus Medium','Antique Olive','Arial','Arial Black','Arial MT','Arial Narrow',
                        'Bazooka','Book Antiqua','Bookman Old Style','Boulder',
                        'Calisto MT','Calligrapher','Century Gothic','Century Schoolbook','Cezanne','CG Omega','CG Times','Charlesworth','Chaucer',
                        'Clarendon Condensed','Comic Sans MS','Copperplate Gothic Bold','Copperplate Gothic Light','Cornerstone','Coronet','Courier','Courier New','Cuckoo',
                        'Dauphin','Denmark','Fransiscan','Garamond','Geneva','Haettenschweiler','Heather','Helvetica','Herald','Impact','Jester','Letter Gothic',
                        'Lithograph','Lithograph Light','Long Island','Lucida Console','Lucida Handwriting','Lucida Sans','Lucida Sans Unicode','Marigold',
                        'Market','Matisse ITC','MS LineDraw','News GothicMT','OCR A Extended','Old Century','Pegasus','Pickwick','Poster','Pythagoras',
                        'Sceptre','Sherwood','Signboard','Socket','Steamer','Storybook','Subway''Tahoma','Technical','Teletype','Tempus Sans ITC','Times',
                        'Times New Roman','Times New Roman PS','Trebuchet MS','Tristan','Tubular','Unicorn','Univers','Univers Condensed','Vagabond','Verdana',
                        'Westminster' )
    font_size.grid(row=0,column=10)
    note_color.grid(row=0,column=1)
    text_color.grid(row=4,column=10)
    text_style.grid(row=4,column=1)
    #binding the action of the mouse with our function to return the selected text
    note_color.current()
    note_color.bind('<<ComboboxSelected>>',note)

    text_color.current()
    text_color.bind('<<ComboboxSelected>>',text)

    font_size.current()
    font_size.bind('<<ComboboxSelected>>',size)

    text_style.current()
    text_style.bind('<<ComboboxSelected>>',style)

    Button(master,text='Quit',command=master.quit).grid(row=7,column=10,sticky=W,pady=4)
    Button(master,text='Show Notes',command= sticky_notes).grid(row=7,column=1,sticky=W,pady=4)
    master.mainloop()

def main_page():
    new= Tk()
    new.title('Rohit Hub')
    new.configure(bg='black')
    labelframe=LabelFrame(new,text='Sticky Notes',
                          highlightthickness=5,highlightbackground='yellow')
    labelframe.grid(padx=120,sticky=N,pady=100)
    Button(labelframe,text='STICKY NOTES',command=sticky,
           font=('Times New Roman',20,'bold','italic'),fg='red',bg='black',relief=RAISED).grid(padx=120,sticky=N,pady=100)

    new.mainloop()

main_page()
