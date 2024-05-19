import math
from src.F00_RNG import *
from src.Important_Function import *

def attributeByLevel(level:int,atkPower:int,defPower:int,hp:int):
    if level != 1:
        atkPower += math.floor(((level-1)*10/100) * atkPower) 
        defPower += math.floor(((level-1)*10/100) * defPower) 
        hp += math.floor(((level-1)*10/100) * hp) 
        return atkPower,defPower,hp
    return atkPower,defPower,hp
        
         
# Menampilkan status monster enemy
def statusMonster(name:str,atkPower:int,defPower:int,hp:int,level:int):
    print(f'Name      : {name}')
    print(f'ATK Power : {atkPower}')
    print(f'DEF Power : {defPower}')
    print(f'HP        : {hp}')
    print(f'Level     : {level}')

def getMonsterAgent(dataMonsterInventory:list,dataMonster:list,userId:int) -> list:
    allMonsterAgent:list = []
    for monster in dataMonsterInventory:
        if monster[0] == str(userId):
            monsterId:str = monster[1]
            level:str = monster[2]
            infoMonster:list = getDataById(monsterId,dataMonster)
            name:str = infoMonster[1]
            atkPower:str = infoMonster[2]
            defPower:str = infoMonster[3]
            hp:str = infoMonster[4]
            allMonsterAgent.append([name,atkPower,defPower,hp,level])
    return allMonsterAgent

def displayMonsterAgent(allMonsterAgent:list):
    print('\n============ MONSTER LIST ============')
    x = 1
    for monster in allMonsterAgent:
        print(f'{x}. {monster[0]}')
        x+=1

def getPotionAgent(dataItemInventory:list,userId:int) -> list:
    allPotionAgent:list = []
    for item in dataItemInventory:
        if item[0] == str(userId) and item[1] != 'monster_ball':
            name:str = item[1]
            quantity:int = int(item[2])
            allPotionAgent.append([name,quantity])
    return allPotionAgent

def displayPotionAgent(allPotionAgent:list):
    if not allPotionAgent:
        print('\nAnda tidak memiliki Potion dalam inventory!')
    else:
        # Menampilkan Potion dalam Inventory
        print('\n==================== POTION LIST ====================')
        x = 1

        for potion in allPotionAgent:
            if potion[0] == 'strength':
                utility:str = 'Increases ATK Power'
            elif potion[0] == 'resilience':
                utility:str = 'Increases DEF Power'
            else:
                utility:str = 'Restores Health'

            print(f'{x}. {potion[0].capitalize()} Potion (Qty: {potion[1]}) - {utility}')
            x+=1

        print(f'{x}. Cancel')

def attack(name:str,atkPower:int,nameRival:str,defPowerRival:int,atkPowerRival:int,hpRival:int,levelRival:int)->int:
    print(f'\nSHEESHHHHH, {name} menyerang {nameRival} !!!\n')

    # Menghitung Att Result
    att:int = getRandomNumber([0.7*atkPower,1.3*atkPower])
    attPercent:float = (att-atkPower)/atkPower*100
    reducedBy:float = defPowerRival/100 * att
    attResult:float = att-reducedBy
    hpRival:int = math.floor(hpRival-attResult)

    # Kondisi HP < 0
    if hpRival<0:
        hpRival:int = 0
    # Menampilkan Status Monster Enemy Setelah Diserang
    statusMonster(nameRival,atkPowerRival,defPowerRival,hpRival,levelRival)
    print('------------------------------------------------------------------------------')
    print(f'Penjelasan: ATT: {att} ({attPercent:.2f}%), Reduced By: {reducedBy:.2f} ({defPowerRival}%), ATT Results: {attResult:.2f}')
    return hpRival


