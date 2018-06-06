from PIL import Image, ImageDraw, ImageFont
# # get an image
# base = Image.open('sample.jpg').convert('RGBA')

# # make a blank image for the text, initialized to transparent text color
# txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

# # get a font
# fnt = ImageFont.truetype('fonts/Montserrat-Light.ttf', 99)
# # get a drawing context
# d = ImageDraw.Draw(txt)

# # draw text, half opacity
# d.text((10, 10), "Hello", font=fnt, fill=(255, 255, 255, 128))
# # draw text, full opacity
# d.text((10, 60), "World", font=fnt, fill=(255, 255, 255, 255))

# d.multiline_text((10, 70), "hello\nbaebae",
#                  font=fnt, fill=(255, 255, 255, 130))

# out = Image.alpha_composite(base, txt)

# out.show()


fnt = ImageFont.truetype('fonts/Montserrat-Light.ttf', 22)
txt = Image.new('RGB', (400, 600), (255, 255, 100))
d = ImageDraw.Draw(txt)
d.text((10, 50), 'asdweweweqqeqeqewqewqewqqe',
       font=fnt, fill=(255, 255, 255, 145))
txt.show()
