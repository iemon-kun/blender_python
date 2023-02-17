import bpy

# アクティブなオブジェクトを取得
active_obj = bpy.context.view_layer.objects.active

# アクティブなノードを取得する
active_node = active_obj.active_material.node_tree.nodes.active

# オブジェクトの全てのマテリアルに対して処理を行う
for material_slot in active_obj.material_slots:
    material = material_slot.material
    
    # ノードエディターを開き、マテリアルのノードツリーを取得
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    node_tree = material.node_tree

    # 画像テクスチャノードがあるかどうかを確認
    has_image_texture = False
    for node in nodes:
        if node.type == 'TEX_IMAGE' and node.image is None:
            has_image_texture = True
            # 画像が未設定の画像テクスチャノードがある場合、アクティブなノードと同じ画像をリンクさせる
            node.image = active_node.image
            break
    
    # 画像テクスチャノードがない場合は処理をスキップ
    if not has_image_texture:
        continue

    # ノードエディターを更新
    node_tree.update_tag()
