# R2 checks and rationale

## Keep the settings that worked

The user confirmed the 76 mm project, SUNLU PLA+, textured PEI, and no changes to
the previous temperature, flow, retraction or Z-offset. The revision therefore
retains the known-working **200°C steady / 205°C initial nozzle temperature**,
**1.00 flow**, **0.06 mm layers**, **0.22 mm widths**, four walls and **18 mm/s
outer wall speed**. It does not try to fix stringing by narrowing the normal
lines or starving the fine detail. The provisional generic-PLA 195°C candidate
was not published as this revision after the material was confirmed.

The custom material preset uses the PLA family with SUNLU branding and explicit
settings for this slow-printing Bowden machine. It is not copied from a high-flow
or direct-drive SUNLU preset for another printer. A spool's label and real flow/
layer-strength checks still matter; PLA+ is not one universal temperature recipe.

## Stringing controls

The retraction length increases modestly from 4 to **4.5 mm**, retraction speed
from 30 to **35 mm/s**, and return speed remains **30 mm/s**. Full retraction now
occurs before the **1.5 mm wipe**. Retraction is eligible for moves as short as
**0.6 mm**, and the option to reduce infill retractions is disabled. Nominal
travel speed increases to **150 mm/s**, with the existing machine acceleration
and speed limits retained. Not every short move reaches that speed.

Very large retractions are deliberately avoided with the 0.2 mm nozzle. This
profile assumes the printer's stock Bowden extruder; a direct-drive conversion
needs its own calibrated retraction. Automatic 0.2 mm Z-hop is retained to avoid
deliberately reducing clearance around fine detail and support crowns.

The previous export-crash workaround remains: **avoid crossing walls is off**.
The original hotend start/end G-code and firmware probing behaviour are retained.

## Base adhesion

The previous file used a **0.20 mm brim gap** plus **0.15 mm first-layer shrink
compensation**. Those values could leave the brim disconnected from the round
base. Revision 2 uses an **8 mm outer brim, zero gap, and zero first-layer shrink
compensation** so the base can be anchored. The small test's exported first-layer
paths were checked for a nominal touching brim. Real contact still depends on
extrusion, plate condition and Z-offset.

First-layer model/infill speeds decrease to **8 / 10 mm/s**, with **40 mm/s first-
layer travel**. Textured PEI is explicitly selected, using **65°C first layer /
60°C afterward**. The fan is off for the first **6 layers**, then ramps to full
at **layer 15**. The automatic tree-brim width setting increases to **6 mm**.
Normal detail cooling and the support contact settings remain unchanged.

Wash the cooled removable PEI plate with the maker's recommended method; mild
dish soap and warm water are commonly suitable. Rinse/dry well and keep fingers
off the print area. Allow the heated plate to stabilize before checking the first
layer. Do not add more flow to compensate for grease or an incorrect Z-offset.

The disk should have joined lines without round detached strands or ridges being
ploughed by the nozzle. Check Z-offset/leveling with the actual replacement nozzle
and PEI surface using the printer's usual procedure. The file does not set a new
probe offset, create a fresh bed mesh, or establish that the stored mesh is valid.

## Yellow/orange pieces and a newly fitted nozzle

The photograph shows discoloured debris but does not identify it. Existing
plastic on the nozzle may bake and fall off; a poor replacement-nozzle seal is
another possibility. Check and clean the nozzle and heater-block exterior using
the hotend maker's procedure before interpreting the stringing test.

If fresh plastic emerges from above the nozzle or around the heater block,
**stop the print and correct the leak before continuing**. Check replacement-
nozzle compatibility and the nozzle/heatbreak seal. Use the manufacturer's fitting
and hot-tightening instructions; do not assume a nozzle should be tightened flush
against the heater block. More retraction cannot repair a leak.

If a clean, correctly assembled hotend still produces webs on the small test,
check filament moisture and dry it according to the spool maker's guidance. If
you see weak layers or missing lines, check temperature and flow rather than
automatically adding still more retraction. Change one item at a time after this
initial multi-issue revision. Nozzle buildup, moisture, plate condition, incorrect
Z-offset and a mechanical leak cannot all be diagnosed or fixed from a photo
and slicer settings alone.

Keep any genuinely calibrated spool flow or printer Z-offset values if you later
establish them. The included 1.00 flow is the previous file's baseline, not a
measurement of actual extrusion. Avoid pulling a large support tree against
delicate details; cut branches into manageable sections and trim the brim at the
flat base edge after cooling.
