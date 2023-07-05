import bpy
import random

def duplicate_objects(obj_name, count, x_range, y_range, z_range):
    bpy.ops.object.select_all(action='DESELECT')
    
    
    # 指定した個数分複製と配置
    for i in range(count):
        # 複製元のオブジェクトを選択
        bpy.context.view_layer.objects.active = bpy.data.objects[obj_name]
        bpy.data.objects[obj_name].select_set(True)
        
        # 複製
        bpy.ops.object.duplicate()
        duplicated_obj = bpy.context.active_object
        
        # ランダムな座標を生成
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        z = random.uniform(z_range[0], z_range[1])
        
        # 座標を設定
        duplicated_obj.location = (x, y, z)
        
        # 複製したオブジェクトを選択解除
        duplicated_obj.select_set(False)
        

# メイン処理
if __name__ == "__main__":
    # パラメータの設定
    object_name = "Cube"  # 複製するオブジェクトの名前
    duplicate_count = 165  # 複製する個数
    x_range = (-1, 1)     # X軸方向の範囲
    y_range = (-1, 1)     # Y軸方向の範囲
    z_range = (0, 2)      # Z軸方向の範囲
    
    # オブジェクトの複製と配置
    duplicate_objects(object_name, duplicate_count, x_range, y_range, z_range)