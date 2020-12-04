import xlrd
from xlutils.copy import copy
import json
from config import case_path, test_result_excel
from lib.log_lib import LogLib


class ExcelLib:
    work_book = None
    test_result_excel = test_result_excel

    def __init__(self, sheet_idx=0, case_path=case_path):
        case_path = case_path
        if not self.work_book:
            try:
                # 读：
                work_book = xlrd.open_workbook(case_path)
                self.sheet_data = work_book.sheet_by_index(sheet_idx)
                # 写： formatting_info=True 只支持xls格式的Excel文件（注意：读的Excel文件必须为新建的xls文件，xlsx文件改后缀名为xls同样会报错）
                work_book = xlrd.open_workbook(case_path, formatting_info=True)
                self.write_work_book = copy(work_book)
            except FileNotFoundError:
                LogLib().write_to_log_error('excel文件路径错误')

    # 获取sheet表行数
    def get_case_count(self):
        return self.sheet_data.nrows

    # 获取单元格数据
    def get_cell_value(self, row, col):
        return self.sheet_data.cell_value(row, col)

    # 获取一般入参或出参数据
    def get_param(self, row, col):
        return self.get_cell_value(row, col)

    # 获取预期retcode
    def get_retcode(self, row, col):
        return int(self.get_cell_value(row, col))

    # excel读取的数据为string类型，封装一个json格式的string转字典的方法
    def str_to_dict(self, str_data):
        return_dict = None
        if str_data:
            return_dict = json.loads(str_data)
        return return_dict

    def get_api_msg_list(self, api_row):
        path_col = 2
        method_col = 3
        headers_col = 4
        api_msg_list = list()

        path = self.sheet_data.cell_value(api_row, path_col)
        method = self.sheet_data.cell_value(api_row, method_col)
        headers = self.str_to_dict(self.sheet_data.cell_value(api_row, headers_col))

        api_msg_list.append(path)
        api_msg_list.append(method)
        api_msg_list.append(headers)
        return api_msg_list

    # 某个单元格内写入数据
    def write_cell_value(self, row, col, value, sheet_idx):
        write_sheet = self.write_work_book.get_sheet(sheet_idx)
        write_sheet.write(row, col, value)
        self.write_work_book.save(self.test_result_excel)


if __name__ == '__main__':
    print(ExcelLib(1).get_case_count())
    print(ExcelLib(1).get_cell_value(3, 7))
    print(ExcelLib(1).get_param(3, 7))
    print(ExcelLib(1).get_retcode(3, 8))
    ExcelLib(1).write_cell_value(3, 3, '------------', 1)
    print(ExcelLib().get_api_msg_list(1))
