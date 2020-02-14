# a basic program which can take any sentence and encrypt it using a shift cipher
# unfixed version
alphabet = ['a', 'b', 'c', 'd', 'e', f, 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(our_num, sentence):
    fully_encrypted = []
    for i in sentence:
        for number, alpha_num in enumerate(alphabet):
            if i == alpha_num:
                shift_num = number + int(our_num)
                try:
                    fully_encrypted.append(alphabet[shift_num])
                except IndexError:
                    shift_num = shift_num - 26
                    fully_encrypted.append(alphabet[shift_num])
    fully_encrypted = ''.join(fully_encrypted)
    print(fully_encrypted)
    return fully_encrypted

def num_shift():
    shifter = input('How many numbers do you want to shift? '
                    'This can not be larger than 26\n')
    while True:
        try:
            if int(shifter) > 25:
                shifter = input('Number too large, '
                            'how many numbers do you want to shift?\n')
            else:
                return shifter
        except TypeError:
            shifter = input('Incorrect input, '
                            'how many numbers do you want to shift?\n')

def our_sentence():
    sentence = lower(input('Please enter your sentence (only a-z)\n'))
    bad_list = []
    while True:
            for i in sentence:
                if i not in alphabet:
                    bad_list.append(i)

            if bad_list != []:
                sentence = input('Please try again \n')
                bad_list = []
            else:
                return sentence

def main():
    sentence = our_sentence()
    number = num_shift()
    encrypt(number)

main()
