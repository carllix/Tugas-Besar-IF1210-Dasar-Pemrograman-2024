def readCSV(path:str):
    data = []
    with open(path,'r') as file:
        for line in file:
            elmt = ''
            row = []
            for char in line:
                if char == ";":
                    row.append(elmt)
                    elmt = ''
                else:
                    elmt = elmt + char
            data.append(row)
    return data

users = readCSV('data/user.csv')
isLoggedIn = False
userName = 'Bozo'

def login(isLoggedIn,userName,users):
    print('-------Login------')
    if isLoggedIn == False:
        username = input("Username: ")
        password = input("Password: ")
        for user in users:
            if user[1] == username:
                if user[2] == password:
                    userId = user[0]
                    userName = user[1]
                    role = user[3]
                    coin = user[4]
                    isLoggedIn = True
                    print(f"Selamat datang kembali, {role} {userName}. Mari lanjutkan petualangan kita!")
                    print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
                    return userId, userName, role, coin, isLoggedIn   
                else: 
                    return print('Password salah!')
        print('Username tidak terdaftar!')

    else:
        print('Login gagal!')
        print(f'Anda telah login dengan username {userName}, silahkan lakukan "LOGOUT" sebelum melakukan login kembali.')

login(isLoggedIn,userName,users)
