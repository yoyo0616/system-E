correct_username = "user123"
correct_password = "password123"

# 輸入用戶名
username = input("請輸入你的帳號: ")

# 輸入密碼（這裡用 input 會顯示在畫面上，通常可以使用 getpass 模組來隱藏密碼輸入）
password = input("請輸入你的密碼: ")

# 驗證用戶名和密碼
if username == correct_username and password == correct_password:
    print("登入成功！")
else:
    print("帳號或密碼錯誤，請再試一次。")