#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymunk
from swine.component import Transform, SpriteRenderer, Viewport
from swine.component.physics import RigidBody
from swine.graphics import Sprite
from swine.object import GameObject, Anchor
from swine.window import Scene

from src.scripts.components.follow import ComponentFollow
from src.scripts.components.move import ComponentMove
from src.scripts.components.world_gen import ComponentWorldGen


class SceneGame(Scene):
    def __init__(self, window):
        Scene.__init__(self, window, pymunk.Vec2d(0, -7))

        self.world_gen = GameObject(self, "WorldGen", [ComponentWorldGen()])

        self.camera = GameObject(self, "Camera", [Transform(), Viewport(),
                                                  ComponentFollow()])

        self.player_sprite = Sprite("src/resources/player/snowball.png", Anchor.MIDDLE_CENTER)
        self.player = GameObject(self, "Player", [Transform(), SpriteRenderer(self.player_sprite), RigidBody(1, False, False),
                                                  ComponentMove()])
