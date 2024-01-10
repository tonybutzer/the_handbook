import merlin
import os

os.environ['CHIPMUNK_URL'] = 'http://localhost:5656/plus/path'


my_config = merlin.cfg.get(profile='chipmunk-ard')

print(type(my_config))

print(my_config)



print("___"*30)
print (my_config['chips_fn'])
print("___"*30)
print (my_config['specs_fn'])
print("___"*30)

print(type(my_config['specs_fn']))
print(dir(my_config['specs_fn']))

print("___"*30)
print("___"*30)
print(my_config['specs_fn'].keywords)

print("___"*30)

print(my_config['specs_fn'].keywords)
print("___"*30)
print(my_config['specs_fn'].keywords['ubids']['qas'])
print(my_config['specs_fn'].keywords['ubids']['thermals'])
print("___"*30)
print(my_config['specs_fn'].args)
print(my_config['specs_fn'].__repr__())
