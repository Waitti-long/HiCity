# Hicity

## 包结构

* HicityData 数据处理包
* HicityLocal 客户端
* HicityServer 服务端
* HicityTest 测试包

## 快速开始

### 使用main.py开启客户端

```sh
python main.py
可选参数：
--excel 生成excel文件
--db db_name 选择一个sqlite db文件作为数据源
--file file 选择一个文件读入数据库
--log_format format 设置日志格式
--log_level level 设置日志等级
--console 开启GUI的同时打开客户端
```

### 使用server-debug.py开启服务端

```shell script
python server-debug.py
```

## 使用server-production.py开启服务端

```shell script
python server-production.py
```

### 服务端每日数据更新

设置每日运行everydata.py

## HicyData

### 实体类entity

```python
from HicityData import entity
# 城市
entity.City
# 天气预报
entity.Forecast
```

### 数据库类SQL

```python
from HicityData import SQL
# 初始化
db_name = "city.db"
sql = SQL(db_name)
# 连接数据库（初始化时自动调用）
sql.connect(db_name)
# 获取session
sql.session()
```

### 抽象类MetaPrinter

```python
from HicityData import MetaPrinter
# 重写MetaPrinter的方法
# 此例程为向console输出
class Printer(MetaPrinter):
    def write(self, *args):
        for i in args:
            print(i)
        
# 必要时可重写clear（清空流）或flush（更新流）方法
```

### 进度条ProcessBar

```python
from HicityData import Progressbar
# Processbar 需要一个Printer作为输出对象，这里直接使用上面写好的Printer
printer = Printer()
bar = Progressbar(printer)
```

### 数据处理类Reader,Parser,Writer

```python
from HicityData import Reader,Writer,Parser
# 这三个类需要Processbar,另外Writer还需要一个Pinter作为错误数据的输出
printer = Printer()
bar = Progressbar(printer)
reader = Reader(bar)
parser = Parser(bar)
writer = Parser(bar, printer)
sql = SQL("city.db")

lines = reader.read_from_file("citycode.txt")
# lines = reader.read_from_db("city.db")
city_map = parser.parse(lines)
writer.save_file_to_db(city_map, sql)
```

### 天气预报ForeCast

```python
from HicityData import ForeCast
# 城市代码
code = "101010100"
# 获取正规化天气预报
forecast = ForeCast.get_forecast(code)
# 获取json格式天气预报
forecast = ForeCast.get_forecast_json(code)
```

