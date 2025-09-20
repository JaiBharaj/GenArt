from PIL import Image
import cmath

# Image settings
width, height = 50000, 50000
im = Image.new("RGB", (width, height), "black")
pixels = im.load()

# Complex plane bounds
xmin, xmax = -2, 2
ymin, ymax = -2, 2

count = 0

# Iteration settings
max_iter = 200
escape_radius = 4

# Define iteration function (Julia-type)
# Try changing c for different patterns
c = complex(-0.7, 0.27015)

def f(z):
    # return (z**2 - 1)**2 + c
    return (z**4 - 1) ** 2 - (z**2 - 1)**2 + c

for x in range(width):
    for y in range(height):
        # Map pixel to complex plane
        zx = xmin + (x / width) * (xmax - xmin)
        zy = ymin + (y / height) * (ymax - ymin)
        z = complex(zx, zy)

        # Iterate
        i = 0
        while abs(z) < escape_radius and i < max_iter:
            z = f(z)
            i += 1

        # Color based on iterations before escape
        color = (i * 9 % 256, i * 7 % 256, i * 13 % 256)
        count += 1
        if count % 1000000 == 0:
            print(f"Pixel Count: {count}")
        pixels[x, y] = color

# Show/save
im.show()
im.save("complex_fract_high_res.png")
