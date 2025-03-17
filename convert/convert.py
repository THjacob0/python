import argparse
import csv
import json
import os

def CSVconvertJSON(infile, outfile):
    """将 CSV 转换为 JSON"""
    try:
        with open(infile, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)  # 读取CSV文件，以字典格式读取，一行一个字典，列名为key
            data = list(reader)  # 转换为列表格式

        # 将数据转为 JSON 字符串，并确保中文不被转义
        json_data = json.dumps(data, indent=4, ensure_ascii=False)

        with open(outfile, mode='w', encoding='utf-8') as f:
            f.write(json_data)  # 将 JSON 字符串写入文件

        print(f"CSV 转换为 JSON 成功：{outfile}")

    except FileNotFoundError:
        print(f"错误：CSV 文件 '{infile}' 不存在！")
    except Exception as e:
        print(f"CSV 转 JSON 失败：{e}")

def JSONconvertCSV(infile, outfile):
    """将 JSON 转换为 CSV"""
    try:
        with open(infile, mode='r', encoding='utf-8') as f:
            data = json.load(f)  # 读取json文件

        if not data:
            raise ValueError("JSON 文件为空或格式错误")

        keys = data[0].keys()  # 获取 CSV 表头是json对象的键

        with open(outfile, mode='w', encoding='utf-8', newline='') as f:
            # 使EXCEL正确识别UTF-8 编码
            f.write('\ufeff')
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()  # 写入表头
            writer.writerows(data)  # 写入数据

        print(f"JSON 转换为 CSV 成功：{outfile}")

    except FileNotFoundError:
        print(f"错误：JSON 文件 '{infile}' 不存在！")
    except json.JSONDecodeError:
        print(f"错误：'{infile}' 不是有效的 JSON 格式！")
    except Exception as e:
        print(f"JSON 转 CSV 失败：{e}")

def main():
    parser = argparse.ArgumentParser()  # 创建命令行参数解析器
    parser.add_argument("mode", choices=["csvtojson", "jsontocsv"])
    parser.add_argument("input_file", help="输入文件路径")
    parser.add_argument("output_file", help="输出文件路径")

    args = parser.parse_args()

    if not os.path.exists(args.input_file):  # 检查输入文件是否存在
        print(f"错误：输入文件 '{args.input_file}' 不存在！")
        return

    if args.mode == "csvtojson":
        CSVconvertJSON(args.input_file, args.output_file)
    elif args.mode == "jsontocsv":
        JSONconvertCSV(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
