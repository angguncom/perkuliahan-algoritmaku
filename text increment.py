import time



i = 0 # variabel increment / starting
j = 23
while i<5:
    print(j)
    if i%2 == 1:
        j-=7
    else:
        j+=3

        
    i+=1
    time.sleep(0.5)
