# Gearshield dwarf: detailed revision

This is a rebuilt, reference-inspired miniature, with a continuous face and torso
sculpt, recessed eyes and nostrils, swept side hair, tapered beard locks and
three-strand braids, articulated fingers, draped clothing, leather seams, a
planked and iron-bound shield, and an ornate steam mace.

The form is an interpretation from one front-view reference. It is not an exact
scan or a reconstruction of unseen sides. Previews show the actual STL geometry
in uniform grey clay, without painted textures or image-generated detail.

## Files and dimensions

- `gearshield_dwarf_v2_50mm.stl`: single-piece printable mesh.
- `gearshield_dwarf_v2.blend`: final sculpt, lighting, and camera.
- `dwarf_v2_editable.blend`: separate construction elements before final union.
- `sculpt_dwarf.py`: generation script for Blender 4.3+.
- `preview_v2.png`, `preview_v2_front.png`, `preview_v2_portrait.png`: mesh renders.
- `stl_validation.json`: independent reimport and topology check.

Import the STL in millimetres. Total height is 53 mm including the base; base
diameter is approximately 40 mm. The editable construction scene precedes the
final height normalization, so regenerate after editing it.

## Filament printing

For the user's 0.4 mm nozzle, start with PLA and a calibrated 0.10–0.12 mm layer
profile, 3 walls and 15–20% infill. Set the flat circular base on the bed. Use
organic/tree supports and inspect the beard, hands, weapon head, nose and belly
overhangs. Allow supports on the model if bed-only supports cannot reach them;
check removal access behind the shield. Use your printer's tested temperature,
cooling and support-interface settings.

The sculpt contains cosmetic grooves and strand relief narrower than 0.4 mm.
These are intended to improve the digital sculpt and to be available at larger
scales; a 0.4 mm nozzle will omit or soften some of them at 50 mm. A 0.2 mm nozzle
or scaling the whole model to 150% (79.5 mm total, 60 mm base) will preserve more
surface detail. Do not expect resin-level detail at 50 mm from a 0.4 mm nozzle.

Check layer preview for missing details and floating islands before printing.
Avoid aggressive support removal around the beard and fingers. This mesh is
digitally validated, but has not been physically test-printed or sliced using a
specific printer profile.

## Regenerate

```sh
blender --background --threads 4 --python sculpt_dwarf.py
```

This generates the sculpt, applies a 0.075 mm voxel union, removes disconnected
sculpt remnants, normalizes overall height to 53 mm, exports the STL, and renders
three views. The final mesh and the source construction are saved separately.
