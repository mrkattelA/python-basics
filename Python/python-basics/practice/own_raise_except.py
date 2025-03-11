def bidic(d):
    d2 = d.copy()
    for k,v in d.items():
        if v in d2.keys():
            raise KeyError("Cannot create bidirectional dic " +
                           "with duplicate keys ")
        d2[v] = k
    return d2

translator = bidic({"hola":"hi","adios":"bye"})
print(translator["hola"])
print(translator["hi"])

translator2 = bidic({"hola":"hi", "adios":"bye", "ciao":"bye"})