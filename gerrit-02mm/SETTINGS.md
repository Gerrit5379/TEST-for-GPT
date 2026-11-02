# 0.2 mm nozzle settings

The self-contained projects include the custom printer, PLA and primary process
profiles. They are intended for the stock Bowden CR-10S Pro V2. Use calibrated
direct-drive retraction instead if your printer has been converted.

| Setting | Fine-detail project value |
|---|---|
| Nozzle diameter | **0.2 mm**, explicitly set in the machine profile |
| Main layer height | **0.06 mm** |
| First layer height / width | 0.12 / 0.25 mm |
| Outer / inner / top / infill line widths | 0.22 mm |
| Support line width | 0.22 mm |
| Wall generator / walls | Arachne / 4 |
| Top / bottom shells | 10 layers, 0.60 mm nominal thickness |
| Infill | 12% gyroid |
| Outer / inner wall speed | 18 / 25 mm/s |
| Small perimeters | 50% of corresponding nominal speed |
| Top / bridge speed | 15 / 15 mm/s |
| Overhang speeds | 15 / 10 / 7 mm/s as severity increases |
| Infill speed | 30 mm/s sparse, 25 mm/s solid |
| First layer speed | 12 mm/s, 15 mm/s first-layer infill |
| Outer / inner wall acceleration | 200 / 300 mm/s² |
| First layer / top acceleration | 200 mm/s² |
| Travel | 100 mm/s, limited by the machine profile |
| Nozzle temperature | 205°C first layer, 200°C afterward |
| Bed temperature | 60°C |
| Fan | Off for first 3 layers, 100% afterward |
| Minimum layer cooling time / speed | 12 seconds / 7 mm/s |
| PLA maximum volumetric speed | 1.5 mm³/s conservative guard |
| Retraction, stock Bowden | 4 mm at 30 mm/s |
| Z-hop | 0.2 mm, inherited automatic-lift behaviour |
| Seam | Back |
| Brim | 4 mm outer brim |
| Raft / ironing / prime tower | Off |
| Geometric toolpath resolution | 0.006 mm |
| Machine layer-height limits | 0.04–0.12 mm |

The smaller nozzle increases extrusion resistance, so the profile uses lower
flow and speeds than the previous 0.4 mm setup. The flow multiplier remains 1.00
as an uncalibrated baseline; the correct multiplier and temperatures depend on
your spool, nozzle construction and extruder calibration. Follow the filament's
recommended temperature range and verify flow before committing to a long print.

## Organic supports

| Setting | Value |
|---|---|
| Type / style | Tree (auto) / Organic |
| Overhang threshold | 35° from horizontal, Creality Print convention |
| Build plate only | Off, so supports can start on the integrated base |
| Top / bottom Z gap | 0.16 / 0.16 mm |
| XY gap | 0.25 mm |
| Top / bottom interface layers | 4 / 3 |
| Top interface spacing | 0.22 mm |
| Support / interface speed | 22 / 15 mm/s |
| Tip diameter | 0.6 mm |
| Initial branch diameter | 2 mm |
| Diameter growth angle | 2° |
| Organic branch spacing | 1.5 mm |
| Maximum / preferred branch angle | 40° / 25° |
| Support walls | 2 |
| Independent support layer height | On |
| Automatic tree brim | On, configured width 4 mm |
| Critical regions only / remove small overhangs | Both off |

The 0.16 mm gap favours removal with the finer support extrusion. For a better
supported underside, test **0.12 mm** on a small supported piece. For contacts
that fuse, test **0.18–0.20 mm**, accepting more underside roughness. Keep
independent support layer height enabled and reslice after any change. These
adjustments need physical testing; no contact gap guarantees mark-free removal.

Retain **avoid crossing walls = off** (`reduce_crossing_wall=0`). That option
caused a reproducible export crash with this character in the tested Creality
Print 7.3.0.6157 build during the earlier setup. Retraction and Z-hop remain active.

## Optional 0.04 mm Ultra Fine preset

`Gerrit_0p2_Ultra_0p04.json` changes the layer height to 0.04 mm and top/bottom
shell counts to 15, retaining 0.60 mm shell thickness. Nozzle diameter, line widths
and support contact gaps remain the same. It is optional: thinner Z layers can
smooth curves further but do not make XY extrusion finer. The 0.06 mm projects
are the full-character slice-validated deliverables; Ultra Fine was validated on
a small cube only. Full-character duration and support behaviour at 0.04 mm must
be checked after selecting that preset and reslicing.

For reuse with other models, the separate machine, filament, Fine Detail and
Ultra Fine JSON presets are included. The two project files already contain all
settings needed for the main 0.06 mm workflow.
