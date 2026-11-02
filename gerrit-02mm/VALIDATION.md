# Validation and estimates

The two exact final 3MF files were reopened and sliced in Creality Print
7.3.0.6157 without external printer, process or filament files. Its GUI-equivalent
preset merge retained the custom 0.2 mm machine and the Fine Detail process.
Both exports completed with return code 0, Success, and no final plate warnings.

| Project height, including base | Slicer time estimate | Total PLA estimate |
|---|---|---|
| 76 mm | 2d 8h 17m 26s | 37.20 g |
| 152 mm | 9d 22h 20m 13s | 184.65 g |

The small support-removal test is estimated at 1 h 30 min and 1.27 g PLA. These
are slicer estimates, not measured printing time, weight or removal force.

The actual exported G-code was checked for 0.2 mm nozzle diameter; 0.04–0.12 mm
machine layer limits; 0.06 mm object layers; 0.22 mm extrusion and support widths;
4 model walls; enabled organic supports; 0.16 mm support Z gaps; 0.25 mm XY gaps;
0.6 mm support tips; 2 support walls; 2° trunk growth; 1.5 mm³/s filament flow
limit; 200/205°C nozzle temperatures; and disabled travel avoidance.

Both model reports contain 2,744,599 input triangles. The 3MF model XML, including
its geometry and placement, is byte-identical to the earlier 0.4 mm project at
the same height. The original model was not smoothed, simplified or resculpted.

The small support test also reopened and exported successfully. Its G-code
contains actual support and interface paths with the intended 0.2 mm nozzle,
0.06 mm layers and 0.16 mm contact gap. Its 0.3, 0.4 and 0.5 mm raised bars provide
a small real-world fine-feature check after printing.

The optional 0.04 mm process was checked by exporting a closed 10 mm cube.
The full character was not sliced or printed with that optional preset. Do not
reuse the main projects' time estimates for 0.04 mm printing.

No physical printing, flow calibration, support-removal test or surface-finish
inspection has been performed. "Fine Detail" is the profile's intended use,
not a claim of experimentally optimal settings for every PLA spool or nozzle.

validation.json records effective settings, underlying runner results, exact
project hashes and the unchanged model-geometry hashes.
