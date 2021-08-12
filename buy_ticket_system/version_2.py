'''
时间 2021/4/12
版本 v2.0
版本功能
v1.0:输入车票的起始地、目的地、发车时间、到达时间、车票价格
并保存在文档中。获取到各种信息后，用户可以购买车票。
v2.0:新增票的数量和改签功能
'''


import random
import time
import os


# 进行改签的函数
def change_visa():

    Y_OR_N = input('是否要进行改签？一张票只能改签一次！(Y/N)')
    while Y_OR_N == 'Y':

        # 判断改签的车票是否存在
        try:
            # 获取准备改签的车票
            visa_information = input('请输入准备改签的车次和数量(以空格间隔)：(车次 车票数)')
            want_change = list(visa_information.split(' '))
            ticket_name = 'Ticket of ' + want_change[0] + ' X ' + want_change[1] + '.txt'

            # 判断该车票是否可以改签
            can_ticket = open(ticket_name, 'r')
            can_do_it = can_ticket.read()
            can_ticket.close()
            if can_do_it[-8:] != '此票不可再次改签':

                # 获取希望改签的车票信息
                new_visa = input('请输入希望改签至的车次和数量(以空格间隔)：(车次 车票数)')
                ready_change = list(new_visa.split(' '))
                ready_go_name = 'Ticket of ' + ready_change[0] + ' X ' + ready_change[1] + '.txt'

                # 询问用户是否要改签
                print('您确定要从{}次列车改签至{}吗？(sure/not)'.format(want_change[0], ready_change[0]))
                are_you_sure = input()

                # 若用户选择确认改签，则删除原车票文件
                if are_you_sure == 'sure':
                    os.remove(ticket_name)

                    # 创建新的车票文件，添加后缀语句禁止第二次改签
                    new_ticket = open(ready_go_name, 'w')
                    message = '您已成功改签至' + ready_change[0] + '次列车，请及时到站乘车！此票不可再次改签'
                    new_ticket.write(message)
                    new_ticket.close()
            else:
                print('此车票已经改签过了，不可再次更改！')
        except FileNotFoundError:
            print('输入的车票不存在，请确定输入的各项信息是否正确！')

        Y_OR_N = input('是否继续改签？(Y/N)')

# 录入车票信息的函数
def ticket_info():

    Y_OR_N = input('是否要开始输入车票信息（Y/N）：')
    # 通过循环获得火车的各种信息
    while Y_OR_N == 'Y':
        information = []

        # 录入各种车票信息
        count = input('请输入车次：')
        start_place = '起始地:' + input('请输入火车的起始地：') + '\n'
        destination_place = '目的地:' + input('请输入火车的目的地：')+ '\n'
        start_time = '发车时间:' + input('请输入火车的发车时间：')+ '\n'
        arrival_time = '到达时间:' + input('请输入火车的到达时间：')+ '\n'
        ticket_money = '车票价格:' + input('请输入火车票的价格：')+ '\n'
        ticket_number = '车票数量:' + input('请输入火车票的数量：') + '\n'

        # 将各种车票信息放入一个列表中
        information = [start_place, destination_place,start_time, arrival_time, ticket_money, ticket_number]

        # 根据车次生成文件的名字
        name = 'ticket_information_' + count + '.txt'

        # 创建新的车票文件
        new_ticket_information = open(name, 'w')

        # 将各种车票信息存入文件中
        for each_information in range( 6 ):
            new_ticket_information.write(information[each_information])

        new_ticket_information.close()

        Y_OR_N = input('是否继续输入（Y/N）?')
    print('车次录入已完成！')

# 买票的函数
def ticket_buy():
    Y_OR_N = input('是否开始买票？（Y/N）')
    while Y_OR_N == 'Y':

        # 检测是否存在车票信息，没有则告诉用户该车次不存在
        try:

            # 输入车次号，根据车次号进行查询车票
            train = input('请输入需要购买的车次的车号:')
            which_ticket = 'ticket_information_' + train + '.txt'

            # 打开该车票的文件
            ticket_info = open(which_ticket,'r')

            random_number = random.randint(4, 8)
            print('查询车票信息中', end = '')
            for i in range(random_number):
                print('.', end = '')
                time.sleep(0.5)

            # 输出车票信息供用户审查
            print('该车次信息如下：')
            for each_info in ticket_info:
                print(each_info)

            ticket_info.close()

            # 生成车票信息，并生成车票文件
            ticket_number = input('请输入需购买车票的数量：')
            train_ticket_name = 'Ticket of ' + train + ' X ' + ticket_number + '.txt'

            the_ticket = open(train_ticket_name, 'w')
            success_info = '您已成功购买' + train + '次列车车票，请及时到站乘车！'
            the_ticket.write(success_info)
            the_ticket.close()

            Y_OR_N = input('是否继续购买车票？（Y/N）')


        except FileNotFoundError:
            print('输入的车次不存在，请确定输入的车次是否正确！')

    print('已退出购票系统')

def main():
    while True:
        print('======================================================')
        print('欢迎进入本车站售票系统！')
        print('录入列车信息请输入 inter')
        print('购买车票请输入 buy')
        print('车票改签请输入 change')
        print('若要退出售票系统请输入 quit')
        print('======================================================')
        command = input('您要做:')

        random_number = random.randint(4, 8)
        print('请稍等', end='')
        for i in range(random_number):
            print('.', end='')
            time.sleep(0.5)
        else:
            print('\n')

        if command == 'inter':
            ticket_info()
        if command == 'buy':
            ticket_buy()
        if command =='change':
            change_visa()
        if command == 'quit':
            break

    print('售票系统已成功退出！')

if __name__ == '__main__':
    main()
