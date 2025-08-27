import streamlit as st
import os
import uuid
from io import BytesIO
import uuid
from PIL import Image, ImageDraw, ImageFont
from modules.swecha import get_categories, upload_file

TELUGU_FONT_PATH = os.path.join("fonts", "NotoSansTelugu-Regular.ttf")
MEME_FOLDER = "uploads"
os.makedirs(MEME_FOLDER, exist_ok=True)

def load_telugu_font(size):
    try:
        return ImageFont.truetype(TELUGU_FONT_PATH, size)
    except OSError:
        st.warning("⚠ Telugu font not found, using default font.")
        return ImageFont.load_default()

def draw_text_with_stroke(draw, text, font, image_width, y):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (image_width - text_width) / 2
    draw.text((x, y), text, font=font, fill="white", stroke_width=3, stroke_fill="black")

def run():
    
    st.title("🎨 Meme Generator (Telugu Supported)")
    title = st.text_input("Top Text (Telugu supported)")
    description = st.text_input("Bottom Text (Telugu supported)")
    file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if st.button("Generate Meme"):
        if not file:
            st.warning("Please upload an image file to generate meme.")
            return

        image = Image.open(file).convert("RGB")
        meme = image.copy()
        draw = ImageDraw.Draw(meme)

        font_size = max(40, meme.height // 15)
        font = load_telugu_font(font_size)

        if title:
            draw_text_with_stroke(draw, title, font, meme.width, 10)

        if description:
            draw_text_with_stroke(draw, description, font, meme.width, meme.height - font_size - 10)

        buffer = BytesIO()
        meme.save(buffer, format="PNG")   # or "PNG"
        buffer.name = f"{str(uuid.uuid4())}.png"
        buffer.type = "image/png"
        buffer.seek(0)

        st.image(meme, caption="Generated Meme", use_container_width=True)

        # file upload 
        res = upload_file(buffer)

        # Create record to upload with file value 
        


        st.write(res)