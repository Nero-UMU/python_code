def find_by_city(info, city):
    had_found = False
    suitable_list = []
    for i in info.keys():
        each_info = info[i]
        the_city = each_info.split(',')
        if the_city[2] == city:
            had_found = True
            suitable_list.append(i)
    return (had_found,  suitable_list)


def find_by_tel(info, tel):
    for i in info.keys():
        employee_info = info[i].split(',')
        if employee_info[1] == tel:
            return i
    else:
        return -1



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
    employee_information = {1: '张晓\t,13800000000,武汉', 2: '李明\t,18500000000,北京', 3: '李浩\t,13912341234,九江',
                            4: '王华\t,15890281734,上海'}
    while True:
        print('=====================================')
        print('欢迎进入员工管理系统！')
        print('通过工号查询员工信息请输入find_id')
        print('通过电话查询员工信息请输入find_tel')
        print('通过城市查询员工信息请输入find_city')
        print('增加员工信息输入add')
        print('删除员工信息请输入delete')
        print('退出请输入quit')
        print('=====================================')
        command = input('您要做：')
        if command == 'find_id':
            id = int(input('请输入需要查询的id号：'))
            if is_find(employee_information, id):
                print_info(employee_information, id)
            else:
                print('查无此人')

        if command == 'add':
            employee_information = add_address(employee_information)
            for each in employee_information.keys():
                print_info(employee_information, each)

        if command == 'delete':
            employee_information = delete_by_id(employee_information)

        if command == 'find_tel':
            tel = input('请输入需要查找的电话号码：')
            outcome = find_by_tel(employee_information, tel)
            if outcome != -1:
                print('查询成功！')
                print(employee_information[outcome])
            else:
                print('查无此号码')

        if command == 'find_city':
            city = input('请输入需要查询的城市：')
            tuple1 = find_by_city(employee_information, city)
            had_not = tuple1[0]
            list1 = tuple1[1]
            if had_not:
                for x in list1:
                    print_info(employee_information, x)
            else:
                print('查不到该城市')

        if command == 'quit':
            break

if __name__ == '__main__':
    main()
