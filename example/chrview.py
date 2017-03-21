#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

from PIL import Image

import neschr


PALETTE = ( 0x00, 0x27, 0x21, 0x30 )


def usage():
    sys.exit("Usage: chrview <CHR>")


def main():
    if len(sys.argv) != 2: usage()

    buf = open(sys.argv[1], "rb").read(4096)
    assert len(buf) == 4096

    decoder = neschr.TileDecoder()
    tiles = decoder.read_tile_table(buf, PALETTE, transparent=True)

    img = Image.new("RGBA", (8*16, 8*16))
    for i, tile in enumerate(tiles):
        x = 8 * (i %  16)
        y = 8 * (i // 16)
        img.paste(tile, (x,y), tile)

    img.show()

if __name__ == "__main__": main()
