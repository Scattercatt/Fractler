#include "func_ptrs.c"

cdouble mandelbrot_set(cdouble Z, cdouble C)
{
    return Z * Z + C;
}
cdouble burning_ship(cdouble Z, cdouble C)
{

}

FractalFuncPtr get_fractal_from_int(int num)
{
    FractalFuncPtr FRACTAL_LIST[] = {
        mandelbrot_set
    };

    return FRACTAL_LIST[num];
}
