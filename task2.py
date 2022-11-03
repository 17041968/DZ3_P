# В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
def first_letter():
	 return input()[0]

def frukt_from_file(letter:str):
    with open('frukt.txt','r',encoding= 'utf-8') as inf:
        frukt = [inf.readline().strip().replace('\n','') for _ in inf]
		
    for fruit in frukt:
        if fruit and fruit[0].lower() == letter.lower():
            print(fruit)
print('Введите первую букву ')

def main():
    char = first_letter()
    frukt_from_file(char)

if __name__ == '__main__':
    main()