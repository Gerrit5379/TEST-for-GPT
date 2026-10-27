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

import random
random.seed(41)

# Smooth, tapered sculpting strokes, rather than constant-width polygon tubes.
def stroke(name, points, radius, taper=False):
    cu=bpy.data.curves.new(name,'CURVE'); cu.dimensions='3D'
    cu.resolution_u=10; cu.bevel_depth=radius; cu.bevel_resolution=3
    cu.use_fill_caps=True
    s=cu.splines.new('BEZIER'); s.bezier_points.add(len(points)-1)
    for i,(p,co) in enumerate(zip(s.bezier_points,points)):
        p.co=co; p.handle_left_type='AUTO'; p.handle_right_type='AUTO'
        p.radius=(.32+.68*math.sin(math.pi*(.15+.8*i/(len(points)-1)))) if taper else 1
    o=bpy.data.objects.new(name,cu); bpy.context.collection.objects.link(o)
    bpy.ops.object.select_all(action='DESELECT'); o.select_set(True)
    bpy.context.view_layer.objects.active=o; bpy.ops.object.convert(target='MESH')
    parts.append(o); return o

def loft(name, rings, n=48):
    # z, x center, y center, x radius, y radius; organic elliptical cross sections.
    verts=[]; faces=[]
    for z,x,y,rx,ry in rings:
        for i in range(n):
            a=2*math.pi*i/n
            verts.append((x+rx*math.cos(a),y+ry*math.sin(a),z))
    for j in range(len(rings)-1):
        for i in range(n):
            a=j*n+i; b=j*n+(i+1)%n
            faces.append((a,b,b+n,a+n))
    faces.append(tuple(reversed(range(n))))
    faces.append(tuple((len(rings)-1)*n+i for i in range(n)))
    me=bpy.data.meshes.new(name); me.from_pydata(verts,[],faces); me.update()
    ob=bpy.data.objects.new(name,me); bpy.context.collection.objects.link(ob)
    bpy.context.view_layer.objects.active=ob
    mod=ob.modifiers.new('Sculpt surface subdivision','SUBSURF'); mod.levels=2
    bpy.ops.object.modifier_apply(modifier=mod.name)
    parts.append(ob); return ob

def merge(objects,name,voxel=.085,smooth=3):
    bpy.ops.object.select_all(action='DESELECT')
    for o in objects:o.select_set(True)
    bpy.context.view_layer.objects.active=objects[0]
    bpy.ops.object.join(); ob=bpy.context.object; ob.name=name
    bpy.ops.object.transform_apply(location=True,rotation=True,scale=True)
    m=ob.modifiers.new('Sculpt union','REMESH'); m.mode='VOXEL'; m.voxel_size=voxel
    bpy.ops.object.modifier_apply(modifier=m.name)
    m=ob.modifiers.new('Sculpt polish','SMOOTH'); m.factor=.45; m.iterations=smooth
    bpy.ops.object.modifier_apply(modifier=m.name)
    return ob

def subtract(ob,cutter):
    if cutter in parts: parts.remove(cutter)
    bpy.context.view_layer.objects.active=ob
    m=ob.modifiers.new('Sculpted recess','BOOLEAN'); m.operation='DIFFERENCE'
    m.solver='EXACT'; m.object=cutter
    bpy.ops.object.modifier_apply(modifier=m.name)
    bpy.data.objects.remove(cutter,do_unlink=True)

def eyelet(name,x,y,z,r=.35):
    ring(name,(x,y,z),r,.18)

# Low stone plinth; natural flagstone cracks, not a decorative toy pedestal.
rod('40 mm bevelled stone base',(0,0,.4),(0,0,2.5),20,vertices=128)
ring('Base bevel',(0,0,.65),19.45,.55,False)
for x,y,sx,sy in [(-10,5,6,4),(0,9,5,5),(9,6,5,4),(11,-5,5,6),(-6,-10,6,4)]:
    o=box('Broken flagstone',(x,y,2.35),(sx,sy,.7),.35)
    o.rotation_euler[2]=random.uniform(-.4,.4)
