from tkinter import *
from tkinter import ttk
from GUItestdata import *


def placeholder():  # used in initMenu
    return None


def init_menu(root):
    # Sets the menu attribute of root, a Tk object, to menu
    menu = Menu(root)
    root.config(menu=menu)

    # Adds a 'file' cascade to menu
    filesection = Menu(menu)
    menu.add_cascade(label='File', menu=filesection)
    filesection.add_command(label='Open', command=placeholder())
    filesection.add_separator()
    filesection.add_command(label='Exit', command=root.quit)
    filesection.add_separator()

    # Adds a 'help' cascade to menu
    helpsection = Menu(menu)
    menu.add_cascade(label='Help', menu=helpsection)
    helpsection.add_command(label="About", command=placeholder())


def init_root(root, rootw, rooth, roottitle):
    # Specifies the name and dimensions for the root object
    root.title(roottitle)
    rootdim = str(rootw) + 'x' + str(rooth)
    root.geometry(rootdim)

    # specifies for row 0 height to have a weight of 1 in the root grid, even after resizing the root window.
    root.rowconfigure(0, weight=1)
    # specifies for col 1 width to take up all the (remaining) space in the root grid (because col 0 takes up space too)
    # , even after resizing the root window.
    root.columnconfigure(1, weight=1)


def init_entry(entryframe):

    entryscrollbar = Scrollbar(entryframe, orient=VERTICAL)
    entrylist = Listbox(entryframe, yscrollcommand=entryscrollbar.set, selectmode=BROWSE)
    entryscrollbar.config(command=entrylist.yview)

    entryscrollbar.pack(side=RIGHT, fill=Y)
    entrylist.pack(side=LEFT, fill=BOTH, expand=1)


def init_entryframe(root):
    entryframe = LabelFrame(root, text='Files')

    # entryframe, being in cell (0,1) of the root's grid, expands to fill the remaining space in the root window because
    # cell (0,1) was specified to do so using rowconfigure() and columnconfigure() in init_root() function.
    # The sticky parameter below tells the entryframe widget to fill the size of its cell (0,1).
    entryframe.grid(row=0, column=1, padx=5, pady=5, sticky=E+W+N+S)

    init_entry(entryframe)



def init_sideframe(root,rootw,rooth, sidewidth):

    # Creates a frame sideframe that fills up the height of the 0,0 cell of the root grid. It also
    sideframe = Frame(root)   # , width=sideframew, height=sideframeh)
    # Places sideframe in cell (0,0) of the root grid
    sideframe.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5)
    # Specifies that sideframe's 2x1 must fully fill cell (0,0) of root's grid.
    sideframe.rowconfigure(0, weight=1)
    sideframe.rowconfigure(1, weight=1)
    sideframe.columnconfigure(0, weight=1)

    # Height of sideframe used to divide sideframe into 2 even sections for filterframe and sortframe
    sideframeheight = sideframe.winfo_height()

    # Creating sortframe within sideframe
    sortframe = LabelFrame(sideframe, text='Sort by Tag Category', width=sidewidth, height=sideframeheight / 2)
    sortframe.grid(row=0, column=0, sticky=W+E+N+S)

    # Creating filtframe within sideframe
    filtframe = LabelFrame(sideframe, text='Filter by Tag Value', width=sidewidth, height=sideframeheight/2)
    filtframe.grid(row=1,column=0, sticky=W+E+N+S)
    filtframe.columnconfigure(0, weight=1)
    # Adding a 'format filter' button
    formatfilt = Button(filtframe, text='Add/Format Filters')
    formatfilt.grid(row=0, column=0, padx=2, pady=1)
    # Adding a Frame that conatins a search bar and label
    searchframe = Frame(filtframe)
    searchframe.grid(row=1,column=0, sticky=N+S+E+W)
    searchlabel = Label(searchframe, text='Search:')
    searchbar = ttk.Combobox(searchframe, values=filtvals)
    searchlabel.pack(side=LEFT, fill=Y, padx=2, pady=5)
    searchbar.pack(side=RIGHT, fill=Y, expand=1, padx=2, pady=5)
    # def init_actfiltview():
    # Adding a Frame actfiltview that contains the widgets of the active filter viewer
    actfiltview = Frame(filtframe)
    actfiltview.grid(row=3, column=0, sticky=N+S+E+W)

    filtscrollbar = Scrollbar(actfiltview, orient=VERTICAL)
    filtlist = Listbox(actfiltview, yscrollcommand=filtscrollbar.set, selectmode=BROWSE)
    filtscrollbar.config(command=filtlist.yview)

    filtscrollbar.pack(side=RIGHT, fill=Y)
    filtlist.pack(side=LEFT, fill=BOTH, expand=1)

    for val in filtvals:
        filtlist.insert(END, val)

    # Next steps
    # - keyboard/dragging shortcuts to rearrange items in the filtlist Listbox
    # - redoing everything in a paned window
    # - adding autodetect functionality to search combobox
    # - making all the buttons functional and stuff








    # To make a column or row stretchable, use this option and supply a value that gives the relative weight of this
    # column or row when distributing the extra space.For example, if a widget w contains a grid layout, these lines will
    # distribute three-fourths of the extra space to the first column and one-fourth to the second column:
    #     w.columnconfigure(0, weight=3)
    #     w.columnconfigure(1, weight=1)
    # If this option is not used, the column or row will not stretch.


    # filterframe = LabelFrame(sideframe, text='Filter by Tag Values', width=200, height=10)
    # sortframe = LabelFrame(sideframe, text='Sort by Tag Categories', width=200, height=10)
    # filterframe.grid(row=0, column=0, sticky=E+W+N+S)
    # sortframe.grid(row=1, column=0, sticky=E+W+N+S)
    # sortframe.rowconfigure(0, weight=1)
    # filterframe.rowconfigure(1, weight=1)


