# Gerrit 76 mm — R3 minimal painted supports

[Download the Creality Print project](https://github.com/Gerrit5379/TEST-for-GPT/raw/refs/heads/main/gerrit-02mm-minimal/Gerrit_76mm_0p2_Minimal_Supports_R3.3mf)

For the CR-10S Pro V2, 0.2 mm nozzle, SUNLU PLA+, textured PEI. Open the 3MF **as a project**, retain its embedded presets and support painting, then slice the plate. Do not switch to automatic support mode. The separate process JSON alone does not include the painted regions or complete printer/material settings.

## What changed

Automatic trees are replaced with eight small painted support regions. No automatic contacts on the beard, hair, shield face, or tool belt ornamentation. Small contacts remain under the weapon's lowest end, two solid hammer-head undersides, the rear elbow, the hanging lantern bottom, and three cloth/coat undersides. The lantern and weapon end begin above the plate and need support.

Support separation increased from 0.16 to 0.24 mm vertically and from 0.25 to 0.45 mm horizontally. Top interface reduced from four to two layers, with 0.45 mm interface spacing instead of 0.22 mm. Branches have one wall and 0.5 mm tips. These changes prioritize removal and protection of fine features; hidden undersides may be rougher and unsupported fine tips may sag.

Model geometry and detail are unchanged. The R2 0.06 mm layers, 0.22 mm line width, 200/205 C temperatures, retraction, textured-PEI bed temperatures, cooling and 8 mm brim are retained.

## Checked in the slicer

Creality Print 7.3.0.6157 successfully sliced the complete project, with all 2,744,599 triangles and an empty final warning message. Extruding support paths use approximately **0.65 g**, versus **11.49 g** in R2: **94.3% less support material**. Estimates: 1d 14h 36m 39s, 26.51 g total. Actual results vary.

The preview images show actual generated G-code support paths sampled every third layer. Green lines are supports, grey is the model. They are illustrative, not every printed layer.

This is an aggressive reduction, not a physically tested guarantee of support removal or successful overhangs. Review the sliced plate before printing. For removal, cut the branches into small pieces and support the nearby model feature; avoid pulling a complete tree against the beard, hair or tools.

[Front support preview](supports_front.png) · [Rear support preview](supports_back.png) · [Validation details](validation.json)