for i in range(17):
    x=random.uniform(-15,15); y=random.uniform(6,13)
    if x*x+y*y<320: ell('Stone chips',(x,y,2.7),(random.uniform(.4,1),.65,.4))

# Weight-bearing legs have an asymmetric stance and shaped footwear.
for side in (-1,1):
    x=side*4.5; y=.5 if side<0 else -.5
    loft('Heavy trouser leg',[(6,x,y,2.2,2.4),(9,x,y,2.6,2.7),
        (13,x+.3*side,y+.5,3,3),(17,x,y+.5,3.1,3.2),(20,x,y+.5,3.5,3.3)])
    ell('Leather boot vamp',(x,y-1.65,4.8),(3.1,4.55,2.1))
    loft('Folded boot shaft',[(4,x,y,2.7,2.7),(6,x,y,2.9,3),(8.7,x,y,2.4,2.4),
        (10,x,y,2.7,2.6),(10.6,x,y,2.8,2.7)])
    ell('Boot welt sole',(x,y-1.6,3.2),(3.2,4.5,.65))
    # Stitched toe seam follows the leather, avoiding raised block armour.
    stroke('Toe cap seam',[(x-2.5,y-3.2,5.1),(x-1.7,y-4.1,6.1),
        (x,y-4.5,6.4),(x+1.8,y-4.0,6.0),(x+2.6,y-3.0,5.2)],.18)
    for j in range(4):
        z=7.0+j*.68
        stroke('Boot crossed lace',[(x-1,y-2.4,z),(x,y-2.8,z+.25),(x+1,y-2.4,z+.55)],.22)
    for j in range(4):
        z=10.7+j*1.5
        stroke('Trouser compression wrinkle',[(x-2.3,y-1.8,z),(x-.4,y-2.7,z+.45),
            (x+1.9,y-2.0,z+.2)],.30,True)

# Sculpt torso separately: continuous belly and chest, with real creases.
skin_start=len(parts)
loft('Torso anatomical form',[(18.5,0,.8,5.9,3.9),(21,0,.7,7.0,4.6),
    (24,.3,0,8.1,5.6),(28,.6,-.7,9.0,6.2),(31.5,.2,-.3,8.8,5.8),
    (35,0,.5,8.0,4.7),(38,0,.8,7.3,4.3),(40,0,.7,5.4,3.4)])
ell('Pectoral left',(-3.0,-.8,35.2),(4.4,2.1,2.5))
ell('Pectoral right',(3.3,-.8,35.0),(4.4,2.0,2.5))
ell('Neck trapezius',(0,.7,40.2),(4.4,3.3,3.8))
skin=merge(parts[skin_start:],'Continuous anatomical torso',.09,7)
parts[skin_start:]=[skin]
subtract(skin,ell('Navel sculpt cutter',(1.9,-6.92,27.1),(.43,.75,.62)))
for side in (-1,1):
    subtract(skin,stroke('Lower belly crease',[(side*.3,-4.8,22.7),
        (side*3.8,-4.65,22.8),(side*6.1,-3.9,23.7)],.22))

# Fabric tunic and uneven skirt edge, folds generated as one draped surface.
loft('Tunic skirt underlayer',[(13,0,1,6.7,4.0),(14,0,1,7.7,4.3),
    (17,0,.6,7.4,4.5),(21,0,.7,6.8,4.4),(23,0,.7,6.9,4.2)])
for i in range(11):
    a=math.pi+(i/10)*math.pi
    x=7.5*math.cos(a); y=.5+4.3*math.sin(a)
    stroke('Draped cloth fold',[(x*.85,y*.85,22),(x*.95,y,19.5),
        (x*1.02,y-.18,16.2),(x*1.0,y,13.8+.5*math.sin(i))],.38,True)
# Front split leather apron with a border and diagonal wear folds.
for side in (-1,1):
    loft('Split leather apron',[(13.4,side*2.0,-4.0,1.9,.42),
        (16.0,side*2.15,-4.0,2.1,.55),(19,side*2.3,-4.2,2.3,.55),
        (22,side*2.35,-4.0,2.5,.65)])
    stroke('Apron stitched edge',[(side*.35,-4.65,21),(side*.5,-4.68,18),
        (side*.25,-4.6,14.2)],.16)
    for j in range(7):
        ell('Apron stitch',(side*.65,-4.72,14.8+j*.83),(.14,.13,.23))

