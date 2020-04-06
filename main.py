import utils
import math
import pygame

# initialize the pygame
pygame.init()

r1, r2 = 200, 200
m1, m2 = 25, 25
a1, a2 = math.pi / 2, math.pi / 2
a1_v, a2_v = 0, 0
a1_a, a2_a = 0.01, 0
px, py = 0, 0
g = 1

# Create the screen
WIDTH = 900     # x axis
HEIGHT = 900    # y axis
cx, cy = WIDTH / 2, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((0, 0, 0))

translate = utils.Translate(pygame.math.Vector2((cx, cy)))

# Title and icon
pygame.display.set_caption("Double Pendullum")

# Game loop
running = True
frame = 1
while running:
	pygame.time.delay(5)
	# Calculating acceleration of 1st pendulum
	num1 = -g * (2*m1 + m2) * math.sin(a1)
	num2 = -m2 * g * math.sin(a1 - 2*a2)
	num3 = -2 * math.sin(a1 - a2) * m2
	num4 = (a2_v * a2_v * r2) + (a1_v * a1_v * r1 * math.cos(a1 - a2))
	den = r1 * (2*m1 + m2 - (m2 * math.cos(2*a1 - 2*a2)))
	# Updating acceleration of 1st pendulum
	a1_a = (num1 + num2 + (num3 * num4)) / den

	# Calculating acceleration of 2nd pendulum
	num1 = 2 * math.sin(a1 - a2)
	num2 = a1_v * a1_v * r1 * (m1 + m2)
	num3 = g * (m1 + m2)* math.cos(a1)
	num4 = a2_v * a2_v * r2 * m2 * math.cos(a1 - a2)
	den = r2 * (2*m1 + m2 - (m2 * math.cos(2*a1 - 2*a2)))
	# Updating acceleration of 2nd pendulum
	a2_a = (num1*(num2 + num3 + num4)) / den

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill((0, 0, 0))	
	screen.blit(canvas, (0, 0))

	# 1st pendulum position calculation
	x1 = translate.applyx(r1 * math.sin(a1))
	y1 = translate.applyy(r1 * math.cos(a1))
	pygame.draw.line(screen, (255, 255, 255), (translate.applyx(0), translate.applyy(0)), (int(x1), int(y1)))
	pygame.draw.circle(screen, (255, 255, 255), (int(x1), int(y1)), m1)
	#pygame.draw.circle(canvas, (255, 255, 255), (int(x1), int(y1)), 1)

	# 2nd pendulum calculation
	x2 = x1 + r2 * math.sin(a2)
	y2 = y1 + r2 * math.cos(a2)
	pygame.draw.line(screen, (255, 255, 255), (int(x1), int(y1)), (int(x2), int(y2)))
	pygame.draw.circle(screen, (255, 255, 255), (int(x2), int(y2)), m2)
	#pygame.draw.circle(canvas, (255, 255, 255), (int(x2), int(y2)), 1)
	if frame > 1:
		pygame.draw.line(canvas, (255, 255, 255), (int(px), int(py)), (int(x2), int(y2)))

	a1_v += a1_a
	a2_v += a2_a
	a1 += a1_v
	a2 += a2_v

	px, py = x2, y2
	frame += 1

	pygame.display.update()