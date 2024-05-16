# F03 - LOGOUT
def logout(isLogin,userId,username,coin,role):
    # Periksa Apakah Pengguna Sudah Login
    if isLogin == True:
        print(f'Anda Berhasil Logout dari Akun dengan username {username}.\n')
        isLogin = False
        userId = 0
        username = ''
        coin = 0
        role = ''
        return isLogin,userId,username,coin,role
    else:
        print('Logout gagal!')
        print('Anda belum login, silahkan lakukan "LOGIN" terlebih dahulu sebelum melakukan logout.\n')
        return isLogin,userId,username,coin,role