__author__ = "heibaizhishang"

# 作业二：编写登陆接口
# 输入用户名密码
# 认证成功后显示欢迎信息输错三次后锁定

pre_lock_name = {}


def check_lock_status(check_name):
    """
    读取【锁定用户名表】，检查用户名是否被锁定
    :param check_name: 待检查的用户名
    :return: 用户名是否被锁定
    """
    status = False
    fo = open("lockUser", "r")

    lines = fo.readline()
    while lines != '':
        if check_name == lines[:-1]:
            status = True
            break
        lines = fo.readline()

    fo.close()

    return status


def password_exist_name(check_name):
    """
    读取【用户密码表】，查询待检查的用户名的密码
    :param check_name: 待检查用户名
    :return: 密码，如不存在的用户名，返回""
    """
    exist_password = ""
    fo = open("user", "r")

    lines = fo.readline()
    while lines != '':
        if lines.startswith(check_name):
            exist_password = lines.split(" ")[1]
            break
        lines = fo.readline()

    fo.close()

    return exist_password


def add_lock_name(lock_name):
    """
    追加要锁定的名字
    :param lock_name: 要锁定的名字
    """
    fo = open("lockUser", "a")

    fo.write(lock_name + "\n")

    fo.close()


def handle_wrong_name(wrong_name):
    """
    处理输入密码错误的用户名
    :param wrong_name: 错误的用户名
    """
    global pre_lock_name

    if wrong_name not in pre_lock_name:
        pre_lock_name.clear()
        pre_lock_name = {wrong_name: 1}
    else:
        if pre_lock_name[wrong_name] == 1:
            pre_lock_name[wrong_name] = 2
        else:
            add_lock_name(wrong_name)
            pre_lock_name.clear()


while True:
    username = input("输入用户名：")
    password = input("输入密码：")

    if check_lock_status(username):
        print("用户名", username, "被锁定")
    else:
        password_exist = password_exist_name(username)
        if password_exist == "":
            print("用户名", username, "不存在")
        elif password_exist == password:
            print("欢迎用户", username, "光临")
            pre_lock_name.clear()
            break
        else:
            print("用户名", username, "密码错误")
            handle_wrong_name(username)
