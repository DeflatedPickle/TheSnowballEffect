#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk
from swine.component import Transform
from swine.object import Component


class ComponentFollow(Component):
    def __init__(self):
        Component.__init__(self)
        self.transform = None

    def start(self):
        self.transform = self.parent.get_component(Transform)

    def update(self, dt=None):
        player = self.parent.scene.get_object("Player")

        if player is not None:
            player_transform = player.get_component(Transform)

            if self.transform is not None and player_transform is not None:
                self.transform.position = pymunk.Vec2d(player_transform.position.x, player_transform.position.y)
