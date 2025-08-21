***
# Image Compression Script

This script compresses a JPEG image to ensure its size is under 1 MB using Python and the Pillow library.

## Prerequisites

- Python 3.x installed
- Pillow library installed

You can install Pillow using pip:

```bash
pip install Pillow
```


## Usage

1. **Save your image** as `IMG_3291.jpg` in the same directory as the script.
2. **Copy and save the below script** as `compress_image.py`:
```python
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
print(f'Final image size: {size_kb} KB, Quality: {quality}')
```

3. **Run the script** from your terminal:
```bash
python compress_image.py
```

4. **Check the output**
A new file named `IMG_3291_compressed.jpg` will be created in the same directory, compressed to less than 1 MB.

***
