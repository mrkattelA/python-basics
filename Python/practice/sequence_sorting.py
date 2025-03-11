ww2_leaders = [
    ('Charles', 'de Gaulle'),
    ('Winston', 'Churchill'),
    ('Teddy', 'Roosevelt'), # Not a WW2 leader, but helps make point
    ('Franklin', 'Roosevelt'),
    ('Joseph', 'Stalin'),
    ('Adolph', 'Hitler'),
    ('Benito', 'Mussolini'),
    ('Hideki', 'Tojo')
]
#ww2_leaders_list = sorted(ww2_leaders, key = lambda name: (name[1].lower(), name[0]))
ww2_leaders_list = sorted(ww2_leaders, key = lambda name: (name[1].lower()))
for name in ww2_leaders_list:
    print(name)