#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

import pymunk
from swine.component import Transform, SpriteRenderer, Viewport
from swine.graphics import Sprite
from swine.object import GameObject, Anchor
from swine.window import Scene

from src.scripts.components.follow import ComponentFollow
from src.scripts.components.roll import ComponentRoll
from src.scripts.components.world_gen import ComponentWorldGen


class SceneGame(Scene):
    def __init__(self, window):
        Scene.__init__(self, window)

        self.world_gen = GameObject(self, "WorldGen", [ComponentWorldGen()])

        self.camera = GameObject(self, "Camera", [Transform(), Viewport(),
                                                  ComponentFollow()])

        self.player_sprite = Sprite("src/resources/player/snowball.png", Anchor.MIDDLE_CENTER)
        self.player = GameObject(self, "Player", [Transform(), SpriteRenderer(self.player_sprite),
                                                  ComponentRoll()])
