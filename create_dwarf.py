"""Create an original, reference-inspired dwarf miniature. Blender 4.3+.
Run: blender --background --python create_dwarf.py
Dimensions are authored in millimetres; STL coordinates are millimetres.
"""
import bpy
import math
import os
import json
from mathutils import Vector

OUT = os.path.dirname(os.path.abspath(__file__))
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
parts = []

def finish(obj, name):
    obj.name = name
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    parts.append(obj)
    return obj

def ell(name, loc, scale):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=32, location=loc)
    o = bpy.context.object
    o.scale = scale
    return finish(o, name)

def box(name, loc, size, bevel=.4):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o=bpy.context.object
    o.scale=size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if bevel:
        m=o.modifiers.new('Rounded edges', 'BEVEL')
        m.width=bevel
        m.segments=3
        bpy.context.view_layer.objects.active=o
        bpy.ops.object.modifier_apply(modifier=m.name)
    return finish(o,name)

def rod(name, a, b, radius, radius2=None, vertices=20):
    d=Vector(b)-Vector(a)
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius,
        radius2=radius if radius2 is None else radius2, depth=d.length,
        location=(Vector(a)+Vector(b))/2)
    o=bpy.context.object
    o.rotation_euler=d.to_track_quat('Z','Y').to_euler()
    return finish(o,name)

def tube(name, points, radius):
    curve=bpy.data.curves.new(name,'CURVE')
    curve.dimensions='3D'
    curve.resolution_u=2
    curve.bevel_depth=radius
    curve.bevel_resolution=3
    curve.use_fill_caps=True
    s=curve.splines.new('POLY')
    s.points.add(len(points)-1)
    for p,co in zip(s.points,points): p.co=(*co,1)
    o=bpy.data.objects.new(name,curve)
    bpy.context.collection.objects.link(o)
    bpy.context.view_layer.objects.active=o
    o.select_set(True)
    bpy.ops.object.convert(target='MESH')
    o.select_set(False)
    parts.append(o)
    return o

def ring(name, center, major, minor, front=True):
    bpy.ops.mesh.primitive_torus_add(major_segments=40,minor_segments=10,
        location=center,major_radius=major,minor_radius=minor,
        rotation=(math.pi/2,0,0) if front else (0,0,0))
    return finish(bpy.context.object,name)

def gear(name,x,y,z,r,n=12):
    # Solid medallion backing keeps every tooth attached to shield.
    rod(name+' plate',(x,y+.35,z),(x,y-.35,z),r*.82,vertices=40)
    ring(name+' rim',(x,y-.40,z),r*.71,.45)
    for i in range(n):
        t=i*2*math.pi/n
        o=box(name+' tooth',(x+r*.87*math.sin(t),y,z+r*.87*math.cos(t)),
            (r*.30,1.0,r*.34),.13)
        o.rotation_euler[1]=t
    for i in range(6):
        t=i*math.pi/3
        rod(name+' spoke',(x,y-.45,z),(x+r*.60*math.sin(t),y-.45,z+r*.60*math.cos(t)),.34)
    rod(name+' axle',(x,y+.2,z),(x,y-1.0,z),r*.22,vertices=16)

# Stable 40 mm base, 3 mm thick; sole of each boot intersects it.
rod('40 mm round plinth',(0,0,.35),(0,0,2.65),20,vertices=96)
ring('Upper base lip',(0,0,2.35),19.25,.65,False)
ring('Lower base lip',(0,0,.65),19.25,.65,False)
for x in (-5,5):
    ell('Heavy boot',(x,-1.6,5.1),(3.9,5.1,3.1))
    box('Boot sole',(x,-1.6,3.25),(7.4,9.3,1.25),.5)
    ell('Trouser leg',(x,0,11.8),(3.5,3.6,7.3))
    box('Knee armour',(x,-3.05,10.0),(5.3,1.7,4.4),.7)
    box('Boot strap',(x,-5.5,5.6),(6.0,1.1,1.1),.25)
    for dx in (-1.9,1.9): ell('Boot rivet',(x+dx,-6.0,5.6),(.45,.35,.45))

ell('Padded skirt core',(0,.3,18.4),(8.0,4.8,6.4))
for x in (-5.4,-2.7,0,2.7,5.4):
    o=box('Long leather apron panel',(x,-3.8,17.7),(3.1,2.1,8.4),.65)
    o.rotation_euler[1]=-.035*x
    for z in (15,18,21): ell('Apron stud',(x,-4.95,z),(.4,.3,.4))
