from src.F15_Save import save
from time import sleep
import sys

# F16 - EXIT
def exit(dataUser:list, dataMonster:list, dataMonsterInventory:list, dataItemInventory:list, dataMonsterShop:list, dataItemShop:list):
    while True:
        response = input("\nApakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N): ").upper()
        if response == "Y":
            print("\nSaving...\n")
            sleep(1)
            save(dataUser, dataMonster, dataMonsterInventory, dataItemInventory, dataMonsterShop, dataItemShop)
            break
        elif response == "N":
            print("\nYahh progress kamu hilang, selamat tinggal :(\n")
            break
        else:
            print("\nInvalid input. Please enter Y or N.\n")
    sys.exit()