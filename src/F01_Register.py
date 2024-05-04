sudah_register = False

def Register():
    # nge-read file CSV
    def readCSV(path:str):
        data = []
        with open(path, 'r') as file:
            for line in file:
                elmt = ''
                row = []
                for char in line:
                    if char == ';':
                        row.append(elmt)
                        elmt = ''
                    else:
                        elmt = elmt + char
                data.append(row)
        return data

    monster = readCSV(r"C:\Users\ASUS\OneDrive\Documents\Tugas\Sem 2\Tugas Besar Daspro\if1210-2024-tubes-k05-d\data\monster.csv")
    user = readCSV(r"C:\Users\ASUS\OneDrive\Documents\Tugas\Sem 2\Tugas Besar Daspro\if1210-2024-tubes-k05-d\data\user.csv")

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
        print('')
        print('Username hanya boleh berisi alfabet, angka, underscore, dan strip!')
    elif username_unik(username) == False:
        print('')
        print('Username',username,'sudah terpakai, silakan gunakan username lain!')
    else:
        # pilih monster
        print('')
        print('Silakan pilih salah satu monster sebagai monster awalmu')
        print('')
        for i in range(1,len(monster)):
            print(f'{i}. {monster[i][1]}')
        print('')
        monster_pilihan = int(input('Monster pilihanmu: '))
        print('')
        print(f'Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster[monster_pilihan][1]}!')

        # role dan OWCA coin awal
        role = 'agent'
        oc = 0

program = True
while program:    
    fungsi = input('>>> ')
    if fungsi == "REGISTER":
        Register()