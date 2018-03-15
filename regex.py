import re, os

class regex_checker():
    def __init__(self, regexnya):
        if regexnya == '':
            regexnya = '(a+b)*aa(a+b)*bb(a+b)*+(a+b)*bb(a+b)*aa(a+b)*'
        regexnya = regexnya.replace('+', '|')
        self.regexnya = regexnya.replace(' ', '')
        self.checker = re.compile(regexnya)

    def cek(self, stringnya):
        data = self.checker.match(stringnya)
        if(data == None):
            return False, stringnya
        elif(data.group() == stringnya):
            return True, data.group()
        else:
            return False, data.group()

    def state(self, current, inputnya):
        state_diagram = {
            'q0': {
                'a': 'q1',
                'b': 'q2'
            },
            'q1': {
                'a': 'q3',
                'b': 'q2'
            },
            'q2': {
                'a': 'q1',
                'b': 'q4'
            },
            'q3': {
                'a': 'q3',
                'b': 'q5'
            },
            'q4': {
                'a': 'q6',
                'b': 'q4'
            },
            'q5': {
                'a': 'q3',
                'b': 'q7'
            },
            'q6': {
                'a': 'q7',
                'b': 'q4'
            },
            'q7': {
                'a': 'q7',
                'b': 'q7'
            }
        }
        return state_diagram[current][inputnya]

    def diagram_print(self):
        file = open('diagram.unknown', 'r')
        gambar = file.read()
        file.close()
        print gambar

if __name__ == '__main__':
    reg = raw_input("Masukkan RE: ")
    regex = regex_checker(reg)
    while True:
        os.system('cls')
        print 'Regex: ' + regex.regexnya
        regex.diagram_print()
        inputan = raw_input("Masukkan string: ")
        if inputan.lower() == "exit":
            exit()
        hasil, bahan = regex.cek(inputan)
        print hasil
        if bool(bahan) == False:
            print 'q0'
        else:
            state = regex.state('q0', bahan[0])
            total_state = state + ' '
            bahan = bahan[1:]
            for b in bahan:
                state = regex.state(state, b)
                total_state += state + ' '
            print total_state
        dump = raw_input('Press any key to continue')