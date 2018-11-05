from .Renderer import Renderer
from .background_renderer import BackgroundRenderer
from .Viewport import Viewport

viewport = Viewport(1280, 720)
renderer = Renderer(viewport)

renderer.add_renderer(BackgroundRenderer(viewport))