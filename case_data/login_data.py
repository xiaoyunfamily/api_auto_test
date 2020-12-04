from lib.excel_lib import ExcelLib

login_sheet_idx = 1
handle_excel = ExcelLib(login_sheet_idx)
num = handle_excel.get_case_count()
case_start_row = 2


def get_login_data():
    data_list = list()
    for i in range(case_start_row, num):
        temp_list = list()
        username_col = 6
        password_col = 7
        retcode_col = 8

        username = handle_excel.get_cell_value(i, username_col)
        password = handle_excel.get_cell_value(i, password_col)
        retcode = int(handle_excel.get_cell_value(i, retcode_col))

        temp_list.append(username)
        temp_list.append(password)
        temp_list.append(retcode)

        data_list.append(temp_list)
    return data_list


if __name__ == '__main__':
    print(get_login_data())
