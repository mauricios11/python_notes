#diferentes formas de filtar elementos de una lista
def filter_by_length(words):
    filtrar = list(filter(lambda item: (len(item)>= 4) , words))
    return filtrar

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)

###########

words = ['amor', 'sol', 'piedra', 'día']
letter_4 = []
for i in words:
    if len(i) >=4:
        letter_4.append(i)
        
print(letter_4)

############

four_letters = {i: "tiene " + str(len(i)) + " letras"  for i in words if len(i)>= 4 }
print(four_letters)