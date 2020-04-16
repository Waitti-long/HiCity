import tkinter as tk
from tkinter.filedialog import askopenfile
import tkinter.messagebox
from HiCityData import Writer, Parser, Reader, Progressbar, MetaPrinter, SQL
from HiCityData import ForeCast
from .tools import CityFinder


def open_file():
    file = askopenfile()
    if file:
        parser = Parser(GUI.progressbar)
        writer = Writer(GUI.progressbar, GUI.printer)
        reader = Reader(GUI.progressbar)
        city_map_temp = parser.parse(reader.read_from_file(file.name))
        writer.save_file_to_db(city_map_temp, GUI.sql)
        GUI.city_map = parser.parse(reader.read_from_db(GUI.sql))


def open_db():
    file = askopenfile()
    if file:
        GUI.sql.connect(file.name)
        parser = Parser(GUI.progressbar)
        reader = Reader(GUI.progressbar)
        GUI.city_map = parser.parse(reader.read_from_db(GUI.sql))


class GUI:
    tk_root = None
    printer = None
    city_finder = None
    progressbar = None
    sql = None
    city_map = None

    @staticmethod
    def init(db_name):
        GUI.tk_root = tk.Tk()
        GUI.tk_root.config(bg="white")
        GUI.tk_root.title("HiCity")

        # button load file or db
        btn_file = tk.Button(GUI.tk_root, text="Load File", bg="white", command=open_file)
        btn_file.grid(row=0, column=0, padx=20, pady=20)
        btn_db = tk.Button(GUI.tk_root, text="Load DB", bg="white", command=open_db)
        btn_db.grid(row=1, column=0, padx=20, pady=20)

        # tip label
        tk.Label(GUI.tk_root, text="City: ", bg="white").grid(row=0, column=1)
        tk.Label(GUI.tk_root, text="CityCode: ", bg="white").grid(row=2, column=1, padx=20, pady=20)

        # show label
        label = tk.Label(GUI.tk_root, bg="white")
        label.grid(row=2, column=2, columnspan=5)

        # input
        input_ = tk.Entry(GUI.tk_root, bg="white")
        input_.grid(row=0, column=2, padx=50, columnspan=5)

        def enter(event):
            code = GUI.city_finder.find_city_code(GUI.city_map, input_.get())
            label.config(text=code)
            if code != "":
                success, forecast = ForeCast.get_forecast(code[0])
                if success:
                    tk.messagebox.askokcancel(title='天气预报', message=forecast)

        input_.bind("<Return>", enter)

        def tab(event):
            res = GUI.city_finder.find_city(GUI.city_map, input_.get())
            if len(res) > 0:
                input_.delete(0, tk.END)
                input_.insert(0, res[0])

        input_.bind("<Tab>", tab)

        # create progress bar
        progress_label = tk.Label(GUI.tk_root, text="", bg="white")
        progress_label.grid(row=2, column=0, pady=20, padx=20)

        class MyPrinter(MetaPrinter):
            def __init__(self, lab):
                self.label = lab

            def write(self, *args):
                for i in args:
                    self.label.config(text=i)

            def clear(self):
                self.label.config(text="")

        progress_label = tk.Label(GUI.tk_root, text="", bg="white")
        progress_label.grid(row=2, column=0, pady=20, padx=20)
        GUI.printer = MyPrinter(progress_label)
        GUI.progressbar = Progressbar(GUI.printer)
        GUI.city_finder = CityFinder()
        GUI.sql = SQL(db_name)
