from CSV_Handler import *

# read file CSV
monster = readCSV("data\monster.csv")
user = readCSV("data\user.csv")

def Register():
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

        # role dan OWCA coin awal
        role = 'agent'
        oc = 0

program = True
while program:    
    fungsi = input('>>> ')
    if fungsi == "REGISTER":
        Register()