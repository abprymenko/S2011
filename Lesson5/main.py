import random
import requests
import colorama
#help(requests)
'''
import requests
r = requests.get('https://www.python.org')
#print(r.content)
payload = dict(key1='Student', key2='Sergii')
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
'''
'''
print(type(requests.Request))
print(dir(requests.Request))
print(dir(requests))
students = list()
for method in dir(students):
    print(method)
'''
name = "Ippial"
print(hasattr(name, "index"))
print(getattr(name, "startswith"))
print(callable(name))
print(f'Is method requests.get callable?: {callable(requests.get)}')
print(issubclass(AttributeError, random.Random))
print(issubclass(AttributeError, Exception))
help(colorama)