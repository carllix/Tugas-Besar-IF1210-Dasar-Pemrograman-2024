import os
import sys
import argparse
from time import sleep

def read_csv(filename, folder_path):
    if folder_path[-1] != '/':
        folder_path += '/'
    file_path = folder_path + filename

    data = []

    # Cek apakah folder tersedia
    if not os.path.exists(file_path):
        print(f'Error: The file {filename} was not found in the folder {folder_path}.')
        return data

    # Read CSV file sebagai matriks
    with open(file_path, mode='r', newline='') as file:
        for line in file:
            row = []
            elmt = ''
            for char in line:
                if char == '\n' or char == '\r':
                    continue
                if char == ';':
                    row.append(elmt)
                    elmt = ''
                else:
                    elmt += char
            if elmt:
                row.append(elmt) 
            data.append(row)
    return data


def load_data(folder):
    data_directory = os.path.dirname(__file__) + '/../data/'
    folder_path = data_directory + folder
    file_csv = ['user.csv', 'monster.csv', 'item_inventory.csv','monster_inventory.csv', 'item_shop.csv', 'monster_shop.csv']

    # Jika terdapat nama folder
    if os.path.exists(folder_path): 

        # Cek apakah ada file csv yang hilang
        missing_file = False
        for i in range(len(file_csv)):
            if os.path.exists(os.path.join(folder_path, file_csv[i])) == False:
                missing_file = True

        if missing_file:
            print('\nTerdapat file csv yang hilang. Harap periksa kembali file csv pada folder Anda!')
        else:
            print('\nLoading...')
            sleep(1)

            # Load data CSV
            dataUser = read_csv('user.csv', folder_path)
            dataMonster = read_csv('monster.csv', folder_path)
            dataMonsterInventory = read_csv('monster_inventory.csv', folder_path)
            dataItemInventory = read_csv('item_inventory.csv', folder_path)
            dataItemShop = read_csv('item_shop.csv', folder_path)
            dataMonsterShop = read_csv('monster_shop.csv', folder_path)

            print('\nSelamat datang di program OWCA!\n')
            return dataUser, dataMonster, dataMonsterInventory, dataItemInventory, dataMonsterShop, dataItemShop

    else:  # Jika nama folder tidak ditemukan
        print(f'\nFolder "{folder}" tidak ditemukan.\n')
        sys.exit()

# F14 - LOAD
def main_load():
    parser = argparse.ArgumentParser(description='Load Data Program OWCA. Format: python main.py <nama_folder>.')
    parser.add_argument('folder', nargs='?', help='Nama folder tempat penyimpanan data program')
    args = parser.parse_args()

    if not args.folder:  
        print('\nTidak ada nama folder yang diberikan!')
        print('Usage : python main.py <nama_folder>\n')
        sys.exit(1)
    else:
        return load_data(args.folder)