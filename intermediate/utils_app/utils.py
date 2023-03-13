# función para obtener la población de un país 
def get_population():
    countries_key = ["col", "mex", "bra", "arg"]
    population_value = [300, 100, 400, 500]
    
    return countries_key , population_value

#obtener la población de un país
def population_by_country(dataset, pais ):
    result = list(filter(lambda x : x["Country"] == pais, dataset))
    return result

    

    