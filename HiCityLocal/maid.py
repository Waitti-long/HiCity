import logging
import argparse
import xlsxwriter
from HiCityData import Reader, Parser, Writer

log_levels = {"DEBUG": logging.DEBUG, "INFO": logging.INFO, "WARN": logging.WARN, "ERROR": logging.ERROR,
              "CRITICAL": logging.CRITICAL}


class ArgsAnalyze:
    """
    对传入参数进行分析，并保存参数解析值
    """

    def __init__(self):
        self.args = self.get_args()

    @staticmethod
    def get_args():
        """
        获取程序参数
        @return 参数 调用格式：args.file
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--excel", help="dump to an excel", action="store_true")
        parser.add_argument("--db", help="specify a db")
        parser.add_argument("--file", help="specify a file, it will be read to db")
        parser.add_argument("--log_format", help="change the log format")
        parser.add_argument("--log_level", help="change the log level", choices=log_levels.keys())
        parser.add_argument("--log_file", help="change the log file")
        args_ = parser.parse_args()
        return args_


class LoggerConfig:
    """
    根据参数配置日志
    """

    @staticmethod
    def config(args):
        """
        配置日志管理器
        @return logger
        """
        logging.basicConfig(
            level=logging.INFO if args.log_level is None else log_levels[args.log_level],
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s" if args.log_format is None else args.log_format,
            filename="city.log" if args.log_file is None else args.log_file,
            filemode="a"
        )


class Extend:
    """
    扩展功能
    """

    @staticmethod
    def save_args_file_to_db(args, progressbar, logger, sql):
        if args.file is not None:
            writer = Writer(progressbar, logger)
            parser = Parser(progressbar)
            reader = Reader(progressbar)
            writer.save_file_to_db(parser.parse(reader.read_from_file(args.file)), sql)

    @staticmethod
    def export_excel(args, city_map):
        if args.excel:
            workbook = xlsxwriter.Workbook("city.xlsx")
            worksheet = workbook.add_worksheet()
            city_list = []
            code_list = []
            for city in city_map:
                for code in city_map[city]:
                    city_list.append(city)
                    code_list.append(code)
            worksheet.write_column(0, 0, city_list)
            worksheet.write_column(0, 1, code_list)
            workbook.close()


def require_log(action):
    """
    自动打日志
    @param action: 行为，即当前在做什么
    """
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            logger = logging.getLogger()
            logger.info(action + " start")
            res = func(*args, **kwargs)
            logger.info(action + " end")
            return res

        return inner_wrapper

    return wrapper
