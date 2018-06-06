from PIL import Image


def get_resize(width, height):
    FIXED_WIDTH = 60
    new_height = int(height / width * FIXED_WIDTH)
    return (FIXED_WIDTH, new_height)


img = Image.open('sample.jpg')
print(img.size)
img.show()
# img.resize((100, 200)).rotate(90, expand=True).show()
img.rotate(90, expand=True).resize((60, 90)).show()
# img.show()
