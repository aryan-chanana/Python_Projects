def playgame():
    import time
    import random
    winner = ""
    arr4 = [" "," "," ",
        " "," "," ",
        " "," "," "]
    def columns():
        print('''1 | 2 | 3 
__|___|___
4 | 5 | 6
__|___|___
7 | 8 | 9''')
    def board():
        print(f'''{arr[0]} | {arr[1]} | {arr[2]} 
__|___|___
{arr[3]} | {arr[4]} | {arr[5]}
__|___|___
{arr[6]} | {arr[7]} | {arr[8]}''')

    arr3 = [1,2,3,
        4,5,6,
        7,8,9]
    l = len(arr3)-1

    while True:
        choice = input("Do you want to play game? (y/n): ")
        if choice == "Y" or choice == "y":
            for i in [3,2,1,'GO']:
                time.sleep(1)
                print(i)
            columns()
            arr = []
            for i in arr4:
                arr.append(i)
            arr2 = []
            for i in arr3:
                arr2.append(i)
            chance = 1
            while chance <= 5:
                pos = int(input("Enter Position:"))
                while pos not in arr2:
                    print("Sorry, the entered position is already occupied!!!")
                    pos = int(input("Enter Positon:"))
                arr[pos-1] = 'x'
                arr2.remove(pos)
                if arr[0] == arr[4] and arr[0] == 'x' and arr[0] == arr[8]:
                    winner = "yes"
                    break

                elif arr[0] == arr[1] and arr[0] == 'x' and arr[0] == arr[2]:
                    winner = "yes"
                    break

                elif arr[3] == arr[4] and arr[3] == 'x' and arr[3] == arr[5]:
                    winner = "yes"
                    break

                elif arr[6] == arr[7] and arr[6] == 'x' and arr[6] == arr[8]:
                    winner = "yes"
                    break

                elif arr[2] == arr[4] and arr[2] == 'x' and arr[2] == arr[6]:
                    winner = "yes"
                    break

                elif arr[0] == arr[3] and arr[0] == 'x' and arr[0] == arr[6]:
                    winner = "yes"
                    break

                elif arr[1] == arr[4] and arr[1] == 'x' and arr[1] == arr[7]:
                    winner = "yes"
                    break

                elif arr[2] == arr[5] and arr[2] == 'x' and arr[2] == arr[8]:
                    winner = "yes"
                    break
                if chance == 5:
                    break

                comp = random.choice(arr2)
                arr[comp-1] = 'o'
                arr2.remove(comp)
                chance += 1
                if arr[0] == arr[4] and arr[0] == 'o' and arr[0] == arr[8]:
                    winner = "no"
                    break

                elif arr[0] == arr[1] and arr[0] == 'o' and arr[0] == arr[2]:
                    winner = "no"
                    break

                elif arr[3] == arr[4] and arr[3] == 'o' and arr[3] == arr[5]:
                    winner = "no"
                    break

                elif arr[6] == arr[7] and arr[6] == 'o' and arr[6] == arr[8]:
                    winner = "no"
                    break

                elif arr[2] == arr[4] and arr[2] == 'o' and arr[2] == arr[6]:
                    winner = "no"
                    break

                elif arr[0] == arr[3] and arr[0] == 'o' and arr[0] == arr[6]:
                    winner = "no"
                    break

                elif arr[1] == arr[4] and arr[1] == 'o' and arr[1] == arr[7]:
                    winner = "no"
                    break

                elif arr[2] == arr[5] and arr[2] == 'o' and arr[2] == arr[8]:
                    winner = "no"
                    break 
                board()
            board()
            if winner == "yes":
                print("WIN")

            elif winner == "no":
                print("LOST")
            else:
                print("TIE")
        elif choice == "n" or choice == "N":
            print("Please visit again!")
            break
        else:
            print("Please enter a valid option!")

playgame()