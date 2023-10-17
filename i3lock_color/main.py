#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
█░░ █▀█ █▀▀ █▄▀  █▀ █▀▀ █▀█ █▀▀ █▀▀ █▄░█ ▀
█▄▄ █▄█ █▄▄ █░█  ▄█ █▄▄ █▀▄ ██▄ ██▄ █░▀█ ▄
https://github.com/Raymo111/i3lock-color
-- -- -- -- -- -- -- -- -- -- -- -- -- --
Usage: i3lock-run [-h] [-s SCHEME] [-а FONT] [-t] [-v]

Wrapper over i3lock-color with a choice of color schemes

options:
  -h,        --help              show this help message and exit
  -s SCHEME, --scheme  SCHEME    set color scheme name
  -f FONT,   --font    FONT      set font style
  -t,        --themes            show available themes
  -v,        --version           show version


The script wraps i3lock-color and uses the configuration I'm using.
The script is packaged as a package for a future extension
so that some options can be changed.

Color schemes are already set.
For portability, I copied all 35 color schemes here
previously collected in the library.
base16-colorlib (pip install base16-colorlib).
The library contains a collection of popular color schemes as well
as the Color class which can help change the color tints (HSL)
of individual elements.

Dependencies:
-- -- -- --
- i3lock-color
"""


# █▀▄▀█ █▀▀ ▀█▀ ▄▀█ ▀
# █░▀░█ ██▄ ░█░ █▀█ ▄
# -------------------
__author__ = "MOIS3Y"
__credits__ = ["Stepan Zhukovsky"]
__license__ = "GPL v3.0"
__version__ = "0.1.0"
__maintainer__ = "Stepan Zhukovsky"
__email__ = "stepan@zhukovsky.me"
__status__ = "Production"


import argparse
import subprocess

from .colors import color_schemes


def i3lock_run(colors, font):
    try:
        subprocess.run([
            # bin:
            'i3lock',
            # params:
            '--screen=1',
            '--blur=2',
            '--clock',
            '--indicator',
            '--line-uses-ring',
            '--radius=110',
            '--ring-width=9',
            '--keylayout=1',
            # colors:
            f'--insidever-color={colors["base02"]}',    # surface
            f'--insidewrong-color={colors["base02"]}',  # surface
            f'--inside-color={colors["base00"]}',       # crust
            f'--ringver-color={colors["base0B"]}',      # green
            f'--ringwrong-color={colors["base08"]}',    # red
            f'--ringver-color={colors["base0B"]}',      # green
            f'--ringwrong-color={colors["base08"]}',    # red
            f'--ring-color={colors["base02"]}',         # surface
            f'--keyhl-color={colors["base0D"]}',        # blue
            f'--bshl-color={colors["base0A"]}',         # yellow
            f'--verif-color={colors["base0B"]}',        # green
            f'--wrong-color={colors["base08"]}',        # red
            f'--layout-color={colors["base0D"]}',       # blue
            f'--separator-color={colors["base05"]}',    # text
            f'--date-color={colors["base05"]}',         # text
            f'--time-color={colors["base05"]}',         # text
            f'--modif-color={colors["base05"]}',        # text
            # font:
            f'--time-font={font}',
            f'--date-font={font}',
            f'--layout-font={font}',
            f'--verif-font={font}',
            f'--wrong-font={font}',
            # text:
            '--time-str=%T',  # %I:%M %p (am/pm)
            '--date-str=%a, %e %b %Y',
            '--verif-text=Verifying...',
            '--wrong-text=Auth Failed',
            '--noinput=No Input',
            '--lock-text=Locking...',
            '--lockfailed=Lock Failed',
            # pass keys:
            '--pass-media-keys',
            '--pass-screen-keys',
            '--pass-volume-keys',
        ])
    except FileNotFoundError as error:
        print(f"i3lock not found.\n{error}")


def show_themes(**color_schemes):
    for scheme in [scheme for scheme in color_schemes]:
        print(scheme)


# entrypoint:
def main():
    parser = argparse.ArgumentParser(
        description='Wrapper over i3lock-color with a choice of color schemes'
    )
    parser.add_argument(
        '-s',
        '--scheme',
        type=str,
        help='set color scheme name'
    )
    parser.add_argument(
        '-f',
        '--font',
        default='Sans',
        type=str,
        help='set font style'
    )
    parser.add_argument(
        '-t',
        '--themes',
        action='store_true',
        help='show available themes'
    )
    parser.add_argument(
        '-v',
        '--version',
        action='store_true',
        help='show version'
    )
    args = parser.parse_args()

    # Show version:
    if args.version:
        print(__version__)
    # Show available color schemes:
    elif args.themes:
        show_themes(**color_schemes)
    # Run lockscreen:
    elif args.scheme:
        if args.scheme in color_schemes:
            i3lock_run(colors=color_schemes[args.scheme], font=args.font)
        else:
            print(f'Scheme - {args.scheme} not found. Available:')
            show_themes(**color_schemes)
    else:
        i3lock_run(
            colors=color_schemes['catppuccin_mocha'],
            font='Sans'
        )


if __name__ == "__main__":
    main()
