#猜数字游戏
#给玩家6次机会猜出0~100随机数
import random , os
count = 0
random_num = random.randint(0,100)#随机产生0~100的数
count = 6
while count != 0 :
    number = int(input("请入一个0~100的数字："))
    if number < random_num :
        count  -= 1
        print('猜小了，还有'+ str(count) + '次机会，加油！\n')
    elif number > random_num :
        count  -= 1
        print('猜大了，还有'+ str(count) + '次机会，加油！\n')
    elif number == random_num :
        print('真棒你猜对了\n')
        break
if count != 0 :
    print('游戏胜利 :） 再玩一次吧\n')
else:
    print('游戏失败): 谜底是' + str(random_num) + '再试一次吧！！！')

        
