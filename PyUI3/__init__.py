"""
WinUI3 with Python!
"""
__version__ = "4.0.0"
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
class ApplicationWindow(self):
    def __init__(self):
        global win
        class app(XamlApplication):
            def OnLaunched(self):
                win = Window()

