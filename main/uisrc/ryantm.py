#python3

import wx
import os
import subprocess
try:
    import wx.lib.platebtn as platebtn
except ImportError:
    import platebtn

#-----file selection filters-----
wildcard = "Python Test (test*.py)|test*.py|" \
           "Python source (*.py)|*.py|" \
           "All files (*.*)|*.*"

#-----window construction-----
class MainFrame(wx.Frame):
    """This is the main window"""

    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw, size=(1280,720))
#-----panel construction-----
        pnl = wx.Panel(self)

#-----header text-----
        st = wx.StaticText(pnl, label=" Chrono Test Manager", pos=(25,25))
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)


#-----directory construction-----
        dir3 = wx.GenericDirCtrl(pnl, -1, size=(400,400),
                                 style=wx.DIRCTRL_SHOW_FILTERS |
                                       wx.DIRCTRL_3D_INTERNAL |
                                       wx.DIRCTRL_MULTIPLE,
                                 filter="Test Files (test*.py)|test*.py|Python files (*.py)|*.py|All files (*.*)|*.*")

#-----button construction-----
        run_select_Btn = wx.Button(pnl, -1,  "   Run Selected Test Case    ",
            size=(200,75))
        edit_select_Btn = wx.Button(pnl, -1, "    Edit Selected Test Case     ",
            size=(200,75))
        import_case_Btn = wx.Button(pnl, -1, "Import Test Case",
            size=(200,75))
        run_full_Btn = wx.Button(pnl, -1,    "      Run Test Suite (Coming Soon!)       ",
            size=(200,75))

#-----button sizer construction-----
        btnSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer.Add(run_select_Btn)
        btnSizer.Add(edit_select_Btn)
        btnSizer.Add(import_case_Btn)
        btnSizer.Add(run_full_Btn)

#-----button panel sizer construction-----
        bs1V = wx.BoxSizer(wx.VERTICAL)
        bs1V.pos = (0,0)
        bs1V.size = (961, 612)
#-----button events-----
        # Create event handlers for buttons in main window
        self.Bind(wx.EVT_BUTTON, self.OnRunTC, run_select_Btn)
        self.Bind(wx.EVT_BUTTON, self.OnEditTC, edit_select_Btn)
        #self.Bind(wx.EVT_BUTTON, self.OnImportTC, import_case_Btn)
        #self.Bind(wx.EVT_BUTTON, self.OnRunTS, run_full_Btn)

#-----title static text in sizer-----
        bs1V.Add(3, 3)
        bs1V.Add(st, 0, wx.EXPAND)
        bs1V.Add(wx.StaticLine(pnl), 0,
                wx.EXPAND|wx.TOP|wx.BOTTOM, 5)

#-----logging window-----
        logcon = wx.TextCtrl(pnl, wx.ID_ANY, size=(400,400),
                          style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)

#-----flex grid set for two columns-----
        sz = wx.FlexGridSizer(cols=5, hgap=2, vgap=1)

        # put items into the two columns, alternating left and right sides
        sz.AddGrowableCol(0)
        #sz.Add(wx.StaticText(pnl, label=" Current Test Suite:")) # left title
        #sz.Add(wx.StaticText(pnl, label="       Choose an option:"))#Right title
        sz.Add(dir3, 0, wx.EXPAND, 20) # directory left
        sz.Add(btnSizer, 0, wx.EXPAND|wx.ALL, 20) # buttons center
        sz.Add(logcon, 0, wx.EXPAND, 20) #logging console right
        # add the two column flexgridsizer to the main box sizer for the panel
        bs1V.Add(sz, 0, wx.EXPAND|wx.ALL, 10)
        pnl.SetSizer(bs1V) # assign the main box sizer to the panel
        #---------------------------------------------
        # set sizer on the frame itself as well,
        # so if we scale frame all else adjusts
        framesizer = wx.BoxSizer()
        framesizer.Add(pnl, 1, wx.EXPAND)
        self.SetSizer(framesizer)
        self.Fit() # calculate so everything fits
        self.SetMinSize(self.GetSize()) # set min size based on the fit

#-----menu and status bar construction-----
        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("Welcome to Chrono Test Manager, v1.0")

    def makeMenuBar(self):
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        newtcItem = fileMenu.Append(-1, "&New Test Case\tCtrl-N", "Create a new test case")
        # newtsItem = fileMenu.Append(-1, "New &Test Suite\tCtrl-T", "Create a new directory for a test suite")
        fileMenu.AppendSeparator()
        runtcItem = fileMenu.Append(-1, "&Run Test Case\tCtrl-R", "Run a test case on your local machine")
        # opentsItem = fileMenu.Append(-1, "Open Test &Suite\tCtrl-S", "Open an existing directory for a test suite")
        fileMenu.AppendSeparator()
        importtcItem = fileMenu.Append(-1, "&Import Test Case\tCtrl-I", "Import a test case into the active test suite")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        editMenu = wx.Menu()
        edittcItem = editMenu.Append(-1, "&Edit Test Case\tCtrl-E", "Select and edit an existing test case")
        # edittsItem = editMenu.Append(-1, "E&dit Test Suite\tCtrl-D", "Manage a test suite from the directory")
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
        self.Bind(wx.EVT_MENU, self.OnRunTC, runtcItem)
        #self.Bind(wx.EVT_MENU, self.OnOpenTS, opentsItem)
        #self.Bind(wx.EVT_MENU, self.OnImportTC, importtcItem)

        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        self.Close(True)


    def OnHello(self, event):
        wx.MessageBox("Hello again from CTM!")


    def OnAbout(self, event):
        wx.MessageBox("Chrono Test Manager is a software testing application\ndeveloped as a project by Ryan Miller, CTFL.",
                      "About Chrono Test Manager",
                      wx.OK|wx.ICON_INFORMATION)

    def OnRunTC(self, event):
        """Open a test case to run"""
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE |
                  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST|
                  wx.FD_PREVIEW
            )
        if dlg.ShowModal() == wx.ID_OK:
            global paths
            paths = dlg.GetPaths()
            subprocess.Popen(['C:\\Users\\Chrono\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe', paths])

    def OnEditTC(self, event):
        """Open a test case to edit"""
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE |
                  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST|
                  wx.FD_PREVIEW
            )
        if dlg.ShowModal() == wx.ID_OK:
            global paths
            paths = dlg.GetPaths()


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MainFrame(None, title='Chrono Test Manager, v.1.0')
    frm.Show()
    app.MainLoop()
