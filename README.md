# i3lock-color-wrapper

Pre-configured script to run i3lock-color with the ability to change the color scheme and some parameters

![image info](https://raw.githubusercontent.com/MOIS3Y/i3lock-color-wrapper/assets/i3lock-color-wrapper.png)

## What is it ?

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

## Usage:

```sh
Usage: i3lock-run [-h] [-s SCHEME] [-а FONT] [-t] [-v]

Wrapper over i3lock-color with a choice of color schemes

options:
  -h,        --help              show this help message and exit
  -s SCHEME, --scheme  SCHEME    set color scheme name
  -f FONT,   --font    FONT      set font style
  -t,        --themes            show available themes
  -v,        --version           show version
```

## Example:

```sh
i3lock-run --scheme catppuccin_mocha --font Inter
```

