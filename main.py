import pygame

pygame.init()
clock = pygame.time.Clock()

# Creating Window
screen = pygame.display.set_mode((1024, 720))
pygame.display.set_caption("PONG By CienKang")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 16)


def show_scores(player_score, opp_score):
    player_text = font.render("Player_Score : " + str(player_score), True, (255, 255, 255))
    screen.blit(player_text, (40, 40))
    player_text = font.render("Opponent_Score : " + str(opp_score), True, (255, 255, 255))
    screen.blit(player_text, (800, 40))


# Players and Ball
ball = pygame.Rect(512 - 15, 360 - 15, 30, 30)
player = pygame.Rect(10, 360 - 70, 10, 140)
player_score = 0
opp = pygame.Rect(1024 - 20, 360 - 70, 10, 140)
opp_score = 0

# Ball Mechanics
ball_speed_X = 6
ball_speed_Y = 6
player_speed = 0
opp_speed = 0


def bound_ball_X(balt):
    if ball.x > 1000:
        global player_score
        player_score += 1
    if ball.x < 0:
        global opp_score
        opp_score += 1
    return ball.x


def change(ball_speed_X):
    if ball.x > 1000:
        ball_speed_X = -ball_speed_X
    if ball.x < 0:
        ball_speed_X = -ball_speed_X
    return ball_speed_X


def bound_ball_Y(ball_speed_Y):
    if ball.y > 700 or ball.y < 1:
        ball_speed_Y = -ball_speed_Y
    return ball_speed_Y


# Players Animation
def player_move(player_speed):
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= 720:
        player.bottom = 720


def opp_move(opp_speed):
    opp.y += opp_speed
    if opp.top <= 0:
        opp.top = 0
    if opp.bottom >= 720:
        opp.bottom = 720


# Main Loop
run_game = True
while run_game:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                opp_speed -= 7
            if event.key == pygame.K_DOWN:
                opp_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                opp_speed += 7
            if event.key == pygame.K_DOWN:
                opp_speed -= 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_speed -= 7
            if event.key == pygame.K_d:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_speed += 7
            if event.key == pygame.K_d:
                player_speed -= 7
                player_speed += player_speed

    if event.type == pygame.QUIT:
        run_game = False

    # Drawing Ball and PLayers
    pygame.draw.rect(screen, (200, 200, 200), player)
    pygame.draw.rect(screen, (200, 200, 200), opp)
    pygame.draw.ellipse(screen, (200, 200, 200), ball)

    # Drawing Boundaries
    pygame.draw.line(screen, (200, 200, 200), (512, 0), (512, 720), 5)
    pygame.draw.line(screen, (255, 0, 0), (0, 0), (1024, 0), 10)
    pygame.draw.line(screen, (255, 0, 0), (0, 720), (1024, 720), 10)
    pygame.draw.line(screen, (0, 0, 255), (0, 0), (0, 720), 10)
    pygame.draw.line(screen, (0, 0, 255), (1022, 0), (1022, 720), 10)
    pygame.draw.circle(screen, (200, 200, 200), (512, 360), 60, 5)

    # Ball Speed and Directions
    ball.x = bound_ball_X(ball.x)
    ball_speed_X = change(ball_speed_X)
    ball_speed_Y = bound_ball_Y(ball_speed_Y)
    ball.x += ball_speed_X
    ball.y += ball_speed_Y
    if ball.colliderect(player) or ball.colliderect(opp):
        ball_speed_X = -ball_speed_X

    # player and Opponent
    player_move(player_speed)
    opp_move(opp_speed)
    show_scores(player_score, opp_score)
    clock.tick(60)
    pygame.display.update()
