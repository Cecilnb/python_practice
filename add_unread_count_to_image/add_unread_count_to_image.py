from PIL import Image, ImageDraw, ImageFont

# 打开图像
image_path = '1.png'  # 替换为您的图像路径
image = Image.open(image_path)

# 在图像上绘制红色数字
unread_count = 10  # 替换为您想要显示的未读消息数量
draw = ImageDraw.Draw(image)

# 计算适当的字体大小
font_size = int(min(image.size) / 6)   # 字体在图片上的绘制大小大概是 1/36

# 指定要使用的字体文件的路径
font_path = 'Arial.ttf'
font_obj = ImageFont.truetype(font_path, font_size, encoding='utf-8')

# 要绘制的文本内容
text = str(unread_count)

# 计算文本位置，将文本绘制在图像右上角，保持一定的距离
x = image.size[0] - font_size - 10
y = -2

# 绘制红色文本
draw.text((x, y), text=text, fill=(255, 0, 0), font=font_obj, anchor=None)

# 保存处理后的图像
output_image_path = 'output_image.jpg'  # 替换为输出图像的路径
image.save(output_image_path)

# 打印处理完成的消息
print("图像处理已完成并保存到:", output_image_path)
