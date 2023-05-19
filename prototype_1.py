

print("Program start")
input_values = [
    -4.353,    # Point 1 R
    -0.323,    # Point 1 I
    1,     # Point 2 R
    1,     # Point 2 I
    100,   # Image size
    0,     # Column to render
    50,    # Max iterations
    0,     # Fractal to render. 0 is The Mandelbrot Set
    0,     # Bailout condition to use. 0 is basic
    0,     # Whether or not the image is julia
    0,     # Julia point R
    0,     # Julia point I
]

string_input_values = [str(val) for val in input_values]

import subprocess

SOURCE_CODE_LOCATION = "./calc/cpu_render/render_column.c"
COMPILED_PROGRAM_NAME = "render_column.exe"

subprocess.run(["gcc", SOURCE_CODE_LOCATION, "-o", COMPILED_PROGRAM_NAME])

print("Compiled")

result = subprocess.run([f"./{COMPILED_PROGRAM_NAME}"] + string_input_values, capture_output = True, text = True)

print("Finished running. stdout:\n")

print(result.stdout)