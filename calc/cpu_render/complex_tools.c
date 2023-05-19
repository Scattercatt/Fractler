#include <stdio.h>
#include <math.h>
#include "func_ptrs.c"
#include "cdouble.c"

void print_complex(cdouble my_complex)
{
    printf("%lf+%lfi", creal(my_complex), cimag(my_complex));
}

double cmod(cdouble my_complex)
{
    double real = creal(my_complex);
    double imag = cimag(my_complex);
    
    return sqrt(real * real + imag * imag);
}