import time

name = input('Your name: ')
attribute1 = input('One of your attributes: ')
attribute2 = input('Another one of your attributes: ')
death = input('Your favourite cartoon character: ')

print('--------------------------------------------------------------------------------------------------')
print(f'Bio\\la jednom jedan\\na {name}.')
time.sleep(2)
print(f'{name} je znao\\la da je jako {attribute1.lower()}...')
time.sleep(2)
print(f'Ali i pored toga, {name} je imao\\la jos jednu osobinu, a to je {attribute2.lower()}.')
time.sleep(2)
print(f'Zbog toga je {name} dobio\\la metak u glavu od strane {death}.')
time.sleep(2)