# Jacket: separate shaped panels, rolled collars, seams, layered pauldrons.
for side in (-1,1):
    loft('Open leather coat side',[(20,side*6.4,1,2.0,3.0),
        (25,side*7.3,1.1,1.7,3.7),(30,side*7.7,1.7,1.8,4.0),
        (35,side*6.4,1.5,2.8,4.0),(39,side*5.8,1.3,3.1,3.4)])
    stroke('Turned jacket lapel',[(side*3.8,-1.9,40),(side*5.4,-3.0,37.5),
        (side*6.2,-3.55,34),(side*7.2,-3.6,30),(side*7.5,-3.3,25)],.7)
    stroke('Raised jacket seam',[(side*8.2,1.5,24),(side*8.8,1.3,29),
        (side*8.2,.5,35),(side*6.9,-.5,38.5)],.22)
    ell('Deltoid under sleeve',(side*8.2,1.2,36.6),(3.6,3.6,3.6))
    for k in range(3):
        z=37.9-k*1.05
        ell('Overlapping shoulder leather',(side*(7.6+k*.55),.4,z),(3.3,3.7,.85))
    for j in range(5):
        ell('Shoulder rivet',(side*(5.6+j*.8),-2.6,37.9-j*.18),(.3,.22,.3))
    ell('Muscular upper arm',(side*9.6,1,33.4),(2.8,3.0,4.1))
    ell('Elbow sleeve',(side*10.0,.2,30.9),(2.7,3.0,2.5))
    stroke('Sleeve rolled edge',[(side*8,-1.3,33),(side*9.6,-2,32.5),
        (side*11.4,-1.4,32.6)],.5)

# Shaped articulated hand on the weapon, visible individual bent fingers.
rod('Right forearm bone',(9.6,0,31),(11.3,-3.2,32.1),2.25,2.1,32)
ell('Right palm',(11.3,-3.2,32.8),(2.15,1.75,2.4))
for j in range(4):
    z=31.15+j*.88
    stroke('Curled gauntlet finger',[(10.0,-4.0,z),(10.6,-5.0,z+.13),
        (11.9,-5.25,z+.1),(12.7,-4.55,z+.13),(12.7,-3.8,z+.25)],.48)
stroke('Right opposing thumb',[(10,-3.0,34.1),(10.4,-4.5,34.7),(11.5,-4.8,34.3)],.65)
for z in (29.8,30.8):
    ring('Right bracer metal rim',(10.7,-1.8,z),2.4,.28,False)
rod('Left shield forearm',(-9.7,.3,32),(-7.4,-4.6,35.8),2.2)
ell('Left palm behind shield',(-7.0,-5.0,36.4),(1.8,1.7,2.3))
for j in range(4):
    z=34.8+j*.91
    stroke('Shield gripping fingers',[(-6.6,-4.4,z),(-5.7,-5.35,z),
        (-6,-6.65,z),(-7,-7.05,z)],.5)

# Belt is irregular and conforms to the belly; detailed buckle and attachments.
loft('Broad waist belt',[(21.1,0,.1,7.4,4.9),(21.4,0,.1,7.7,5.15),
    (23.0,0,.1,7.8,5.25),(23.4,0,.1,7.5,5.0)])
for z in (21.5,23.0):
    stroke('Belt sewn edge',[(-6,-3,z),(-3,-4.8,z),(0,-5.1,z),(3,-4.8,z),(6,-3.2,z)],.18)
box('Buckle recessed back',(1,-5.25,22.2),(3.8,.65,2.6),.3)
stroke('Ornate buckle frame',[(-.8,-5.85,21.2),(-.95,-5.85,22.3),
    (-.5,-5.85,23.4),(2.5,-5.85,23.4),(2.9,-5.85,22.2),(2.6,-5.85,21.2),(-.8,-5.85,21.2)],.32)
