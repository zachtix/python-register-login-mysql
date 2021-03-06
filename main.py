import mysql.connector
import base64
import getpass

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="testsql"
)
mycursor = mydb.cursor()

def login_verification():
    username = input('username : ')
    password = getpass.getpass('password : (type password don\'t show in display)').encode("utf-8")
    passwordencoded = base64.b64encode(password)
    sql = "select * from users where username = %s and password = %s"
    mycursor.execute(sql,[(username),(passwordencoded)])
    results = mycursor.fetchone()
    if results:
        print('Login Success')
        # print(results)
        # print(type(results))
        print('Username : ', results[1])
        # decoded password
        # passx = base64.b64decode(results[2]).decode('utf-8')
        # print('Password : ', passx)
        menu()
    else:
        print('Login fail username or password wrong')
        menu()

def register():
    username = input('Register Sytem\nusername : ')
    sql = "select * from users where username = %s"
    mycursor.execute(sql,[(username)])
    results = mycursor.fetchone()
    if results:
        print('Username Already\nPls try again')
        register()
    else:
        while(True):
            password = getpass.getpass('password : (type password don\'t show in display)')
            confirmpassword = getpass.getpass('confirm password : (type password don\'t show in display)')
            password_utf8 = password.encode("utf-8")
            passwordencoded = base64.b64encode(password_utf8)
            if password == confirmpassword:
                print('password match')
                sql = "insert into users (username, password) values (%s, %s)"
                mycursor.execute(sql, [(username),(passwordencoded)])
                mydb.commit()
                print('Register Success')
                # break
                menu()
            else:
                print('password not match\ntry again')

def menu():
    try:
        print('[1]Login\n[2]Register\n[3]Exit')
        selecetmenu = int(input('Choice Menu : '))
        if selecetmenu == 1:
            login_verification()
        elif selecetmenu == 2:
            register()
        elif selecetmenu == 3:
            exit()
    except ValueError:
        print('[Error] Pls enter number')
        menu()


if __name__ == "__main__":
    menu()