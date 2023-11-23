# Challenge

country = input("Country? ")
visits = input("How many visits? ")
list_of_cities = eval(input())


travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 3,
    },
]


def add_new_country(country, visits, list_of_cities):
    new_country = {
        "country": country,
        "cities_visited": list_of_cities,
        "total_visits": visits,
    }
    travel_log.append(new_country)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']}")
print(f"My favourite city was {travel_log[2]['cities_visited'][1]}")
