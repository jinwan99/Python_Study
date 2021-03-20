def fizzbuzz(number):
    result = str(number)
    if number%3==0 and number%5==0:
        result = 'FizzBuzz'
    elif number%3==0:
        result = 'Fizz'
    elif number%5==0:
        result = 'Buzz'
    return result

number = input('何か数値を入力してください : ')
number = int(number)

print(fizzbuzz(number))