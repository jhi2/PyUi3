"""
WinUI3 with Python!
"""
version = "2.0.0"
description = "WinUI3 with Python!"
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
import subprocess
import tkinter
from tkinter import ttk
class Application(XamlApplication):
    def __init__(self,**kwrgs):
        loader = tkinter.Tk()
        loader.attributes("-topmost",True)
        loader.attributes("-toolwindow",True)
        ad = tkinter.Label(loader,text="Powerd by PyUi3",font=("Segoe UI",10))
        ad.pack()
        bar = ttk.Progressbar(loader,orient="horizontal",mode="indeterminate")
        bar.pack()
        bar.start()
        subprocess.Popen("TIMEOUT /T 5 /NOBREAK")
        bar.stop()
        loader.destroy()
        super().__init__(**kwrgs)

