import argparse
from .path import validate_path


def parse_args() -> dict:
    """Parse arguments from cli

    Returns:
        dict: Paramters from cli
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--image",
        required=True,
        type=validate_path,
        metavar="image_file_path",
        help="image file path ex: selfie_image_path.[jpg|png]",
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type=int,
        choices=range(-100, 101, 1),
        metavar="[-100-100]",
        required=True,
        help="threshold of change nose or left eye",
    )

    args = vars(parser.parse_args())
    return args
