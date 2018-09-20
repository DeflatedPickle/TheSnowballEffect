#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk
from pyglet.window import key
from swine.component.physics import RigidBody
from swine.object import Component

from src.scripts.components.grow import ComponentGrow


class ComponentMove(Component):
    def __init__(self):
        Component.__init__(self)
        self.input = None

        self.rigid = None
        self.grow = None

        self.speed = 20

    def start(self):
        self.input = self.parent.scene.window.input_manager

        self.rigid = self.parent.get_component(RigidBody)
        self.grow = self.parent.get_component(ComponentGrow)

    def update(self, dt):
        force = pymunk.Vec2d(0, 0)

        if self.input.get_key(key.A):
            force.x = -self.speed

        if self.input.get_key(key.D):
            force.x = self.speed

        if self.input.get_key(key.S):
            force.y = 10

        if self.rigid is not None:
            self.rigid.add_force(force.x, force.y - self.grow.mass)
