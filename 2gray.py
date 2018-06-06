# import cv2
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from multiprocessing import Pool, freeze_support
import time
# image = cv2.imread(r'C:\Users\Dinh Anh Vu\Downloads\end-hed.jpg')

# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow('color_image', image)
# cv2.imshow('gray_image', gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

levels = " .:-=+*#%@"
levels_contrast = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''


# img.show()

# img = Image.open(r'C:\Users\Dinh Anh Vu\Downloads\end-hed.jpg')
# img.show()
# print(img.size)
# enh = ImageEnhance.Contrast(img)
# enh.enhance(2).show('30% more contrast')

def get_text(img):
    text = ''
    width, height = img.size
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            index = int(pixel[0]//25.5)
            index -= 0 if index == 0 else 1
            character_representation = levels[index]
            text += character_representation
        text += '\n'
    return text


def foo(index):
    # img = Image.open('sample-fullhd.jpg')
    img = Image.open('sample.jpg')
    img = img.convert('LA')
    # img = img.rotate(90, expand=True).resize((60, 90))
    fnt = ImageFont.truetype('fonts/Montserrat-Light.ttf', 1)
    # txt = Image.new('RGBA', img.size, (255, 255, 255, 1))
    txt = Image.new('RGB', img.size, (255, 255, 255))
    d = ImageDraw.Draw(txt)
    # with open('output/out{}.txt'.format(index), 'w') as file:
    #     print(img.size)
    #     width, height = img.size
    #     for y in range(height):
    #         for x in range(width):
    #             # print(img.getpixel((0,1)))
    #             # file.write(levels_contrast[int(img.getpixel((x,y))[0]//3.64)])
    #             pixel = img.getpixel((x, y))
    #             index = int(pixel[0]//25.5)
    #             # index = int(pixel[0]//(255 / 70))
    #             index -= 0 if index == 0 else 1
    #             character_representation = levels[index]
    #             d.text((x, y), character_representation,
    #                    font=fnt, fill=(0, 0, 0))
    #             # character_representation = levels_contrast[index]
    #             # file.write(character_representation)
    #         # file.write('\n')
    img_text = get_text(img)
    with open('output/out.txt', 'w') as file:
        file.write(img_text)
    d.multiline_text((0, 0), img_text, font=fnt, fill=(0, 0, 0))
    txt.show()


def main():
    # start = time.time()
    # indexes = [i for i in range(100)]
    # # freeze_support()
    # with Pool(processes=10) as pool:
    #     pool.map(foo, indexes)
    #     pool.close()
    #     pool.join()

    # print('{}'.format(time.time() - start))
    foo(0)


if __name__ == '__main__':
    main()
