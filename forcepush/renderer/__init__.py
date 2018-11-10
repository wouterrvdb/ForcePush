import pygame

from forcepush.renderer.debug_renderer import DebugRenderer
from .terrain_renderer import TerrainRenderer
from .Renderer import Renderer
from .BackgroundRenderer import BackgroundRenderer
from .PlayerRenderer import PlayerRenderer
from .Viewport import Viewport

viewport = Viewport(1280, 720)
renderer = Renderer(viewport)
clock = pygame.time.Clock()

terrain_renderer = TerrainRenderer(viewport)
background_renderer = BackgroundRenderer(viewport)
player_renderer = PlayerRenderer(viewport)

renderer.add_renderer(background_renderer)
renderer.add_renderer(terrain_renderer)
renderer.add_renderer(player_renderer)
renderer.add_renderer(DebugRenderer(viewport, clock))
