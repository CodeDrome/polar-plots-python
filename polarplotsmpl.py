import math

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def plot(title: str, radius: float, start_degrees: int, end_degrees: int,
         function, color: str):
    
    # these are for the x and y coordinates
    x = []
    y = []

    # iterate range,
    # calculate x and y,
    # and add them to lists
    for degrees in range(start_degrees, end_degrees + 1):
        
        radians = math.radians(degrees)

        pos = function(radians, radius)

        x.append(pos["x"])
        y.append(pos["y"])

    # standard Matplotlib stuff to plot values
    plt.plot(x,
             y,
             linestyle="-",
             linewidth=0.5,
             color=color)    

    plt.title(title)
    plt.grid(True)
    plt.gca().set_aspect('equal')

    plt.show()
