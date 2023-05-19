#include <stdbool.h>
#include "cdouble.c"

typedef cdouble (*FractalFuncPtr)(cdouble, cdouble);
typedef bool (*BailoutFuncPtr)(cdouble, cdouble);