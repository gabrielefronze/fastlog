from colored import colors, style, fore
from enum import Enum

SILENT = 0
ERROR = 1
INFO = 2
DEBUG = 3

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

fastlog_styles = { SILENT : fastlog_style(fore.BLACK), ERROR : fastlog_style(fore.RED, style.BOLD), INFO : fastlog_style(fore.CYAN), DEBUG : fastlog_style(fore.BLACK)}

logLevel = DEBUG
def set_log_level(ll):
    global logLevel
    logLevel = ll

def fastlog(level, *args, **kwargs):
    global logLevel
    if level <= logLevel:
        fastlog_styles[level].styleprint(*args, **kwargs)
