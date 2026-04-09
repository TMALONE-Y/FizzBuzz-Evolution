def fizzbuzz(number):

    result = ""
    if number % 3 == 0:
        result += "Fizz"

    if number % 7 == 0:
        result += "Buzz"

    if result == "" and "3" in str(number):
        return "Almost Fizz"

    return result if result else str(number)


def main():
    print("Welcome to FizzBuzz!")
    
    try:
        limit = int(input("Enter the limit: "))
        for i in range(1, limit + 1):
            print(fizzbuzz(i))
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()