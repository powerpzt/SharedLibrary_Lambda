#include <stdio.h>

int add(int a, int b){
    printf("add\n");
    return a+b;
}

int addin(int a, int b)
{
    int result;
    result = add(a,b);
    printf("result : %d\n", result);
    return 0;
}

