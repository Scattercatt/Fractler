#include <stdio.h>
#include <stdlib.h>
#include "..\fractal_definitions.c"
#include <complex.h>

struct Point {
    int x;
    int y;
};

int main(int argc, char *argv[])
{   
    if (argc < 7)
    {
        printf("Must specify all args");
        return 1;
    }

    // Arg 1 is X position of point 1
    // Arg 2 is Y position of point 1
    struct Point p1;
    p1.x = atoi(argv[1]);
    p1.x = atoi(argv[2]);

    // Arg 3 is X position of point 2
    // Arg 4 is Y position of point 2
    struct Point p2;
    p2.x = atoi(argv[3]);
    p2.x = atoi(argv[4]);

    // Arg 5 is the size of the desired output array
    int img_size = atoi(argv[5]);

    // Arg 6 is the column number
    int column_to_render = atoi(argv[6]);

    complex double test1 = 0.1 + 1.2 * I;
    complex double test2 = 0.1 + 1.2 * I;

    complex double test = mandelbrot_set(test1, test2);

    printf("%lf %lf", creal(test), cimag(test));
}