ell('Broad torso',(0,.5,32.6),(8.4,5.0,9.0))
ell('Round bare belly',(.7,-1.5,28.6),(8.0,5.5,7.1))
ell('Navel rim',(2.0,-6.73,28.4),(.6,.35,.7))
ell('Navel inset',(2.0,-6.99,28.4),(.23,.12,.27))
# Broad belt wraps around waist; prominent rectangular mechanical buckle.
ell('Belt backing',(0,-.2,22.7),(8.65,5.3,1.8))
box('Belt front',(0,-5.0,22.9),(14.7,1.65,2.8),.55)
box('Buckle body',(1,-6.0,22.8),(4.7,1.2,3.5),.45)
ring('Buckle inset',(1,-6.7,22.8),1.1,.4)
for x in (-6,-4,5,7): ell('Belt rivet',(x,-5.9,23),(.45,.3,.45))

# Jacket sides and raised leather chest straps.
for side in (-1,1):
    ell('Jacket shoulder',(side*7.3,.3,37.8),(3.7,4.0,4.4))
    tube('Harness strap',[(side*5.1,-3.3,40),(side*6.7,-4.0,36),
        (side*7.4,-4.35,32),(side*7,-4.6,27)],.86)
    for z in (34,37): ell('Harness rivet',(side*6.7,-4.8,z),(.46,.3,.46))
    ell('Upper arm',(side*9.4,0,34.7),(3.0,3.2,4.9))
    ell('Armoured elbow',(side*10.1,-.4,31.4),(3.0,3.25,2.7))

# Shield arm and fist, embedded behind the shield.
rod('Left forearm',(-10,-1,32),(-11,-5,33),2.4)
ell('Left shield fist',(-10.1,-4.9,33.1),(2.6,2.8,2.7))
# Great tower shield on viewer left. It touches the base for rigidity.
box('Tower shield',(-12,-6.1,23.0),(11.7,3.3,39.8),1.1)
for x in (-17.1,-6.9):
    box('Shield vertical iron rail',(x,-8.0,23),(1.15,1.25,38.6),.22)
for z in (4.5,17,30,41.6):
    box('Shield transverse band',(-12,-8.0,z),(10.9,1.15,1.25),.22)
for x in (-17.1,-6.9):
    for z in (6.5,11.5,18.5,24,31.5,37.5,40):
        ell('Shield rivet',(x,-8.8,z),(.6,.45,.6))
# Panel seams and substantial raised gear ornaments.
for x in (-14.7,-12,-9.3):
    box('Shield panel rib',(x,-7.86,23),(.52,.5,36),.18)
gear('Main shield gear',-12,-8.8,25.0,4.5,12)
gear('Upper shield gear',-12.1,-8.65,35.3,2.65,10)
gear('Lower shield gear',-12.0,-8.65,12.2,2.8,10)

# Opposite hand holds a short, thick steam hammer: connected to fist and hip.
rod('Right forearm',(10,-.2,32),(11,-3,32.8),2.55)
ell('Right gauntlet',(11,-3.0,32.8),(2.65,2.6,2.8))
for z in (31.5,32.6,33.7): box('Gauntlet knuckle',(11,-5.2,z),(3.6,1.0,.7),.25)
rod('Hammer haft',(12.4,-2.9,21.5),(12.4,-2.9,43),1.2,vertices=24)
for z in (24,26,28,30,35.4,36.8): ring('Haft collar',(12.4,-2.9,z),1.18,.3,False)
box('Steam hammer head',(12.4,-2.9,41.5),(8.0,5.3,5.7),.65)
for x in (8.9,15.9): box('Hammer striking cap',(x,-2.9,41.5),(1.3,5.8,6.2),.45)
gear('Hammer medallion',12.3,-5.7,41.5,1.8,8)
tube('Hammer steam pipe',[(12,-.4,39),(12.8,.3,37),(12.8,.3,30),(10.8,.2,26)],.7)

