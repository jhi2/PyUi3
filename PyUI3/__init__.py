"""
WinUI3 with Python!
"""
__version__ = "4.0.4"
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
class ApplicationWindow():
    def __init__(self):
        self.roster = []
        class app(XamlApplication):
            def __init__(self):
                super().__init__(appargs)
            def OnLaunched(self):
                self.win = Window(winargs)
        self.application = app()
    def add(self, item):
        self.roster.append(item)
    def run(self):
        self.application.Start()
        for item in self.roster:
            self.win.content = item
        self.win.Activate()

