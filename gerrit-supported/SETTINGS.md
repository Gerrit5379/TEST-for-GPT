# Settings for this model

These settings prioritize detailed surfaces and support accessibility over speed.
They were checked in Creality Print 7.3.0.6157 with the official CR-10S Pro V2
0.4 mm printer definition. A physically optimal PLA profile still requires
calibration on the user's actual printer and filament.

| Setting | Project value |
|---|---|
| Orientation | Upright, flat base on plate |
| Layer height / first layer | 0.12 / 0.20 mm |
| Wall generator / walls | Arachne / 3 |
| Outer / inner line width | 0.42 / 0.45 mm |
| Top / bottom shells | 7 layers, 0.84 mm nominal |
| Infill | 12% gyroid |
| Outer / inner wall speed | 25 / 35 mm/s |
| Small perimeters | 50% of the corresponding nominal speed |
| Top surface / bridge speed | 25 / 20 mm/s |
| Sparse infill speed | 40 mm/s |
| Outer wall acceleration | 300 mm/s² |
| First layer speed / acceleration | 15 mm/s / 300 mm/s² |
| Travel | 100 mm/s, subject to machine limits |
| Seam | Back; inspect and paint locally if a rear detail is important |
| PLA nozzle | 205°C first layer, 200°C subsequent layers |
| Bed | 60°C |
| Cooling | Off for first 3 layers, 100% afterward |
| Retraction, stock Bowden | 4 mm at 35 mm/s |
| Filament volumetric flow limit | 8 mm³/s |
| Model brim | 4 mm outer brim |
| Raft / ironing / prime tower | Off |

If the printer has been converted to direct drive, replace the Bowden retraction
values with your calibrated direct-drive profile. Match nozzle temperature and
flow to your spool's recommended range and your existing calibration.

## Supports

| Setting | Project value |
|---|---|
| Enable supports | On |
| Type / style | Tree (auto) / Organic |
| Threshold angle | 35° **from horizontal**, as defined by Creality Print |
| Build plate only | Off, to reach overhangs above the integrated base |
| Top / bottom Z separation | 0.24 / 0.24 mm |
| XY separation | 0.40 mm |
| Interface top / bottom layers | 3 / 2 |
| Top interface spacing | 0.35 mm |
| Support / interface speed | 30 / 25 mm/s |
| Tip diameter | 0.8 mm |
| Initial organic branch diameter | 2 mm; branches thicken as required |
| Branch diameter growth angle | 2°, to avoid excessively bulky trunks |
| Organic branch spacing | 2 mm |
| Maximum / preferred branch angle | 40° / 25° |
| Support walls | 1 |
| Tree brim | Automatic, 4 mm configured width |
| Independent support layer height | On |
| Critical regions only | Off |
| Remove small overhangs | Off, so small detailed overhangs remain eligible |

The angle convention matters: this threshold supports downward-facing slopes
below 35° to horizontal, rather than treating every slope above 35° to vertical
as needing support. A higher threshold adds support to gentler slopes.

## Why "avoid crossing walls" is off

With this model and these supports, enabling `reduce_crossing_wall` caused
Creality Print 7.3.0.6157 to crash during G-code export. A debugger located the
failure in `AvoidCrossingPerimeters::travel_to` / `EdgeGrid::Grid`. Disabling that
travel option allowed the full exports to finish. Retraction and the official
profile's Z-hop remain available. Re-enabling this option invalidates that
successful export check.

## Remove supports carefully

1. Let the print and bed cool. Remove the model and its supports together.
2. Snip the larger tree trunks into accessible sections. Work from the outer
   branches inward, particularly behind the shield and under the weapon.
3. Hold the model close to each contact while peeling away small interface
   sections. Do not pull the whole support tree against a beard braid or finger.
4. Trim remaining nubs with a sharp tool. Keep sanding away from sculpted texture.

The 0.24 mm top gap favours separation, with some underside roughness as the
tradeoff. On a small support test, try **0.20 mm** if undersides sag too much, or
**0.28 mm** if supports fuse. Keep independent support layer height enabled and
reslice after a change. Removal and surface finish need a physical test; they
cannot be certified from the model or G-code alone.

Before a long print, verify bed level/Z-offset, first-layer adhesion, cooling,
and PLA flow/retraction using your usual calibrated printer workflow.
