"""
WinUI3 with Python!
"""

__version__ = "5.0.1"
#The never-ending list of imports HAHA
from win32more.Microsoft.UI.Xaml.Controls import (
    AnimatedIcon,
    AutoSuggestBox,
    BreadcrumbBar,
    Button,
    CalendarDatePicker,
    CalendarView,
    CheckBox,
    ColorPicker,
    ComboBox,
    CommandBar,
    CommandBarFlyout,
    ContentDialog,
    DatePicker,
    DropDownButton,
    Expander,
    FlipView,
    Flyout,
    GridView,
    HyperlinkButton,
    Image,
    InfoBar,
    ListView,
    MapControl,
    MediaPlayerElement,
    MenuBar,
    MenuFlyout,
    NavigationView,
    NumberBox,
    ParallaxView,
    PasswordBox,
    PersonPicture,
    PipsPager,
    ProgressBar,
    ProgressRing,
    RadioButton,
    RatingControl,
    RichEditBox,
    RichTextBlock,
    ScrollViewer,
    SemanticZoom,
    Slider,
    SplitButton,
    SplitView,
    SwipeControl,
    TabView,
    TeachingTip,
    TextBlock,
    TextBox,
    TimePicker,
    ToggleSwitch,
    ToggleSplitButton,
    ToolTip,
    TreeView,
    TwoPaneView,
)

from win32more.Microsoft.UI.Xaml import Window
from win32more.xaml import XamlApplication
from win32more.Microsoft.UI.Xaml.Media import MicaBackdrop
#The class for the window
class ApplicationWindow:
    def __init__(self):
        #Initalizes the roster,application,and adds a shortcut to the window
        self.roster = []
        self.app = App()
        self.win = self.app.win

    def add(self, item): #Adds a new item to the window
        self.roster.append(item)

    def run(self): #Starts the application
        self.app.Start()
        for item in self.roster:
            self.win.Content = item
        self.win.Activate()

    def set_title(self, title): #Sets the window title
        self.win.Title = str(title)

    def set_mica(self, mode): #Turns on or off mica on the app
        if mode:
            self.win.SystemBackdrop = MicaBackdrop()
        else:
            self.win.SystemBackdrop = None
#The code for a PyUI3 Binding Application, required by ApplicationWindow
class App(XamlApplication):
    def __init__(self):
        super().__init__()

    def OnLaunched(self, args):
        self.win = Window()


