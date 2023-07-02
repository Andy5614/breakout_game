"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    brick_number = 0  # clear brick number
    lives = NUM_LIVES
    while lives > 0:
        pause(FRAME_RATE)
        dx = graphics.get__dx()  # initial dx value
        dy = graphics.get__dy()  # initial dy value
        if graphics.go:
            while True:
                if brick_number >= graphics.total_brick:
                    break
                graphics.ball.move(dx, dy)
                is_break = False
                for i in range(0, graphics.ball.width+1, graphics.ball.width):
                    for j in range(0, graphics.ball.height+1, graphics.ball.height):
                        obj_x = graphics.ball.x + i
                        obj_y = graphics.ball.y + j
                        obj = graphics.window.get_object_at(obj_x, obj_y)
                        if obj is not None:
                            if obj is graphics.paddle:
                                if dy > 0:
                                    dy = -abs(dy)
                            else:
                                graphics.window.remove(obj)
                                brick_number += 1
                                dy = -dy
                            is_break = True
                            break
                    if is_break:
                        break
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    dx = -dx
                if graphics.ball.y <= 0:
                    dy = -dy
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    graphics.go = False
                    lives -= 1
                    break
                if brick_number == 100:
                    break
                pause(FRAME_RATE)
            graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                y=(graphics.window.height - graphics.ball.height) / 2)
        if brick_number >= graphics.total_brick:
            break
    if lives == 0:  # live = 0  is fail
        graphics.window.add(graphics.fail)
        graphics.window.remove(graphics.ball)
    if brick_number == 100:  # total brick number =100 is success
        graphics.window.add(graphics.success)
        graphics.window.remove(graphics.ball)


if __name__ == '__main__':
    main()
