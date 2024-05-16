def help(isLogin, role, username):
    print("=========== HELP ===========")
    if isLogin == False:
        print('Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.')
        print('\t1. Login: Masuk ke dalam akun yang sudah terdaftar')
        print('\t2. Register: Membuat akun baru')
    else:
        if role == 'agent':
            print(f'Halo Agent {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:\n')
            print('\t1. Logout: Keluar dari akun yang sedang digunakan')
            print('\t2. Inventory: Melihat owca-dex yang dimiliki oleh Agent') 
            # TAMBAHIN LAGI PENJELASANNYA
        else: # role == 'admin'
            print(f'Selamat datang, Admin {username}. Berikut adalah hal-hal yang dapat kamu lakukan:\n')
            print('\t1. Logout: Keluar dari akun yang sedang digunakan')
            print('\t2. Shop : Melakukan manajemen pada SHOP sebagai tempat jual beli perlatan Agent')
            # TAMBAHIN LAGI PENJELASANNYA
            
    # Footnote
    print('\nFootnote:')
    print('\t1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar')
    print('\t2. Jangan lupa untuk memasukkan input yang valid')