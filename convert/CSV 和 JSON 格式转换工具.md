# CSV 和 JSON 格式转换工具

这是一个简单的 Python 文件格式转换工具，支持CSV转JSON和JSON转CSV。

## 功能点

- 从 CSV 转换为 JSON。
- 从 JSON 转换为 CSV。
- 确保 UTF-8 编码，避免中文乱码。
- 支持命令行操作。

## 安装要求

在运行该工具之前，请确保你的系统中已经安装了 Python 运行环境。下载并安装新版本的 Python。

### 必要的 Python 库

该工具使用了以下 Python 标准库：
- `argparse`：处理命令行参数。
- `csv`：处理 CSV 文件的读取和写入。
- `json`：处理 JSON 文件的读取和写入。
- `os`：进行文件路径检查。

这些库为Python默认库。

## 使用方法

### 1. 从 CSV 转换为 JSON

你可以使用以下命令将 CSV 文件转换为 JSON 文件：

```bash
python convert.py csvtojson input.csv output.json 
```

### 2.从 JSON 转换为 CSV

你可以使用以下命令将 CSV 文件转换为 JSON 文件：

```
python convert.py jsontocsv input.csv output.json 
```

