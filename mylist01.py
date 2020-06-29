#!/usr/bin/python3

# comment defining option 1

'''
comment defining option 2

Python lists
'''

def main():
    movies = [] # one way to create list
    movies.append("Parasite") #.append is a list method that applies the 
                              #value passed to it at the END of the list
    movies.append("1917")

    print(movies) #use the print FUNCTION to display the std out

    # ["Parasite", "1917"]]
    print(movies[0])

    movies.append("Ghostbusters")

    print(movies[2])
    print(movies[-1])
    print(movies.index("Ghostbusters"))
    print(movies[movies.index("Ghostbusters")])

# this is best way to run the main function
if __name__ == "__main__" :
    main()
