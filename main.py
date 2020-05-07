from HiCityData import Parser, Reader
from HiCityLocal import ArgsAnalyze, LoggerConfig, Extend, require_log, GUI


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


if __name__ == '__main__':
    args = init()
    if args.db is None:
        read_db("city.db")
    else:
        read_db(args.db)
    Extend.save_args_file_to_db(args, GUI.progressbar, GUI.printer, GUI.sql)
    Extend.export_excel(args, GUI.city_map)
    Extend.with_console(args, GUI.city_map)
    GUI.tk_root.mainloop()
