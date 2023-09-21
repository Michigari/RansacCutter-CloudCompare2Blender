# これを走らせる前に、全てのオブジェクトを全トランスフォーム適用して、原点を重心に移動しなおす。
# 全トランスフォームを適用しないと、拡大縮小の倍率がおかしくなる
# 屋根メッシュのみにしておく。.shpは消す
import bpy
import time
# シーン内のすべてのオブジェクトの名前を取得し、配列に保存
object_names = [obj.name for obj in bpy.context.scene.objects]

# 屋根をブリーリアンで削る
def apply_boolean_difference(boolee, booler, magnification_power):
    if boolee is not None and booler is not None:
        # boolerオブジェクトの初期スケールを保存
        # initial_scale = booler.scale.copy()

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
        # booler.scale = initial_scale
        booler.scale = (1,1,1)

for i in range(len(object_names)):
    print(i)
    time.sleep(0.5)
    boolee = bpy.data.objects.get(object_names[i])
    booler = bpy.data.objects.get(object_names[(i + 1) % len(object_names)])
    apply_boolean_difference(boolee, booler, 4)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)