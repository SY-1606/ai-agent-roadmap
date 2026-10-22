#功能：用户名和密码验证，最多尝试三次。

correct_username = "admin"
correct_password = "123456"

success = False #标识

for attempt in range(3):
    username = input("请输入用户名：")
    password = input("请输入密码：")

    if username == correct_username and password == correct_password:
        print("登录成功")
        success = True
        break
    else:
        print(f"用户名或密码错误，还剩 {2 - attempt} 次机会")

if not success:
    print("尝试次数过多，登录失败")
