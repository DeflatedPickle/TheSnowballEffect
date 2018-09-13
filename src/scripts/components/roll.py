#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk
from swine.component import Transform
from swine.object import Component


class ComponentRoll(Component):
    def __init__(self):
        Component.__init__(self)
        self.transform = None

        self.move_by = 0
        self.increment = 0

    def start(self):
        self.transform = self.parent.get_component(Transform)

    def update(self, dt):
        if self.transform is not None:
            pos = self.transform.position
            self.transform.position = pymunk.Vec2d(pos.x, pos.y - self.move_by)

            self.increment += 0.00005
            self.move_by = self.increment
