shopping_dict = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

ilosc_rzeczy = 0
for sklep, rzeczy in shopping_dict.items():
    ilosc_rzeczy += len(rzeczy)
    capitalized = [thing.capitalize() for thing in rzeczy]
    print(f"Idę do {sklep.capitalize()} i kupuję tam {capitalized}")


print(f"W sumie kupuję {ilosc_rzeczy} produktów")


