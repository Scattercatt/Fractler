#include <complex.h>
#include "complex_func_ptr.c"

complex double mandelbrot_set(complex double Z, complex double C)
{
    return Z * Z + C;
}

ComplexFuncPtr get_fractal_from_int(int num)
{
    ComplexFuncPtr FRACTAL_LIST[] = {
        mandelbrot_set
    };

    return FRACTAL_LIST[num];
}
