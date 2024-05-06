listem = ['a','b','c','d']
print(type(listem))
print(listem)
word = 'happy'
print(list(word))
print(list('a b c'))
text = 'Clarusway'
print(list(text))
print([text])
listem = [1,2,3]
print(len(listem))
print(list(listem))
yeni= [listem]
print(yeni)
print(len(yeni))
a=[[1,2,3],['ali','ayse'],[True,False]]
print(len(a))
print(list(a))
liste_a = [a]
print([a])
print(len(liste_a))
print(len(a))

text ="2023's perfect"
print(list(text))
print([text])

print(list('1234'))
listem = [[1,2,3], 'bir string', 7.23,True]
print(len(listem))

bos1 = []
print(len(bos1))
bos2 = list()
print(len(bos2))

numbers = [1,4,7]
numbers.append(9)
numbers.append('9')
print(numbers)

numbers.append(['a','b','c'])
print(numbers)

empty_list = []
empty_list.append(6666)
empty_list.append('Multiverse')
empty_list.append([0])
print(empty_list)

numbers = [1,4,7]
numbers.insert(2,9)
print(numbers)
numbers.insert(2,6)
print(numbers)

listem = ['a','b','c','d']
listem.insert(3,12)
print(listem)

listem = [1,2,3,4,]
listem.insert(-1,5)
print(listem)
listem = [1,2,3,4,]
print(listem)
listem.insert(4,5)
print(listem)

numbers = [1,4,7,9]
numbers.remove(7)
print(numbers)

numbers=[1,4,7,9,'9',['a','b','c']]
numbers.remove(9)
print(numbers)
numbers.remove('9')
print(numbers)
numbers.remove(['a','b','c'])
print(numbers)
listem=[1,2,3,4,2,3,4,3]
listem.remove(2)
print(listem)
listem.pop()
print(listem)
print(listem.pop(4))
print(listem)
listem = ['a','b','c','d']
listem.remove('c')
print(listem)
listem.pop(1)
print(listem)

listem = [2,7,3,0,5,7]
listem.sort()
print(listem)
listem.sort(reverse=True)
print(listem)

isimler = ['veli','ali','ayse','kemal']
isimler.sort()
print(isimler)
isimler.append('Zeki')
print(isimler)
isimler.sort()
print(isimler)
print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(chr(97))

list_1 = ['one','four','nine']
list_1.sort()
print(list_1)
list_2 = ['*-','@','False']
list_2.sort()
print(list_2)
list_3 = [True,False]
list_3.sort()
print(list_3)
list_4 = [[3],[44],[-12]]
list_4.sort()
print(list_4)
list_5 = [[1,3],[44,0],[-12,1]]
list_5.sort()
print(list_5)
isimler = ['veli','ali','ayse','kemal']
sorted(isimler)
isimler = sorted(isimler)
print(isimler)
print(sorted(isimler,reverse=True))
print([1,2,3]+['a','b','c'])
print([1,2,3] * 3)
print(['a','b','c'] * 3)
