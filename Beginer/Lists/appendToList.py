countries = ['Germany','Bulgaria','Italy']
n = 0
countries.append('Great Britan')
countries.insert(2,'France')
for country in countries:
    n+=1
    print('{} {}'.format(n,country))
