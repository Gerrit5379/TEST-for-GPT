# Gearshield dwarf miniature

An original stylized sculpt inspired by your reference: a broad dwarf with a
large belly, braided beard, forehead goggles, a gear-covered tower shield,
steam hammer, and belt equipment. It is an interpretation of the visible front
view, not an exact reconstruction of the original character.

## Files

- `gearshield_dwarf_50mm.stl`: final single-piece print mesh, coordinates in mm.
- `gearshield_dwarf.blend`: final mesh, materials, lighting, and preview camera.
- `dwarf_editable.blend`: editable construction from individual shapes before
  the final union and size adjustment. Regenerate the final mesh after edits.
- `preview.png` and `preview_front.png`: actual final geometry rendered in clay.
- `create_dwarf.py`: reproducible Blender 4.3+ generation script.
- `mesh_validation.json`: measured mesh dimensions and topology checks.

## Size and starting slicer settings

- Approximately 50 mm figure above a 3 mm base; 53 mm total height.
- Base: 40 mm diameter. Import STL in millimetres at 100% scale.
- Printer: filament, 0.4 mm nozzle. PLA is a reasonable first material.
- Layer height: 0.10–0.12 mm; use your printer's calibrated extrusion widths.
- Start with 3 walls and 15–20% infill. Let the slicer handle narrow solid areas.
- Place the flat circular base on the build plate.
- Enable organic/tree supports. Inspect coverage below the beard, fists,
  hammer head and belly; allow support on the model if bed-only supports do
  not reach those areas. Start with your slicer's PLA support interface and
  separation defaults, and check access for removal before printing.
- Use your tested PLA temperature/cooling profile. Slow down external walls
  and enable minimum-layer-time cooling for the face and goggles.
- A brim is optional if your printer needs help with adhesion.

The solid shield reaches the base and the equipment attaches to the body.
Fine beard and gear ornament is intentionally exaggerated for this scale, but
some shallow details may soften or disappear with a 0.4 mm nozzle. Scaling
the model down will weaken details and attachments.

Check the slicer's layer preview for missing features, unsupported islands,
and supports trapped behind the shield. Support removal near the face still
requires care. The mesh has been checked digitally; it has not been sliced
for a specific printer or physically test-printed. These are starting settings,
not a verified printer profile.

## Regenerate

Run from this folder with Blender installed:

```sh
blender --background --threads 4 --python create_dwarf.py
```

This writes the model files and two previews in the same folder. The final
mesh uses a 0.10 mm voxel union, removes loose sub-millimetre remnants, and
is scaled to 53 mm total height. The saved Blender scene uses metric units;
the exported STL uses millimetre coordinate values.
