from src.F08_Battle import *
from src.Important_Function import *

# F09 - ARENA
def arena(userId:int,username:str,dataMonster:list,dataMonsterInventory:list,dataItemInventory:list,coin:int) -> int:
    print('\n===========================================================================================================')
    print('''
                                ─█▀▀█ ░█▀▀█ ░█▀▀▀ ░█▄─░█ ─█▀▀█ 
                                ░█▄▄█ ░█▄▄▀ ░█▀▀▀ ░█░█░█ ░█▄▄█ 
                                ░█─░█ ░█─░█ ░█▄▄▄ ░█──▀█ ░█─░█''')
    print('\n===========================================================================================================')

    # Menampilkan Monster Agent
    print('\nSelamat Datang di Arena!!')
    allMonsterAgent = getMonsterAgent(dataMonsterInventory,dataMonster,userId)
    displayMonsterAgent(allMonsterAgent)

    # Validasi Pilihan Monster Agent
    while True:
        choiceMonster = input('\nPilih monster untuk bertarung: ')
        if isNum(choiceMonster) == False:
            print('Pilihan tidak valid!')
        else:
            if 1<=int(choiceMonster)<=len(allMonsterAgent):
                break
            else:
                print('Pilihan nomor tidak tersedia!')
    
    # Mengambil Data Monster Agent
    monsterAgent = allMonsterAgent[int(choiceMonster)-1]
    nameMonsterAgent = monsterAgent[0]
    atkPowerMonsterAgent = int(monsterAgent[1])
    defPowerMonsterAgent = int(monsterAgent[2])
    hpMonsterAgent = int(monsterAgent[3])
    levelMonsterAgent = int(monsterAgent[4])

    allPotionAgent = getPotionAgent(dataItemInventory,userId)

    # Menyesuaikan Atributte Monster Agent Berdasarkan Level
    atkPowerMonsterAgent,defPowerMonsterAgent,hpMonsterAgent = attributeByLevel(levelMonsterAgent,atkPowerMonsterAgent,defPowerMonsterAgent,hpMonsterAgent)
    currentHpMonsterAgent = hpMonsterAgent

    # Menampilkan Status Monster Agent
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣧⡀⠀⠀⠀⣀⣤⣶⣶⣦⣀⡴⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢶⣦⣿⣿⣿⣶⠲⠟⣿⡿⠟⢋⠉⣿⣾⣿⣅⣤⣶⠛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣷⣤⣾⢿⣰⣦⣼⣿⣿⣿⣿⣧⠞⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠟⣻⣏⣉⣠⣿⣾⡟⣿⡏⢻⣭⣿⠋⠁⠀⠀⢀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⡾⣴⣏⣻⣿⣟⡿⢿⣿⣿⡷⣿⣿⣿⣶⠚⣉⠙⣿⡍⠻⣷⡄⠀
⠀⠀⠀⣠⠶⣯⠉⠻⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⢹⣧⠼⢿⣤⣾⣧⠀⡏⢹⠀
⠀⣠⣾⢁⣼⡇⠀⠀⣿⣿⣿⣿⣿⡆⠈⢰⣤⣈⠇⡏⣠⢰⣾⣿⣿⣿⣿⡿⢿⡄
⢸⣿⣿⣬⣿⠀⠀⠀⠿⠟⠛⠻⠯⣿⣟⣌⣯⠏⠀⢹⡿⠏⠙⠀⠙⢺⣷⣤⣿⡇
⠀⢯⠹⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⢀⣿⢙⡗⠒⠶⠶⠿⠟⠋⠉⠀
⠀⠈⠳⠿⠛⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠉⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠄⠈⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣷⠦⠤⠤⣄⣀⣀⣠⣴⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣸⠿⡄⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⣴⣾⡿⠖⠒⠒⠒⢶⣏⢙⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠙⢷⣿⣿⡿⠶⠂⠀⠀⠀⠀⠀⠀⠀⠀''')
    print(f'\nRAWRRR, Agent {username} mengeluarkan Monster {nameMonsterAgent} !!!\n')
    statusMonster(nameMonsterAgent,atkPowerMonsterAgent,defPowerMonsterAgent,currentHpMonsterAgent,levelMonsterAgent)

    # STAGE
    levelEnemy = 0
    reward = [50,100,150,200,300]
    stage = 0
    sumCoin = 0
    damageDealt = 0
    damageReceived = 0

    while stage<5:
        # Mengambil Data Monster Enemy
        enemy = dataMonster[getRandomNumber([1,len(dataMonster)])]
        nameEnemy = enemy[1]
        atkPowerEnemy = int(enemy[2])
        defPowerEnemy = int(enemy[3])
        hpEnemy = int(enemy[4])
        levelEnemy+=1

        # Menyesuaikan Atributte Monster Enemy Berdasarkan Level
        atkPowerEnemy,defPowerEnemy,hpEnemy = attributeByLevel(levelEnemy,atkPowerEnemy,defPowerEnemy,hpEnemy)
        currentHpEnemy = hpEnemy
        
        # Menampilkan Status Monster Enemy
        print(f'\n============= STAGE {stage+1} =============')
        print('''
