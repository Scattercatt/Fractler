
"""
input_values = [
    -1,    # Point 1 R
    -1,    # Point 1 I
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


"""

import subprocess
import multiprocessing as mp
import time
import math

RENDER_COLUMN_EXECUTABLE = "render_column.exe"

class FracGenParams:
    def __init__(self, 
                 point_one_r: float, 
                 point_one_i: float, 
                 point_two_r: float, 
                 point_two_i: float, 
                 image_size: int,
                 max_iterations: int,
                 fractal_to_render: int, #Make this a string
                 bailout_to_use: int, #Make this a string
                 julia: bool,
                 julia_point_r: float = 0.0,
                 julia_point_i: float = 0.0,
                 ) -> None:
        self.point_one = [point_one_r, point_one_i]
        self.point_two = [point_two_r, point_two_i]
        self.image_size = image_size
        self.max_iterations = max_iterations
        self.fractal_to_render = fractal_to_render
        self.bailout_to_use = bailout_to_use
        self.julia = julia
        self.julia_point = [julia_point_i, julia_point_r]


    #TODO Write this or something
    def init_from_dict(self, data: dict) -> None:
        point_one = data["point_one"]
        if not isinstance(point_one, list) and len(point_one) != 2:
            raise Exception(f"{self} object passed dict with invalid point 1 {point_one}!")
        self.point_one: tuple = point_one


        point_two = data["point_two"]
        if not isinstance(point_two, list) and len(point_two) != 2:
            raise Exception(f"{self} object passed dict with invalid point 1 {point_two}!")
        self.point_two: tuple = point_two

        # image_size = data["image_size"]
        # if not isinstance()
        # self.image_size: int = image_size

    def single_thread_render(self) -> list:
        ret_map = []
        for column in range(self.image_size):   
            input_vals = [
                self.point_one[0],
                self.point_one[1],
                self.point_two[0],
                self.point_two[1],
                self.image_size,
                column,
                self.max_iterations,
                self.fractal_to_render,
                self.bailout_to_use,
                self.julia,
                self.julia_point[0],
                self.julia_point[1]
            ]

            string_input_vals = [str(val) for val in input_vals]

            result = subprocess.run([f"./{RENDER_COLUMN_EXECUTABLE}"] + string_input_vals, capture_output = True, text = True)
            
            result_list = result.stdout.split(" ")
            del result_list[-1]

            ret_map.append(result_list)
        
        
        return ret_map

    def run_subprocess_render(self, executable: str, input_vals: list, output_vals: list) -> list:
        string_input_vals = [str(val) for val in input_vals]
        result = subprocess.run([f"./{executable}"] + string_input_vals, capture_output = True, text = True)
        result_list = result.stdout.split(" ")
        del result_list[-1]
        return result_list

    def multi_thread_render(self) -> list:

        def modify_vals_column(input_vals: list, column: int) -> list:
            ret = input_vals.copy()
            ret[5] = column
            return ret

        input_vals = [
                self.point_one[0],
                self.point_one[1],
                self.point_two[0],
                self.point_two[1],
                self.image_size,
                0,
                self.max_iterations,
                self.fractal_to_render,
                self.bailout_to_use,
                self.julia,
                self.julia_point[0],
                self.julia_point[1]
            ]
        
        ret_map = [0 for z in range(self.image_size)]
        
        process_pool = mp.Pool()
        tasks = [
            process_pool.apply_async(
                self.run_subprocess_render, 
                args = (RENDER_COLUMN_EXECUTABLE, modify_vals_column(input_vals = input_vals, column = proc), ret_map)
            ) 
            for proc in range(self.image_size)
        ]

        ret_map = [task.get() for task in tasks]
        
        return ret_map
    
    