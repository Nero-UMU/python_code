class gun:
    def __init__(self, name, bullet):
        self.name = name
        self.bullet = bullet

    def shoot(self):
        if bullet >= 1:
            print('枪%s发射出了一发子弹！'%self.name)
        else:
            print('枪%s里没有子弹，需要装弹！'%self.name)

class soldier:
    def __init__(self, name):
        self.name = name
        self.gun_list = []

    def get_gun(self, gun):
        print('士兵%s获得了一把%s！'%(self.name, gun.name))
        self.gun_list.append(gun.name)

    def fire(self, gun):
        if gun.name in self.gun_list:
            if gun.bullet >= 1:
                print('%s使用%s发射了一发子弹！'%(self.name, gun.name))
                gun.bullet -= 1
            else:
                print('%s中没有子弹，%s无法发射子弹！'%(gun.name, self.name))
        else:
            print('士兵%s暂未获得该枪'%self.name)

    def reload(self, gun):
        if gun.name in self.gun_list:
            gun.bullet = 10
        else:
            print('士兵%s暂未获得该枪'%self.name)

def main():
    AK47 = gun('AK47', 0)
    Rien = soldier('Rien')
    Rien.fire(AK47)
    Rien.get_gun(AK47)
    Rien.fire(AK47)
    Rien.reload(AK47)
    Rien.fire(AK47)

if __name__ == '__main__':
    main()