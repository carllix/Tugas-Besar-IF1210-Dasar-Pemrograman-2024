import os
from time import sleep

def writeCSV(folder_path, csv_file, array_data):
    with open(folder_path + "/" + csv_file, "w", newline="") as file:
        for i in range(len(array_data)):
            line = ""
            for j in range(len(array_data[i])):
                line += str(array_data[i][j])
                if j < len(array_data[i])-1:
                    line += ";"
                else:
                    line += "\n"
            file.write(line)

# F15 - SAVE
def save(dataUser, dataMonster, dataMonsterInventory, dataItemInventory, dataMonsterShop, dataItemShop):
    folder_name = input("\nMasukkan nama folder : ")
    data_directory = os.path.dirname(__file__) + "/../data/"
    folder_path = data_directory + f"/{folder_name}"
    if os.path.exists(data_directory):
        if os.path.exists(folder_path):
            print(f"Folder data/{folder_name} sudah ada.")
            sleep(1)
            print('\nSaving...\n')
            sleep(1)

            # Convert data to CSV file
            writeCSV(folder_path, "user.csv", dataUser)
            writeCSV(folder_path, "monster.csv", dataMonster)
            writeCSV(folder_path, "monster_inventory.csv", dataMonsterInventory)
            writeCSV(folder_path, "item_inventory.csv", dataItemInventory)
            writeCSV(folder_path, "monster_shop.csv", dataMonsterShop)
            writeCSV(folder_path, "item_shop.csv", dataItemShop)
            print(f"Berhasil menyimpan data di folder data/{folder_name}!\n")

        else:  
            os.makedirs(folder_path)
            print('\nSaving...\n')
            sleep(1)
            print(f"Membuat folder data/{folder_name}...")
            
            # Convert data to CSV file
            writeCSV(folder_path, "user.csv", dataUser)
            writeCSV(folder_path, "monster.csv", dataMonster)
            writeCSV(folder_path, "monster_inventory.csv", dataMonsterInventory)
            writeCSV(folder_path, "item_inventory.csv", dataItemInventory)
            writeCSV(folder_path, "monster_shop.csv", dataMonsterShop)
            writeCSV(folder_path, "item_shop.csv", dataItemShop)
            print(f"Berhasil menyimpan data di folder data/{folder_name}!\n")

    else:
        print("Folder data tidak ditemukan.")
        print('\nSaving...\n')
        sleep(1)
        print(f"Membuat folder data/...")
        sleep(1)
        os.makedirs(data_directory)
        print(f"Membuat folder data/{folder_name}...")
        sleep(1)
        os.makedirs(folder_path)

        # Convert data to CSV file
        writeCSV(folder_path, "user.csv", dataUser)
        writeCSV(folder_path, "monster.csv", dataMonster)
        writeCSV(folder_path, "monster_inventory.csv", dataMonsterInventory)
        writeCSV(folder_path, "item_inventory.csv", dataItemInventory)
        writeCSV(folder_path, "monster_shop.csv", dataMonsterShop)
        writeCSV(folder_path, "item_shop.csv", dataItemShop)
        print(f"Berhasil menyimpan data di folder data/{folder_name}!\n")