def update_file(info):
    f1 = open('address_book.txt', 'w')
    for each in info.keys():
        each_info = str(each) + ':' + str(info[each]) + '\n'
        f1.write(each_info)
    f1.close()


def open_file():
    with open('address_book.txt') as f1:
        f1_list = f1.read().splitlines()
        f2 = {}
        for i in range(1, len(f1_list) + 1):
            f3 = f1_list[i - 1].split(':')
            f2[i] = f3[1]
    return f2

def is_find(info, employee_id):
    have_find = False
    for each in info.keys():
        if employee_id == each:
            have_find = True
    return have_find


def find_by_name(info):
    the_name = input('请输入需要查找的姓名：')
    suitable_list = []
    have_find = False
    for i in info.keys():
        each_info = info[i]
        name = each_info.split(' ')
        if the_name == name[0]:
            have_find = True
            suitable_list.append(i)

    return (have_find, suitable_list)


def find_by_city(info, city):
    had_found = False
    suitable_list = []
    for i in info.keys():
        each_info = info[i]
        the_city = each_info.split(' ')
        if the_city[2] == city:
            had_found = True
            suitable_list.append(i)
    return (had_found,  suitable_list)


def find_by_tel(info, tel):
    for i in info.keys():
        employee_info = info[i].split(' ')
        if employee_info[1] == tel:
            return i
    else:
        return -1


def delete_by_name(info):
    name = input('请输入需要删除的员工的名字：')
    info_list = []
    have_find = False
    for each in info.keys():
        each_info = info[each].split(' ')
        if each_info[0] == name:
            info_list.append(each)
            have_find = True
    if have_find:
        print('与该员工姓名匹配的信息如下：')
        for i in info_list:
            print_info(info, i)
            print('')
        info =  delete_by_id(info)
    else:
        print('找不到此员工')
    return info


def change_info(info, id):
    info[id] = input('请输入修改后的员工信息：')
    return info


def add_address(info):
    while True:
        new_id = int(input('请输入需要添加员工的ID号码：'))
        if is_find(info, new_id):
            print('此工号已经存在！')
            print_info(info, new_id)
            want_change = input('\n是否要对该员工信息进行修改？(y/n)')
            if want_change == 'y':
                change_info(info, new_id)
        else:
            new_info = input('请输入需要添加员工的各项信息（姓名，电话，城市）以空格隔开：')
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
        y_n = input('您确定要删除吗？y/n')
        if y_n == 'y':
            del info[delete_id]
        else:
            print('已取消，未发生任何改变')
    else:
        print('没有此人的ID号码！')

    return info


def print_info(info, employee_id):
    try:
        employee_info = info[employee_id]
        employee_list = employee_info.split(' ')
        print('ID：{}，姓名：{}，电话号码：{}，城市：{}'.format(employee_id, employee_list[0], employee_list[1], employee_list[2]),end='')
    except KeyError:
        print('请输入正确的ID号')


def main():
    employee_information = open_file()

    while True:
        print('=====================================')
        print('欢迎进入员工管理系统！')
        print('查找员工请输入find')
        print('查看员工信息请输入scan')
        print('增加员工信息请输入add')
        print('删除员工信息请输入del')
        print('保存并退出员工系统请输入quit')
        print('=====================================\n')

        command = input('您要做：')
        if command == 'find':
            print('通过ID寻找请输入id')
            print('通过电话寻找请输入tel')
            print('通过城市寻找请输入city')
            print('通过姓名寻找请输入name')
            command_1 = input()
            if command_1 == 'id':
                employee_id = int(input('请输入需要查找的ID号：'))

                if is_find(employee_information, employee_id):
                    print('找到此人了')
                    print_info(employee_information, employee_id)
                    print('')
                else:
                    print('查无此人')

            if command_1 == 'tel':
                phone = input('请输入需要查找的电话号码：')
                find_tel = find_by_tel(employee_information, phone)
                if find_tel != -1:
                    print('找到此人了')
                    print_info(employee_information, find_tel)
                    print('')
                else:
                    print('没有这个电话号码')
            if command_1 == 'city':
                the_city = input('请输入需要查找的城市：')
                my_tuple = find_by_city(employee_information, the_city)
                found = my_tuple[0]
                suitable_info = my_tuple[1]
                if found:
                    print('符合的信息如下：')
                    for i in suitable_info:
                        print_info(employee_information, i)
                        print('')
                else:
                    print('没有此城市的员工')

            if command_1 == 'name':
                name_find = find_by_name(employee_information)
                name_list = name_find[1]
                if name_find[0]:
                    print('找到此人了！')
                    for each in name_list:
                        print_info(employee_information, each)
                        print('')
                else:
                    print('查无此人')


        if command == 'scan':
            for each in employee_information.keys():
                print_info(employee_information, each)
                print('')

        if command == 'del':
            print('通过ID号删除请输入id')
            print('通过姓名删除请输入name')
            command_2 = input()
            if command_2 == 'id':
                employee_information = delete_by_id(employee_information)
                for each in employee_information.keys():
                    print_info(employee_information,each)
                    print('')

            if command_2 == 'name':
                employee_information = delete_by_name(employee_information)
                for each in employee_information.keys():
                    print_info(employee_information,each)
                    print('')


        if command == 'add':
            employee_information = add_address(employee_information)
            for i in employee_information.keys():
                print_info(employee_information, i)
                print('')

        if command == 'quit':
            break
    update_file(employee_information)


if __name__ == '__main__':
    main()
