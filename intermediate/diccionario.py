def message_creator(text):
   # Escribe tu solución 👇
   opciones = {
      "computadora": "Con mi computadora puedo programar usando Python",
      "celular" : "En mi celular puedo aprender usando la app de Platzi",
      "cable" : "¡Hay un cable en mi bota!"
   }

   if text in opciones.keys():
       return opciones[text]
        
text = 'celular'
response = message_creator(text)
#print(response)


a = {1,2}
b = {2,3}


if __name__ == "__main__":
   print(response)
   print(a|b)
