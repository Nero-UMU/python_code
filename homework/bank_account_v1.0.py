'''
日期：2021.5.7
作者：WJK
功能:实现简单的银行账户交易
需求：
1  银行账户 有如下属性
    用户名 username
    账号card_id
    余额balance
2  能够执行如下操作
    存款 deposit
    取款 withdraw
    转账 transfer
    打印流水 history
3 业务分析
    存款：金额合法
    取款：金额合法 并且 余额大于等于取款金额
    转账：涉及两个账户，需要金额合法且余额大于等于金额，且对方账户存在
    打印流水
版本：v1.0
'''


import time

class Bank_account:
    def __init__(self, username, card_id, balance):
        self.username = username
        self.balance = balance
        self.card_id = card_id
        self.history_list = []

    def now_time(self):
        now_struct = time.localtime()
        day_and_time = time.strftime('%Y-%m-%d %H:%M:%S', now_struct)
        return day_and_time

    # 判断金额是否合法的方法
    def is_amount_legal(self, amount):
        if not isinstance(amount, (float, int)) or amount <= 0:
            print('输入的金额不合法或者金额小于零~~~')
            return False
        return True

    # 存款方法
    def deposit(self, amount):
        if self.is_amount_legal(amount):
            self.balance += amount
            now = self.now_time()
            log = '亲爱的{}，您的账户{}在{}存款{}元成功，账户余额{}'.format(self.username, self.card_id, now, amount, self.balance)
            print(log)
            self.history_list.append(log)

    def withdraw(self, amount):
        if self.is_amount_legal(amount):
            if amount <= self.balance:
                self.balance -= amount
                now = self.now_time()
                log = '亲爱的{}，您的账户{}在{}取款{}元成功，账户余额{}'.format(self.username, self.card_id, now, amount,self.balance)
                print(log)
                self.history_list.append(log)
            else:
                print('余额不足，无法取钱~')

    def transfer(self, that, amount):
        if self.is_amount_legal(amount):
            if amount <= self.balance:
                self.balance -= amount
                that.balance += amount
                now = self.now_time()
                log1 = '亲爱的{}，您的账户{}，在{}转账{}元给{}，账户{}，账户余额为{}'.format(self.username, self.card_id, now, amount, that.username, that.card_id, self.balance)
                print(log1)
                self.history_list.append(log1)
                that.balance += amount
                log2 = '亲爱的{}，账户{}于{}给您的账户{}转账{}元，账户余额为{}'.format(that.username, self.card_id, now, that.card_id, amount, that.balance)
                that.history_list.append(log2)

    def print_history(self):
        print(self.history_list)

def main():
    Tim = Bank_account('Tim', '557913203', 57810.2)
    Bob = Bank_account('Bob', '123847644', 48887)

    Tim.withdraw(404)
    Bob.deposit(2048)

    Tim.transfer(Bob, 1024)

    print('\nTim流水如下：')
    print(Tim.history_list)
    print('Bob流水如下：')
    print(Bob.history_list)


if __name__ == '__main__':
    main()