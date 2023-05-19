print("Program start")

import time
from fractal_gen_params import FracGenParams

ITERATIONS = 100000

test_fractal = FracGenParams(
    -2,    # Point 1 R
    -1.0,    # Point 1 I
    -0,     # Point 2 R
    1.0,     # Point 2 I
    200,   # Image size
    ITERATIONS,    # Max iterations
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

start = time.time()
results = test_fractal.single_thread_render()
end = time.time()

print(results)

for row in results:
    for col in row:
        if int(col) == ITERATIONS:
            print("X", end = "")
        else:
            print(" ", end = "")
    print()

print(f"Time taken to render: {end-start}")