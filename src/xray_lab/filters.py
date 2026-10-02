"""Image filters."""
import cv2
import numpy as np


def to_gray(image: np.ndarray) -> np.ndarray:
    """Convert a BGR image to grayscale (no-op if already gray)."""
    if image.ndim == 2:
        return image
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def enhance_contrast(image: np.ndarray, clip_limit: float = 2.0, tile: int = 8) -> np.ndarray:
    """Improve local contrast with CLAHE. Returns a grayscale image."""
    gray = to_gray(image)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(tile, tile))
    return clahe.apply(gray)


def detect_edges(image: np.ndarray, low: int = 80, high: int = 200) -> np.ndarray:
    """Canny edge detection. Returns a binary edge map."""
    gray = to_gray(image)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return cv2.Canny(blurred, low, high)
