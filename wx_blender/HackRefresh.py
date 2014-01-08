#!/usr/bin/env python

import bpy

def HackRefresh(event=None):
    """
    When moving/sizing the wxFrame, It smears across the blender GUI,
    making it look ugly.

    What is being attempted here is a refresh,
    so to clear the ugliness from the screen.
    """
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