rod('Buckle prong',(.1,-5.9,22.2),(2.3,-5.9,22.2),.18)
for x in (-5,-3.5,4.8,6): ell('Belt stud',(x,-4.4 if abs(x)>4 else -5,22.2),(.25,.3,.27))
for x in (6.8,8.1):
    box('Leather pouch',(x,-.5,19.6),(2.9,3.6,4.2),.75)
    stroke('Pouch flap seam',[(x-1.2,-2.45,20.7),(x,-2.6,19.9),(x+1.1,-2.4,20.7)],.21)
    ell('Pouch clasp',(x,-2.65,20),(.28,.2,.35))
rod('Potion bottle',(-6.2,-4.2,17),(-6.2,-4.2,20),1.05,vertices=32)
ell('Flask shoulder',(-6.2,-4.2,20),(1.05,1.05,.65))
rod('Bottle neck',(-6.2,-4.2,20),(-6.2,-4.2,21.5),.62,vertices=24)
for z in (17.4,19.8):ring('Bottle cage band',(-6.2,-4.2,z),1.07,.23,False)
for dx in (-.7,.7): rod('Bottle cage strap',(-6.2+dx,-4.85,17.1),(-6.2+dx,-4.85,20),.18)

# Tower shield, with crowned timber, wrought iron straps, inlays and wear marks.
sx=-12.1; sy=-6.3
for j in range(6):
    x=sx-4.8+j*1.92
    h=41.0+.65*math.cos((j-2.5)*.4)
    box('Individual aged oak shield plank',(x,sy,3+h/2),(2.04,2.65,h),.35)
    for k in range(3):
        xx=x+(k-1)*.48
        points=[]
        for m in range(8):
            z=5+m*5.2
            points.append((xx+.14*math.sin(m*1.3+j+k),sy-1.34,z))
        stroke('Oak raised grain',points,.10)
for x in (sx-5.6,sx+5.6):
    box('Forged iron shield edge',(x,sy-1.25,24),(1.05,1.1,42.2),.23)
    for z in (5,10,17,24,31,38,43):
        rod('Shield hex rivet',(x,sy-1.6,z),(x,sy-2.05,z),.38,vertices=6)
for z in (4.6,16.8,31,44.0):
    box('Shield cross brace',(sx,sy-1.35,z),(11.7,1.05,1.2),.18)
    for dx in (-4.5,4.5): ell('Cross brace peened rivet',(sx+dx,sy-1.98,z),(.3,.22,.3))
for z,r in ((25.1,4.25),(37.8,2.5),(10.4,2.6)):
    gear('Engraved shield clockwork',sx,sy-2.0,z,r,16 if r>3 else 12)
    ring('Gear inner concentric rim',(sx,sy-2.65,z),r*.44,.17)
    for j in range(6):
        a=j*math.pi/3
        rod('Gear countersunk bolt',(sx+r*.52*math.sin(a),sy-2.4,z+r*.52*math.cos(a)),
            (sx+r*.52*math.sin(a),sy-2.85,z+r*.52*math.cos(a)),.22,vertices=6)
# Diagonal scuffs are substantial enough to remain as metal wear relief.
for x,z in [(sx-3,20),(sx+2.8,34),(sx-2,40),(sx+3,7)]:
    stroke('Shield diagonal battle scar',[(x-.6,sy-1.44,z-.9),(x+.6,sy-1.45,z+.9)],.15)

# Elaborate brass steam mace, replacing the oversized rectangular toy hammer.
wx=12.0; wy=-3.8
rod('Mace central shaft',(wx,wy,20),(wx,wy,42.3),.9,vertices=32)
for z in [25+i*.66 for i in range(9)]:
    ring('Leather wrapped grip',(wx,wy,z),.94,.17,False)
for z in (20.3,23.5,34.8,36.4,39.7,43.0):
    ring('Mace brass collar',(wx,wy,z),1.12,.28,False)
ell('Mace pommel',(wx,wy,20.2),(1.35,1.35,1.4))
loft('Steam pressure chamber',[(36.3,wx,wy,1.25,1.25),(37,wx,wy,2.15,2.15),
    (41.3,wx,wy,2.15,2.15),(42.4,wx,wy,1.5,1.5)])
