class MetaPrinter:
    """
    输出流的抽象类
    """

    def write(self, *args):
        """
        向输出流中写入数据
        """
        pass

    def clear(self):
        """
        清空输出流
        """
        pass
