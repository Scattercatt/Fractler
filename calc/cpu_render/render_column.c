#include <stdio.h>
#include <stdlib.h>

#include "../fractal_definitions.c"
#include "../bailout_definitions.c"

int main(int argc, char *argv[])
{   
    const int EXPECTED_ARG_COUNT = 13;
    const cdouble C_ZERO = 0;

    if (argc < EXPECTED_ARG_COUNT)
    {
        printf("Must specify all args for render_column.c");
        return 1;
    }

    // Arg 1 is X position of point 1
    // Arg 2 is Y position of point 1
    cdouble p1 = strtod(argv[1], NULL) + strtod(argv[2], NULL) * I;

    // Arg 3 is X position of point 2
    // Arg 4 is Y position of point 2
    cdouble p2 = strtod(argv[3], NULL) + strtod(argv[4], NULL) * I;

    // Arg 5 is the size of the desired output array
    int img_size = atoi(argv[5]);

    // Arg 6 is the column number
    int column_to_render = atoi(argv[6]);

    if (column_to_render >= img_size)
    {
        printf("Render column cannot be greater than or equal to image size!");
        return 1;
    }

    // Arg 7 is the max iteration count
    int max_iterations = atoi(argv[7]);

    // Arg 8 is the fractal to render. 
    int fractal_int = atoi(argv[8]);
    FractalFuncPtr selected_fractal = get_fractal_from_int(fractal_int);

    // Arg 9 is the bailout condition
    int bailout_int = atoi(argv[9]);
    BailoutFuncPtr selected_bailout = get_bailout_from_int(bailout_int);

    // Arg 10 is whether or not the image is a julia
    bool is_julia = (atoi(argv[10]) != 0);

    // Arg 11 and 12 are the julia points.
    int julia_point_real, julia_point_imag;
    if (is_julia)
    {
        julia_point_real = atoi(argv[11]);
        julia_point_imag = atoi(argv[12]);
    }
    

    // Column separation amount
    double column_separation_amount = (creal(p2) - creal(p1)) / (float) img_size;

    // Column double to render across
    double column_to_render_down = column_separation_amount * column_to_render;


    // Define data return var
    int calculated_iterations[img_size];

    // Begin fractal calculation
    int pixel;
    double row;
    for (row = cimag(p1), pixel = 0; row < cimag(p2); row += column_separation_amount, pixel++)
    {
        // Set initial Z and C based on is_julia
        cdouble Z, C;
        if (!is_julia)
        {
            Z = C_ZERO;

            C = column_to_render_down + row * I;
        }
        else
        {
            Z = column_to_render_down + row * I;

            C = julia_point_real + julia_point_imag;
        }
        
        int its = 0;
        while (its < max_iterations)
        {
            bool bailout_succeeded = selected_bailout(Z, C);
            if (bailout_succeeded)
            {
                break;
            }
            Z = selected_fractal(Z, C);

            its++;
        }

        calculated_iterations[pixel] = its;
    }

    for (int i = 0; i < img_size; i++)
    {
        printf("%d ", calculated_iterations[i]);
    }

    return 0;
}