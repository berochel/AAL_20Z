import random
import re

alphabet = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'w': 22,
    'y': 23,
    'z': 24,
    'ą': 25,
    'ś': 26,
    'ć': 27,
    'ź': 28,
    'ż': 29,
    'ó': 30,
    'ł': 31,
    'ę': 32
}


class Dict:
    probability_table = []

    def generate_words(self, f):
        output = ""
        for x in range(f):
            i = 0
            j = 0
            rand_number = random.randint(1, 31)  # ę not included in generating new words
            # print(rand_number)
            # print(list(alphabet.keys())[list(alphabet.values()).index(rand_number)])
            j = rand_number
            output += list(alphabet.keys())[list(alphabet.values()).index(j)]
            while j < 33:

                rand_number = random.randint(1, 33 + len(output))
                if rand_number > 33:
                    rand_number = 33
                rand_number2 = random.randint(0, 100000) / 100000
                if self.probability_table[j][rand_number] < rand_number2:
                    if rand_number < 33:
                        output += list(alphabet.keys())[list(alphabet.values()).index(rand_number)]
                    j = rand_number
            print(output)
            output = ""

    def __init__(self):
        self.probability_table = [[0.0 for i in range(34)] for j in range(33)]
        with open('365_dni.txt', 'r', encoding='utf-8') as file:

            # reading each line
            for line in file:
                # reading each word
                for word in line.split():
                    j = 0
                    i = 0
                    word_clean = re.sub("\W+", '', word.lower())
                    for letter in word_clean:
                        i = 0

                        for key, value in alphabet.items():
                            if letter == key:
                                i = value
                                # print(letter)
                                # print(str(i) + " " + str(j))
                                # print(np.matrix(self.probability_table))
                                self.probability_table[i][0] += 1
                                self.probability_table[j][i] += 1
                                j = i
                        # print(letter)
                    i = 33  # code for the "end of word" sign
                    self.probability_table[j][i] += 1
                    # print(str(i) + " " + str(j))
                    # displaying the words
                    # print(word)
        # print('\n'.join([''.join(['{:8.3f}'.format(item) for item in row])
        #                 for row in self.probability_table]))

        for keyrow, valuerow in alphabet.items():
            if self.probability_table[valuerow][0] != 0:
                for keycol, valuecol in alphabet.items():
                    self.probability_table[valuerow][valuecol] /= self.probability_table[valuerow][0]
                self.probability_table[valuerow][33] /= self.probability_table[valuerow][0]

        print('\n'.join([''.join(['{:8.3f}'.format(item) for item in row])
                         for row in self.probability_table]))