for j in range(8):
    a=j*math.pi/4
    rod('Pressure chamber vertical rib',(wx+1.9*math.cos(a),wy+1.9*math.sin(a),37.2),
        (wx+1.9*math.cos(a),wy+1.9*math.sin(a),41.5),.34)
rod('Mace round head axle',(wx-2.7,wy,42.4),(wx+2.7,wy,42.4),1.8,vertices=48)
ell('Mace rounded outer cap',(wx+2.6,wy,42.4),(1.0,1.85,1.85))
gear('Pressure valve face',wx,wy-2.1,39.2,1.7,10)
stroke('Steam recirculation pipe',[(wx+1,-2.1,41),(wx+2.5,-1.7,40),
    (wx+2.7,-1.7,36.4),(wx+1,-2,35.2)],.52)
for z in (37.7,40.9):
    rod('Steam head bolt',(wx-.9,wy-2.1,z),(wx-.9,wy-2.65,z),.3,vertices=6)

# Head sculpt: cranial mass, heavy brow, planar cheeks, drooping nose and ears.
head_start=len(parts)
ell('Skull',(0,-.05,44.9),(3.9,3.3,4.7))
ell('Lower jaw',(0,-.6,42.3),(3.7,2.9,2.3))
ell('Forehead',(0,-1.35,47.1),(3.55,2.1,2.4))
for side in (-1,1):
    ell('Cheekbone',(side*2.25,-2.45,44.0),(1.65,1.3,1.65))
    ell('Jowl',(side*2.4,-1.9,42.8),(1.4,1.6,1.6))
    ell('Ear outer helix',(side*3.86,.05,44.5),(.87,.8,1.56))
    stroke('Heavy expressive brow',[(side*.35,-3.17,46.1),(side*1.5,-3.63,46.15),
        (side*2.65,-3.13,45.85)],.43)
ell('Nose bridge',(0,-3.0,45.0),(.78,1.05,1.8))
ell('Bulbous nose tip',(.05,-4.15,43.9),(1.22,1.25,1.02))
for side in (-1,1): ell('Nostril wing',(side*.88,-3.8,43.8),(.65,.8,.61))
head=merge(parts[head_start:],'Sculpted dwarf face',.065,5)
parts[head_start:]=[head]
for side in (-1,1):
    subtract(head,ell('Eye socket',(side*1.63,-3.45,45.23),(1.0,.8,.58)))
    subtract(head,ell('Nostril',(side*.75,-4.45,43.45),(.32,.5,.26)))
    subtract(head,ell('Ear concha',(side*4.15,-.6,44.65),(.39,.4,.85)))
    ell('Small inset eye',(side*1.6,-3.20,45.22),(.48,.32,.22))
    stroke('Upper eyelid',[(side*.95,-3.35,45.28),(side*1.6,-3.57,45.46),
        (side*2.25,-3.31,45.28)],.23)
    stroke('Lower eyelid',[(side*.9,-3.4,45.1),(side*1.6,-3.72,44.91),
        (side*2.35,-3.32,45.12)],.19)
    stroke('Nasolabial fold',[(side*1.2,-3.4,43.6),(side*1.7,-3.25,42.9),
        (side*1.95,-3.15,42.2)],.24,True)
    for j in range(2):
        stroke('Temple age line',[(side*2.55,-2.97,45.0-j*.4),
            (side*3.05,-2.6,44.9-j*.45)],.13)
for j in range(2):
    stroke('Forehead age furrow',[(-2.2,-2.65,47.3+j*.45),(-1,-3.25,47.5+j*.42),
        (0,-3.45,47.55+j*.42),(1,-3.25,47.5+j*.42),(2.2,-2.65,47.3+j*.45)],.13)
stroke('Lower lip',[(-1.45,-3.43,42.2),(0,-3.8,42.0),(1.45,-3.43,42.2)],.34,True)

