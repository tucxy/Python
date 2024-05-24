import pygame
import networkx as nx
import os
import math

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Function to scale positions to fit the screen
def scale_pos(pos, width, height):
    for node in pos:
        x, y = pos[node]
        pos[node] = ((x + 1) / 2 * width, (1 - (y + 1) / 2) * height)
    return pos

# Function to draw the graph with labels
def draw_graph(screen, G, pos):
    screen.fill((255, 255, 255))  # WHITE
    for edge in G.edges():
        pygame.draw.line(screen, (200, 200, 200), pos[edge[0]], pos[edge[1]], 2)  # GRAY
    for node in G.nodes():
        pygame.draw.circle(screen, (0, 0, 255), (int(pos[node][0]), int(pos[node][1])), 10)  # BLUE
        # Draw node labels
        node_label = str(node)
        font = pygame.font.SysFont('Arial', 18)
        text = font.render(node_label, True, (0, 0, 0))  # BLACK
        text_rect = text.get_rect()
        screen.blit(text, (pos[node][0] + 15, pos[node][1] - 10))  # Moved the label beside the node

    # Draw Save button
    pygame.draw.rect(screen, (0, 255, 0), (650, 50, 100, 50))
    save_text = font.render("Save", True, (0, 0, 0))  # BLACK
    screen.blit(save_text, (650 + 50 - save_text.get_width() // 2, 50 + 25 - save_text.get_height() // 2))

    pygame.display.flip()

# Function to generate LaTeX code
def generate_latex(pos, G, output_dir, name):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    latex_code = "\\documentclass{standalone}\n\\usepackage{tikz}\n\\begin{document}\n\\begin{tikzpicture}[every node/.style={draw, circle, fill=black, minimum size=4pt, inner sep=0pt}]\n"
    
    for node, (x, y) in pos.items():
        node_label = str(node)
        # Reflect y-coordinate for LaTeX
        y = HEIGHT - y
        latex_code += f"\\node[fill=black, label=below:{{\\color{{black}}${node_label}$}}] (N{node}) at ({x/100:.2f},{y/100:.2f}) {{}};\n"
    
    for edge in G.edges():
        x, y = edge
        latex_code += f"\\draw (N{x}) -- (N{y});\n"
    
    latex_code += "\\end{tikzpicture}\n\\end{document}"
    
    with open(os.path.join(output_dir, f"{name}.tex"), "w") as f:
        f.write(latex_code)
    
    print(f"LaTeX code saved to {os.path.join(output_dir, f'{name}.tex')}")

# Function to visualize the graph using Pygame and optionally save as LaTeX
def visualize(G, name):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Interactive Draggable Graph")

    pos = nx.spring_layout(G)
    pos = scale_pos(pos, WIDTH, HEIGHT)

    running = True
    selected_node = None
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 650 < mouse_x < 750 and 50 < mouse_y < 100:
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    output_dir = os.path.join(script_dir, name)
                    generate_latex(pos, G, output_dir, name)
                else:
                    for node in pos:
                        node_x, node_y = pos[node]
                        if (node_x - mouse_x) ** 2 + (node_y - mouse_y) ** 2 < 10 ** 2:
                            selected_node = node
                            break
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_node = None
            elif event.type == pygame.MOUSEMOTION and selected_node is not None:
                pos[selected_node] = event.pos

        draw_graph(screen, G, pos)

    pygame.quit()
