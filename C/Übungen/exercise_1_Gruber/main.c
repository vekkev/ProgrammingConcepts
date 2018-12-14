#include <stdio.h>
#include <stdlib.h>


long fibonacci(long n) {
    if (n < 2) {
        return n;
    }
    return fibonacci(n - 2) + fibonacci(n - 1);
}

int main(int argc, char* argv[]) {
    if(argc != 2)
    {
        printf("usage fib <number>\n");
        return 1;
    }

    int value = atoi(argv[1]);
    int result = fibonacci(value);
    printf("fib(%d) = %d\n",value,result);

    return 0;
}

