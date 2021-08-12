def add_address(info):
    while True:
        new_id = int(input('请输入需要添加员工的ID号码：'))
        if is_find(info, new_id):
            print('此工号已经存在！')
        else:
            new_info = input('请输入需要添加员工的各项信息（姓名，电话，城市）：')
            info[new_id] = new_info
        y_or_n = input('是否继续添加员工信息？(y/n)')
        if y_or_n == 'y':
            pass
        else:
            break

    return info


def delete_by_id(info):
    delete_id = int(input('请输入需要删除的ID号：'))
    if is_find(info, delete_id):
        del info[delete_id]

        for each in info.keys():
            print_info(info, each)

    return info


def print_info(info, employee_id):
    try:
        employee_info = info[employee_id]
        employee_list = employee_info.split(',')
        print('ID：{}，姓名：{}，电话号码：{}，城市：{}'.format(employee_id, employee_list[0], employee_list[1], employee_list[2]))
    except KeyError:
        print('请输入正确的ID号')


def is_find(info, employee_id):
    have_find = False
    for each in info.keys():
        if employee_id == each:
            have_find = True
    return have_find


def main():
    employee_information = {1: '张晓,13800000000,武汉', 2: '李明,18500000000,北京', 3: '李浩,13912341234,九江',
                            4: '王华,15890281734,上海'}
    print('=====================================')
    print('欢迎进入员工管理系统！')
    print('=====================================')
    employee_id = int(input('请输入需要查找的ID号：'))

    if is_find(employee_information, employee_id):
        print('找到此人了')
    else:
        print('查无此人')

    print_info(employee_information, employee_id)
    employee_information = delete_by_id(employee_information)
    print(employee_information)
    employee_information = add_address(employee_information)
    print(employee_information)


if __name__ == '__main__':
    main()
