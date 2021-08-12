'''
将文档text_passage_1.txt中的对话按对话的人分开，
三段对话共创造6个txt文档
版本：v1.0
'''


file = open('text_passage_1.txt', 'r', encoding = 'utf-8')

boy = []
girl = []
count = 1

for each_line in file:
    if each_line[:6] != '======':
        (role, talk_things) = each_line.split(':', 1)
        if role == '小甲鱼':
            boy.append(talk_things)
        if role == '小客服':
            girl.append(talk_things)
    else:
        file_name_boy = 'file_' + str(count) + 'boy' + '.txt'
        file_name_girl = 'file_' + str(count) + 'girl' + '.txt'

        boy_file = open(file_name_boy, 'w')
        girl_file = open(file_name_girl, 'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1
(role, talk_things) = each_line.split(':', 1)
if role == '小甲鱼':
    boy.append(talk_things)
if role == '小客服':
    girl.append(talk_things)
file_name_boy = 'file_' + str(count) + 'boy' + '.txt'
file_name_girl = 'file_' + str(count) + 'girl' + '.txt'

boy_file = open(file_name_boy, 'w')
girl_file = open(file_name_girl, 'w')

boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()

boy = []
girl = []
count += 1

file.close()
