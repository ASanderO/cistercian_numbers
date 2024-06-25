from PIL import Image, ImageDraw
import os

def draw_cistercian_number(number):
    if not (0 <= number <= 9999):
        raise ValueError("O número deve estar entre 1 e 9999.")

    img_size = 300
    stroke_width = 10
    img = Image.new('RGB', (img_size, img_size), 'white')
    draw = ImageDraw.Draw(img)

    a = (0 + stroke_width, 0 + stroke_width)
    b = (100, 0 + stroke_width)
    c = (200 - stroke_width, 0 + stroke_width)
    d = (0 + stroke_width, 100)
    e = (100, 100)
    f = (200 - stroke_width, 100)
    g = (0 + stroke_width, 200)
    h = (100, 200)
    i = (200 - stroke_width, 200)
    j = (0 + stroke_width, 300 - stroke_width)
    k = (100, 300 - stroke_width)
    l = (200 - stroke_width, 300 - stroke_width)

    def draw_line(start, end):
        draw.line([start, end], fill='black', width=stroke_width)

    draw_line((100, 0 + stroke_width / 2), (100, 300 - stroke_width / 2))

    num_str = str(number).zfill(4)

    # 1000s
    if num_str[0] == '1':
        draw_line(j, k)
    elif num_str[0] == '2':
        draw_line(g, h)
    elif num_str[0] == '3':
        draw_line(g, k)
    elif num_str[0] == '4':
        draw_line(j, h)
    elif num_str[0] == '5':
        draw_line(k, j)
        draw_line(j, h)
    elif num_str[0] == '6':
        draw_line(g, j)
    elif num_str[0] == '7':
        draw_line(g, j)
        draw_line(j, k)
    elif num_str[0] == '8':
        draw_line(j, g)
        draw_line(g, h)
    elif num_str[0] == '9':
        draw_line(h, g)
        draw_line(g, j)
        draw_line(j, k)

    # 100s
    if num_str[1] == '1':
        draw_line(k, l)
    elif num_str[1] == '2':
        draw_line(h, i)
    elif num_str[1] == '3':
        draw_line(k, i)
    elif num_str[1] == '4':
        draw_line(h, l)
    elif num_str[1] == '5':
        draw_line(h, l)
        draw_line(l, k)
    elif num_str[1] == '6':
        draw_line(i, l)
    elif num_str[1] == '7':
        draw_line(k, l)
        draw_line(l, i)
    elif num_str[1] == '8':
        draw_line(h, i)
        draw_line(i, l)
    elif num_str[1] == '9':
        draw_line(h, i)
        draw_line(i, l)
        draw_line(l, k)

    # 10s
    if num_str[2] == '1':
        draw_line(a, b)
    elif num_str[2] == '2':
        draw_line(d, e)
    elif num_str[2] == '3':
        draw_line(d, b)
    elif num_str[2] == '4':
        draw_line(a, e)
    elif num_str[2] == '5':
        draw_line(b, a)
        draw_line(a, e)
    elif num_str[2] == '6':
        draw_line(a, d)
    elif num_str[2] == '7':
        draw_line(d, a)
        draw_line(a, b)
    elif num_str[2] == '8':
        draw_line(a, d)
        draw_line(d, e)
    elif num_str[2] == '9':
        draw_line(b, a)
        draw_line(a, d)
        draw_line(d, e)

    # 1s
    if num_str[3] == '1':
        draw_line(b, c)
    elif num_str[3] == '2':
        draw_line(e, f)
    elif num_str[3] == '3':
        draw_line(b, f)
    elif num_str[3] == '4':
        draw_line(c, e)
    elif num_str[3] == '5':
        draw_line(b, c)
        draw_line(c, e)
    elif num_str[3] == '6':
        draw_line(c, f)
    elif num_str[3] == '7':
        draw_line(b, c)
        draw_line(c, f)
    elif num_str[3] == '8':
        draw_line(e, c)
        draw_line(c, f)
    elif num_str[3] == '9':
        draw_line(b, c)
        draw_line(c, f)
        draw_line(f, e)

    return img

def generate_images_for_number(number):
    for output_dir in ["cistercian_numbers/train", "cistercian_numbers/test"]:
        number_dir = os.path.join(output_dir, str(number))
        os.makedirs(number_dir, exist_ok=True)

        for i in range(100):
            img = draw_cistercian_number(number)
            img.save(os.path.join(number_dir, f"{number}_{i}.png"))

os.makedirs("cistercian_numbers/train", exist_ok=True)
os.makedirs("cistercian_numbers/test", exist_ok=True)

# Loop para gerar imagens de 1 a 49
for number in range(0, 10):
    generate_images_for_number(number)

print("Imagens geradas com sucesso!")
