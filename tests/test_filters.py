import numpy as np

from xray_lab import __version__
from xray_lab.detect import find_bright_regions
from xray_lab.filters import detect_edges, enhance_contrast


def test_version_format():
    parts = __version__.split(".")
    assert len(parts) == 3 and all(p.isdigit() for p in parts)


def test_contrast_keeps_shape():
    img = np.random.randint(0, 255, (64, 64), dtype=np.uint8)
    assert enhance_contrast(img).shape == (64, 64)


def test_edges_binary():
    img = np.zeros((64, 64), np.uint8)
    img[:, 32:] = 255
    edges = detect_edges(img)
    assert set(np.unique(edges)).issubset({0, 255})
    assert edges.sum() > 0


def test_detect_finds_square():
    img = np.zeros((100, 100), np.uint8)
    img[20:50, 20:50] = 255
    boxes = find_bright_regions(img)
    assert len(boxes) == 1
