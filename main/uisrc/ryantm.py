#python3

import wx

class MainFrame(wx.Frame):
    """
    A Frame that says Chrono Test Manager
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MainFrame, self).__init__(*args, **kw, size=(1280,720))

        # create a panel in the frame
        #pnl = wx.Panel(self)

        # and put some text with a larger bold font on it
        #st = wx.StaticText(pnl, label="Chrono Test Manager!", pos=(25,25))
        #font = st.GetFont()
        #font.PointSize += 10
        #font = font.Bold()
        #st.SetFont(font)
#------------------------------------------------------------------
# Ed added this code - sits directly on top of the Static Text "Chrono Test Manager!"
# not what we want but got some visual results going

        #txt3 = wx.StaticText(self, -1, "wx.DIRCTRL_SHOW_FILTERS\nwx.DIRCTRL_3D_INTERNAL\nwx.DIRCTRL_MULTIPLE")
        dir3 = wx.GenericDirCtrl(self, -1, size=(640,640),
                                 style=wx.DIRCTRL_SHOW_FILTERS |
                                       wx.DIRCTRL_3D_INTERNAL |
                                       wx.DIRCTRL_MULTIPLE,
                                 filter="All files (*.*)|*.*|Test Files (test*.py)|test*.py|Python files (*.py)|*.py")
        sz = wx.FlexGridSizer(cols=2, hgap=1, vgap=1)
        sz.Add((35, 35))  # some space above
        sz.Add((35, 35))
        sz.Add((35, 35))

        #sz.Add(st, 0, wx.EXPAND)
        sz.Add(dir3, 0, wx.EXPAND)

        sz.Add((35,35))  # some space below
        self.SetSizer(sz)
        self.SetAutoLayout(True)
#----------------------------------------------------------------------

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to Chrono Test Manager, v1.0")




    def makeMenuBar(self):
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        newtcItem = fileMenu.Append(-1, "&New Test Case\tCtrl-N", "Create a new test case")
        newtsItem = fileMenu.Append(-1, "New &Test Suite\tCtrl-T", "Create a new directory for a test suite")
        fileMenu.AppendSeparator()
        opentcItem = fileMenu.Append(-1, "&Open Test Case\tCtrl-O", "Open a test case on your local machine")
        opentsItem = fileMenu.Append(-1, "Open Test &Suite\tCtrl-S", "Open an existing directory for a test suite")
        fileMenu.AppendSeparator()
        importtcItem = fileMenu.Append(-1, "&Import Test Case\tCtrl-I", "Import a test case into the active test suite")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        editMenu = wx.Menu()
        edittcItem = editMenu.Append(-1, "&Edit Test Case\tCtrl-E", "Select and edit an existing test case")
        edittsItem = editMenu.Append(-1, "E&dit Test Suite\tCtrl-D", "Manage a test suite from the directory")
        prefItem = editMenu.Append(-1, "&Preferences\tCtri-P", "Open options and preferences for CTM")

        viewMenu = wx.Menu()
        statbarItem = viewMenu.Append(-1, "Status Bar", "Toggle the status bar on/off")

        helpMenu = wx.Menu()
        howtoItem = helpMenu.Append(-1, "Using CTM", "A quick guide on how to use Chrono Test Manager")
        linksItem = helpMenu.Append(-1, "Helpful Links", "A list of helpful links for software testers")
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(editMenu, "&Edit")
        menuBar.Append(viewMenu, "&View")
        menuBar.Append(helpMenu, "&Help")


        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        #self.Bind(wx.EVT_MENU, self.OnNewTC, newtcItem)
        #self.Bind(wx.EVT_MENU, self.OnNewTS, newtsItem)
        #self.Bind(wx.EVT_MENU, self.OnOpenTC, opentcItem)
        #self.Bind(wx.EVT_MENU, self.OnOpenTS, opentsItem)
        #self.Bind(wx.EVT_MENU, self.OnImportTC, importtcItem)

        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def createNotebook(self):
        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)
        widgets = Widgets(notebook)

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("Chrono Test Manager is a program developed as a project by Ryan Miller.",
                      "About Chrono Test Manager",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MainFrame(None, title='CTM v1.0')
    frm.Show()
    app.MainLoop()
