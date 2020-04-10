import sys
def fizz_buzz(limit):
    print(limit)
    for i in range(1, limit+1):
        if i % 3 == 0:
            print('fizz')
        if i % 5 == 0:
            print('fizz')
        if i % 3 and i % 5:
            print(i)

def main(number):
    fizz_buzz(int)

if __name__ == '__main__':
    main(sys.argv[1])
 