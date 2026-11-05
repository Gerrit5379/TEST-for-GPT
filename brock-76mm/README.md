# Brock — 76 mm detail project

[Open the project file page](https://github.com/Gerrit5379/TEST-for-GPT/blob/main/brock-76mm/Brock_76mm_0p2_Selective_Supports.3mf), then click **Download raw**. Open the downloaded 3MF **as a project** in Creality Print and keep its embedded settings and painting. Slice the plate before printing. Do not change support mode to automatic or import the file as geometry only.

## Setup

Creality CR-10S Pro V2, 0.2 mm nozzle, 1.75 mm SUNLU PLA+, textured PEI. Upright model, 76 mm including the original base. All original geometry is retained: no smoothing, decimation, or removal of fine details. Both source meshes are closed; base and figure remain registered.

This carries forward the Gerrit minimal-support profile as the starting point; it is not a physically calibrated optimum for every spool or feature. The included process JSON is a reference preset. The 3MF contains the model, support painting, printer and filament settings needed for this project.

| Setting | Value |
|---|---|
| Layer height / first layer | 0.06 / 0.12 mm |
| Normal / first-layer line width | 0.22 / 0.25 mm |
| Walls / sparse infill | 4 / 12% |
| Outer / inner wall speed | 18 / 25 mm/s |
| First-layer speed | 8 mm/s |
| Nozzle temperature | 205 C first, 200 C thereafter |
| Textured PEI bed | 65 C first, 60 C thereafter |
| Retraction | 4.5 mm at 35 mm/s; return 30 mm/s |
| Flow ratio / max volumetric flow | 1.00 / 1.5 mm3/s |
| Cooling | Off for first 6 layers, full by layer 15 |
| Brim | 8 mm, zero gap |
| Seam / wall generator | Rear / Arachne |
| Supports | Organic trees, painted manual regions only |
| Top / bottom support gap | 0.24 / 0.24 mm |
| Support XY separation | 0.45 mm |
| Support distance priority | Z over XY, to reach small underside patches |
| Top interface | 2 layers, 0.45 mm spacing |
| Branch wall count / tip diameter | 1 / 0.5 mm |

## Supports and removal

The 25 selected patches target floating cloth curls, the lowest points of fingers and earrings, and two lower hair lobes. Most hair, the face, torso, and ornamental cloth surfaces are blocked from support generation. Unlike the earlier dwarf, Brock has multiple fine features that start above empty space; eliminating all contacts there risks losing those features. Support placement was selected from the full mesh and inspected in the generated toolpath preview.

The wide separation and sparse interfaces favor removal. They can leave rougher undersides or allow tiny unsupported curl tips to droop. A 0.2 mm nozzle still has physical limits at this scale. Support removal and the print itself have not been physically tested. Cut trunks into short sections, stabilize the adjacent feature, and clip small contacts individually rather than pulling a complete tree against fingers, earrings or cloth tips.

## Digital validation

Creality Print 7.3.0.6157 sliced the complete project successfully, with all 1,197,120 triangles and an empty final warning message. Estimated print time: **1d 3h 20m 21s**. Estimated total filament: **17.62 g**, including approximately **1.47 g** of extruding support paths (1.75 mm PLA at 1.24 g/cm3). Estimates are not measured results.

[Front support preview](supports_front.png) · [Rear support preview](supports_back.png) · [Validation](validation.json)

Green lines show generated G-code support paths sampled every third layer, over the unchanged grey model; they do not show every printed layer. Original unpainted previews are included as model_front.png and model_back.png.
