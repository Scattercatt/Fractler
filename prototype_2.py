print("Program start")

from fractal_gen_params import FracGenParams

test_fractal = FracGenParams(
    -1,    # Point 1 R
    -1,    # Point 1 I
    1,     # Point 2 R
    1,     # Point 2 I
    100,   # Image size
    50,    # Max iterations
    0,     # Fractal to render. 0 is The Mandelbrot Set
    0,     # Bailout condition to use. 0 is basic
    0,     # Whether or not the image is julia
    0,     # Julia point R
    0,     # Julia point I
)


import subprocess

SOURCE_CODE_LOCATION = "./calc/cpu_render/render_column.c"
COMPILED_PROGRAM_NAME = "render_column.exe"

subprocess.run(["gcc", SOURCE_CODE_LOCATION, "-o", COMPILED_PROGRAM_NAME])

print("Compiled")

results = test_fractal.render()

print(results)

for row in results:
    for col in row:
        if int(col) == 50:
            print("X", end = "")
        else:
            print(" ", end = "")
    print()