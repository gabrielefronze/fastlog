from colored import colors, style, fore
from enum import Enum

SILENT = 0
ERROR = 1
WARNING = 2
INFO = 3
DEBUG = 4
UI = -1

class fastlog_style:
    def __init__(self, fg, style = None, bg = None):
        self.bg = bg
        self.fg = fg
        self.style = style
        self.style_str = None

    def get_style(self):
        if not self.style_str:
            self.style_str = ''
            if self.fg:
                self.style_str += self.fg
            if self.style:
                self.style_str += self.style
            if self.bg:
                self.style_str += self.bg

        return self.style_str

    def styleprint(self, *args, **kwargs):
        print(self.get_style() + " ".join(map(str,args)) + style.RESET, **kwargs)

fastlog_styles = {  
                    UI : fastlog_style(fore.MAGENTA),
                    SILENT : fastlog_style(fore.BLACK), 
                    ERROR : fastlog_style(fore.RED, style.BOLD), 
                    WARNING : fastlog_style(fore.ORANGE_1),
                    INFO : fastlog_style(fore.CYAN), 
                    DEBUG : fastlog_style(fore.BLACK)
                }

logLevel = DEBUG
def set_log_level(ll):
    if ll > UI: # UI should always be visible
        global logLevel
        logLevel = ll

def fastlog(level, *args, **kwargs):
    global logLevel
    if level <= logLevel:
        fastlog_styles[level].styleprint(*args, **kwargs)
