from CSV_Handler import *

# read file CSV
monster = readCSV(r"C:\Users\ASUS\OneDrive\Documents\Tugas\Sem 2\Tugas Besar Daspro\if1210-2024-tubes-k05-d\data\monster.csv")
user = readCSV(r"C:\Users\ASUS\OneDrive\Documents\Tugas\Sem 2\Tugas Besar Daspro\if1210-2024-tubes-k05-d\data\user.csv")

data_register = []

def Register():

    if len(data_register) == 0:
        # input username & password
        username = input('Masukan Username: ')
        password = input('Masukan Password: ')

        while len(password) == 0:
            password = input('Password tidak boleh kosong, Masukan Password: ')

        # validasi username
        def username_valid(x):
            for i in range(len(username)):
                if username[i] not in ('-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'):
                    return False
            return True

        # validasi keunikan username
        def username_unik(x):
            for i in range(len(user)):
                if user[i][1] == username:
                    return False
            return True

        # nge-print sesuai kondisi
        if username_valid(username) == False:
            print('\nUsername hanya boleh berisi alfabet, angka, underscore, dan strip!')
        elif username_unik(username) == False:
            print('\nUsername',username,'sudah terpakai, silakan gunakan username lain!')
        else:
            # pilih monster
            print('\nSilakan pilih salah satu monster sebagai monster awalmu\n')
            for i in range(1,len(monster)):
                print(f'{i}. {monster[i][1]}')
            monster_pilihan = int(input('\nMonster pilihanmu: '))
            print(f'\nSelamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster[monster_pilihan][1]}!')

            # menyimpan username, password, role, dan OWCA dalam list
            data_register.append(username)
            data_register.append(password)
            data_register.append('agent')
            data_register.append('0')

    # kondisi jika register gagal
    else:
        print('Register gagal')
        print('Anda telah login dengan username',data_register[0],'silakan lakukan "LOGOUT" sebelum melakukan register.')

program = True
while program:    
    fungsi = input('\n>>> ')
    if fungsi == "REGISTER":
        Register()