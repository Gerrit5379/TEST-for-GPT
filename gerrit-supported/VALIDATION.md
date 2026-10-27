# Digital validation and support comparison

The two final self-contained 3MF projects were reopened by Creality Print
7.3.0.6157 and sliced without external printer, process or filament preset files.
Its project loader performed the same preset merge used by the GUI. Both runs
completed G-code export with success and an empty final plate-warning field.

The actual exported G-code settings were checked for enabled organic supports,
35° support threshold, 2° trunk growth, 0.24 mm contact separation, 0.12 mm layers,
3 walls, the intended nozzle temperatures, and disabled travel avoidance.

| Final project | Slicer time estimate | Total PLA estimate | Support PLA estimate | Support saving vs same setup with 5° trunk growth |
|---|---|---|---|---|
| 76 mm | 19h 28m 18s | 46.82 g | 15.39 g | 33.9% |
| 152 mm | 3d 8h 4m 45s | 239.55 g | 69.97 g | 29.1% |

Estimates include the base and generated supports. Support mass is calculated
from actual support and interface extrusion using 1.75 mm filament and the PLA
profile's 1.24 g/cm³ density. Estimates are not measured print time or weight.

## Comparison method

At 76 mm, organic supports allowing starts on the model, organic supports limited
to the build plate, and tree-slim supports were sliced. Build-plate-only supports
triggered substantially more recovered branch-routing notices around this base
and detailed figure. Starts on the model's base were retained for reachability.

The selected setup uses a 35° threshold and 2 mm organic branch spacing. A final
trunk-growth comparison reduced diameter growth from 5° to 2°, keeping contact
gap, interface layers, and printing settings fixed. This removed bulky trunks
while preserving the same overhang-support policy. The final branch previews
were inspected from front and back for reachability and removal access.

Successful slicing does not prove branch strength, mark-free contacts, perfect
unsupported slopes, or easy physical removal. Those need a physical print. Use
a support-gap test before a long high-detail print. See SETTINGS.md.

## Source geometry and preservation

The archive was reassembled from the supplied numbered ZIP parts. The OBJ has
one detailed mesh and three cylinder objects. The detailed mesh contains
1,371,586 vertices, 2,744,227 faces, six boundary edges and 12 non-manifold edges;
the three cylinders are closed individually. The source OBJ was retained intact.

The delivered 3MFs retain the source surface geometry, combine its parts into
one registered print object, and set explicit millimetre dimensions and upright
placement. No sculpt smoothing, simplification, voxel remeshing or detail removal
was applied. Both final slicer reports count 2,744,599 input triangles. Successful
slicing is not a claim that the original OBJ is watertight.

## Slicer limitation found

Enabling "avoid crossing walls" reproducibly crashed G-code export for this model.
A cube succeeded, and a debugger isolated the model run's failure to
`AvoidCrossingPerimeters::travel_to` / `EdgeGrid::Grid`. The supported configuration
sets `reduce_crossing_wall=0`; the complete final exports then succeeded.

The JSON report includes the effective toolpath settings, comparison estimates,
runner results and SHA-256 hashes of the exact final project files.
