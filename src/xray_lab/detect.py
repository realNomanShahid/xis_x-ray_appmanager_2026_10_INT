"""Simple region detection."""
import cv2
import numpy as np

from .filters import to_gray


def find_bright_regions(image: np.ndarray, threshold: int = 200, min_area: int = 100):
    """Find bright blobs and return a list of (x, y, w, h) boxes."""
    gray = to_gray(image)
    _, mask = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxes = [cv2.boundingRect(c) for c in contours if cv2.contourArea(c) >= min_area]
    return sorted(boxes)


def draw_boxes(image: np.ndarray, boxes) -> np.ndarray:
    """Return a colour copy of the image with green rectangles drawn."""
    out = image.copy()
    if out.ndim == 2:
        out = cv2.cvtColor(out, cv2.COLOR_GRAY2BGR)
    for (x, y, w, h) in boxes:
        cv2.rectangle(out, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return out
