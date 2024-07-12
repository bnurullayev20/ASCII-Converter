import os
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "
INPUT_DIR = "images"
OUTPUT_DIR = "ascii_art"
ASCII_WIDTH = 240
ASCII_HEIGHT = 108

def resize_image(image, new_width=ASCII_WIDTH, new_height=ASCII_HEIGHT):
    return image.resize((new_width, new_height))

def grayscale_image(image):
    return image.convert("L")

def map_pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 32] for pixel in pixels])
    return ascii_str

def create_ascii_image(image_path, new_width=ASCII_WIDTH, new_height=ASCII_HEIGHT):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Невозможно открыть изображение {image_path}: {e}")
        return None
    
    image = resize_image(image, new_width, new_height)
    image = grayscale_image(image)
    ascii_str = map_pixels_to_ascii(image)
    ascii_image = "\n".join([ascii_str[index:index + new_width] for index in range(0, len(ascii_str), new_width)])
    return ascii_image

def save_ascii_image(ascii_image, output_path):
    with open(output_path, "w") as f:
        f.write(ascii_image)

def process_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)

        if os.path.isfile(input_path) and filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            print(f"Обработка файла: {filename}")
            ascii_image = create_ascii_image(input_path)
            if ascii_image:
                output_filename = f"{os.path.splitext(filename)[0]}.txt"
                output_path = os.path.join(output_dir, output_filename)
                save_ascii_image(ascii_image, output_path)
                print(f"ASCII изображение сохранено в {output_path}")
                
if __name__ == "__main__":
    process_images(INPUT_DIR, OUTPUT_DIR)
    print("Все изображения обработаны.")
