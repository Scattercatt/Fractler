#include <stdio.h>
#include <complex.h>
#include "complex_func_ptr.c"

void print_complex(complex double my_complex)
{
    printf("%lf+%lfi", creal(my_complex), cimag(my_complex));
}