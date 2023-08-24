# gimp-plugin-starnet - GIMP plugin to run Starnet++  

### This plugin does the following:
- Copy visible and paste it to a new temporary image.
- Set the temporary image precision to 16 bit integer.
- Flatten the temporary image.
- Export a temporary TIF file.
- Run Starnet++ on the temporary TIF file.
- Load Starnet++ output file into a new layer named "starless".
- Temporary files are then removed.

### Support
Tested on Windows and Linux. Hopefully works on MacOS too?

### Installation
- Download the latest [plugin-starnet++.py](https://raw.githubusercontent.com/pigeond/gimp-plugin-starnet/master/plugin-starnet%2B%2B.py).
- Windows: Copy `plugin-starnet++.py` into `%APPDATA%\Roaming\GIMP\2.10\plug-ins\` (Example: `C:\Users\Pigeon\AppData\Roaming\GIMP\2.10\plug-ins\`)

  Linux: Copy `plugin-starnet++.py` into `$HOME/.config/GIMP/2.10/plug-ins/`. Then make sure it is executable, for example, by running `chmod +x $HOME/.config/GIMP/2.10/plug-ins/plugin-starnet++.py` at the shell.
- Edit `plugin-starnet++.py` and set `STARNET_DIR` and `STARNET_BINARY` to the appropriate path and binary name. Examples are in the code.

### Starnet++ installation
- Download at https://www.starnetastro.com/download/

### Quick demo
[Video on Instagram](https://www.instagram.com/p/Cg-pwT_pL7N/)
