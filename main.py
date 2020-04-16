from HiCityData import MetaPrinter, Progressbar, SQL, Reader, Writer, Parser


if __name__ == '__main__':
    class PlainPrinter(MetaPrinter):
        def write(self, *args):
            for i in args:
                print(i)


    printer = PlainPrinter()
    bar = Progressbar(printer)
    sql = SQL("city.db")
    reader = Reader(bar)
    lines = reader.read_from_file("citycode.txt")
    parser = Parser(bar)
    city_map = parser.parse(lines)
    writer = Writer(bar, printer)
    writer.save_file_to_db(city_map, sql)
    city_map = parser.parse(reader.read_from_db(sql))
    print(city_map)
