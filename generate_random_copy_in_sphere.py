import bpy
import random
from mathutils import Vector
from math import sin, cos, pi

def is_within_exclusion_range(location, exclusion_center, exclusion_radius):
    """
    指定された位置が除外範囲内にあるかどうかを判定する関数
    """
    distance = (location - exclusion_center).length
    return distance <= exclusion_radius

def duplicate_objects(obj_name, count, radius, exclusion_center=None, exclusion_radius=0):
    bpy.ops.object.select_all(action='DESELECT')

    # 指定した個数分複製と配置
    for i in range(count):
        # 複製元のオブジェクトを選択
        bpy.context.view_layer.objects.active = bpy.data.objects[obj_name]
        bpy.data.objects[obj_name].select_set(True)

        # 複製
        bpy.ops.object.duplicate()
        duplicated_obj = bpy.context.active_object

        # ランダムな球面座標を生成
        theta = random.uniform(0, 2 * 3.14159)
        phi = random.uniform(0, 3.14159)
        r = random.uniform(0, radius)

        # 座標を設定
        x = r * sin(phi) * cos(theta)
        y = r * sin(phi) * sin(theta)
        z = r * cos(phi)

        location = Vector((x, y, z))

        # 除外範囲内の場合は再生成
        while exclusion_center and is_within_exclusion_range(location, exclusion_center, exclusion_radius):
            theta = random.uniform(0, 2 * 3.14159)
            phi = random.uniform(0, 3.14159)
            r = random.uniform(0, radius)

            x = r * sin(phi) * cos(theta)
            y = r * sin(phi) * sin(theta)
            z = r * cos(phi)

            location = Vector((x, y, z))

        duplicated_obj.location = location

        # 複製したオブジェクトを選択解除
        duplicated_obj.select_set(False)

# メイン処理
if __name__ == "__main__":
    # パラメータの設定
    object_name = "Cube"  # 複製するオブジェクトの名前
    duplicate_count = 165  # 複製する個数
    sphere_radius = 1.0   # 球の半径
    exclusion_center = Vector((0, 0, 0))  # 除外範囲の中心座標
    exclusion_radius = 0  # 除外範囲の半径

    # オブジェクトの複製と配置
    duplicate_objects(object_name, duplicate_count, sphere_radius, exclusion_center, exclusion_radius)
