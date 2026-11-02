# Gerrit 76 mm — Revision 2 for SUNLU PLA+ and textured PEI

For the confirmed **Creality CR-10S Pro V2, stock Bowden setup, 0.2 mm nozzle,
76 mm character, SUNLU PLA+, textured PEI**. This revision targets the reported
stringing and poor base anchoring while retaining the detail settings that
printed well. It is a candidate correction, not a physically proven fix.

## Download

- **[Start with the small stringing and adhesion test](https://github.com/Gerrit5379/TEST-for-GPT/raw/refs/heads/main/gerrit-02mm-rev2/Stringing_Adhesion_Test_Rev2.3mf)** — approximately 75 minutes and 1 g PLA.
- **[76 mm character project](https://github.com/Gerrit5379/TEST-for-GPT/raw/refs/heads/main/gerrit-02mm-rev2/Gerrit_76mm_0p2_Rev2.3mf)**.
- [Setting changes and hotend/plate checks](CHANGES.md).
- [Digital validation and print estimates](VALIDATION.md).

Open the 3MF **as a project**, keeping its included settings, then click **Slice
Plate**. Confirm the **0.2 mm** nozzle, **Gerrit R2 - SUNLU PLA+ Detail** process,
**SUNLU PLA+ R2 - 200C** filament and **Textured PEI Plate** selection.
The projects contain their settings; importing the separate JSON files is optional.

The test is three tapered posts on a 32 mm flat disk. Check its joined first-layer
lines, attached brim, extrusion quality and strings between posts. Its smaller
disk cannot prove warping resistance for the full character base. Supports are
not required for the posts, so unexpected webs between them are easy to recognize.

## What changed

| Setting | Previous file | Revision 2 |
|---|---|---|
| Steady / initial nozzle temperature | 200 / 205°C | **200 / 205°C, retained** |
| Normal layer height / line width | 0.06 / 0.22 mm | **Retained** |
| Flow ratio / model walls | 1.00 / 4 | **Retained** |
| Retraction length | 4 mm | **4.5 mm** |
| Retraction / return speed | 30 / 30 mm/s | **35 / 30 mm/s** |
| Retract before wipe | 70% | **100%** |
| Wipe distance | 2 mm | **1.5 mm** |
| Minimum travel eligible for retraction | 1 mm | **0.6 mm** |
| Nominal travel speed | 100 mm/s | **150 mm/s**, retained machine limits |
| Brim width / model gap | 4 / 0.20 mm | **8 / 0 mm** |
| First-layer shrink compensation | 0.15 mm | **0 mm**, for brim anchoring |
| First-layer / first-layer infill speed | 12 / 15 mm/s | **8 / 10 mm/s** |
| First / subsequent bed temperature | 60 / 60°C | **65 / 60°C** |
| First layers without fan | 3 | **6**, then ramp to full at layer 15 |

The normal model speeds, 0.12 mm first-layer height, 0.25 mm first-layer width,
1.5 mm³/s flow cap, original geometry, upright placement and support contacts
remain unchanged. The 8 mm attached brim will require careful trimming at the
flat base edge; it is intended to anchor the base rather than form a detached ring.

**200°C is retained because it produced good detail in the reported print.** It
is not presented as SUNLU's universal recommendation for every PLA+ formulation,
colour, spool or printer. Check your spool's label and layer bonding; use a
spool-appropriate calibrated temperature if required and reslice.

## Before the small test: yellow/orange debris

The photograph cannot identify those pieces. Plastic baked onto the nozzle or
debris from a nozzle/heatbreak leak are possibilities. **A slicer file cannot
repair a leak or remove existing buildup.** Inspect and clean the hotend using
the manufacturer's procedure before another long print. If fresh plastic is
coming from above the nozzle or around the heater block, stop printing and
correct the seal and nozzle compatibility before continuing. See CHANGES.md.

Clean the cooled PEI sheet using the plate maker's method, rinse/dry fully and
avoid touching the print area. Recheck bed leveling and Z-offset with the actual
nozzle and PEI surface. This file does not guess a new probe offset or change
firmware probing behaviour. Dry the filament according to SUNLU's guidance if
moisture is suspected or strings persist after the hotend check.

Neither the test nor character has been physically printed with this revision.
Digital slice success cannot certify removal force, adhesion, absence of strings
or the cause of the discoloured debris. Try the small test before the full job.
