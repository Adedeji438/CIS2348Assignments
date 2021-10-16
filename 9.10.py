#Adedeji Akingbola
#PSID:1793979

import csv

if __name__ == '__main__':
    file_name = input()
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        freq = {}
        for row in reader:
            for word in row:
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1

        for word in freq:
            print(word + " " + str(freq[word]))