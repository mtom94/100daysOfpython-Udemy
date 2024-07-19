#Nesting

capitals = {
    "France":"Paris",
    "Germany":"Berlin"
}

#Nesting a List in a Dictionary

#in python we do not use multiple values in the same key
#instead of we add these multiple keys into a list.
# travel_log = {
#     "France": "Paris","Lille","Dijon"
# }
travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin","Hamburg","Stuttgart"]
}

#Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris","Lille","Dijon"],"total_visits":12},
    "Germany":{"cities_visited": ["Berlin","Hamburg","Stuttgart"], "total_visits":5},
}

#Nesting dictionary in a list
travel_log =[
    { "country":"France",
     "cities_visited":["Paris","Lille","Dijon"],
     "total_visits":12 },
    {
        "country": "Germany",
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":5
    },

]
print(travel_log)