⠀⢠⠤⢲⢯⢫⡉⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣴⡊⣟⠆
⠀⠀⡸⣘⡲⢾⡡⠂⠀⡠⠔⠒⠒⠢⡄⠀⠀⠀⠀⣐⡨⠯⠗⣩⡶
⠀⣨⣀⠔⠘⠖⡘⠀⠘⠀⠀⣶⡆⠀⠈⣆⠀⠀⢈⠐⠞⢲⠂⢱⠀
⢠⡟⠄⠁⡒⠈⢀⠔⠙⣄⠀⠀⠀⠀⡰⠁⠈⢂⠀⠓⡤⠔⠈⣵⠂
⠘⡁⠀⠀⠻⡄⡜⢨⣄⡀⠉⠲⠮⠉⢀⣠⣤⡙⠄⡤⠃⠀⠀⠜⡆
⠀⠣⠀⠀⠀⠹⡀⠸⣿⢾⡗⢢⣤⣶⠿⣾⠝⠀⡘⠁⠀⠀⠀⡔⠀
⠀⠀⠳⡀⠀⠀⠹⣄⠀⠉⠉⠙⠋⠈⠉⠀⣄⡴⠁⠀⠀⢀⡜⠁⠀
⠀⠀⠀⠉⢄⠀⠀⠉⠑⠤⣄⣀⢀⣤⣠⠺⠃⠀⠀⠀⡔⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠡⡀⠠⣄⢀⠀⠈⠉⠡⠁⠀⣠⠜⠀⠸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⠓⠀⠁⠙⠑⠄⣠⡤⠺⠊⠋⠀⠀⢣⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⡀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡀⠀⡘⢦⠀⡍⠁⠒⠒⠒⠂⢉⡁⠀⡠⠁⠀⠀⠀⠀⠀
⠀⠀⠀⣗⣈⣭⢞⢷⣷⠚⡄⠀⠀⠀⠠⣿⣳⢭⣏⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠳⠬⢤⣁⣭⠛⢾⠀⠀⠀⠀⠈⡕⠯⠄⠀⣴⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀''')
        print(f'\nRAWRRR, Monster {nameEnemy} telah muncul !!!\n')
        statusMonster(nameEnemy,atkPowerEnemy,defPowerEnemy,currentHpEnemy,levelEnemy)

        # Battle Mechanism
        turn = 1
        countStrength = 0
        countResilience = 0
        countHealing = 0
        isWin = True
        
        while isWin == True or stage <= 5:
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
                currentHpEnemy = attack(nameMonsterAgent,atkPowerMonsterAgent,nameEnemy,defPowerEnemy,atkPowerEnemy,currentHpEnemy,levelEnemy)

                if currentHpEnemy == 0:
                    print(f'\nSelamat, Anda berhasil mengalahkan monster {nameEnemy} !!!')
                    rewardCoin = reward[stage]
                    sumCoin+= rewardCoin
                    print(f'\nSTAGE CLEARED! Anda akan mendapatkan {rewardCoin} pada sesi ini!')
                    isWin = True

                    # Jika Berhasil Menyelsaikan Seluruh Stage
                    if stage == 4:
                        print('\nSelamat, Anda berhasil menyelesaikan seluruh stage Arena !!!')
                    break
                else:
                    # Enemy Turn
                    print(f'\n============ TURN {turn} ({nameEnemy}) ============')
                    currentHpMonsterAgent = attack(nameEnemy,atkPowerEnemy,nameMonsterAgent,defPowerMonsterAgent,atkPowerMonsterAgent,currentHpMonsterAgent,levelMonsterAgent)
                    if currentHpMonsterAgent == 0:
                        print(f'\nYahhh, Anda dikalahkan monster {nameEnemy}. Jangan menyerah, coba lagi !!!')
                        print(f'\nGAME OVER! Sesi latihan berakhir pada stage {stage+1}!')
                        isWin = False
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
                print('\nGAME OVER! Anda mengakhiri sesi latihan!!')
                isWin = False
                break

        # Kondisi Kememnangan Pada Stage
        if isWin == False or stage==4:
            damageDealt += hpEnemy-currentHpEnemy
            damageReceived += hpMonsterAgent-currentHpMonsterAgent

            if stage==4:
                stage+=1

            # Menampilkan Stat
            print('\n============== STATS ==============')
            print(f'Total hadiah      : {sumCoin} OC')
            print(f'Jumlah stage      : {stage}')
            print(f'Damage diberikan  : {damageDealt}')
            print(f'Damage diterima   : {damageReceived}')
            coin += sumCoin
            break
        else:
            damageDealt += hpEnemy-currentHpEnemy
            damageReceived += hpMonsterAgent-currentHpMonsterAgent
            print('\n\nMemulai stage berikutnya...')

            # Memulihkan attribute monster agent
            monsterAgent = allMonsterAgent[int(choiceMonster)-1]
            nameMonsterAgent = monsterAgent[0]
            atkPowerMonsterAgent = int(monsterAgent[1])
            defPowerMonsterAgent = int(monsterAgent[2])
            hpMonsterAgent = int(monsterAgent[3])
            levelMonsterAgent = int(monsterAgent[4])

            # Menyesuaikan Atributte Monster Agent Berdasarkan Level
            atkPowerMonsterAgent,defPowerMonsterAgent,hpMonsterAgent = attributeByLevel(levelMonsterAgent,atkPowerMonsterAgent,defPowerMonsterAgent,hpMonsterAgent)
            currentHpMonsterAgent = hpMonsterAgent

            # Menampilkan Status Monster Agent
            print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣧⡀⠀⠀⠀⣀⣤⣶⣶⣦⣀⡴⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢶⣦⣿⣿⣿⣶⠲⠟⣿⡿⠟⢋⠉⣿⣾⣿⣅⣤⣶⠛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣷⣤⣾⢿⣰⣦⣼⣿⣿⣿⣿⣧⠞⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠟⣻⣏⣉⣠⣿⣾⡟⣿⡏⢻⣭⣿⠋⠁⠀⠀⢀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⡾⣴⣏⣻⣿⣟⡿⢿⣿⣿⡷⣿⣿⣿⣶⠚⣉⠙⣿⡍⠻⣷⡄⠀
⠀⠀⠀⣠⠶⣯⠉⠻⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⢹⣧⠼⢿⣤⣾⣧⠀⡏⢹⠀
⠀⣠⣾⢁⣼⡇⠀⠀⣿⣿⣿⣿⣿⡆⠈⢰⣤⣈⠇⡏⣠⢰⣾⣿⣿⣿⣿⡿⢿⡄
⢸⣿⣿⣬⣿⠀⠀⠀⠿⠟⠛⠻⠯⣿⣟⣌⣯⠏⠀⢹⡿⠏⠙⠀⠙⢺⣷⣤⣿⡇
⠀⢯⠹⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⢀⣿⢙⡗⠒⠶⠶⠿⠟⠋⠉⠀
⠀⠈⠳⠿⠛⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠉⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠄⠈⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣷⠦⠤⠤⣄⣀⣀⣠⣴⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣸⠿⡄⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⣴⣾⡿⠖⠒⠒⠒⢶⣏⢙⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠙⢷⣿⣿⡿⠶⠂⠀⠀⠀⠀⠀⠀⠀⠀''')
            statusMonster(nameMonsterAgent,atkPowerMonsterAgent,defPowerMonsterAgent,currentHpMonsterAgent,levelMonsterAgent)

            stage += 1

     # Merubah kuantitas potion pada data item inventory
    for item in dataItemInventory:
        for potion in allPotionAgent:
            if item[0] == str(userId) and item[1] == potion[0]:
                item[2] = potion[1]
                
    return coin