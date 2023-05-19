#include <stdio.h>
#include <stdlib.h>

#include "../fractal_definitions.c"
#include "../complex_tools.c"

int main(int argc, char *argv[])
{   
    const int EXPECTED_ARG_COUNT = 9;

    if (argc < EXPECTED_ARG_COUNT)
    {
        printf("Must specify all args for render_column.c");
        return 1;
    }

    // Arg 1 is X position of point 1
    // Arg 2 is Y position of point 1
    complex double p1 = strtod(argv[1], NULL) + strtod(argv[2], NULL) * I;

    // Arg 3 is X position of point 2
    // Arg 4 is Y position of point 2
    complex double p2 = strtod(argv[3], NULL) + strtod(argv[4], NULL) * I;

    // Arg 5 is the size of the desired output array
    int img_size = atoi(argv[5]);

    // Arg 6 is the column number
    int column_to_render = atoi(argv[6]);

    if (column_to_render > img_size)
    {
        printf("Render column cannot be greater than image size!");
        return 1;
    }

    // Arg 7 is the max iteration count
    int max_iterations = atoi(argv[7]);

    // Arg 8 is the fractal to render. 
    int fractal_int = atoi(argv[8]);
    ComplexFuncPtr fractal_ptr = get_fractal_from_int(fractal_int);

    print_complex(fractal_ptr(p1, p2));



    // Column separation amount
    double column_separation_amount = (creal(p2) - creal(p1)) / (float) img_size;

    // Column double to render across
    double column_to_render_across = column_separation_amount * column_to_render;

    for (double i = cimag(p1); i < cimag(p2); i += column_separation_amount)
    {

    }

    return 0;
}