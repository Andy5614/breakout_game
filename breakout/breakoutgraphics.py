
"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # A switch to judge whether the ball has moved
        self.go = False
        # game success or fail front
        self.success = GLabel("Success", x=self.window.width/6, y=(self.window.height/2))
        self.success.font = "-100"
        self.success.color = "yellow"
        self.fail = GLabel("Fail", x=self.window.width/4, y=self.window.height/2)
        self.fail.font = "-100"
        self.fail.color = "red"
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=(self.window.height-paddle_offset))
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        self.total_brick = brick_cols * brick_rows
        onmouseclicked(self.click)
        onmousemoved(self.paddle_move)
        # Draw bricks
        for i in range(BRICK_COLS):
            for y in range(BRICK_ROWS):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                if i == 0:
                    self.brick.fill_color = "red"
                elif i < 2:
                    self.brick.fill_color = "red"
                elif i < 4:
                    self.brick.fill_color = "orange"
                elif i < 6:
                    self.brick.fill_color = "yellow"
                elif i < 8:
                    self.brick.fill_color = "green"
                elif i < 10:
                    self.brick.fill_color = "blue"
                self.window.add(self.brick, x=y * BRICK_SPACING + y * BRICK_WIDTH,
                                y=BRICK_OFFSET + i * BRICK_SPACING + i * BRICK_HEIGHT)

    def paddle_move(self, event):
        if event.x > self.window.width-PADDLE_WIDTH/2:
            self.paddle.x = self.window.width - PADDLE_WIDTH
        elif event.x < PADDLE_WIDTH/2:
            self.paddle.x = 0
        else:
            self.paddle.x = event.x - self.paddle.width / 2
        self.window.add(self.paddle)

    def click(self, event):
        if not self.go:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = random.randint(INITIAL_Y_SPEED, INITIAL_Y_SPEED)
            if random.random() > 0.5:
                self.__dx = - self.__dx
        self.go = True

    def get__dx(self):
        return self.__dx

    def get__dy(self):
        return self.__dy

