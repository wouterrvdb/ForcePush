import pygame

from forcepush.renderer.debug_renderer import DebugRenderer
from .terrain_renderer import TerrainRenderer
from .PlayerRenderer import PlayerRenderer
from .Renderer import Renderer
from .background_renderer import BackgroundRenderer
from .Viewport import Viewport

viewport = Viewport(1280, 720)
renderer = Renderer(viewport)
clock = pygame.time.Clock()

terrain_renderer = TerrainRenderer(viewport)

player_renderer = PlayerRenderer(viewport)

renderer.add_renderer(BackgroundRenderer(viewport))
renderer.add_renderer(terrain_renderer)
renderer.add_renderer(DebugRenderer(viewport, clock))