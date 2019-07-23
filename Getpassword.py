#此程序不能在pycharm或IDLE中执行,可以在ＣＭＤ中执行
import getpass,os ,time#用于隐藏用户输入的字符串，常用来接收密码

dict_pass = {'email' : ',.wawjlmm',
        'qq'    : '123qwe'   ,
        'wechat': '!213'
        }

def checkuser(user,passwd):
    if user == 'hehe' and passwd == '123':
        return True
    else:
        return False

def getuserpassword(idem):
    if idem in dict_pass.keys():
        print (idem + '密码是：'+ dict_pass[idem])
    else:
        print('不存在' + idem +'的密码')

pass_flag = 0
try_time = 3

while try_time != 0 :
    try_time -= 1
    userr = input('请输入用户名:')
    passwdd = getpass.getpass('请输入用户密码:')

    if checkuser(userr,passwdd):
        #print('用户名、密码输入正确!')
        pass_flag = 0
        break

    else:
        print('用户或密码错误，您还可以输入' + str(try_time) + '次！' )
        pass_flag = 1

if pass_flag != 0:
    print('3次用户名或密码输入错误，退出!!!')
    exit()
else:
    idem = input('请输入你要查询的项目：')
    getuserpassword(idem)
time.sleep(5)