# Confirmed-material R2 validation

These checks verify saved files and generated toolpaths, not physical improvement
of stringing, adhesion, debris, layer strength or support removal.

Both exact files were reopened by Creality Print 7.3.0.6157 using its GUI-equivalent
preset merge, without external settings files. The character and small test both
completed slicing and G-code export successfully, with no final plate warnings.

| Project | Slicer time estimate | PLA estimate |
|---|---|---|
| 76 mm character | 2d 13h 40m 56s | 37.28 g |
| Stringing / adhesion test | 1h 15m 11s | 0.97 g |

The exported G-code was checked for the confirmed Textured PEI Plate selection,
SUNLU PLA+ material preset, 200C steady / 205C initial nozzle target, 65C initial /
60C subsequent textured-plate target, and all R2 changes documented in README.md.
The intended 0.2 mm nozzle, 0.06 mm layers, 0.22 mm widths, 4 walls, 1.00 flow,
18 mm/s outer walls and existing support contacts were retained and checked.

The small test includes repeated actual 4.5 mm retract commands at F2100 (35 mm/s),
the 65C bed wait and the 200C nozzle command. A first-layer spacing check measured
approximately 0.237 mm median distance between the test disk's outer perimeter
and nearest brim centrelines, for nominal 0.25 mm first-layer beads. This is
consistent with a nominal touching brim, not proof of adhesion on the real plate.

The character's input count is 2,744,599 triangles, and its 3MF model XML is
byte-identical to the previous 76 mm 0.2 mm project. No geometry, detail or
placement was changed. Only machine/material/process settings changed.

The 195C generic-PLA candidate prepared before the user's material clarification
is not included. These final checks are for the confirmed 76 mm SUNLU PLA+ /
textured-PEI setup at the retained working 200C temperature.

The photo does not identify the yellow/orange pieces. A slicer file cannot remove
hotend buildup, repair a nozzle/heatbreak leak, dry filament, clean PEI or choose
the correct physical Z-offset. Follow the checks in CHANGES.md and use the small
test before the long print. No revised physical print has been inspected.

validation.json contains the runner results, effective settings, unchanged model
hash and SHA-256 hashes of the exact downloadable projects.