# Receding scalp and naturally swept side hair; no tall cartoon hairstyle.
for side in (-1,1):
    ell('Side hair mass',(side*3.3,.4,44.3),(1.25,2.5,3.4))
    for i in range(13):
        a=i/12
        stroke('Swept individual side hair',[(side*(2.5+.7*a),1.6-3*a,48.1-.5*a),
            (side*(3.7+.2*a),1.6-3.0*a,46.5),(side*4.0,1.5-2.8*a,43.7),
            (side*4.5,1.2-2.5*a,41.0)],.22,True)
ell('Back hair silhouette',(0,2.0,44.4),(3.6,2.0,4.1))
for i in range(14):
    x=-3.3+i*.5
    stroke('Back hair lock',[(x,2.4,47.3),(x*1.15,3.55,44.6),(x*1.3,3.1,40.9)],.29,True)

# Beard follows curved masses; many tapered locks with secondary strand relief.
ell('Beard understructure',(0,-3.3,39.4),(4.7,2.5,3.8))
for i in range(29):
    a=(i-14)/14
    x=a*4.2
    endz=33.8+2.7*abs(a)+random.uniform(-.65,.65)
    sway=random.uniform(-.45,.45)
    pts=[(x*.67,-3.75,42.4-.35*abs(a)),(x*.95+sway,-5.6,40.5),
        (x*1.14-sway,-5.85,38.2),(x*1.08+sway,-5.1,endz+.7),
        (x*.98,-4.6,endz)]
    stroke('Major sculpted beard curl',pts,.42+random.uniform(-.08,.16),True)
    for k in (-1,1):
        stroke('Beard strand definition',[(p[0]+k*.16,p[1]-.32,p[2]-.05) for p in pts],.13,True)
for side in (-1,1):
    stroke('Natural drooping moustache',[(side*.1,-4.02,43.0),(side*1.25,-4.5,42.8),
        (side*2.7,-4.3,42.1),(side*3.45,-4.0,40.6)],.65,True)
    for j in range(4):
        stroke('Moustache strand',[(side*.35,-4.35,43.05-j*.18),
            (side*1.7,-4.87,42.7-j*.13),(side*3.0,-4.35,41.5-j*.2)],.13,True)
    # Braids made of three interwoven tapered strands, supported by thicker core.
    path=[(side*3.7,-4.9,42),(side*4.8,-5.8,39),(side*5.8,-5.5,35.6),(side*6.2,-5.0,32.3)]
    stroke('Braid supporting core',path,1.04,True)
    for strand in range(3):
        pts=[]
        for j in range(43):
            t=j/42; ang=t*math.pi*7+strand*math.pi*2/3
            pts.append((side*(3.7+2.6*t)+.57*math.cos(ang),
                -5.1-.65*math.sin(math.pi*t)+.57*math.sin(ang),42-9.7*t))
        stroke('Woven three-strand beard braid',pts,.47)
    for z,r in ((33.0,1.02),(34.2,1.05)):
        rod('Engraved beard ferrule',(side*6.0,-5.1,z-.35),(side*6.0,-5.1,z+.35),r,vertices=32)
    for j in range(5):
        stroke('Loose beard tip',[(side*(5.6+j*.22),-5.1,32.8),
            (side*(5.6+j*.25),-5.3,31.8),(side*(5.4+j*.25),-5.0,31.2)],.22,True)

# Small goggles resting on forehead: rims, bridge, leather strap and side screws.
for x in (-1.55,1.55):
    rod('Goggle lens mounting',(x,-2.3,48),(x,-3.15,48),1.05,vertices=48)
    ring('Goggle outer rim',(x,-3.2,48),1.04,.23)
    ring('Goggle inner rim',(x,-3.28,48),.78,.12)
    for dx in (-.72,.72):ell('Goggle rim screw',(x+dx,-3.4,48),(.16,.12,.16))
stroke('Goggle bridge',[(-.55,-3.3,48),(0,-3.45,48.25),(.55,-3.3,48)],.2)
stroke('Goggle strap',[(-3.2,-1.1,47.8),(-3.7,.4,47.8),(-2.6,2.5,48),
    (0,3.1,48),(2.6,2.5,48),(3.7,.4,47.8),(3.2,-1.1,47.8)],.36)

