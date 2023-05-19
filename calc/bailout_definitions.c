#include "complex_tools.c"
#include "func_ptrs.c"
#include "cdouble.c"

bool basic(cdouble Z, cdouble C)
{
    return (cmod(Z) > 4);
}
bool follicle(cdouble Z, cdouble C)
{
    return (creal(Z) + cimag(Z) > 1000);
}

BailoutFuncPtr get_bailout_from_int(int num)
{
    BailoutFuncPtr BAILOUT_LIST[] = {
        basic,
        follicle
    };

    return BAILOUT_LIST[num];
}


