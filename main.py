users:list=[
    {"name":"Mateusz","location":"Węgorzewo","posts":100},
    {"name":"Wiktoria","location":"Chełm","posts":6},
    {"name":"Sabina","location":"Opole","posts":110},
    {"name":"Weronika","location":"Tomaszów Mazowiecki","posts":300},
    {"name":"Julia","location":"Żyradów","posts":50},

]

print(f"witaj {users[0]["name"]}")

for user in users:
    print(f"Twój znajomy {user["name"]} z {user["location"]} opublikował {user["posts"]} postów.")