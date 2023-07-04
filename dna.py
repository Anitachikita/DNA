import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("python dna.py data.csv sequence.txt")
        sys.exit


    # TODO: Read database file into a variable
    database = []
    with open(sys.argv[1], 'r') as csv_file:
        dnareader = csv.DictReader(csv_file)
        for row in dnareader:
            database.append(row)
    #with open('eggs.csv', newline='') as csvfile:
    #reader = csv.DictReader(csvfile)
    #for row in reader:
        #print(row['first_name'], row['last_name'])

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as txtfile:
        dna = txtfile.read()


    # TODO: Find longest match of each STR in DNA sequence
    dna_patterns = list(database[1].keys())[1:]

    result= {}
    for str in dna_patterns:
        result[str] = longest_match(dna,str)

    # TODO: Check database for matching profiles
    for candidate in database:
        matches = 0
        for str in dna_patterns:
            if int(candidate[str]) == result[str]:
                matches +=1

        if matches == len(dna_patterns):
            print(candidate["name"])
            return
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
