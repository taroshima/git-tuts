from functools import lru_cache

@lru_cache(maxsize=200)
def fib(n):
    if n==1 or n==0:
        return 1
    return fib(n-1) + fib(n-2)
def main():
    print(fib(int(input("Enter a number:\n"))))
if __name__ == '__main__':
    main()