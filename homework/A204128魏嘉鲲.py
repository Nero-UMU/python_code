'''
日期：2021.5.21
作者：魏嘉鲲
功能：员工管理系统
每个员工的信息包括：工号、姓名、性别、出生年月、学历、职务、电话、住址等
功能：
1查询：按特定条件查找员工（查询条件设计应包含：主关键字查询（如工号）、次关键字查询（如姓名））。
2修改：按工号对某个员工的某项信息进行修改。
3插入：加入新员工的信息。
4删除：按工号删除已离职员工的信息。
5打印：输出某个指定员工的信息。

员工信息存储在相应的数据文件worker.txt中
设计要求。
1．设计两个类：员工类和文件操作类
2．没有特殊要求时，指定条件均为工号
'''


class file:
    def update_file(info):
        f1 = open('worker.txt', 'w')
        for each in info.keys():
            each_info = str(each) + ':' + str(info[each]) + '\n'
            f1.write(each_info)
        f1.close()


    def open_file():
        with open('worker.txt') as f1:
            f1_list = f1.read().splitlines()
            f2 = {}
            for i in range(1, len(f1_list) + 1):
                f3 = f1_list[i - 1].split(':')
                f2[i] = f3[1]
        return f2

class employee:
    def change(info):
        id = int(input('请输入需要改变的员工的id：'))
        if employee.is_find(info, id):
            print('该员工的信息如下：')
            employee.print_info(info, id)
            print('\n改变姓名请输入name')
            print('改变性别请输入agent')
            print('改变出生年月请输入birth')
            print('改变学历请输入study')
            print('改变职务请输入work')
            print('改变电话请输入phone')
            print('改变住址请输入address')

            new_info = info[id].split(' ')

            to_do = input('需要改变：')
            if to_do == 'name':
                new = input('请输入需要改变成什么信息：')
                new_info[0] = new

            if to_do == 'agent':
                new = input('请输入需要改变成什么信息：')
                new_info[1] = new

            if to_do == 'birth':
                new = input('请输入需要改变成什么信息：')
                new_info[2] = new

            if to_do == 'study':
                new = input('请输入需要改变成什么信息：')
                new_info[3] = new

            if to_do == 'work':
                new = input('请输入需要改变成什么信息：')
                new_info[4] = new

            if to_do == 'phone':
                new = input('请输入需要改变成什么信息：')
                new_info[5] = new

            if to_do == 'address':
                new = input('请输入需要改变成什么信息：')
                new_info[6] = new

            each_info = new_info[0] + ' ' + new_info[1] + ' ' + new_info[2] + ' ' + new_info[3] + ' ' + new_info[4] + ' ' + new_info[5] + ' ' + new_info[6]
            info[id] = each_info
        else:
            print('没有此员工！')

        return info


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
            if the_city[6] == city:
                had_found = True
                suitable_list.append(i)
        return (had_found,  suitable_list)


    def find_by_tel(info, tel):
        for i in info.keys():
            employee_info = info[i].split(' ')
            if employee_info[5] == tel:
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
                employee.print_info(info, i)
                print('')
            info =  employee.delete_by_id(info)
        else:
            print('找不到此员工')
        return info


    def change_info(info, id):
        info[id] = input('请输入修改后的员工信息（姓名、性别、出生年月、学历、职务、电话、住址）：')
        return info


    def add_address(info):
        while True:
            new_id = int(input('请输入需要添加员工的ID号码：'))
            if employee.is_find(info, new_id):
                print('此工号已经存在！')
                employee.print_info(info, new_id)
                want_change = input('\n是否要对该员工信息进行修改？(y/n)')
                if want_change == 'y':
                    employee.change_info(info, new_id)
            else:
                new_info = input('请输入需要添加员工的各项信息（姓名、性别、出生年月、学历、职务、电话、住址）以空格隔开：')
                info[new_id] = new_info
            y_or_n = input('是否继续添加员工信息？(y/n)')
            if y_or_n == 'y':
                pass
            else:
                break

        return info


    def delete_by_id(info):
        delete_id = int(input('请输入需要删除的ID号：'))
        if employee.is_find(info, delete_id):
            y_n = input('您确定要删除吗？y/n：')
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
            print('工号:{},姓名:{},性别:{},出生年月:{},学历:{},职务:{},电话:{},住址:{}'.format(employee_id, employee_list[0], employee_list[1], employee_list[2], employee_list[3], employee_list[4], employee_list[5], employee_list[6]),end='')
        except KeyError:
            print('请输入正确的ID号')


def main():
    employee_information = file.open_file()

    while True:
        print('=====================================')
        print('欢迎进入员工管理系统！')
        print('查找员工请输入find')
        print('查看员工信息请输入scan')
        print('增加员工信息请输入add')
        print('删除员工信息请输入del')
        print('改变员工信息请输入change')
        print('保存并退出员工系统请输入quit')
        print('=====================================\n')

        command = input('您要做：')
        if command == 'find':
            print('通过ID寻找请输入id')
            print('通过电话寻找请输入tel')
            print('通过住址寻找请输入home')
            print('通过姓名寻找请输入name')
            command_1 = input()
            if command_1 == 'id':
                employee_id = int(input('请输入需要查找的ID号：'))

                if employee.is_find(employee_information, employee_id):
                    print('找到此人了')
                    employee.print_info(employee_information, employee_id)
                    print('')
                else:
                    print('查无此人')

            if command_1 == 'tel':
                phone = input('请输入需要查找的电话号码：')
                find_tel = employee.find_by_tel(employee_information, phone)
                if find_tel != -1:
                    print('找到此人了')
                    employee.print_info(employee_information, find_tel)
                    print('')
                else:
                    print('没有这个电话号码')
            if command_1 == 'home':
                the_city = input('请输入需要查找的城市：')
                my_tuple = employee.find_by_city(employee_information, the_city)
                found = my_tuple[0]
                suitable_info = my_tuple[1]
                if found:
                    print('符合的信息如下：')
                    for i in suitable_info:
                        employee.print_info(employee_information, i)
                        print('')
                else:
                    print('没有此住址的员工')

            if command_1 == 'name':
                name_find = employee.find_by_name(employee_information)
                name_list = name_find[1]
                if name_find[0]:
                    print('找到此人了！')
                    for each in name_list:
                        employee.print_info(employee_information, each)
                        print('')
                else:
                    print('查无此人')


        if command == 'scan':
            for each in employee_information.keys():
                employee.print_info(employee_information, each)
                print('')

        if command == 'del':
            print('通过ID号删除请输入id')
            print('通过姓名删除请输入name')
            command_2 = input()
            if command_2 == 'id':
                employee_information = employee.delete_by_id(employee_information)
                for each in employee_information.keys():
                    employee.print_info(employee_information,each)
                    print('')

            if command_2 == 'name':
                employee_information = employee.delete_by_name(employee_information)
                for each in employee_information.keys():
                    print_info(employee_information,each)
                    print('')


        if command == 'add':
            employee_information = employee.add_address(employee_information)
            for i in employee_information.keys():
                employee.print_info(employee_information, i)
                print('')

        if command == 'change':
            employee_information = employee.change(employee_information)

        if command == 'quit':
            break
    file.update_file(employee_information)


if __name__ == '__main__':
    main()
