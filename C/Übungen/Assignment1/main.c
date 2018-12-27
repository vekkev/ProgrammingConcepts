#include <stdio.h>
#include <stdlib.h>


long fibonacci(long n) {
    long fibonac = 0;
    long m = 1;
    long temp = 0;

    for (int i = 0; i < n; i++){
        temp = fibonac;
        fibonac += m;
        m = temp;
    }
    return fibonac;

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
