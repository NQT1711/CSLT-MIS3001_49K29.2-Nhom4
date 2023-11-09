n = str(input('Name of month:'))
a = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
b = ['april', 'june', 'september', 'november']
if n.lower() in a:
    print(n, 'has 31 days')
if n.lower() in b:
    print(n, 'has 30 day')
if n.lower() == 'february':
    print(n, 'has 28 or 29 days')
