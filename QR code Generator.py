import qrcode
from PIL import Image, ImageDraw, ImageFont

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# add any link for website, youtube video link between "".
qr.add_data("")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Add logo path between "".
logo_path = ""
try:
    logo = Image.open(logo_path)
except FileNotFoundError:
    print("Logo file not found. Please check the path.")
    exit()

logo_size = min(img.size[0] // 3, img.size[1] // 3)  # Logo size as a fraction of QR code size
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

logo_pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)

img.paste(logo, logo_pos, logo)

try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

draw = ImageDraw.Draw(img)

# add text which you want to display under the qr code.
text = ""

text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

img_width, img_height = img.size

total_height = img_height + text_height + 10  
new_img = Image.new("RGB", (img_width, total_height), "white")

new_img.paste(img, (0, 0))

text_x = (img_width - text_width) // 2
text_y = img_height + 5  
draw = ImageDraw.Draw(new_img)
draw.text((text_x, text_y), text, font=font, fill="black")

# add the name with .png to save it 
new_img.save(".png")
