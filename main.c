#include <stdio.h>
#include <stdlib.h>
int n = 6;
int array[100] = {0};
int sign[100] = {0};
int vim[100] = {0};
int prime(int num){ //decide whether n is prime
    int i = 2;
    for (;i < num/2 + 1; i++){
        if (num%i == 0)
            return 0; // no
    }
    return 1; // yes
}

int dsf(int x){
    if (x >= n && prime(array[x] + array[0])){
        for (int i = 0 ; i < n; i++){
            printf("%d ,", vim[i]);
        }
        printf("\n");
    }
    else{
        for (int i = 1; i < n; i++){
            if (prime(vim[x - 1] + array[i]) && !sign[i]){
                sign[i] = 1;
                vim[x] = array[i];
                dsf(x + 1);
                sign[i] = 0;
                vim[i] = 0;
            }
        }

    }
}

int main()
{
    printf("please input n = ");
    scanf("%d" , &n);
    int i = 0;
    sign[0] = 1;
    vim[0] = 1;
    for (;i < n; i++){
        array[i] = i + 1;
    }
    int j = 0;
    j = dsf(1);
    return 0;
}

