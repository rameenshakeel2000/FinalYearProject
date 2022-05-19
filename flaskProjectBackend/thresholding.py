from PIL import Image
import io
import base64
import cv2
import numpy as np


def apply_adpt_thr(imgB64Bytes):
    # 1. Read the image i.e. Generate Image from base64 string
    img_out = Image.open(
        io.BytesIO(
            base64.b64decode(imgB64Bytes)
        )
    )
    # Convert to greyscale
    img_out = img_out.convert('L')
    # 2. Apply operation for thresholding
    img_array = np.asarray(img_out)
    _, thresh1 = cv2.threshold(img_array, 127, 255, cv2.THRESH_BINARY)
    img_out = Image.fromarray(thresh1)

    # 2b. Convert Back to PIL format
    # 3. Convert image back into base64 format
    buffered = io.BytesIO()
    img_out.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())

    return bytes("data:image/jpeg;base64,", encoding='utf-8') + img_str