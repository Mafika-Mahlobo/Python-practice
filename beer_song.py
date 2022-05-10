name = "bottles"

for num_of_beers in range(99,0,-1):
    print(num_of_beers,name,"of beer on the wall.")
    print(num_of_beers,name,"of beer.")
    print("take one.")
    print("pass it around.")
    if num_of_beers == 1:
        print("no more bottles of beer on the wall.")
    else:
        new_num = num_of_beers - 1
        if new_num == 1:
            name = "bottle"
            print(new_num,name,"of beer on the wall.")
        print(new_num,name,"of beer on the wall.")
        print()
