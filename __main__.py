#!/usr/bin/env python
# -*- coding: utf-8 -*-
from swine.window import Window, Layer

from src.scripts.scenes.game import SceneGame

window = Window()

snow = Layer(window, "Snow")
logs = Layer(window, "Logs")
player = Layer(window, "Player")
rocks = Layer(window, "Rocks")
leaves = Layer(window, "Leaves")

game = SceneGame(window)

window.mainloop()
