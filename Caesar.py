print("Вас приветствует программа ШИФР ЦЕЗАРЯ")
step = int(input('Введите шаг сдвига для шифровки ( >0 ) или дешифровки ( <0 ): '))


en_alphabet = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]
ru_alphabet = [chr(i) for i in range(1040, 1104)]


def cezar(text):
    if txt[0] in en_alphabet:
        alphabet = en_alphabet
        alphabet_lan = 26
    else:
        alphabet = ru_alphabet
        alphabet_lan = 32
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                print(alphabet[(alphabet.index(text[i]) + step) % alphabet_lan], end='')
            else:
                print(alphabet[(alphabet.index(text[i]) + step) % alphabet_lan + alphabet_lan], end='')
        else:
            print(text[i], end='')


txt = input("Введите текст: ")
cezar(txt)
