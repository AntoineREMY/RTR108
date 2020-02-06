Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> bag = dict()
bag["money"] = 1
bag[42] = 2
bag[42] = "value"
print(bag)
bag["money"] += 2
print(bag)

bag2 = {"key1": 3,"key2" : 5}
print(bag2)


frequency = "sfjklawnjf;wanf;anojnac wn;ejfawokufha;joigaergnaeoājiropq"
frequencDict = {}
for a in frequency:
    if a in frequencDict:
        frequencDict[a] += 1
    else:
        frequencDict[a] = 1
print(frequencDict)

print(frequencDict.get("f",0))

SyntaxError: multiple statements found while compiling a single statement
>>> bag = dict()
>>> SyntaxError: multiple statements found while compiling a single statementbag["money"] = 1
SyntaxError: invalid syntax
>>> bag["money"] = 1
>>> bag[42] = 2
bag[42] = "value"
SyntaxError: multiple statements found while compiling a single statement
>>> 
=============================== RESTART: Shell ===============================
>>> bag = dict()
>>> bag["money"] = 1
>>> bag[42] = 2
>>> bag[42] = "value"
>>> print(bag)
{'money': 1, 42: 'value'}
>>> bag["money"] += 2
>>> print(bag)
{'money': 3, 42: 'value'}
>>> bag2 = {"key1": 3,"key2" : 5}
>>> print(bag2)
{'key1': 3, 'key2': 5}
>>> frequency = "sfjklawnjf;wanf;anojnac wn;ejfawokufha;joigaergnaeoājiropq"
>>> frequencDict = {}
>>> for a in frequency:
    if a in frequencDict:
        frequencDict[a] += 1
    else:
        frequencDict[a] = 1

        
>>> print(frequencDict)
{'s': 1, 'f': 5, 'j': 6, 'k': 2, 'l': 1, 'a': 8, 'w': 4, 'n': 6, ';': 4, 'o': 5, 'c': 1, ' ': 1, 'e': 3, 'u': 1, 'h': 1, 'i': 2, 'g': 2, 'r': 2, 'ā': 1, 'p': 1, 'q': 1}
>>> print(frequencDict.get("f",0))
5
>>> counts = dict()
>>> names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
>>> for name in names :
    counts[name] = counts.get(name, 0) + 1

    
>>> print(counts)
{'csev': 2, 'cwen': 2, 'zqian': 1}
>>> counts = dict()
>>> print('Enter a line of text:')
Enter a line of text:
>>> line = input('')

>>> words = line.split()
>>> print('Words:', words)
Words: []
>>> print('Counting...')
Counting...
>>> for word in words:
    counts[word] = counts.get(word,0) + 1

    
>>> print('Counts', counts)
Counts {}
>>> 
