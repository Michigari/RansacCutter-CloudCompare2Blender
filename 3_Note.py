# これを走らせる前に、全てのオブジェクトを全トランスフォーム適用して、原点を重心に移動しなおす。
# 全トランスフォームを適用しないと、拡大縮小の倍率がおかしくなる
# 屋根メッシュのみにしておく。.shpは消す
import bpy

# シーン内のすべてのオブジェクトの名前を取得し、配列に保存
object_names = [obj.name for obj in bpy.context.scene.objects]
# object_names 配列に名前が保存されました
print(object_names)

# 屋根をブリーリアンで削る
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

# シーン内のオブジェクト数を取得
def count_objects_in_scene():
    # シーン内のすべてのオブジェクトを取得
    objects = bpy.context.scene.objects

    # カウント用の変数を初期化
    object_count = 0

    # オブジェクトをカウント
    for obj in objects:
        if obj.type == 'MESH':  # メッシュオブジェクトの場合
            object_count += 1

    return object_count


# MESH_005_mesh_オブジェクトをbooleeに格納
boolee = bpy.data.objects.get("MESH_005_mesh_")

# MESH_006_mesh_オブジェクトをboolerに格納
booler = bpy.data.objects.get("MESH_006_mesh_")

# 関数を呼び出してブール演算を適用
apply_boolean_difference(boolee, booler, magnification_power=4)
