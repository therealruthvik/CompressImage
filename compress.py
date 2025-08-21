from PIL import Image
import io
# Load the uploaded image
with open('IMG_3291.jpg', 'rb') as f:
    img = Image.open(f)
    img = img.convert('RGB')
    # Compress image iteratively to be under 1MB
    quality = 95
    while True:
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=quality)
        size_kb = buffer.tell() / 1024
        if size_kb <= 1024 or quality <= 20:
            break
        quality -= 5
    # Save final compressed image
    with open('IMG_3291_compressed.jpg', 'wb') as out_f:
        out_f.write(buffer.getvalue())
size_kb, quality
