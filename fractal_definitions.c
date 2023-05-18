#include <complex.h>

double complex mandelbrot_set(double complex Z, double complex C)
{
    return Z * Z + C;
}