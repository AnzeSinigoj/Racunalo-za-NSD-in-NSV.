import math, numpy, time

st1 = int(input("Napiši številko: "))
st2 = int(input("Napiši drugo številko: "))

def racunanje():
    gdc_oz_lcm = input("Napiši 1 za največji skupni delitelj ali pritisni 2 za najmanjši skupni večkratnik. (Ali 3 za izhod): ")

    if gdc_oz_lcm == "1":
        skupni_delitelj = math.gcd(st1,st2)
        print("Največji skupni deletielj števil", st1, "in", st2, "je: ", skupni_delitelj)
        racunanje()
    elif gdc_oz_lcm == "2":
        najmanjsi_veckratnik = numpy.lcm(st1,st2)
        print("Najmanjši skupni večkratnik števil", st1, "in", st2, "je: ", najmanjsi_veckratnik)
        racunanje()
    elif gdc_oz_lcm == "3":
        print("Izhod v 3 sekundah!")
        time.sleep(3)
        exit()
    else:
        while len(gdc_oz_lcm) == 0:
            print("Morate izbrati veljavno možnost.")
            racunanje()
       
    
racunanje()







