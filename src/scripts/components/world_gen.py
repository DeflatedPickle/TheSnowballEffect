#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

import pymunk
from swine.component import Transform
from swine.object import Component

from src.scripts.prefabs.tile_snow import PrefabTileSnow
from src.scripts.prefabs.tiny_rock import PrefabTinyRock
from src.scripts.prefabs.tree import PrefabTree


class ComponentWorldGen(Component):
    def __init__(self):
        Component.__init__(self)

        self.last_row = None

    def start(self):
        window = self.parent.scene.window

        for y in range((-window.height // 2) + 16, window.height // 2, 32):
            self.new_row(y)

    def update(self, dt=None):
        player_y = self.parent.scene.get_object("Player").get_component(Transform).position.y

        if round(player_y - self.last_row.y) <= 480:
            self.new_row(self.last_row.y - 32)

    def new_row(self, y):
        window = self.parent.scene.window

        items = []
        for x in range((-window.width // 2) + 16, window.width // 2, 32):
            self.last_row = pymunk.Vec2d(x, y)

            snow = PrefabTileSnow(self.parent.scene)
            snow.get_component(Transform).position = self.last_row
            items.append(snow)

            random = randint(0, 100)
            obj = None

            if 21 < random < 29:
                obj = PrefabTree(self.parent.scene)

            elif 51 < random < 59:
                obj = PrefabTinyRock(self.parent.scene)

            if obj is not None:
                obj.get_component(Transform).position = pymunk.Vec2d(x, y)

            if obj is not None:
                items.append(obj)

        return items
