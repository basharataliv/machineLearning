import argparse
from math_utils.operations import add, multiply
from string_utils.formatter import greet, shout

def main():
    parser = argparse.ArgumentParser(description="Demo CLI for math and greeting functions")
    parser.add_argument("name", help="Name to greet")
    parser.add_argument("num1", type=int, help="First number")
    parser.add_argument("num2", type=int, help="Second number")

    args = parser.parse_args()

    print(greet(args.name))            
    print(shout("Let's go!"))          
    print(f"Add: {add(args.num1, args.num2)}")
    print(f"Multiply: {multiply(args.num1, args.num2)}")

if __name__ == "__main__":
    main()