# FO8 - BATTLE
def battle(userId:int,username:str,dataMonster:list,dataMonsterInventory:list,dataItemInventory:list,coin:int) -> int:
    allPotionAgent = getPotionAgent(dataItemInventory,userId)

    # Mengambil Data Monster Enemy
    enemy:list = dataMonster[getRandomNumber([1,len(dataMonster)])]
    nameEnemy:str = enemy[1]
    atkPowerEnemy:int = int(enemy[2])
    defPowerEnemy:int = int(enemy[3])
    hpEnemy:int = int(enemy[4])
    levelEnemy:int = getRandomNumber([1,5])

    # Menyesuaikan Atributte Monster Enemy Berdasarkan Level
    atkPowerEnemy,defPowerEnemy,hpEnemy = attributeByLevel(levelEnemy,atkPowerEnemy,defPowerEnemy,hpEnemy)

    print('\n===========================================================================================================')
    print('''
                                ░█▀▀█ ─█▀▀█ ▀▀█▀▀ ▀▀█▀▀ ░█─── ░█▀▀▀ 
                                ░█▀▀▄ ░█▄▄█ ─░█── ─░█── ░█─── ░█▀▀▀ 
                                ░█▄▄█ ░█─░█ ─░█── ─░█── ░█▄▄█ ░█▄▄▄''')
    print('\n===========================================================================================================')

    # Menampilkan Status Monster Enemy
    print('''
⠀⠀⠀⢠⣾⣿⣦⣤⣭⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⠏⠀⢹⣻⣭⣭⡧⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⠏⠀⠴⠚⣷⣿⣿⠀⠀⢀⡤⠖⠛⠹⠶⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡏⠀⠀⠀⡼⠉⠉⠁⢀⡴⠋⠀⠀⠤⢄⡀⠀⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡇⠀⠀⠀⢧⡀⠀⢠⠎⠀⢠⣤⡞⠒⠲⡌⠃⠀⠀⠀⠱⢤⡀⠀⢀⣀⣀⣀⠀⠀
⠀⣧⠀⠀⠀⠀⠙⠲⠏⠀⢀⡀⠙⣇⠀⠀⢘⡶⠆⣤⠤⠔⢲⣯⡖⠉⠀⠀⠈⢧⠀
⠀⢺⣦⡀⠀⠂⠀⠀⠀⠀⠀⢠⣄⠼⣗⠒⠋⠀⠀⠹⣄⣠⣿⡋⡀⢠⣤⡆⠀⢸⠀
⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠈⠦⣠⠴⣄⢀⣠⣄⣸⠇⠀⣳⣿⣧⠈⢹⠁
⠀⠀⠀⠘⠶⡆⠀⠆⢶⣴⠀⢾⠀⠀⠀⠀⠀⠀⠈⠉⡼⡭⣭⡴⠖⠼⠛⣿⣿⠏⠀
⠀⠀⠀⠀⠀⢻⠀⠀⠀⠁⠀⠘⡄⠀⣠⢤⣀⡤⡄⢸⣿⣿⠋⠀⠀⠀⠀⠙⠁⠀⠀
⠀⠀⠀⠀⠀⣏⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠘⠛⢱⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⠁⠀⠀⠸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠃⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⡆⠀⠀⠀⣷⣄⢠⡀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠃⠀⡄⠀⠀⠺⠾⠃⠀⠀⠀⠀⠾⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣀⡴⠋⠀⠛⠁⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⢀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠁⠀⠀⠀⠀⣤⡄⠀⠀⠀⡴⠛⠲⡄⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⣀⠀⠘⠀⠀⣠⠞⠁⠀⠀⢣⠀⠀⠀⠀⠠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⠒⠒⠶⠁⠉⠉⠉⠉⠁⠀⠀⠀⠀⡞⠀⠀⠰⠇⠐⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣼⠁⠀⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠷⠤⠤⠤⠤⠿⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
    print(f'\nRAWRRR, Monster {nameEnemy} telah muncul !!!\n')
    statusMonster(nameEnemy,atkPowerEnemy,defPowerEnemy,hpEnemy,levelEnemy)

    # Menampilkan Monster Agent
    allMonsterAgent:list = getMonsterAgent(dataMonsterInventory,dataMonster,userId)
    displayMonsterAgent(allMonsterAgent)

    # Validasi Pilihan Monster Agent
    while True:
        choiceMonster:str = input('\nPilih monster untuk bertarung: ')
        if isNum(choiceMonster) == False:
            print('Pilihan tidak valid!')
        else:
            if 1<=int(choiceMonster)<=len(allMonsterAgent):
                break
            else:
                print('Pilihan nomor tidak tersedia!')
    
    # Mengambil Data Monster Agent
    monsterAgent:list = allMonsterAgent[int(choiceMonster)-1]
    nameMonsterAgent:str = monsterAgent[0]
    atkPowerMonsterAgent:int = int(monsterAgent[1])
    defPowerMonsterAgent:int = int(monsterAgent[2])
    hpMonsterAgent:int = int(monsterAgent[3])
    levelMonsterAgent:int = int(monsterAgent[4])

    # Menyesuaikan Atributte Monster Agent Berdasarkan Level
    atkPowerMonsterAgent,defPowerMonsterAgent,hpMonsterAgent = attributeByLevel(levelMonsterAgent,atkPowerMonsterAgent,defPowerMonsterAgent,hpMonsterAgent)

    # Menampilkan Status Monster Agent
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⠉⡙⠿⢟⣛⡷⠶⣤⣄⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⣱⣄⠀⠀⠈⠀⠀⠈⢉⣛⣶⣤⣀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⡇⠙⢷⠀⠀⠀⠀⣴⠟⠉⠀⠈⠁
⠀⠀⠀⠀⠀⣠⡴⠾⠋⠡⠰⣴⡏⠀⠀⠀⣠⣤⣤⣶⠞⠛⠿⣿⢿⠛⠛⠳⢶⣤⣀⠀⢀⣿⠀⠃⠀⠀⠳⣄⠀⢠⡇⠀⠀⠀⠀⠀
⠀⠀⢀⡴⠛⠉⠀⠀⠀⢀⠎⠀⣷⣄⣴⡏⣀⣼⣿⣿⡇⢀⠀⠈⣇⢳⠀⠀⠀⠀⠉⠳⣾⣯⠃⠀⠀⢀⣀⡈⢳⠀⣿⡀⠀⠀⠀⠀
⢀⣴⣫⠴⠒⠒⠒⠲⣤⡀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⡀⡟⠘⠆⠀⠀⠀⣀⣴⡿⠃⣠⡶⠛⠋⠉⠛⠛⢷⣼⣧⠀⠀⠀⠀
⠚⠋⠀⠀⠀⠀⠀⠀⣺⡴⠛⢶⣾⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⢣⠇⠀⠀⠀⢠⢿⡏⠉⠀⡰⢿⡆⠀⠀⠀⠀⠀⠀⠘⠛⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⠁⠀⢸⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢠⠟⠀⠀⠀⠀⠀⠘⠛⠉⣹⠇⠘⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠈⠉⠀⠀⠀⠀⠀⠄⣱⠏⣰⠇⠀⠀⠀⠀⠀⢠⣾⡏⠀⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢧⡀⠀⠀⠀⠂⢈⡤⢞⡡⠚⠁⠀⠀⠀⠀⠀⠀⢸⡿⠀⢰⣻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠙⠛⠲⠶⠒⠛⠉⠒⠉⢀⣀⣀⠀⣀⠀⠀⠀⠠⠟⠁⣠⢏⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠈⣶⣤⣄⣀⣰⣿⣿⣿⣿⣮⣣⡀⠀⠀⢠⢞⠏⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⣾⠿⠶⡼⠇⠀⠉⠛⢿⣿⣿⣿⣿⡿⡿⠗⠀⠀⠕⠋⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠀⠀⠀⠀⣀⣀⣀⠀⠙⢿⣿⣿⣷⠀⠀⠀⠀⠀⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠟⠉⠉⠉⠙⠻⣾⣿⣿⠏⠀⠀⢀⡄⠈⣹⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⢠⣤⣤⣀⣠⣾⠟⣉⠔⠂⠀⢼⠇⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣠⡾⠃⠘⢦⡀⠈⠙⠒⠈⠁⠀⠀⠀⠉⠀⣄⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⣿⠉⠀⠈⠉⠀⠀⠀⠀⠙⣦⡀⠀⠀⠀⠀⠀⠀⣀⠀⠈⢾⣷⡀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⢱⡀⠀⠀⠀⠀⠀⠀⠀⣀⡾⠉⠢⠀⣀⠴⠒⠉⠀⡀⠀⠀⠉⠙⠛⠛⠉⠉⠀⠈⠙⠲⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠖⠛⠉⠁⠀⠀⢀⡞⡁⠀⠀⠀⢸⣿⢳⢠⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠈⢳⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠉⠀⠀⡀⠤⠀⠂⠀⠀⣼⢰⠃⠀⢀⠀⣠⡥⠶⢧⣤⠤⠴⠒⠛⠉⠁⠀⠉⠻⣦⡀⢻⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⢠⠟⣿⠛⠛⠛⠛⠛⢻⣾⠀⠀⠸⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⣸⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡀⠸⠄⢿⡀⠀⠀⠀⠀⠈⢿⡀⠀⠙⠲⠿⠷⠶⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⢸⡅⣾⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⣄⣀⠙⠦⣄⠀⠀⠀⠀⠙⠦⣤⣤⣤⣤⣤⣄⡀⠙⢦⡀⠀⠀⠀⠀⢀⣼⠗⣸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⡆⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠟⠀⠀⢠⡇⠀⠀⠀⠀⠀⠙⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠚⣋⡼⠃⠀⠀⠀⠀⠀⠀⠀⢾⣁⣀⣀⣠⡴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
    print(f'\nRAWRRR, Agent {username} mengeluarkan Monster {nameMonsterAgent} !!!\n')
    statusMonster(nameMonsterAgent,atkPowerMonsterAgent,defPowerMonsterAgent,hpMonsterAgent,levelMonsterAgent)

    # Battle Mechanism
    turn:int = 1
    countStrength:int = 0
    countResilience:int = 0
    countHealing:int = 0

    while True:
        print(f'\n============ TURN {turn} ({nameMonsterAgent}) ============')
        print('1. Attack')
        print('2. Use Potion')
        print('3. Quit')

        # Validasi Action Turn
        while True:
            actionTurn = input('\nPilih perintah: ')
            if isNum(actionTurn) == False:
                print('Perintah tidak valid!')
            else:
                if actionTurn == '1' or actionTurn == '2' or actionTurn == '3':
                    break
                else:
                    print('Perintah tidak valid!')
        
        # Kondisi Pilihan Perintah
        if actionTurn == '1': 
            # Agent Turn
            hpEnemy:int = attack(nameMonsterAgent,atkPowerMonsterAgent,nameEnemy,defPowerEnemy,atkPowerEnemy,hpEnemy,levelEnemy)

            if hpEnemy == 0:
                print(f'\nSelamat, Anda berhasil mengalahkan monster {nameEnemy} !!!')
                rewardCoin:int = getRandomNumber([5,30])
                coin+= rewardCoin
                print(f'\nTotal OC yang diperoleh: {rewardCoin}')
                break
            else:
                # Enemy Turn
                print(f'\n============ TURN {turn} ({nameEnemy}) ============')
                hpMonsterAgent = attack(nameEnemy,atkPowerEnemy,nameMonsterAgent,defPowerMonsterAgent,atkPowerMonsterAgent,hpMonsterAgent,levelMonsterAgent)
                if hpMonsterAgent == 0:
                    print(f'\nYahhh, Anda dikalahkan monster {nameEnemy}. Jangan menyerah, coba lagi !!!')
                    break
            turn+=1
    
        elif actionTurn == '2':

            # Menampilkan Potion Agent
            displayPotionAgent(allPotionAgent)

            # Validasi Pilihan Potion
            while True:
                choicePotion = input('\nPilih perintah: ')
                if isNum(choicePotion) == False:
                    print('Perintah tidak valid!')
                else:
                    if 1<=int(choicePotion)<=len(allPotionAgent):
                        # Kasus ketika quantity potion 0
                        if allPotionAgent[int(choicePotion)-1][1] == 0:
                            print(f'Maaf {allPotionAgent[int(choicePotion)-1][0].capitalize()} Potion kamu telah habis, silahkan beli lagi di SHOP!')
                            break

                        # Menampilkan Efek dari Potion
                        if allPotionAgent[int(choicePotion)-1][0] == 'strength':
                            if countStrength == 1:
                                print(f'\nKamu mencoba memberikan ramuan ini kepada {nameMonsterAgent}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.')
                            else:
                                print(f'\nSetelah meminum ramuan ini, aura kekuatan terlihat mengelilingi {nameMonsterAgent} dan gerakannya menjadi lebih cepat dan mematikan.')
                                allPotionAgent[int(choicePotion)-1][1] -= 1
                                countStrength += 1
                                # Kenaikan ATK Power
                                atkPowerMonsterAgent += 0.05*atkPowerMonsterAgent
                        elif allPotionAgent[int(choicePotion)-1][0] == 'resilience':
                            if countResilience == 1:
                                print(f'\nKamu mencoba memberikan ramuan ini kepada {nameMonsterAgent}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.')
                            else:
                                print(f'\nSetelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar {nameMonsterAgent} yang membuatnya terlihat semakin tangguh dan sulit dilukai.')
                                allPotionAgent[int(choicePotion)-1][1] -= 1
                                countResilience+=1
                                # Kenaikan DEF Power
                                defPowerMonsterAgent += 0.05*defPowerMonsterAgent
                        else:
                            if countHealing == 1:
                                print(f'\nKamu mencoba memberikan ramuan ini kepada {nameMonsterAgent}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.')
                            else:
                                print(f'\nSetelah meminum ramuan ini, luka-luka yang ada di dalam tubuh {nameMonsterAgent} sembuh dengan cepat. Dalam sekejap, Pikachow terlihat kembali prima dan siap melanjutkan pertempuran.')
                                allPotionAgent[int(choicePotion)-1][1] -= 1
                                countHealing+=1
                                # Kenaikan HP
                                hpMonsterAgent += 0.25*hpMonsterAgent
                                # Kondisi Ketika HP Melebihi Maksimum
                                if hpMonsterAgent>monsterAgent[3]:
                                    hpMonsterAgent = monsterAgent[3]
                        break
                    elif int(choicePotion) == len(allPotionAgent)+1:
                        break
                    else:
                        print('Perintah tidak valid!')
            
        else:
            print('\nAnda berhasil kabur dari BATTLE!')
            break
    
    # Merubah kuantitas potion pada data item inventory
    for item in dataItemInventory:
        for potion in allPotionAgent:
            if item[0] == str(userId) and item[1] == potion[0]:
                item[2] = potion[1]

    return coin