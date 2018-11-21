from PIL import Image, ImageDraw, ImageFont
import random
# 获取随机颜色的函数
def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

# 生成一个图片对象
img_obj = Image.new(
    'RGB',
    (220, 35),
    get_random_color()
)
img_obj.show()

draw_obj = ImageDraw.Draw(img_obj)
font_obj = ImageFont.truetype("static/font/kumo.ttf",28)