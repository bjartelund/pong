import pygame

# Initialize pygame
pygame.init()

# Set screen size and caption
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)

# Load font
font = pygame.font.Font(None, 30)

# Set initial scores
player1_score = 0
player2_score = 0

# Set initial positions for paddles and ball
paddle1_x = 30
paddle1_y = 225
paddle2_x = 650
paddle2_y = 225
ball_x = 350
ball_y = 250

# Set initial speeds for paddles and ball
paddle1_speed = 0
paddle2_speed = 0
ball_speed_x = 1
ball_speed_y = 1

# Set paddle and ball dimensions
paddle_width = 20
paddle_height = 75
ball_radius = 20

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_speed = -1
    elif keys[pygame.K_s]:
        paddle1_speed = 1
    else:
        paddle1_speed = 0
    if keys[pygame.K_UP]:
        paddle2_speed = -1
    elif keys[pygame.K_DOWN]:
        paddle2_speed = 1
    else:
        paddle2_speed = 0
    
    # Update paddle positions
    paddle1_y += paddle1_speed
    paddle2_y += paddle2_speed
    
    # Keep paddles on screen
    if paddle1_y < 0:
        paddle1_y = 0
    elif paddle1_y > size[1] - paddle_height:
        paddle1_y = size[1] - paddle_height
    if paddle2_y < 0:
        paddle2_y = 0
    elif paddle2_y > size[1] - paddle_height:
        paddle2_y = size[1] - paddle_height
    
    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Check for ball collision with paddles
    if ball_x - ball_radius < paddle1_x + paddle_width and ball_y > paddle1_y and ball_y < paddle1_y + paddle_height:
        ball_speed_x = -ball_speed_x
    elif ball_x + ball_radius > paddle2_x and ball_y > paddle2_y and ball_y < paddle2_y + paddle_height:
        ball_speed_x = -ball_speed_x
    
    # Check for ball collision with top and bottom of screen
    if ball_y - ball_radius < 0 or ball_y + ball_radius > size[1]:
        ball_speed_y = -ball_speed_y
    elif ball_y+ball_radius > paddle2_x and ball_x > paddle2_x and ball_x < paddle2_x + paddle_height:
        ball_speed_y = -ball_speed_y
# Check for ball passing left or right of screen
    if ball_x < 0:
        player2_score += 1
        ball_x = 350
        ball_y = 250
    elif ball_x > size[0]:
        player1_score += 1
        ball_x = 350
        ball_y = 250

    # Clear screen
    screen.fill(black)

    # Draw paddles and ball
    pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (int(ball_x), int(ball_y)), ball_radius)

    # Display scores
    player1_text = font.render("Player 1: " + str(player1_score), True, white)
    player2_text = font.render("Player 2: " + str(player2_score), True, white)
    screen.blit(player1_text, (50, 50))
    screen.blit(player2_text, (500, 50))

    # Update screen
    pygame.display.flip()
    pygame.time.wait(10)
