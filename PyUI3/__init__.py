"""
WinUI3 with Python!
"""

__version__ = "5.3.0"

import pythoncom
from win32more.Microsoft.UI.Xaml.Controls import (
    AnimatedIcon, AutoSuggestBox, BreadcrumbBar, Button, CalendarDatePicker,
    CalendarView, CheckBox, ColorPicker, ComboBox, CommandBar, CommandBarFlyout,
    ContentDialog, DatePicker, DropDownButton, Expander, FlipView, Flyout,
    GridView, HyperlinkButton, Image, InfoBar, ListView, MapControl,
    MediaPlayerElement, MenuBar, MenuFlyout, NavigationView, NumberBox,
    ParallaxView, PasswordBox, PersonPicture, PipsPager, ProgressBar,
    ProgressRing, RadioButton, RatingControl, RichEditBox, RichTextBlock,
    ScrollViewer, SemanticZoom, Slider, SplitButton, SplitView, SwipeControl,
    TabView, TeachingTip, TextBlock, TextBox, TimePicker, ToggleSwitch,
    ToggleSplitButton, ToolTip, TreeView, TwoPaneView,
)

from win32more.Microsoft.UI.Xaml import Window
from win32more.xaml import XamlApplication
from win32more.Microsoft.UI.Xaml.Media import MicaBackdrop

class App(XamlApplication):
    def __init__(self):
        pythoncom.CoInitialize()
        super().__init__()
        self.win = None

    def OnLaunched(self, args):
        self.win = Window()

class ApplicationWindow:
    def __init__(self):
        self.roster = []
        self.app = App()
        self.win = self.app.win

    def add(self, item):
        self.roster.append(item)

    def run(self):
        for item in self.roster:
            self.win.Content = item
        XamlApplication.Start(self.app)
        self.win.Activate()

    def set_title(self, title):
        self.win.Title = str(title)

    def set_mica(self, mode):
        if mode:
            self.win.SystemBackdrop = MicaBackdrop()
        else:
            self.win.SystemBackdrop = None
