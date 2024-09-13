import pygame
import random

# Initialize Pygame
pygame.init()

# Game Variables
screen_width = 400
screen_height = 600
bird_x = 50
bird_y = screen_height // 2
bird_width = 34
bird_height = 24
bird_speed = 0
gravity = 0.15
flap_strength = -5
pipe_width = 70
pipe_gap = 200
pipe_speed = 3
pipe_frequency = 1500  # milliseconds

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Load bird image
bird_img = pygame.Surface((bird_width, bird_height))
bird_img.fill((255, 255, 0))  # yellow bird

# Load pipe image
pipe_img = pygame.Surface((pipe_width, screen_height))
pipe_img.fill((0, 255, 0))  # green pipe

# Set the frame rate
clock = pygame.time.Clock()

# Define the font
font = pygame.font.SysFont(None, 50)

# Function to display the score
def display_score(score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Function to generate random pipes
def generate_pipes():
    pipe_height = random.randint(100, 400)
    bottom_pipe = pipe_img.get_rect(midtop=(screen_width + pipe_width, pipe_height + pipe_gap))
    top_pipe = pipe_img.get_rect(midbottom=(screen_width + pipe_width, pipe_height))
    return {"top": top_pipe, "bottom": bottom_pipe, "passed": False}

# Main game loop
def main():
    global bird_y, bird_speed
    score = 0
    running = True
    bird_rect = bird_img.get_rect(center=(bird_x, bird_y))
    
    # Pipe timer and list
    pipe_list = []
    pygame.time.set_timer(pygame.USEREVENT, pipe_frequency)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_speed = flap_strength

            if event.type == pygame.USEREVENT:
                pipe_list.append(generate_pipes())

        # Bird movement
        bird_speed += gravity
        bird_y += bird_speed
        bird_rect.centery = bird_y

        # Pipe movement
        for pipe_set in pipe_list:
            pipe_set["top"].x -= pipe_speed
            pipe_set["bottom"].x -= pipe_speed

        # Remove pipes that have moved off the screen
        pipe_list = [pipe_set for pipe_set in pipe_list if pipe_set["top"].right > 0]

        # Collision detection
        for pipe_set in pipe_list:
            if bird_rect.colliderect(pipe_set["top"]) or bird_rect.colliderect(pipe_set["bottom"]):
                running = False  # End the game if collision happens

        # Update score when the bird successfully passes a pipe
        for pipe_set in pipe_list:
            if pipe_set["top"].right < bird_x and not pipe_set["passed"]:
                score += 1
                pipe_set["passed"] = True  # Mark pipe as passed

        # Check if bird hits the top or bottom
        if bird_rect.top <= 0 or bird_rect.bottom >= screen_height:
            running = False

        # Fill screen with a background color
        screen.fill((135, 206, 235))  # sky blue

        # Draw bird
        screen.blit(bird_img, bird_rect)

        # Draw pipes
        for pipe_set in pipe_list:
            screen.blit(pipe_img, pipe_set["top"])
            screen.blit(pipe_img, pipe_set["bottom"])

        # Display score
        display_score(score)

        # Update the display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(60)

    # Game over message
    screen.fill((0, 0, 0))
    game_over_text = font.render(f"Game Over! Score: {score}", True, (255, 255, 255))
    screen.blit(game_over_text, (screen_width // 6, screen_height // 2))
    pygame.display.update()
    pygame.time.wait(2000)

# Run the game
if __name__ == "__main__":
    main()
    pygame.quit()
