import sys


FileOpen = open("chal1.txt")
FileRead = FileOpen.read()

NumberDictionary = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven','eight','nine']

lines = FileRead.split('\n')


def BackChecking(x):
    for a in range(len(x) - 1, -1, -1):
        if (x[a]).isdigit():
            return x[a]
        else:
            IndexDict = 0
            for word in NumberDictionary:
                IndexDict +=1
                length = len(word)

                if x[a] == word[length - 1]:
                    index1 = (a + 1) - length

                    CheckWord = x[index1: a+1]
                    if CheckWord == word:
                        return (IndexDict - 1)
                    else:
                        continue


def Checking(x):
    index = 0
    for a in x:
        if a.isdigit():
            return a
        IndexDict = 0
        for word in NumberDictionary:
            IndexDict+=1
            if a ==word[0]:
                length = len(word)
                index1 = index + length

                CheckWord = x[index: index1]
                if CheckWord == word:

                    return (IndexDict - 1) 

                else:
                    continue
        index+=1


def main():
    sum = 0
    for word in lines:
        Output = Checking(word)
        BackOutput = BackChecking(word)

        print(f'{Output}{BackOutput}')
        sum+=int(f'{Output}{BackOutput}')

    print(sum)

main()