print('SCULPT_COMPONENTS',len(parts),flush=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT,'dwarf_v2_editable.blend'))
model=merge(parts,'Gearshield dwarf — detailed revision',.075,2)
dec=model.modifiers.new('Optimized sculpt surface','DECIMATE'); dec.ratio=.55
bpy.ops.object.modifier_apply(modifier=dec.name)

# Keep just the connected sculpt, normalize print height and validate topology.
import bmesh
bm=bmesh.new(); bm.from_mesh(model.data)
seen=set(); comps=[]
for v in bm.verts:
    if v in seen:continue
    todo=[v]; seen.add(v); vs=[]
    while todo:
        v=todo.pop();vs.append(v)
        for e in v.link_edges:
            w=e.other_vert(v)
            if w not in seen:seen.add(w);todo.append(w)
    comps.append(vs)
largest=max(comps,key=len)
discarded=[v for vs in comps if vs is not largest for v in vs]
print('Removed floating sculpt remnants:',len(discarded),flush=True)
bmesh.ops.delete(bm,geom=discarded,context='VERTS')
lo=min(v.co.z for v in bm.verts); hi=max(v.co.z for v in bm.verts)
for v in bm.verts:v.co.z=(v.co.z-lo)*53/(hi-lo)
bm.to_mesh(model.data);model.data.update();bpy.context.view_layer.update()
stats={'dimensions_mm':list(model.dimensions),'connected_shells':1,
    'non_manifold_edges':sum(not e.is_manifold for e in bm.edges),
    'signed_volume_mm3':bm.calc_volume(signed=True),'faces':len(bm.faces)}
bm.free()
with open(os.path.join(OUT,'validation.json'),'w') as f:json.dump(stats,f,indent=2)
print('VALIDATION',json.dumps(stats),flush=True)
bpy.ops.object.select_all(action='DESELECT');model.select_set(True)
bpy.context.view_layer.objects.active=model
bpy.ops.wm.stl_export(filepath=os.path.join(OUT,'gearshield_dwarf_v2_50mm.stl'),export_selected_objects=True)

# Render the real print mesh in uniform grey clay, with no painted-on detail.
for p in model.data.polygons:p.use_smooth=True
mat=bpy.data.materials.new('Neutral sculpt clay');mat.diffuse_color=(.32,.35,.37,1)
mat.use_nodes=True;bs=mat.node_tree.nodes.get('Principled BSDF')
bs.inputs['Base Color'].default_value=(.32,.35,.37,1);bs.inputs['Roughness'].default_value=.61
model.data.materials.clear();model.data.materials.append(mat)
scene=bpy.context.scene;scene.unit_settings.system='METRIC';scene.unit_settings.scale_length=.001
scene.render.engine='CYCLES';scene.cycles.samples=48;scene.cycles.use_denoising=False
scene.render.resolution_x=1300;scene.render.resolution_y=1500;scene.render.resolution_percentage=100
scene.world.color=(.07,.07,.07);scene.view_settings.view_transform='AgX'
def aim(o,p):o.rotation_euler=(Vector(p)-o.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.camera_add(location=(60,-150,78));cam=bpy.context.object
aim(cam,(0,-.5,26));cam.data.type='ORTHO';cam.data.ortho_scale=65;scene.camera=cam
for loc,power,size in [((-45,-60,95),75000,55),((50,-25,60),28000,50),((20,40,75),100000,40)]:
    bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object
    o.data.energy=power;o.data.shape='DISK';o.data.size=size;aim(o,(0,0,26))
scene.render.image_settings.file_format='PNG';scene.render.filepath=os.path.join(OUT,'preview_v2.png')
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT,'gearshield_dwarf_v2.blend'))
bpy.ops.render.render(write_still=True)
cam.location=(0,-150,64);aim(cam,(0,0,27));cam.data.ortho_scale=61
scene.render.filepath=os.path.join(OUT,'preview_v2_front.png');bpy.ops.render.render(write_still=True)
cam.location=(45,-130,65);aim(cam,(0,-1,42));cam.data.ortho_scale=24
scene.render.filepath=os.path.join(OUT,'preview_v2_portrait.png');bpy.ops.render.render(write_still=True)

