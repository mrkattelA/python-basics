def main():
    words = ['Woodstock', 'Gary', 'Tucker', 'Gopher', 'Spike', 'Ed',
             'Faline', 'Willy', 'Rex', 'Rhino', 'Roo', 'Littlefoot',
             'Bagheera', 'Remy', 'Pongo', 'Kaa', 'Rudolph', 'Banzai',
             'Courage', 'Nemo', 'Nala', 'Alvin', 'Sebastian', 'Iago']
    three_leter_words = [x for x in words if len(x) == 3]
    print(three_leter_words)

main()