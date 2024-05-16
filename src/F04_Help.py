def help_menu(login, agent, admin, username):
    print("=========== HELP ===========")
    if login == False:
        print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.\n"
              "\n1. Login: Masuk ke dalam akun yang sudah terdaftar\n"
              "2. Register: Membuat akun baru\n"
              "\nFootnote: \n1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar\n"
              "2. Jangan lupa untuk memasukkan input yang valid")
    elif login == True and agent == True:
        print("Halo Agent {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, "
              "semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:\n"
              "1. Logout: Keluar dari akun yang sedang digunakan\n"
              "2. Inventory: Melihat owca-dex yang dimiliki oleh Agent") 
    else:
        print("Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:\n"
              "\n1. Logout: Keluar dari akun yang sedang digunakan\n"
              "2. Shop : Melakukan manajemen pada SHOP sebagai tempat jual beli perlatan Agent\n"
              "\nFootnote: \n1. Untuk menggunakan aplikasi, silahkan masukan nama fungsi yang terdaftar\n"
              "2. Jangan lupa untuk memasukkan input yang valid")
