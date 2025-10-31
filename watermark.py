from PIL import Image
from os import listdir
from pathlib import Path

def calc_watermark_size(image, watermark):
    image_ratio = image.size[0] / image.size[1]
    print(f"image ratio: {image_ratio}")

    if image_ratio > 1:
        watermark_ratio = watermark.size[1] / watermark.size[0]
        print(f"watermark ratio: {watermark_ratio}")
        watermark_size_x = image.size[0] * 0.2
        return (int(watermark_size_x), int(watermark_size_x * watermark_ratio))
    else:
        watermark_ratio = 1 / (watermark.size[0] / watermark.size[1])
        print(f"watermark ratio: {watermark_ratio}")
        watermark_size_y = image.size[1] * 0.2
        return (int(watermark_size_y), int(watermark_size_y * watermark_ratio))

def main():
    supported_file_types = ["jpg", "jpeg", "png"]
    watermark = Image.open("watermark.png")
    input_dir = "input"
    output_dir = "output"

    Path(output_dir).mkdir(exist_ok=True)

    for filename in listdir(input_dir):
        print("--")
        print(filename)
        if not "." in filename or not filename.split(".")[-1] in supported_file_types:
            print("not a valid file")
            continue
        
        image = Image.open(f"{input_dir}/{filename}")
        watermark_resized = watermark.resize(calc_watermark_size(image, watermark))
        y = image.size[1] - watermark_resized.size[1]
        print(f"y: {y}")
        image.paste(watermark_resized, (0, y), watermark_resized)
        image.save(f"{output_dir}/{filename}")

main()