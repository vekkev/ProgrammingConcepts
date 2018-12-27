#include <stdio.h>
#include <stdlib.h>


long fibonacci(long n) {
    long fibonacci = 0;
    long temp = 0;
    long m = 1;

    for (int i = 0; i < n; i++){
        temp = fibonacci;
        fibonacci += m;
        m = temp;
    }
    return fibonacci;

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
