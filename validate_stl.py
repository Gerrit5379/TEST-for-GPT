"""Independently reimport the exported STL and validate its mesh."""
import bpy,bmesh,json,os
OUT=os.path.dirname(os.path.abspath(__file__))
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.wm.stl_import(filepath=os.path.join(OUT,'gearshield_dwarf_50mm.stl'))
o=bpy.context.object
bm=bmesh.new(); bm.from_mesh(o.data)
seen=set(); shells=0
for v in bm.verts:
    if v in seen: continue
    shells+=1; todo=[v]; seen.add(v)
    while todo:
        n=todo.pop()
        for e in n.link_edges:
            w=e.other_vert(n)
            if w not in seen: seen.add(w); todo.append(w)
result={'source':'reimported binary STL','dimensions_mm':list(o.dimensions),
        'triangles':len(bm.faces),'connected_shells':shells,
        'non_manifold_edges':sum(not e.is_manifold for e in bm.edges),
        'signed_volume_mm3':bm.calc_volume(signed=True)}
assert shells==1, result
assert result['non_manifold_edges']==0, result
assert result['signed_volume_mm3']>0, result
assert abs(o.dimensions.z-53)<.01, result
with open(os.path.join(OUT,'stl_validation.json'),'w') as f: json.dump(result,f,indent=2)
print('STL_VALIDATION',json.dumps(result),flush=True)
bm.free()