# Head, ears, cheeks and large nose. Top of hair is 53 mm above plate.
ell('Neck',(0,0,40.4),(3.7,3.2,3.3))
ell('Dwarf head',(0,-.1,44.5),(4.7,3.9,5.1))
for side in (-1,1):
    ell('Ear',(side*4.5,-.1,44.4),(1.15,1.0,1.8))
    ell('Cheek',(side*2.8,-2.85,43.6),(1.9,1.4,1.8))
    ell('Heavy brow',(side*1.85,-3.05,46.7),(1.7,1.0,.9))
    ell('Eye',(side*1.7,-3.72,45.85),(.6,.35,.42))
ell('Broad nose',(0,-4.0,44.9),(1.65,1.8,1.6))
ell('Hair crown',(0,.5,48.3),(3.9,3.2,1.8))
for x in (-2.8,-1.5,0,1.5,2.8):
    ell('Swept hair',(x,.8,49.0),(1.0,2.5,1.6))
# Goggles sit on forehead, lenses backed by head rather than unsupported holes.
for x in (-1.85,1.85):
    rod('Goggle lens backing',(x,-2.15,48.6),(x,-3.1,48.6),1.22,vertices=32)
    ring('Goggle thick rim',(x,-3.2,48.6),1.14,.38)
rod('Goggle bridge',(-.8,-3.1,48.6),(.8,-3.1,48.6),.4)
tube('Goggle strap',[(-4,-.4,48),(-3.8,-2.0,48.4),(0,-2.9,48.6),(3.8,-2,48.4),(4,-.4,48)],.45)

# Solid beard mass keeps individual locks firmly attached.
ell('Beard foundation',(0,-3.35,39.7),(5.0,3.0,5.2))
for side in (-1,1):
    tube('Sweeping moustache',[(0,-5.2,43.7),(side*1.7,-5.5,43.3),
        (side*3.5,-5.15,42.5),(side*4.3,-4.7,41.2)],.95)
    # Thick, twisted hanging side braids; collar bands hide small intersections.
    for strand in range(2):
        pts=[]
        for j in range(36):
            t=j/35
            angle=t*math.pi*5+strand*math.pi
            pts.append((side*(3.7+1.4*t)+.52*math.sin(angle),
                -4.9-.52*math.cos(angle),42.0-9.2*t))
        tube('Twisted side beard braid',pts,.82)
    rod('Beard brass clasp',(side*5.0,-5.0,33),(side*5.0,-5.0,34.5),1.22,vertices=16)
    ell('Braid tip',(side*5.1,-4.95,32.6),(1.0,1.15,1.3))
for i in range(7):
    x=(i-3)*1.12
    pts=[]
    for j in range(13):
        t=j/12
        pts.append((x*(1-.2*t)+.2*math.sin(t*math.pi*3+i),-6.0-.35*math.sin(t*math.pi),42-6.9*t))
    tube('Sculpted beard lock',pts,.9)

# Belt equipment, all joined to body. No fragile dangling chains.
box('Leather utility pouch',(7.6,-1.9,20.4),(3.8,4.3,5.2),.8)
box('Pouch flap',(7.8,-4.1,21.7),(3.5,.9,2.3),.5)
ell('Pouch clasp',(7.8,-4.65,21.2),(.6,.3,.7))
rod('Potion flask',(-7.2,-4.6,18),(-7.2,-4.6,21.5),1.35,vertices=20)
ell('Flask bottom',(-7.2,-4.6,18.1),(1.35,1.35,1.0))
rod('Flask stopper',(-7.2,-4.6,21.2),(-7.2,-4.6,22.2),.85,vertices=16)
for z in (18.5,20.7): ring('Flask cage',(-7.2,-4.6,z),1.35,.32,False)

# Preserve the editable primitive construction in its own file.
bpy.ops.object.select_all(action='DESELECT')
for o in parts: o.select_set(True)
bpy.context.view_layer.objects.active=parts[0]
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT,'dwarf_editable.blend'))
bpy.ops.object.join()
model=bpy.context.object
model.name='Gearshield dwarf — 50 mm figure, 40 mm base'
# Voxel union removes intersecting internal shells, creating a printable solid.
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
rem=model.modifiers.new('Watertight voxel union 0.10 mm','REMESH')
rem.mode='VOXEL'
rem.voxel_size=.10
rem.use_smooth_shade=True
bpy.ops.object.modifier_apply(modifier=rem.name)
smooth=model.modifiers.new('Gentle surface relaxation','SMOOTH')
smooth.factor=.25
smooth.iterations=2
bpy.ops.object.modifier_apply(modifier=smooth.name)
dec=model.modifiers.new('Reduce STL size','DECIMATE')
dec.ratio=.45
bpy.ops.object.modifier_apply(modifier=dec.name)
# Remove sub-millimetre floating sculpt remnants; keep the connected figure/base.
import bmesh
bm=bmesh.new(); bm.from_mesh(model.data)
seen=set(); components=[]
for v in bm.verts:
    if v in seen: continue
    todo=[v]; seen.add(v); component=[]
    while todo:
        n=todo.pop(); component.append(n)
        for e in n.link_edges:
            w=e.other_vert(n)
            if w not in seen: seen.add(w); todo.append(w)
    components.append(component)
