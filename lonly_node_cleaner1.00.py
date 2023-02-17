import bpy

# アクティブなオブジェクトを取得
obj = bpy.context.active_object

# 全てのマテリアルについて処理
for material_slot in obj.material_slots:
    material = material_slot.material

    # マテリアルが存在する場合
    if material:
        # ノードグラフを取得
        nodes = material.node_tree.nodes

        # 全てのノードについて処理
        for node in nodes:
            # 入力・出力ともに接続がないノードを削除
            if not isinstance(node, bpy.types.ShaderNodeOutputMaterial) and not node.inputs[0].is_linked and not node.outputs[0].is_linked:
                nodes.remove(node)
