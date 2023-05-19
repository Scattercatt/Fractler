"""
Prototype 4 uses multiprocesing and Tkinter as a test UI. WAY too slow
"""

import subprocess
import tkinter as tk
import random

from fractal_gen_params import FracGenParams

def draw_pixel(x, y, color, canvas):
    canvas.create_rectangle(x, y, x, y, fill = color, outline = "")

def simple_coloring_algorithm(iteration, max_iteration, color_type) -> str:
    
    color = format(round(float(iteration) / float(max_iteration) * 255.0), "02x")
    if color_type == 0:
        return f"#{color}0000"
    if color_type == 1:
        return f"#00{color}00"
    if color_type == 2:
        return f"#0000{color}"

def draw_fractal(contents: list, canvas):
    canvas.delete("all")
    color_type = random.randrange(0, 3)
    for ix, elemx in enumerate(results):
        for iy, elemy in enumerate(elemx):
            draw_pixel(ix, iy, simple_coloring_algorithm(results[ix][iy], ITERATIONS, color_type), canvas)
    print("Drawn")

    canvas.pack()

if __name__ == "__main__":
    print("Program start")

    window = tk.Tk()
    window.title("Prototype 5")
    window.geometry("800x600")

    
    

    SOURCE_CODE_LOCATION = "./calc/cpu_render/render_column.c"
    COMPILED_PROGRAM_NAME = "render_column.exe"

    subprocess.run(["gcc", SOURCE_CODE_LOCATION, "-o", COMPILED_PROGRAM_NAME, "-O3"])

    print("Compiled")

    ITERATIONS = 100
    test_fractal = FracGenParams(
        -2,    # Point 1 R
        -1.0,    # Point 1 I
        -0,     # Point 2 R
        1.0,     # Point 2 I
        400,   # Image size
        ITERATIONS,    # Max iterations
        0,     # Fractal to render. 0 is The Mandelbrot Set
        0,     # Bailout condition to use. 0 is basic
        0,     # Whether or not the image is julia
        0,     # Julia point R
        0,     # Julia point I
    )

    results = test_fractal.multi_thread_render()
    print("Rendered")

    canvas = tk.Canvas(window, width=400, height=400)
    button = tk.Button(window, text = "generate", command = lambda: draw_fractal(results, canvas))
    button.pack()    

    window.mainloop()