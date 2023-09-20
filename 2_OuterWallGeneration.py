import bpy

# カーブオブジェクトを選択
curve_obj = bpy.context.active_object

# カーブをメッシュに変換
bpy.ops.object.select_all(action='DESELECT')  # すべてのオブジェクトの選択を解除
curve_obj.select_set(True)  # カーブオブジェクトを選択
bpy.context.view_layer.objects.active = curve_obj  # アクティブオブジェクトに設定

# カーブをメッシュに変換
bpy.ops.object.convert(target='MESH')

# 新しいメッシュオブジェクトの参照
mesh_obj = bpy.context.active_object

# メッシュを編集モードに切り替え
bpy.ops.object.mode_set(mode='EDIT')

# 全ての頂点を選択
bpy.ops.mesh.select_all(action='SELECT')

# 選択した頂点をExtrude（押し出し）して面を作成
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 100.0)})

# オブジェクトモードに戻す
bpy.ops.object.mode_set(mode='OBJECT')
