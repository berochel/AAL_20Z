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
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'w': 21,
    'y': 22,
    'z': 23,
    'ą': 24,
    'ś': 25,
    'ć': 26,
    'ź': 27,
    'ż': 28,
    'ó': 29,
    'ł': 30,
    'ę': 31
}


class Dict:
    probability_table = []

    def generate_words(self, f):
        output_list = []
        output = ""
        for x in range(f):
            rand_number = random.randint(1, 30)  # ę not included in generating new words
            j = rand_number
            output += list(alphabet.keys())[list(alphabet.values()).index(j)]
            while j < 32:
                rand_number = random.randint(1, 32)
                if rand_number > 32:
                    rand_number = 32
                rand_number2 = random.randint(0, 100000) / 100000
                if self.probability_table[j][rand_number] > rand_number2:
                    if rand_number < 32:
                        output += list(alphabet.keys())[list(alphabet.values()).index(rand_number)]
                    j = rand_number

            output_list += [output]
            output = ""
            j = 0
        return output_list

    def __init__(self):
        self.probability_table = [[0.0 for i in range(33)] for j in range(32)]
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
                                self.probability_table[i][0] += 1
                                self.probability_table[j][i] += 1
                                j = i

                    i = 32  # code for the "end of word" sign
                    self.probability_table[j][i] += 1

        for keyrow, valuerow in alphabet.items():
            if self.probability_table[valuerow][0] != 0:
                for keycol, valuecol in alphabet.items():
                    self.probability_table[valuerow][valuecol] /= self.probability_table[valuerow][0]
                self.probability_table[valuerow][32] /= self.probability_table[valuerow][0]

        print('\n'.join([''.join(['{:10.3f}'.format(item) for item in row])
                         for row in self.probability_table]))
