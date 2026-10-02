"""Command line interface."""
import argparse

from . import __version__
from .detect import draw_boxes, find_bright_regions
from .filters import detect_edges, enhance_contrast
from .utils import load_image, save_image


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="xray_lab", description="Practice computer-vision toolkit")
    p.add_argument("--version", action="version", version=f"xray_lab {__version__}")
    p.add_argument("--input", required=True, help="path to input image")
    p.add_argument("--output", default="output/result.png", help="where to save the result")
    p.add_argument("--mode", choices=["contrast", "edges", "detect"], default="contrast")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    image = load_image(args.input)

    if args.mode == "contrast":
        result = enhance_contrast(image)
    elif args.mode == "edges":
        result = detect_edges(image)
    else:
        boxes = find_bright_regions(image)
        print(f"Found {len(boxes)} bright region(s): {boxes}")
        result = draw_boxes(image, boxes)

    save_image(args.output, result)
    print(f"Saved: {args.output}")
    return 0
