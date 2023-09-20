# これを走らせる前に、全てのオブジェクトを全トランスフォーム適用して、原点を重心に移動しなおす。
# 全トランスフォームを適用しないと、拡大縮小の倍率がおかしくなる
import bpy

def apply_boolean_difference(boolee, booler, magnification_power=4):
    if boolee is not None and booler is not None:
        # boolerオブジェクトの初期スケールを保存
        initial_scale = booler.scale.copy()

        # boolerオブジェクトをアクティブに設定
        bpy.context.view_layer.objects.active = booler

        # オブジェクトモードに切り替え
        bpy.ops.object.mode_set(mode='OBJECT')

        # boolerオブジェクトを指定の倍率で拡大
        booler.scale = (magnification_power, magnification_power, magnification_power)

        # booleeオブジェクトをアクティブに設定
        bpy.context.view_layer.objects.active = boolee

        # ブールモディファイアを追加
        bool_mod = boolee.modifiers.new(name="Boolean", type='BOOLEAN')
        bool_mod.operation = 'DIFFERENCE'  # 差分モード

        # ブール演算に使用するオブジェクトとしてboolerを設定
        bool_mod.use_self = True
        bool_mod.object = booler

        # ブールモディファイアを適用
        bpy.ops.object.modifier_apply(modifier=bool_mod.name)

        # boolerオブジェクトのスケールを元に戻す
        booler.scale = initial_scale

# MESH_005_mesh_オブジェクトをbooleeに格納
boolee = bpy.data.objects.get("MESH_005_mesh_")

# MESH_006_mesh_オブジェクトをboolerに格納
booler = bpy.data.objects.get("MESH_006_mesh_")

# 関数を呼び出してブール演算を適用
apply_boolean_difference(boolee, booler, magnification_power=4)
