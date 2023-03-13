text = "Ella es meteoróloga"
text_len = len(text)
slice_ultima = text[-1]
slice_penultima = text[-2]

print(f' Letra en el índice sub 0: "{text[0]}"')
print(f' Letra en el índice sub 1: "{text[1]}"')
print(f' Letra en el índice sub 2: "{text[2]}" \n\n{"* " *20}')


print(f' \n largo del string (con len() se empieza a contar desde el "1"): {len(text)} ')
print(f' Letra en el último índice (slices): "{slice_ultima}"')
print(f' Letra en el último índice (len() = 19): "{text[text_len -1]}" \n (-1 para contar desde el 0)\n')
print (f' Letra en el penúltimo índice (slices) "{slice_penultima}" ')

#slices
print("\n" + ("* " *20) + "\n" + "slices\n")
