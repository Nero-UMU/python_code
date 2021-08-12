import time
import random


class user_account():
    # 创建账号的函数
    def enroll_account():
        print('欢迎进入用户注册系统')

        # 录入用户名
        user_name = input('用户名：')

        while True:
            # 录入用户性别
            user_gender = input('性别（男/女）：')

            # 录入用户身份证信息，并检测身份证信息是否正确
            user_id = input('请输入身份证号')
            while len(user_id) != 18:
                user_id = input('身份证信息有误，请重新输入（身份证的长度为18位）：')

            odd_number = ['1', '3', '5', '7', '9']
            even_number = ['0', '2', '4', '6', '8']
            if ( user_gender == '男' ) and ( user_id[-2] in even_number ):
                print('身份信息与输入的信息不匹配，请重新输入！')
            elif ( user_gender == '女' ) and ( user_id[-2] in odd_number ):
                print('身份信息与输入的信息不匹配，请重新输入！')
            else:
                break

        # 录入密码
        user_password_1 = input('请输入您的密码（密码长度为6 ~ 18位，至少含有一个字母和数字）：')

        while True:
            # 判断密码长度，若长度不符合要求则要求重新录入密码
            while (len(user_password_1) < 6 or len(user_password_1) > 18) or (user_password_1.isalpha() or user_password_1.isdigit() ):
                print('密码应由字母与数字组成，且长度在6 ~ 18位之间！请重新输入：', end = '')
                user_password_1 = input()

            # 再次输入密码以确定密码输入正确
            user_password_2 = input('请再次输入密码：')
            if user_password_1 == user_password_2:
                break
            else:
                user_password_1 = input('两次输入的密码不一致！请重新输入密码：')

        # 创建用户身份信息文件
        user_name_1 = '姓名：' + user_name + '\n'
        user_id = '身份证：' + user_id + '\n'
        user_gender = '性别：' + user_gender + '\n'
        user_password_1 = '密码：' + user_password_1 + '\n'

        info = [user_name_1, user_id, user_gender, user_password_1]

        name_info = user_name + '.txt'
        user_each_info = open(name_info, 'w')
        for each_info in range(4):
            user_each_info.write(info[each_info])
        user_each_info.close()

        random_number = random.randint(4, 8)
        print('正在创建账号中', end = '')
        for i in range(random_number):
            print('.', end = '')
            time.sleep(0.5)
        print('\n账号创建成功！')

    def sign_up():
        print('欢迎进入登录系统')
        while True:
            try:
                user_name = input('请输入用户名（退出登录请输入exit）：')
                if user_name != 'exit':
                    user_password = input('请输入密码：')
                    file_name = user_name + '.txt'
                    account = open(file_name)
                    account_str =
                else:
                    break


            except FileNotFoundError:
                print('用户名不存在！')

