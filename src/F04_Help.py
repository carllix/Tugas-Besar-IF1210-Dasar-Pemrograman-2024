def help(isLogin:bool, role:str, username:str):
    print('\n============================================================================================================')
    print('''
                                        ░█─░█ ░█▀▀▀ ░█─── ░█▀▀█ 
                                        ░█▀▀█ ░█▀▀▀ ░█─── ░█▄▄█ 
                                        ░█─░█ ░█▄▄▄ ░█▄▄█ ░█───''')
    print('\n============================================================================================================')
    if isLogin == False:
        print('\nKamu belum login sebagai role apapun. Silahkan login terlebih dahulu.')
        print('\t1. Login: Masuk ke dalam akun yang sudah terdaftar')
        print('\t2. Register: Membuat akun baru')
    else:
        if role == 'agent':
            print(f'\nHalo Agent {username} !')
            print('Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian.')
            print('Berikut adalah hal-hal yang dapat kamu lakukan sekarang:\n')
            print('\t1. LOGOUT: Keluar dari akun yang sedang digunakan')
            print('\t2. INVENTORY: Melihat owca-dex yang dimiliki oleh Agent')
            print('\t3. BATTLE: Bertarung melawan monster secara random')
            print('\t4. ARENA: Pertarungan dengan aturan seperti battle selama 5 stage')
            print('\t5. SHOP: Tempat Agent membeli monster dan potion menggunakan owca-coin')
            print('\t6. LABORATORY: Tempat Agent melakukan upgrade level monster yang dimiliki di inventory') 

        else: # role == 'admin'
            print(f'\nSelamat datang, Admin {username}. Berikut adalah hal-hal yang dapat kamu lakukan:\n')
            print('\t1. LOGOUT: Keluar dari akun yang sedang digunakan')
            print('\t2. SHOP: Melakukan manajemen pada SHOP sebagai tempat jual beli perlatan Agent')
            print('\t3. MONSTER: Mengatur manajemen monster di dalam owca-dex')

    # Footnote
    print('\nFootnote:')
    print('\t1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar')
    print('\t2. Jangan lupa untuk memasukkan input yang valid')