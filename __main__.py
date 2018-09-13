#!/usr/bin/env python
# -*- coding: utf-8 -*-
from swine.window import Window

from src.scripts.scenes.game import SceneGame

window = Window()

game = SceneGame(window)

window.mainloop()
