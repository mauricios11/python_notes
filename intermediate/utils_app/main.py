import utils

countries, population = utils.get_population()
print(f' keys: {countries} population: {population}')

data = [
    {"Country" : "Colombia", "population" : 300},
    {"Country": "México", "population": 400},
    {"Country": "Brasil" , "population": 500},
    {"Country": "Uruguay", "population" : 600}     
]

def run():
    print("de qué país quieres quieres saber la población? " )
    pais_input = int(input("\n [Colombia = 0] [México = 1] [Brasil = 2] [Uruguay = 3] R: "))


    def select_country(pais_input):
        pais_value = ["Colombia", "México", "Brasil", "Uruguay"]
        pais_key = [i for i in range( len(pais_value ))]

        pais_dict = { key : value for key , value in zip( pais_key, pais_value)}

        if pais_input in pais_dict.keys():
            pais_selected = pais_dict[pais_input]
        
        return pais_selected

    if not pais_input in range(0,4):
        print("elegir opción válida")
        
    else:
        pais_select = select_country(pais_input)
        result = utils.population_by_country(data, pais_select)
        print(result)

if __name__ == "__main__":
    run()

