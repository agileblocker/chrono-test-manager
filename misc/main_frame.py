import wx
BACKGROUNDCOLOR = (240, 240, 240, 255)

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.createWidgets()
        self.Show()


    def createWidgets(self):
        self.CreateStatusBar()
        self.createMenu()
        self.createNotebook()

    def createMenu(self):
        # create the Menu
        filemenu = wx.Menu()
        editmenu = wx.Menu()
        viewmenu = wx.Menu()
        helpmenu = wx.Menu()

        # add menu items to the menu
        filemenu.Append(wx.ID_NEW, "&New", " Create a new file")
        filemenu.Append(wx.ID_OPEN,"&Open\tCtrl-O", " Open an existing file")
        filemenu.Append(wx.ID_SAVE,"&Save\tCtrl-S", " Save this file")
        filemenu.Append(wx.ID_SAVEAS,"&Save &As", " Save in a new file")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_PRINT,"&Print", " Print this file")
        filemenu.AppendSeparator()
        f_exit = filemenu.Append(wx.ID_EXIT, "E&xit", " Exit the GUI")

        editmenu.Append(wx.ID_CUT, "Cut", " Remove selection")
        editmenu.Append(wx.ID_COPY,"Copy", " Copy selection")
        editmenu.Append(wx.ID_PASTE,"Paste", "Paste selection")
        editmenu.AppendSeparator()
        editmenu.Append(wx.ID_FIND,"&Find", " Search for selection")
        editmenu.Append(wx.ID_SELECTALL, "Select all", " Select all")

        helpmenu.Append(wx.ID_HELP, "&Help", "Help docs")
        h_about = helpmenu.Append(wx.ID_ABOUT, "&About", "wxPython GUI")

        # create the MenuBar
        menuBar = wx.MenuBar()

        # give the menu bar a title
        menuBar.Append(filemenu, "File")
        menuBar.Append(editmenu, "Edit")
        menuBar.Append(viewmenu, "View")
        menuBar.Append(helpmenu, "Help")

        # connect the menuBar to the frame
        self.SetMenuBar(menuBar)

        # bind the menu items to callbacks
        self.Bind(wx.EVT_MENU, self.exitGUI, f_exit)

        # menu callbacks
        def exitGUI(self, event):
            exit()

        def onEx


    def createNotebook(self):
        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)
        widgets = Widgets(notebook)

        notebook.AddPage(widgets, "Widgets")
        notebook.SetBackgroundColour(BACKGROUNDCOLOR)
        # layout
        boxSizer = wx.BoxSizer()
        boxSizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizerAndFit(boxSizer)

class Widgets(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.panel = wx.Panel(self)
        self.createWidgetsFrame()
        self.createManageFilesFrame()
        self.addWidgets()
        self.addFileWidgets()
        self.layoutWidgets()

    # -----------------------------------
    def createWidgetsFrame(self):
        staticBox = wx.StaticBox(self.panel, wx.ID_ANY, "Widget Frame", size=(285, -1))
        self.statBoxSizerV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)

    # -----------------------------------------------
    def createManageFilesFrame(self):
        staticBox = wx.StaticBox(self.panel, -1, "Manage Files", size=(285, -1))
        self.statBoxSizerMgrV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)
    # -----------------------------------------------
    def layoutWidgets(self):
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerV.Add(self.statBoxSizerV, 1, wx.ALL)
        boxSizerV.Add(self.statBoxSizerMgrV, 1, wx.ALL)

        self.panel.SetSizer(boxSizerV)
        boxSizerV.SetSizeHints(self.panel)

    def addWidgets(self):
        self.addCheckBoxes()
        self.addRadioButtons()
        self.addStaticBoxWithLabels()
        self.addTextCtrl()
        self.addButtons()

    def addCheckBoxes(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        cb1 = wx.CheckBox(self.panel, label='Disabled')
        cb1.SetValue(True)
        cb1.Disable()
        boxSizerH.Add(cb1)

        cb2 = wx.CheckBox(self.panel, label="UnChecked")
        boxSizerH.Add(cb2, flag=wx.LEFT, border=10)

        cb3 = wx.CheckBox(self.panel, label='Toggle')
        boxSizerH.Add(cb3, flag=wx.LEFT, border=10)
        cb3.SetValue(True)

        # add this box sizer to the static sizer of the widget frame
        self.statBoxSizerV.Add(boxSizerH, flag=wx.LEFT, border=10)
        self.statBoxSizerV.Add((0, 8)) # add some blank vertical space

    def addRadioButtons(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add((2, 0))
        boxSizerH.Add(wx.RadioButton(self.panel, -1, 'Blue', style=wx.RB_GROUP))
        boxSizerH.Add((33, 0))
        boxSizerH.Add(wx.RadioButton(self.panel, -1, 'Gold'))
        boxSizerH.Add((45, 0))
        boxSizerH.Add(wx.RadioButton(self.panel, -1, 'Red'))
        # add this to the widgets frame
        self.statBoxSizerV.Add(boxSizerH, 0, wx.ALL, 8)


    def addStaticBoxWithLabels(self):

        staticBox = wx.StaticBox(self.panel, -1, "Labels within a Frame")
        staticBoxSizerV = wx.StaticBoxSizer(staticBox, wx.VERTICAL)
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        staticText1 = wx.StaticText(self.panel, -1, "Choose a number:")
        boxSizerH.Add(staticText1, 0, wx.ALL)
        staticText2 = wx.StaticText(self.panel, -1, "Label 2")
        boxSizerV.Add(staticText2, 0, wx.ALL)
        # -----------------------------------------------------------------
        staticBoxSizerV.Add(boxSizerV, 0, wx.ALL)
        boxSizerH.Add(staticBoxSizerV)
        #------------------------------------------------------------------
        boxSizerH.Add(wx.SpinCtrl(self.panel, size=(50, -1), style=wx.BORDER_RAISED))
        # add this local boxSizer to the widget frame
        self.statBoxSizerV.Add(boxSizerH, 1, wx.ALL)

    # ------------------------------------------------------------------
    def addTextCtrl(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add(wx.TextCtrl(self.panel, size=(275, -1), style=wx.TE_MULTILINE))
        self.statBoxSizerV.Add(boxSizerH, 1, wx.ALL)

    # ------------------------------------------------------------------
    def addButtons(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add(wx.Button(self.panel, label='All Time Zones'))
        boxSizerH.Add(wx.Button(self.panel, label='Local Zone'))
        boxSizerH.Add(wx.Button(self.panel, label='New York'))
        self.statBoxSizerV.Add(boxSizerH, 1, wx.ALL)

    # ------------------------------------------------
    def addFileWidgets(self):
        boxSizerH = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH.Add(wx.Button(self.panel, label='Browse to File...'))
        boxSizerH.Add(wx.TextCtrl(self.panel, size=(174, -1), value="Z:\\"))
        boxSizerH1 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizerH1.Add(wx.Button(self.panel, label='Copy File To:    '))
        boxSizerH1.Add(wx.TextCtrl(self.panel, size=(174, -1), value= "Z:\\Backup"))

        # stack these two box sizers vertically
        boxSizerV = wx.BoxSizer(wx.VERTICAL)
        boxSizerV.Add(boxSizerH)
        boxSizerV.Add(boxSizerH1)

        # add them to the manage files frame
        self.statBoxSizerMgrV.Add(boxSizerV, 1, wx.ALL)

# =============================
# Start GUI
# =============================
app = wx.App()
MainFrame(None, title="Python GUI using wxPython", size=(350,450))
app.MainLoop()
# ------------------------------------------------