largest=max(components,key=len)
bmesh.ops.delete(bm,geom=[v for c in components if c is not largest for v in c],context='VERTS')
lo=min(v.co.z for v in bm.verts)
height=max(v.co.z for v in bm.verts)-lo
for v in bm.verts: v.co.z=(v.co.z-lo)*53.0/height
bm.to_mesh(model.data); bm.free(); model.data.update()
bpy.context.view_layer.update()
for p in model.data.polygons: p.use_smooth=True
bpy.ops.wm.stl_export(filepath=os.path.join(OUT,'gearshield_dwarf_50mm.stl'),export_selected_objects=True)

# Validate final exported geometry topology and shell count without external packages.
import bmesh
bm=bmesh.new()
bm.from_mesh(model.data)
seen=set()
sizes=[]
for v in bm.verts:
    if v in seen: continue
    todo=[v]; seen.add(v); count=0
    while todo:
        n=todo.pop(); count+=1
        for e in n.link_edges:
            w=e.other_vert(n)
            if w not in seen: seen.add(w); todo.append(w)
    sizes.append(count)
stats={'dimensions_mm':list(model.dimensions),'vertices':len(bm.verts),
       'faces':len(bm.faces),'connected_shells':len(sizes),
       'non_manifold_edges':sum(not e.is_manifold for e in bm.edges),
       'volume_mm3':bm.calc_volume(signed=False)}
bm.free()
with open(os.path.join(OUT,'mesh_validation.json'),'w') as f: json.dump(stats,f,indent=2)
print('MESH_VALIDATION',json.dumps(stats),flush=True)

# Neutral clay preview shows the actual printable mesh.
mat=bpy.data.materials.new('Warm bronze clay')
mat.diffuse_color=(.33,.19,.085,1)
mat.use_nodes=True
bsdf=mat.node_tree.nodes.get('Principled BSDF')
bsdf.inputs['Base Color'].default_value=(.33,.19,.085,1)
bsdf.inputs['Metallic'].default_value=.30
bsdf.inputs['Roughness'].default_value=.48
model.data.materials.clear()
model.data.materials.append(mat)
scene=bpy.context.scene
scene.unit_settings.system='METRIC'
scene.unit_settings.scale_length=.001
scene.render.engine='CYCLES'
scene.cycles.samples=64
scene.cycles.use_denoising=False
scene.render.resolution_x=1100
scene.render.resolution_y=1100
scene.render.resolution_percentage=100
scene.world.color=(.23,.23,.23)
scene.view_settings.view_transform='AgX'

def aim(obj,point): obj.rotation_euler=(Vector(point)-obj.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.camera_add(location=(72,-130,79))
cam=bpy.context.object
aim(cam,(0,-.3,25))
cam.data.type='ORTHO'
cam.data.ortho_scale=68
scene.camera=cam
for loc,power,size in [((15,-60,100),160000,65),((-60,-25,55),110000,55),((30,45,80),180000,45)]:
    bpy.ops.object.light_add(type='AREA',location=loc)
    light=bpy.context.object
    light.data.energy=power
    light.data.shape='DISK'
    light.data.size=size
    aim(light,(0,0,25))
scene.render.image_settings.file_format='PNG'
scene.render.filepath=os.path.join(OUT,'preview.png')
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT,'gearshield_dwarf.blend'))
bpy.ops.render.render(write_still=True)
# Straight-on second view helps inspect facial and shield details.
cam.location=(0,-150,64)
aim(cam,(0,0,25))
scene.render.filepath=os.path.join(OUT,'preview_front.png')
bpy.ops.render.render(write_still=True)
