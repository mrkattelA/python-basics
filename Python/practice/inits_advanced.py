def get_inits(name):
    inits = [x[0] for x in name.split()]
    return ".".join(inits) + "."

def main():
    people = ['George Washington', 'John Adams', 
              'Thomas Jefferson', 'John Quincy Adams']
    
    inits = [get_inits(per) for per in people]
    print(inits)

main()
