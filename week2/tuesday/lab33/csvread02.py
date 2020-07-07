import csv

def main():
    csvfile = input("Enter .CSV File Name -> ")

    with open(csvfile, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}') # python3.6 way
                                                              ## to do things
                print('Column names are {}'.format(", ".join(row)))
                line_count += 1
            # print(f'\t{row["name"]} aka {row["heroname"]} was born in {row["birthday month"]}.')
            # above is the python3.6+ way to do things
            print('\tThis id {} has name {}.'.format(row["id"],row["name"]))
            line_count += 1
        # print(f'Processed {line_count} lines.') # python3.6 way to do things
    print('Processed {} lines.'.format(line_count))
if __name__ == "__main__":
    main()
