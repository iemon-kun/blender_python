import bpy

# アクティブなオブジェクトを取得する
active_obj = bpy.context.view_layer.objects.active

# アクティブなノードを取得する
active_node = active_obj.active_material.node_tree.nodes.active

# 全てのマテリアルに対して、ノードをペーストする
for material in active_obj.material_slots:
    # マテリアルにノードが存在する場合、新しいノードを作成してペーストする
    if material.material.node_tree:
        new_node = material.material.node_tree.nodes.new(active_node.bl_idname)
        new_node.location = active_node.location
        new_node.hide = active_node.hide
        new_node.mute = active_node.mute
