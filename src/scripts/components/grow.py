#!/usr/bin/env python
# -*- coding: utf-8 -*-
from swine.component import SpriteRenderer
from swine.component.physics import RigidBody
from swine.object import Component


class ComponentGrow(Component):
    def __init__(self):
        Component.__init__(self)
        self.sprite_render = None
        self.rigid_body = None

        self.mass = 0.5

        self.timer = 0

        self.speed = 0
        self.increase = 0.0001

    def start(self):
        self.sprite_render: SpriteRenderer = self.parent.get_component(SpriteRenderer)
        self.rigid_body: RigidBody = self.parent.get_component(RigidBody)

    def update(self, dt):
        self.timer += 1

        if self.timer >= 5:
            self.mass += 0.5
            self.sprite_render.sprite.scale += self.increase

            self.timer = 0
