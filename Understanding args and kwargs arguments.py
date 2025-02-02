import json

def greet():
    print('Hello user')
def main():
    greet()
if __name__=='__main__':
    main()

def greet(user):
    print(f'Hello {user}')
def main():
    greet('milltech')
if __name__== '__main__':
    main()

def purp(learning):
    print(f'purposed {learning}')
def main():
    purp('is knowledge')
if __name__== '__main__':
    main()
    
    
def purp(studying):
    print(f'purposed {studying}')
def main():
    purp('is still for the sake of knowledge')
if __name__== '__main__':
    main()

def purp(study):
    print(f'purpose{study}')
def main():
    purp(', Its for the sake of knowledge and to become a better person in the society and impact life around me')
if __name__== '__main__':
    main()    
    
def purp(Eating):
    print(f'Why {Eating}')
def main():
    purp('eating is to keep healthy and stay alive because food is what keep on going in life, without food, its death')
    purp('although one can stay without food for days but not for ever')
if __name__== '__main__':
    main()
    
    
def pos_arg(a,b,c):
    print(f'The value of a is: {a}')
    print(f'The value of b is: {b}')
    print(f'The value of c is: {c}')
    
def main():
    pos_arg(10,20,30)
    
if __name__=='__main__':
    main()

def pos_arg(A=0,B=0,C=0):
    print(f'The value of a is:{A}')
    print(f'The value of b is:{B}')
    print(f'The value of c is:{C}')
def main():
    pos_arg(50, C=100)
if __name__== '__main__':
    main()
    
def greet(*users):
    for user in users:
        print(f'Welcome sir {user}')
def main():
    greet('Bob','Paul', 'Tom')
if __name__== '__main__':
    main()
    
def greet(**users):
    for key, value in users.items():
        print(f'{key} => {value}.')
def main():
    greet(user='Tom', city='Istanbul', pet=['Rat','Dog','Cat'])
if __name__=='__main__':
    main()
