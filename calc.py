import time
import math

#simplu calculator adaptiv fara GUI pe care in dinsu poti faci calcule

while True:
    time.sleep(0.2)
    while True:
        a = input('first num = ')
        b = input('second num = ')
        try:
            a = int(a)
            b = int(b)
            break
        except:
            print('error write type(int)')
            
    time.sleep(0.2)
    list_of_operations = ['+' ,'-' , '*' ,'/', '^', '!', 'sqrt','lm']
    print (list_of_operations)
    print('NOTE: lm = liberty mode')
    time.sleep(1)
    c = input('write your symbol of operation: ')

#liberty mode:
    if c == 'lm':
        count = 0
        while True:
            print('answ:',eval(input()))
            count += 1
            if count >= 5:
                inp = input('again? :')
                if inp == 'no':
                    break

#adunarea
    elif c == '+' :
        def adunarea(x, y):
            time.sleep(0.5)
            time.sleep(1)
            for i in range(3):
                time.sleep(1)
                print('\r','loading.' + '.' * i, end='')
                time.sleep(1)            
            print ('answ :',x + y)
        adunarea(a, b)

#scaderea
    elif c == '-':
        def scaderea(x, y):
            time.sleep(0.05)
            time.sleep(1)
            for i in range(3):
                time.sleep(1)
                print('\r','loading.' + '.' * i, end='')
                time.sleep(1)            
            print ( 'answ :',x - y)
        scaderea(a, b)

#inmultirea
    elif c == '*':
        def inmultirea(x, y):
            time.sleep(0.05)
            time.sleep(1)
            for i in range(3):
                time.sleep(1)
                print('\r','loading.' + '.' * i, end='')
                time.sleep(1)
                        
            print ('answ :',x * y )
        inmultirea(a, b)

#impartirea
    elif c == '/':
        def impartirea(x, y):
            time.sleep(0.05)
            time.sleep(1)
            for i in range(3):
                time.sleep(1)
                print('\r','loading.' + '.' * i, end='')
                time.sleep(1)
                        
            print ('answ :',round(x / y, 4))
        impartirea(a, b)

#ridicarea la putere
    elif c == '^':
        def puterea(x, y):
            print(x, y)
            alege = int(input('write or choose your num for exponent: '))
            exp = int(input('exponent: '))
            time.sleep(1)
            for i in range(3):
                time.sleep(1)
                print('\r','loading.' + '.' * i, end='')
                time.sleep(1)
                        
            print('answ :',alege ** exp)
        puterea(a, b)

#factorial
    elif c == '!':
        def alegerea_fact(a, b):
            print(a, b)
            aleg = int(input('write or choose num: '))

            rasp = math.factorial(aleg)
            return rasp
        ras = alegerea_fact(a, b)
        time.sleep(1)
        for i in range(3):
            time.sleep(1)
            print('\r','loading.' + '.' * i, end='')
            time.sleep(1)
                        
        print('answ: ', ras)

#radicalul
    else: #daca user nu va scrie nimic sau va scrie altceva, se va pune operatie de radical
        def radicalul(x, y): #ca o exceptie sau daca user s-a incurcat cu simboluri.
            print(a, b)
            aleg = input('choose a number for sqrt: ')
            
            if aleg == x:
                def rad(x):
                    time.sleep(0.4)
                    time.sleep(1)
                    for i in range(3):
                        time.sleep(1)
                        print('\r','loading.' + '.' * i, end='')
                        time.sleep(1)
                        
                    print('answ:', x ** 0.5)
                rad(a, b)
            
            else:
                def rad_b(y):
                    time.sleep(0.4)
                    time.sleep(1)
                    for i in range(3):
                        time.sleep(1)
                        print('\r','loading.' + '.' * i, end='')
                        time.sleep(1)
                        
                    print('answ:', y ** 0.5)
                rad_b(b)
        radicalul(a, b)

#deciderea daca user doreste sa incepe de la inceput codul
    time.sleep(4.0)
    decision = input('restart?: ')
    
    if decision == 'no':
        break