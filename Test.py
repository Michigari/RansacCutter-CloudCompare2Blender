import bpy
import math

# 1. "CLOUD"から始まる名前を持つオブジェクトを削除
objects_to_delete = [obj for obj in bpy.data.objects if obj.name.startswith("CLOUD")]

# オブジェクトを削除
for obj in objects_to_delete:
    bpy.data.objects.remove(obj)

# 2. スケールの増加率を設定します。この例では2倍にしますが、必要に応じて変更してください。
scale_factor = 2.0

# 3. すべてのメッシュオブジェクトに対して処理を行います。
for obj in bpy.data.objects:
    # オブジェクトがメッシュであるか確認します。
    if obj.type == 'MESH':
        # オブジェクトのスケールを取得します。
        current_scale = obj.scale
        # スケールを増加率で乗算します。
        new_scale = (current_scale[0] * scale_factor, current_scale[1] * scale_factor, current_scale[2] * scale_factor)
        # 新しいスケールを設定します。
        obj.scale = new_scale

        # 各面の法線角度をチェックし、条件に合致するかどうかを判断します。
        delete_object = False  # メッシュを削除するかどうかを示すフラグ
        normal_angles = []  # 各面の法線角度を格納するリスト

        for polygon in obj.data.polygons:
            normal = polygon.normal
            angle_degrees = math.degrees(normal.angle((0, 0, 1)))
            normal_angles.append(angle_degrees)

        # 法線角度の平均を計算します。
        avg_angle = sum(normal_angles) / len(normal_angles)

        # 平均の法線角度が90度±5度の範囲にある場合、オブジェクトを削除フラグを設定します。
        if abs(avg_angle - 90) <= 5:
            delete_object = True

        # メッシュを削除するフラグが設定されていれば、オブジェクトを選択状態にします。
        if delete_object:
            obj.select_set(True)

# 選択したメッシュオブジェクトを削除します。
bpy.ops.object.delete()

# メッセージを表示
print("CLOUDから始まるオブジェクトを削除し、すべてのメッシュオブジェクトのスケールを増加させ、法線角度が90度±5度のメッシュを削除しました。")
