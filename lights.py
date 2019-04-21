import sys
import numpy as np
import colorsys
from serial_library import write, write_channel
from color_library import color_names


NUM_LEDS = 226
rgb = np.array([(255, 255, 255)]*NUM_LEDS)


# read in the color arguments
args = sys.argv[1:]
if len(args) == 1:
    color_name = args[0]
    if color_name in color_names:
        rgb[:] = color_names[color_name]
    pass
elif len(args) % 3 == 0:
    a = np.array(list(map(int, args))).reshape(-1,3)
    indexes = np.arange(NUM_LEDS)*a.shape[0]//NUM_LEDS
    indexes = indexes.astype(int)
    rgb = a[indexes,:]



write(rgb)

