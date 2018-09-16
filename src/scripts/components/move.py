#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk
from pyglet.window import key
from swine.component.physics import RigidBody
from swine.object import Component


class ComponentMove(Component):
    def __init__(self):
        Component.__init__(self)
        self.input = None

        self.rigid = None

        self.speed = 20

    def start(self):
        self.input = self.parent.scene.window.input_manager

        self.rigid = self.parent.get_component(RigidBody)

    def update(self, dt):
        force = pymunk.Vec2d(0, 0)

        if self.input.get_key(key.A):
            force.x = -self.speed

        if self.input.get_key(key.D):
            force.x = self.speed

        if self.rigid is not None:
            self.rigid.add_force(force.x, force.y)
