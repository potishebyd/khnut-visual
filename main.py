def func_prefix(s: str) -> list:
    """
    Fills Pi-function array
    :param str: lookip string
    :return: result
    """
    l = len(s)
    P = [0]*l
    i, j = 0, 1
    while j < l :
        if s[i] == s[j]:
            P[j] = i + 1
            i += 1
            j += 1
        # s[i] != s[j]:
        elif i:         # i > 0
            i = P[i - 1]
        else:           # i == 0
            P[j] = 0
            j += 1
    return P

def kmp(text: str, sub: str) -> list:
    sub_len = len(sub)
    text_len = len(text)
    #print(text_len, sub_len)
    if not text_len or sub_len > text_len:
        return []
    P = func_prefix(sub)
    #print(">>>", P)
    entries = []
    i = j = 0
    while i < text_len:
        print("Нажмите Enter чтобы перейти к следующему шагу.")
        input()
        print(text)
        y = i - j
        print(' '*y + sub)
        print('^'*(i) + '0')
        if text[i] == sub[j]:
            #print(j, i)

            if j == sub_len - 1:
                entries.append(i - sub_len + 1)
                print("Найдено вхождение")
                j = P[j]
            else:
                j += 1
            i += 1
        # text[i] 1= sub[j]
        elif j:     # j > 0
            j = P[j-1]
        else:
            i += 1
        print()
    return entries

if __name__ == '__main__':
    s = input("Введите строку:")
    sub = input("Введите подстраку:")
    P = kmp(s, sub)
    print(P)
    #for i in P:
    #    print(s[i:i + len(sub)])