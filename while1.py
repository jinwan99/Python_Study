import random
answer = random.randint(1,100)

number = int(input('100までの数値を入力してください : '))

while number != answer:
    if number > answer :
        print('小さい値です。')
    if number < answer :
        print('大きい値です。')
    number = int(input('100までの数値を入力してください : '))

print('素晴らしい！正解です。')