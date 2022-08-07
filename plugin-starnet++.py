#!/usr/bin/env python

'''
Gimp plugin "Starnet++"
This plugin does the following:
- Copy visible and paste it to a new temporary image.
- Set temporary precision to 16 bit integer.
- Flatten the temporary image.
- Export the temporary to a temporary TIF file.
- Run Starnet++ on the temporary TIF file
- Load Starnet++ output file into a new layer named "starless"
- Temporary files are then removed.
'''

from gimpfu import *
import os
import tempfile
import subprocess

STARNET_DIR = "D:\\Apps\\StarNetv2CLI_Win"
STARNET_BINARY = "starnet++.exe"
#STARNET_DIR = "/home/xxxxx/StarNetv2CLI_linux"
#STARNET_BINARY = "starnet++"

STARNET_DEFAULT_TILESIZE = 256

def plugin_main(image, drawable, tile_size):

    tmpdir = tempfile.gettempdir()
    tmpinfile = os.path.join(tmpdir, "starnet-stars.tif")
    tmpoutfile = os.path.join(tmpdir, "starnet-starless.tif")

    pdb.gimp_edit_copy_visible(image)
    tmpImage = pdb.gimp_edit_paste_as_new_image()
    pdb.gimp_image_convert_precision(tmpImage, 250)
    tmpLayer = pdb.gimp_image_flatten(tmpImage)
    pdb.file_tiff_save(tmpImage, tmpLayer, tmpinfile, tmpinfile, 0)
    pdb.gimp_image_delete(tmpImage)

    os.chdir(STARNET_DIR)
    proc = subprocess.Popen([
        os.path.join(STARNET_DIR, STARNET_BINARY),
        tmpinfile,
        tmpoutfile,
        str(tile_size)
        ])
    proc.communicate()

    starless_layer = pdb.gimp_file_load_layer(image, tmpoutfile)
    pdb.gimp_layer_set_name(starless_layer, 'starless')
    image.add_layer(starless_layer)
    os.remove(tmpinfile)
    os.remove(tmpoutfile)

    return


register(
    "python_fu_starnetplusplus",
    "Run Starnet++ on the current visible",
    "Run Starnet++ on the current visible",
    "PigeonD",
    "Copyright 2022",
    "2022",
    "Starnet++...",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input drawable", None),
        (PF_INT, "tile_size", "Tile size", STARNET_DEFAULT_TILESIZE),
    ],
    [],
    plugin_main,
    menu="<Image>/Filters",
    )

main()

