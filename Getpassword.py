


import getpass #用于隐藏用户输入的字符串，常用来接收密码

def checkuser(user,passwd):
    if user == 'hehe' and passwd == '123':
        return True
    else:
        return False

if __name__ == "__main__":
    userr = input('Input the user:')
    passwdd = getpass.getpass('Input the passwd:')

    if checkuser(userr,passwdd):
        print('OK!')
    else:
        print('ERROR!')