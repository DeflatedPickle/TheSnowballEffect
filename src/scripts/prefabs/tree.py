#!/usr/bin/env python
# -*- coding: utf-8 -*-
from swine.component import Transform, SpriteRenderer
from swine.graphics import Sprite
from swine.object import GameObject, Anchor


class PrefabTree(GameObject):
    def __init__(self, scene):
        self.sprite = Sprite("src/resources/tree.png", Anchor.MIDDLE_CENTER)

        GameObject.__init__(self, scene, f"Tree{len(scene.object_list)}", [Transform(), SpriteRenderer(self.sprite)], never_reload=True)
