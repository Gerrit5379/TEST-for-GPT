# Brock — 76 mm, CR-10S Pro V2, 0.4 mm nozzle

[Download the revised project](https://github.com/Gerrit5379/TEST-for-GPT/raw/refs/heads/main/brock-76mm/Brock_76mm_0p4_Selective_Supports.3mf). Open it **as a project in Creality Print**, retaining the embedded printer, filament, process and support painting. Slice before printing. The original 0.2 mm project remains available separately.

The printer is the **Creality CR-10S Pro V2**, with its stock Bowden arrangement and BLTouch, a **0.4 mm nozzle**, **1.75 mm SUNLU PLA+**, and **textured PEI**. The model stays upright and **76.00 mm tall including its original base**. The complete model XML, placement and support painting are byte-identical to the original project: 598,524 vertices, 1,197,120 triangles, with 4,872 triangles painted as support enforcers and 1,192,248 as blockers. The 25 selected support patches are retained; no automatic repainting, smoothing, decimation or scaling was applied.

## Detail and removal settings

| Setting | Revised value |
|---|---|
| Layer height / first layer | 0.08 / 0.16 mm |
| Outer / general / first-layer width | 0.40 / 0.42 / 0.45 mm |
| Support width | 0.40 mm |
| Walls / infill | 3 / 12% gyroid |
| Top / bottom shells | 10 layers, minimum 0.8 mm |
| Wall generator / seam | Arachne / rear |
| Outer / inner / top speeds | 18 / 25 / 15 mm/s |
| First-layer speed | 8 mm/s |
| Outer-wall / default acceleration | 200 / 500 mm/s² |
| Nozzle, first / later | 210 / 205 °C |
| Textured PEI, first / later | 65 / 60 °C |
| Flow / maximum volumetric flow | 1.00 / 3 mm³/s |
| Retraction / retract speed / return speed | 4.5 mm / 35 / 30 mm/s |
| Cooling | Off for first 3 layers, full by layer 8 |
| Brim | 8 mm, outer only, zero gap |
| Supports | Manual painted organic trees, enabled |
| Top / bottom Z gaps | 0.24 / 0.24 mm |
| XY separation / priority | 0.45 mm / Z over XY |
| Top / bottom interface layers | 2 / 2 |
| Top interface spacing | 0.50 mm |
| Tree tip / branch wall count | 0.60 mm / 1 |

The widths now match a 0.4 mm nozzle. Fine layers and slow outer walls prioritize detail; the 0.24 mm contact gaps, sparse interfaces and single-wall trees prioritize release. The wider nozzle cannot reproduce every tiny curl or ornament possible with the original 0.2 mm nozzle. Sparse contacts can leave rough undersides or allow tiny tips to droop. These settings are a practical starting profile, not physically calibrated results for this spool and machine.

The start sequence explicitly sets absolute XYZ and relative extrusion, heats the bed, homes, and runs `G29` with the stock BLTouch before final nozzle heating and purging. It therefore probes a fresh mesh rather than assuming a saved mesh survives homing. The end sequence retracts, lifts 10 mm, presents the bed and turns heaters and fan off. End-script Unicode paragraph separators from the original were replaced with normal newlines.

Allow the PEI plate to cool before releasing the brim. Clip tree trunks into short sections, support each nearby finger, earring or cloth tip, and cut contacts individually. Avoid pulling an entire tree against fine features. Check first-layer adhesion and the Bowden retraction on your actual printer.

## Digital slice validation

Creality Print **7.3.0.6157** completed a full slice with return code **0**, `Success.`, **1,197,120 triangles**, and an **empty final warning message**. Its organic-support engine logged noncritical placeable-area cache/performance diagnostics; these did not prevent slicing or G-code export.

- **949 layers**, ending at **Z = 76.00 mm**.
- Estimated print time: **14h 27m 51s**.
- Estimated total filament: **21.32 g**; support and interface extrusion: approximately **2.22 g**.
- Generated both organic support and support-interface toolpaths from the retained manual painting.
- Extruding toolpath centers occupy X **117.032–182.951**, Y **117.043–182.960**, Z **0.16–76.00 mm**, comfortably inside the 300 × 300 × 400 mm build volume, including line width. End moves reach only Z 86 mm and Y 290 mm.
- Exported G-code settings confirm the 0.4 mm nozzle, actual line widths, layer heights, temperatures, textured PEI, manual organic supports and contact gaps.

[Validation report](validation_0p4.json) · [Reference process preset](Brock_0p4_Detail_Process.json) · [Front supports](supports_0p4_front.png) · [Rear supports](supports_0p4_back.png)

The previews show green support paths and orange interface paths sampled every third layer, over the unchanged grey source mesh. They demonstrate support placement; the grey surface does not simulate which fine features survive extrusion. Estimates are not measurements. **No physical print or support-removal test has been performed.** Re-slice the project for your printer rather than using G-code from an unverified machine profile.
