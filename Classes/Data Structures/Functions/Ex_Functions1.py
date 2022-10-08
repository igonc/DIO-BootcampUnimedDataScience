def message1():
    print('Hellow World!')

def message2(name):
    print(f'Welcome home {name}!')

def message3(name='Anonymous'):
    print(f'Welcome home {name}!')

message1()
message2(name='Jacob')
message2('Rachel')
message3()
message3(name='Marcello')
message3('Gionanni')
