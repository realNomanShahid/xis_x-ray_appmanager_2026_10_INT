"""Regenerate assets/sample_xray.png (a fake, synthetic 'scan' for practice)."""
import cv2
import numpy as np

rng = np.random.default_rng(42)
img = np.full((400, 400), 60, np.uint8)
cv2.ellipse(img, (200, 200), (150, 180), 0, 0, 360, 110, -1)   # body outline
cv2.rectangle(img, (180, 60), (220, 340), 150, -1)              # "spine"
for y in range(100, 320, 40):
    cv2.ellipse(img, (200, y), (110, 14), 0, 0, 360, 130, 2)    # "ribs"
cv2.circle(img, (120, 250), 22, 235, -1)                        # bright spots
cv2.circle(img, (290, 150), 16, 240, -1)
noise = rng.normal(0, 8, img.shape)
img = np.clip(img + noise, 0, 255).astype(np.uint8)
cv2.imwrite("assets/sample_xray.png", img)
print("done")
