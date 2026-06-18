def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num >= 1:
                return num
        except ValueError:
            pass


def sing(starting_bottles):
    bottles = starting_bottles

    while bottles > 0:

        bottle_word = "bottle" if bottles == 1 else "bottles"

        print(f"{bottles} {bottle_word} of beer on the wall, "
              f"{bottles} {bottle_word} of beer.")

        if bottles == 1:
            print("Take it down, pass it around, "
                  "no more bottles of beer on the wall!")
        else:
            next_bottles = bottles - 1
            next_word = "bottle" if next_bottles == 1 else "bottles"

            print(f"Take one down, pass it around, "
                  f"{next_bottles} {next_word} of beer on the wall.")
        
        print()

        bottles -= 1
