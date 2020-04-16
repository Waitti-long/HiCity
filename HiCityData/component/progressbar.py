class Progressbar:
    """
    简易进度条
    @param printer 实现meta-printer中的接口
    """

    def __init__(self, printer, window):
        self.max_value = 0
        self.__now = 0
        self.__last = 0.0
        self.printer = printer
        self.window = window

    def start(self):
        self.__now = 0
        self.__last = 0
        self.printer.clear()

    def update(self, value):
        self.__now = value
        this = self.__now / self.max_value
        if self.max_value != 0 and ((this - self.__last > 0.1) or self.__now == self.max_value - 1):
            self.printer.write("{:.1f}% ({} of {})".format(this * 100, self.__now, self.max_value))
            self.__last = this
            self.window.update()

    def end(self):
        self.printer.clear()
        self.window.update()

    def set_target(self, value):
        self.max_value = value
