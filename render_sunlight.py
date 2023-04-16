import glfw
from OpenGL.GL import *
import numpy as np

class SimpleRenderingEngine:
    def __init__(self, width, height):
        # Initialize GLFW
        if not glfw.init():
            raise Exception("GLFW initialization failed")

        # Create a window
        self.window = glfw.create_window(width, height, "Simple OpenGL Rendering Engine", None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("GLFW window creation failed")

        # Make the window's OpenGL context current
        glfw.make_context_current(self.window)

        # Enable depth testing for 3D rendering
        glEnable(GL_DEPTH_TEST)

    def render(self):
        # Rendering loop
        while not glfw.window_should_close(self.window):
            # Clear the color and depth buffers
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # Render the sun using orthographic projection
            self.render_sun()

            # Render the 3D rotating cube using perspective projection
            self.render_cube()

            # Swap the front and back buffers
            glfw.swap_buffers(self.window)

            # Poll for events
            glfw.poll_events()

        # Terminate GLFW
        glfw.terminate()

    def render_sun(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, 1, 0, 1, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glColor3f(1, 1, 0)  # Yellow color for the sun
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(0.9, 0.9)  # Center of the sun
        for i in range(33):
            angle = 2 * np.pi * i / 32
            x = 0.9 + 0.05 * np.cos(angle)
            y = 0.9 + 0.05 * np.sin(angle)
            glVertex2f(x, y)
        glEnd()

    def render_cube(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1, 1, -1, 1, 1.5, 20.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslate(0.0, 0.0, -5.0)

        # Rotate the cube
        glRotatef(glfw.get_time() * 30, 1, 1, 0)

        # Render the cube
        self.draw_cube()

    def draw_cube(self):
        # Vertices of the cube
        vertices = np.array([
            [-1, -1, -1],
            [ 1, -1, -1],
            [ 1,  1, -1],
            [-1,  1, -1],
            [-1, -1,  1],
            [ 1, -1,  1],
            [ 1,  1,  1],
            [-1,  1,  1]
        ], dtype=np.float32)

        # Indices of the vertices that form each face
        faces = np.array([
            [0, 1, 2, 3],
            [1, 5, 6, 2],
            [5, 4, 7, 6],
	    [4, 0, 3, 7],
            [3, 2, 6, 7],
            [4, 5, 1, 0]
        ], dtype=np.uint32)
        glBegin(GL_QUADS)
        for face in faces:
            for vertex in vertices[face]:
                glColor3f(*vertex)  # Use vertex coordinates as colors
                glVertex3f(*vertex)
        glEnd()

# Create the rendering engine and render the scene
rendering_engine = SimpleRenderingEngine(800, 600)
rendering_engine.render()

