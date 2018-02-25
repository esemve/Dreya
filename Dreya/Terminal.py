class Terminal:

    FONT_RED = '\033[93m'
    FONT_GREEN = '\033[92m'
    FONT_END = '\033[0m'
    FONT_BOLD = '\033[1m'
    FONT_UNDERLINE = '\033[4m'

    @staticmethod
    def info(msg = "", type = "info", exception = ""):
        print(Terminal.FONT_GREEN + "[" + type + "]" + Terminal.FONT_END + " " + msg, exception)

    @staticmethod
    def error(msg = "", type = "error", exception = ""):
        print(Terminal.FONT_GREEN + "[" + type + "]" + Terminal.FONT_END + " " + msg, exception)