class Window:

    def __init__(self):

        # EDIT WINDOW SIZE & NAME HERE:
        # initializes root window dimensions & title
        rootw = 960
        rooth = 540
        roottitle = 'CreativePDB'
        sidew = 200

        # Tk object is created
        root = Tk()

        # Initialize other parts of window
        init_root(root, rootw, rooth, roottitle)
        init_menu(root)
        init_entryframe(root)
        init_sideframe(root, rootw, rooth, sidew)

        # init_entries() is called within init_entryframe


        root.mainloop()





Window()







# #Creating a dropdown menu
# tkvar = StringVar(root) # the list of options
# filepath='C:\\Users\\Shahaan\\Documents\\DeltahacksPR\\jsonfiletemplate.json'
# #Actually, I want to get the full list of tag objects here (below)
# choices = getTagsfromJSON(filepath)
# choices['none']=['']
# #choices = {"Category1", "Category2"}
# tkvar.set('') #set default option for dropdown
# popupMenu = OptionMenu(mainframe,tkvar,*choices)
# Label(mainframe,text='Choose a Tag Category').grid(row=1,column=1)
# popupMenu.grid(row=2,column=1)
# def change_dropdown(*args):
#     print(tkvar.get())
# tkvar.trace('w',change_dropdown)
# root.mainloop()




# #Other stuff?
# label_1 = Label(root, text='Name')
# label_2 = Label(root, text='Password')
#
# label_1.grid(row=0,sticky=E)
# label_2.grid(row=1,sticky=E)
#
# entry_1 = Entry(root)
# entry_2 = Entry(root)
#
# c = Checkbutton(root,text='something')
# c.grid(columnspan=2)
#
# entry_1.grid(row=0,column=1)
# entry_2.grid(row=1,column=1)



# topFrame = Frame(root)
# topFrame.pack() #Anything to be displayed must be .packed
# bottomFrame = Frame(root, bg='red')
# bottomFrame.pack(side=BOTTOM)
#
# button1 = Button(topFrame, text='Button 1', fg='red')
# button2 = Button(topFrame, text='Button 2', fg='blue')
# button3 = Button(topFrame, text='Button 3', fg='green')
# button4 = Button(bottomFrame, text='Button 4', fg='purple')
# button5 = Button(bottomFrame, text='Button 5', fg='orange')
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=LEFT)
# button5.pack(side=LEFT)

#display on the screen