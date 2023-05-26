#schedule for timing
import TEST1
def timing_schu(Fun,FTime):

    import time
    c=Fun
#saving time when run APP
    NOW=time.time()
# check time
    perTime=NOW+FTime
    
    secTime=time.time()
    while True: 
        secTime=time.time()

        
        if secTime>perTime:
            print(secTime)
            print(perTime)
            c
            NOW=time.time()
            break
        else:
            pass
     
b=TEST1.a()
    
timing_schu(b,20)