# create a list of animals with 3 letter names

def main():

    animallist = ["Fox", "Fly", "Ant", "Bee","Cod", "Cat", "Dog", "Yak", "Cow", "Hen"]

    # display list1
    print(animallist)

    # print list without 'list' symbols
    for animal in animallist:
        print(animal, end= " ")

    print()


if __name__ == "__main__":
        main()
