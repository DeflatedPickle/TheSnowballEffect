#!/usr/bin/env python
# -*- coding: utf-8 -*-
from swine.component import Transform, SpriteRenderer
from swine.graphics import Sprite
from swine.object import GameObject, Anchor


class PrefabTileSnow(GameObject):
    def __init__(self, scene):
        self.sprite = Sprite("src/resources/tile/snow.png", Anchor.MIDDLE_CENTER)

        GameObject.__init__(self, scene, f"Tree{len(scene.object_list)}", [Transform(), SpriteRenderer(self.sprite, scene.window.get_layer_by_name("Snow"), scale=2)], never_reload=True)
