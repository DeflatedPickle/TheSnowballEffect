#!/usr/bin/env python
# -*- coding: utf-8 -*-
from swine.component import Transform, SpriteRenderer
from swine.graphics import Sprite
from swine.object import GameObject, Anchor


class PrefabTree(GameObject):
    def __init__(self, scene):
        self.log = Sprite("src/resources/tree/log.png", Anchor.MIDDLE_CENTER)
        self.leaves = Sprite("src/resources/tree/leaves.png", Anchor.MIDDLE_CENTER)

        GameObject.__init__(self, scene, f"Tree{len(scene.object_list)}", [Transform(), SpriteRenderer(self.log, scene.window.get_layer_by_name("Logs")),
                                                                           SpriteRenderer(self.leaves, scene.window.get_layer_by_name("Leaves"))], never_reload=True)
