import os

# 图片目录路径
img_dir = './images'

# HTML文件名
html_file = 'index.html'

# HTML基础结构
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery</title>
</head>
<body>
    <h1>Image Gallery</h1>
    {} <!-- 图片标签将插入在这里 -->
</body>
</html>
'''

# 收集所有图片标签的HTML代码
img_tags = ""
for i in range(1, 6):
    img_path = os.path.join(img_dir, f'image{i}.jpg')
    img_tag = f'<img src="{img_path}" alt="Image {i}">\n'
    img_tags += img_tag

# 将图片标签插入到HTML基础结构中
final_html_content = html_content.format(img_tags)

# 写入HTML文件
with open(html_file, 'w', encoding='utf-8') as file:
    file.write(final_html_content)

print(f'HTML file "{html_file}" created successfully!')
