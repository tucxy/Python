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
        # Calculate edge label
        x, y = edge
        l_e = min(abs(x - y), 21 - abs(x - y))
        mid_x = (pos[edge[0]][0] + pos[edge[1]][0]) / 2
        mid_y = (pos[edge[0]][1] + pos[edge[1]][1]) / 2
        angle = math.atan2(pos[edge[1]][1] - pos[edge[0]][1], pos[edge[0]][0] - pos[edge[1]][0])
        angle_deg = math.degrees(angle)

        if angle_deg < -90 or angle_deg > 90:
            angle_deg += 180
            angle_deg %= 360

        font = pygame.font.SysFont('Arial', 18)
        sub_font = pygame.font.SysFont('Arial', 14)
        text = font.render(str(l_e), True, (0, 255, 0))  # GREEN
        sub_text = sub_font.render(str(l_e % 7), True, (255, 0, 0))  # RED
        text = pygame.transform.rotate(text, -angle_deg)
        sub_text = pygame.transform.rotate(sub_text, -angle_deg)
        text_rect = text.get_rect(center=(mid_x, mid_y))
        sub_text_rect = sub_text.get_rect(center=(mid_x, mid_y))
        screen.blit(text, text_rect.topleft)
        screen.blit(sub_text, (text_rect.right - 5, text_rect.bottom - 5))
    for node in G.nodes():
        pygame.draw.circle(screen, (0, 0, 255), (int(pos[node][0]), int(pos[node][1])), 10)  # BLUE
        # Draw custom node labels with subscript
        mod_21 = node % 21
        mod_7 = node % 7
        node_label = f"{mod_21}"
        sub_label = f"{mod_7}"
        text = font.render(node_label, True, (0, 0, 0))  # BLACK
        sub_text = sub_font.render(sub_label, True, (255, 0, 0))  # RED
        text_rect = text.get_rect()
        screen.blit(text, (pos[node][0] + 15, pos[node][1] - 10))  # Moved the label beside the node
        screen.blit(sub_text, (pos[node][0] + 15 + text_rect.width - 5, pos[node][1] - 10 + text_rect.height - 5))

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
        mod_21 = node % 21
        mod_7 = node % 7
        y = HEIGHT - y  # Reflect y-coordinate for LaTeX
        latex_code += f"\\node[fill=black, label=below:{{\\color{{black}}${mod_21}_{{\\textcolor{{red}}{mod_7}}}$}}] (N{node}) at ({x/100:.2f},{y/100:.2f}) {{}};\n"
    
    for edge in G.edges():
        x, y = edge
        l_e = min(abs(x - y), 21 - abs(x - y))
        latex_code += f"\\draw (N{x}) -- node[midway, sloped, above, draw=none, fill=none] {{\\textcolor{{green}}{{{l_e}}}$_{{\\textcolor{{red}}{{{l_e % 7}}}}}$}} (N{y});\n"
    
    latex_code += "\\end{tikzpicture}\n\\end{document}"
    
    with open(os.path.join(output_dir, f"{name}.tex"), "w") as f:
        f.write(latex_code)
    
    print(f"LaTeX code saved to {os.path.join(output_dir, f'{name}.tex')}")

# Function to visualize the graph using Pygame
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

