import time
import os
import msvcrt
steps = 0


def cnc():
    global steps
    try:
        steps = int(input("How many steps: "))
        if steps == 0:
            print("Not Aplicable, Try Again")
            return(cnc())
        if steps % 2 == 0:
            return steps/2
        elif steps % 2 != 0:
            return (steps+1)/2
    except:
        print("Not   Aplicable, Try Again")
        return(cnc())


def main():
    # Man on running horizontal escalator
    t = int(cnc())
    print('Press any key to stop')
    time.sleep(0.4)

    for i in range(steps):
        time.sleep(0.2)
        os.system('cls')
        print((" "*i)+"   \N{grinning face with smiling eyes}   ")
        print((" "*i)+"=-( )-=")
        print((" "*i)+"  _U_  ")
        print("\">\">\">\""+">\""*(t), end='\r')
        print('\r')
        print('\r')
        print('\r')
        time.sleep(0.2)
        if msvcrt.kbhit():
            print("Stopping......")
            break
        os.system('cls')
        print(" "*(i+2)+"   \N{grinning face with smiling eyes}   ")
        print(" "*(i+2)+"=-( )-=")
        print(" "*(i+2)+"  _U_  ")
        print(">\">\">\">\""+">\""*(t), end='\r')
        print('\r')
        print('\r')
        print('\r')


main()
