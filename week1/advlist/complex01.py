#!/usr/bin/env python3

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    # print list1[1] = 'artista_eos''
    print(list1[1])

    # craete new list list2
    list2 = ["Jupiter"]

    # extend list1 by list2
    list1.extend(list2)

    #print new combined list which is list1
    print(list1)

    # create new list list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    # append operation to append list1 by list3
    list1.append(list3)

    #print the new coplext list1
    print(list1)

    # display the list of IP addresses
    print(list1[4])

    #display the first item in the list (oth item) - first IP address
    print(list1[4][0])

if __name__ == "__main__":
    main()
