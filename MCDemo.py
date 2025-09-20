import numpy as np
from PIL import Image, ImageDraw

# CONSTANTS
beta = 1.0
mu = 0.0
std = 1.0


def MHMC_step(potential, arr):
    curr_state = arr[-1]
    new_state = curr_state + np.random.normal(mu, std)
    acceptance_prob = np.exp(- beta * (potential(new_state) - potential(curr_state)))
    if np.random.rand() < acceptance_prob:
        arr.append(new_state)
    else:
        arr.append(curr_state)  # stay in same state if rejected


def double_well(x, a=1.0, b=1.0):
    return a * (x ** 2 - b) ** 2


# store MHMC states
states = [0.0]

# create a transparent image (RGBA)
im = Image.new("RGBA", (1000, 1000), (255, 255, 255, 255))  # white background
# center_x, center_y = 500, 500  # fixed center

# Run MHMC and draw circles
for _ in range(200):  # number of steps
    MHMC_step(double_well, states)
    # radius = abs(states[-1] * 200)  # scale radius for visibility
    center_x, center_y = abs(states[-1] * 500), abs(states[-1] * 500)  # fixed center
    radius = 20

    # make a transparent overlay for this circle
    circle_layer = Image.new("RGBA", im.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(circle_layer)

    # bounding box
    left_up = (center_x - radius, center_y - radius)
    right_down = (center_x + radius, center_y + radius)

    # draw with fixed transparency = 10 (very faint)
    draw.ellipse([left_up, right_down], fill=(255, 0, 0, 10), outline=None)

    # composite
    im = Image.alpha_composite(im, circle_layer)

# show final image
im.show()
