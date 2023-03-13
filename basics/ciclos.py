#ciclos

#hacer un ciclo infinito
#while True:
#    print("press ctrl + c to cancel this ∞ loop ")

#hacer un ciclo  con un rango de 20, y que se detenga  cuando llegue a 15
counter = 0
counter_list = []
i = 0
while counter < 20 :
    counter += 1
    counter_list.append(counter)
    if counter == 15:
        print("this is {} iterarion!!!!!".format(str(counter)))
        counter_list.remove(counter)
        continue
    if counter == 18:
        print(18)
        break
    print ("this is a while loop number: {}".format(str(counter)))
    
print(counter_list)
    
#hacer un ciclo que continue a la siguiente línea de cógigo (y no ejecute lo demás del while)