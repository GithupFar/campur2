import re

class regex_checker():
    def __init__(self, regexnya):
        regexnya = regexnya.replace('+', '|')
        regexnya = regexnya.replace(' ', '')
        self.checker = re.compile(regexnya)

    def cek(self, stringnya):
        data = self.checker.match(stringnya)
        if(data.group() == stringnya):
            return True
        else:
            return False

if __name__ == '__main__':
    reg = raw_input("Masukkan RE: ")
    regex = regex_checker(reg)
    while True:
        inputan = raw_input("Masukkan string: ")
        if inputan.lower() == "exit":
            exit()
        print regex.cek(inputan)