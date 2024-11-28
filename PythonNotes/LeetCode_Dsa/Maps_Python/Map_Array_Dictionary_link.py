country_population = {
    "India": 1500,
    "USA": 300,
    "China": 1400,
    "Brazil": 210
}


countries = ["India", "USA", "China"]


for i in countries:
    if i in country_population:
        print(i,"population is",country_population[i])

    
