# Felix and portal — original foliage, 76 mm

[Download the project](https://github.com/Gerrit5379/TEST-for-GPT/raw/refs/heads/main/felix-portal-76mm/Felix_76mm_0p4_Selective_Supports.3mf). Open the 3MF **as a project in Creality Print**, retaining its embedded printer, filament, process and support painting, then slice before printing.

This project retains **all the original leaves, branches, figure and portal geometry** from the 14 uploaded OBJ parts. The complete composition is upright and uniformly scaled to **76.00 mm tall**, including its base. No leaves were pruned, thickened or re-angled; no smoothing or decimation was applied. Source polygons were triangulated for 3MF. Both source meshes remain registered, with 2,716,537 vertices and 5,439,054 triangles in total.

## Printer and detail profile

**Creality CR-10S Pro V2**, stock Bowden arrangement and BLTouch, **0.4 mm nozzle**, **1.75 mm SUNLU PLA+**, **textured PEI**.

| Setting | Value |
|---|---|
| Layer height / first layer | 0.08 / 0.16 mm |
| Outer / general / first-layer line widths | 0.40 / 0.42 / 0.45 mm |
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
| Retraction / retract / return speed | 4.5 mm / 35 / 30 mm/s |
| Cooling | Off for first 3 layers, full by layer 8 |
| Brim | 8 mm, outer only, 0.1 mm gap |
| Supports | Manual painted organic trees, from build plate only |
| Top / bottom Z gaps | 0.24 / 0.24 mm |
| XY separation / priority | 0.50 mm / Z over XY |
| Top / bottom interface layers | 2 / 2 |
| Top interface spacing | 0.45 mm |
| Tree tip / branch wall count | 0.60 mm / 1 |

The start sequence sets absolute XYZ and relative extrusion, heats the bed, homes, probes a fresh mesh with `G29`, and then heats the nozzle for purging. This assumes the stock CR-10S Pro V2 BLTouch and firmware. The end sequence retracts, raises Z 10 mm, presents the bed and turns heaters and fan off.

## Selective supports and removal

The painted regions target isolated print starts and broad near-horizontal undersides, including the foliage, hands, garment details and branches. The other triangles are blocked. Keep **manual tree** mode when opening the project; importing geometry alone loses the painting.

The original foliage creates many small print starts. These leaf clusters need many individual contacts to preserve their small features. This project uses a selective setup, with sparse interfaces and 0.24 mm contact gaps to help release. It uses approximately **19% less support extrusion** than the automatic-tree reference slice of the original model. That comparison is an estimate, not a physical removal test.

After cooling, cut the trunks into short pieces. Stabilize each adjacent leaf or finger and clip individual contacts; avoid pulling a complete tree through the canopy. Inspect first-layer adhesion and calibrate flow, temperature and retraction on the actual spool and printer.

## Digital validation and limitations

Creality Print **7.3.0.6157** sliced the complete original-leaf project successfully. It completed **949 layers to Z 76.00 mm**, estimating **1d 14h 49m 47s**, **51.61 g total filament**, and approximately **8.96 g of support/interface extrusion**. The fresh delivered-file slice retains the earlier original geometry and effective settings; small variations in organic-tree generation change the estimates slightly between runs. See [validation.json](validation.json) for the delivered project checksum, slice outcome, effective settings, geometry checks and estimates.

[Original front](model_front.png) · [Original rear](model_back.png) · [Support front](supports_front.png) · [Support rear](supports_back.png) · [Reference process preset](Felix_0p4_Detail_Process.json)

Green lines show generated support paths and orange lines show interfaces, sampled every fourth layer over the unchanged grey source mesh. The grey surface is not a simulation of printed detail. The run logged 15 possible branch-routing fallback diagnostics while producing an empty final warning message. The final generated support views were inspected; this does not verify contact or release at every tiny feature physically. Fine leaves and ornaments can be thinner than the nozzle width, and neither support release nor the survival of every small feature has been physically verified. These are starting settings for a detailed FDM print, with the original model preserved.
