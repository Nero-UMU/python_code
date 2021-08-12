def print_info(info):
    employee_id = int(input('请输入要查询的元的ID号：'))
    employee_info = info[employee_id]
    employee_list = employee_info.split(',')
    print('ID：{}，姓名：{}，电话号码：{}，城市：{}'.format(employee_id, employee_list[0], employee_list[1], employee_list[2]))


def main():
    employee_information = {1: '张晓,13800000000,武汉', 2: '李明,18500000000,北京', 3: '李浩,13912341234,九江',
                            4: '王华,15890281734,上海'}
    print_info(employee_information)


if __name__ == '__main__':
    main()
