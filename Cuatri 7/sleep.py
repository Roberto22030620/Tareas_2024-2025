import time, threading

def contar (x,y):
    i=1
    
    while (i<=x):
        print(f'Hilo: {y} conteo: {i}')
        i+=1
        
#"""        
h1=threading.Thread(target=contar, args=(10,1))
h2=threading.Thread(target=contar, args=(10,2))
h1.start()
#time.sleep(2)
h2.start()
#"""
#contar(10,1)
#contar(10,2)