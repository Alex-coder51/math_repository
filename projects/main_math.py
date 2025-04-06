from art import text2art
import time
import os

os.system('cls')

def salutare():
    ascii_art = text2art('Math')
    print(ascii_art)
    print('Developed by Alexandru')
    time.sleep(2)
    os.system('cls')
    print()
    print('hello i am a programm what calculates some theorems')
salutare()

time.sleep(3)

while True:
    os.system('cls')
    print('choose a theorem')
    print()
    lsit = [
        '---pythagora--- (pythagorean theorem)',
        '---cathet--- (theorem of leg)',
        '---height--- (theorem of height )',
        '---math--- (simple and advanced math operations)',
    ]
    time.sleep(1)
    print('commands:')
    print('_____________________________________________________________________________________________')
    for item in lsit:
        print(item)
        print('_____________________________________________________________________________________________')
    print()
    inpo = input('choose a theorem: ')

    if inpo == 'pythagora':
        os.system('cls')
        time.sleep(2)    
        art = text2art('pythagorean   theorem')
        print(art)
        time.sleep(2)
        os.system('cls')

        while True:
            print('what do you want to find out? ')
            time.sleep(1)
            print('cathet or hypotenuse')
            print('if you want to break, write "ctrl + C" ')
            inp = input('> ')

            if inp == 'hypotenuse':
                while True:
                    print('')
                    catet1 = input('cathet_1 (cm): ')
                    catet2 = input('cathet_2 (cm): ')
                    try:
                        catet1 = int(catet1)
                        catet2 = int(catet2)
                    except:
                        print('Error')
                        time.sleep(1)
                        os.system('cls')
                    else:
                        break

                def ipotenuza(x , y):
                    try:
                        x = abs(x)
                        y = abs(y)
                    except:
                        print('ErRor')
                    ipot = (x ** 2) + (y ** 2)
                    ipot = ipot ** 0.5
                    
                    return ipot
                
                rasp = ipotenuza(catet1, catet2)

                time.sleep(1)
                for i in range(3):
                    time.sleep(0.5)
                    print('\r', 'loading.' + '.' * i, end='')

                time.sleep(1)
                print('\r', 'answ: ', round(rasp, 4))

            elif inp == 'cathet':
                
                while True:
                    print()
                    ipotenuz = input('hypotenuse (cm): ')
                    catet3 = input('cathet (cm): ')
                    try:
                        ipotenuz = int(ipotenuz)
                        catet3 = int(catet3)
                    except:    
                        print('ErRor')
                    else:
                        ipotenuz = abs(ipotenuz)
                        catet3 = abs(catet3)
                        
                    if ipotenuz > catet3:
                        break
                    if ipotenuz < catet3:
                        print('hypotenuse cannot be shorter than cathet')
                
                def catet(catet3, ipotenuz):

                    cateta = (ipotenuz ** 2) - (catet3 ** 2)
                    cateta = cateta ** 0.5

                    return cateta
                
                rasp = catet(catet3, ipotenuz)

                time.sleep(1)
                for i in range(3):
                    time.sleep(0.5)
                    print('\r', 'loading.' + '.' * i, end='')

                time.sleep(1)
                print('\r', 'answ: ', round(rasp, 4) )

            elif inp == 'break':
                break

            else:
                time.sleep(1)
                print('ErRor, choose "cathet" or "hypotenuse" ')

            print()
            time.sleep(2)
            print('again? ')
            inpu = input()
            if inpu == 'nu':
                print('\r')
                break

            os.system('cls')
            print()

    elif inpo == 'cathet':
        os.system('cls')
        time.sleep(2)
        artt = text2art('Theoreme   of   cathet')
        print(artt)
        time.sleep(2)
        os.system('cls')

        while True:
            time.sleep(1)
            print('in caz de intrerupere, scrieti "ctrl + C" ')
            print()
            time.sleep(1)
            
            while True:
                inp_1 = input('lungimea primei parti ale ipoteunzei: ')
                inp_2 = input('lungimea totala a ipotenuzei (daca nu stiti scrieti nu): ')
                
                try:
                    inp_1 = int(inp_1)
                    inp_2 = int(inp_2)
                    break
                
                except:
                    if inp_2 == 'nu':
                        while True:
                            ipot_total = input('scrieti a doua parte a ipotenuzei (scrieti "nu" daca nu stiti): ')
                
                            try:
                                ipot_total = int(ipot_total) #int(ipot_total)
                                ipot_total = abs(ipot_total) #abs(ipot_total)
                                break

                            except :
                                if ipot_total == 'nu':
                                    time.sleep(1)
                                    print('cu pareri de rau nu pot ajuta nimic')
                                    break
                                else:
                                    print('err scrieti type(int) sau "nu" daca nu stiti lungimea ipotenuzei')

                        
                        def calcul(ipot_total, inp_1):
                            
                            inp_1 = abs(inp_1) #inp_1 = abs

                            cateta = inp_1 * (ipot_total - inp_1)
                            cateta = cateta ** 0.5

                            return cateta
                        
                        rasp = calcul(ipot_total, inp_1)

                        time.sleep(1)
                        for i in range(3):
                            time.sleep(1)
                            print('\r','loading.' + '.' * i, end='')
                            time.sleep(1)
                        
                        time.sleep(1)
                        print('\r','raspunsul: ', round(rasp, 4))
                        
            def calc(inp_1, inp_2):

                inp_1 = abs(inp_1)
                inp_2 = abs(inp_2)
            
                cateta = inp_1 * inp_2
                cateta = cateta ** 0.5

                return cateta 
            
            rasp = calc(inp_1, inp_2)

            time.sleep(1)
            for i in range(3):
                time.sleep(1)
                print('\r','loading.' + '.' * i, end='')
                time.sleep(1)
                        
            time.sleep(1)
            print('\r','raspunsul: ', round(rasp, 4))
            time.sleep(4)
                                   
            
            inppp = input('again? ')
            if inppp == 'no':
                break
    
    elif inpo == 'height':
        os.system('cls')
        time.sleep(2)
        artt = text2art('Theoreme   of   height')
        print(artt)
        time.sleep(2)
        os.system('cls')

        while True:
            time.sleep(1)
            print('if you want to break, write "ctrl + C" ')
            print()
            time.sleep(1)
            
            while True:
                inp_1 = input('1 part of hypotenuse: ')
                inp_2 = input('2 part of hypotenuse (if you do not know, write nu): ')
                
                try:
                    inp_1 = int(inp_1)
                    inp_2 = int(inp_2)
                    break
                
                except:
                    if inp_2 == 'no':
                        while True:
                            ipot_total = input('write lenght of hypotenuse (write "no" if you do not know): ')
                
                            try:
                                ipot_total = int(ipot_total) #int(ipot_total)
                                ipot_total = abs(ipot_total) #abs(ipot_total)
                                break

                            except :
                                if ipot_total == 'nu':
                                    time.sleep(1)
                                    print('I have no idea how to help you :(')
                                    break
                                else:
                                    print('err write type(int) or"no" if you do not know the lenght of hypotenuse')

                        
                        def calcul(ipot_total, inp_1):
                            
                            inp_1 = abs(inp_1) #inp_1 = abs

                            cateta = inp_1 * (ipot_total - inp_1)
                            cateta = cateta ** 0.5

                            return cateta
                        
                        rasp = calcul(ipot_total, inp_1)

                        time.sleep(1)
                        for i in range(3):
                            time.sleep(1)
                            print('\r','loading.' + '.' * i, end='')
                            time.sleep(1)
                        
                        print()
                        time.sleep(1)
                        print('\r','answ: ', round(rasp, 4) )
                        
            def calc(inp_1, inp_2):

                inp_1 = abs(inp_1)
                inp_2 = abs(inp_2)
            
                cateta = inp_1 * inp_2
                cateta = cateta ** 0.5

                return cateta 
            
            rasp = calc(inp_1, inp_2)

            time.sleep(1)
            for i in range(3):
                time.sleep(1)
                print('\r','loading.' + '.' * i, end='')
                time.sleep(1)
                        
            print()
            time.sleep(1)
            print('\r','answ: ', round(rasp, 4))
            time.sleep(4)
                                   
            
            inppp = input('again? ')
            if inppp == 'no':
                break

    elif inpo == 'math':
        os.system('cls')
        time.sleep(2)
        art = text2art('math  operations')
        print(art)
        time.sleep(2)
        os.system('cls')
        from calc import run as run_calc






