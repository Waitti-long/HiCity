import unittest

from HiCityData import *
from HiCityLocal import *
from HiCityServer import *


class Printer(MetaPrinter):
    def write(self, *args):
        for i in args:
            print(i)


class DataCase(unittest.TestCase):
    def test_printer(self):
        printer = Printer()
        bar = Progressbar(printer)
        parser = Parser(bar)
        reader = Reader(bar)
        writer = Writer(bar, printer)
        sql = SQL("city.db")

        print(parser.parse(reader.read_from_db(sql)))
        writer.save_file_to_db(parser.parse(reader.read_from_file("citycode.txt")), sql)
        self.assertNotEqual(parser.parse(reader.read_from_file("citycode.txt")),
                            parser.parse(reader.read_from_db(sql)))


def init():
    args = ArgsAnalyze.get_args()
    LoggerConfig.config(args)
    return args


@require_log("read from db")
def read_db(db_name):
    @require_log("gui init")
    def gui_init():
        GUI.init(db_name)

    gui_init()

    @require_log("read data")
    def read_data():
        reader = Reader(GUI.progressbar)
        parser = Parser(GUI.progressbar)
        lines = reader.read_from_db(GUI.sql)

        @require_log("parser data")
        def parse_data():
            GUI.city_map = parser.parse(lines)

        parse_data()

    read_data()


class LocalCase(unittest.TestCase):
    def test(self):
        try:
            args = init()
            if args.db is None:
                read_db("city.db")
            else:
                read_db(args.db)
            Extend.save_args_file_to_db(args, GUI.progressbar, GUI.printer, GUI.sql)
            Extend.export_excel(args, GUI.city_map)
            self.assertTrue(True)
        except Exception as e:
            self.assertTrue(False)
            print(e)


class ServerCase(unittest.TestCase):
    def test(self):
        sql = SQL("city.db")
        ForeCastCache.read(sql)
        # app.run(port=8080)


if __name__ == '__main__':
    unittest.main()
