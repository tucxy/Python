import pygame
import networkx as nx
import os
import math

# Screen dimensions
DEFAULT_WIDTH, DEFAULT_HEIGHT = 1200, 800
LEFT_TAB_WIDTH = 200
RIGHT_TAB_WIDTH = 200
MARGIN = 10

# Function to scale positions to fit the screen
def scale_pos(pos, width, height):
    for node in pos:
        x, y = pos[node]
        pos[node] = ((x + 1) / 2 * (width - LEFT_TAB_WIDTH - RIGHT_TAB_WIDTH) + LEFT_TAB_WIDTH, (1 - (y + 1) / 2) * height)
    return pos

# Function to draw the graph with labels
def draw_graph(screen, G, pos, show_vertex_labels, show_vertex_sublabels, show_edge_labels, show_edge_sublabels):
    for edge in G.edges():
        pygame.draw.line(screen, (200, 200, 200), pos[edge[0]], pos[edge[1]], 2)  # GRAY
        # Calculate edge label
        x, y = edge
        l_e = "∞" if x == math.inf or y == math.inf else min(abs(x - y), 21 - abs(x - y))
        if x == math.inf:
            l_mod_7 = y
        elif y == math.inf:
            l_mod_7 = x
        else:
            l_mod_7 = (x + y) % 7

        mid_x = (pos[edge[0]][0] + pos[edge[1]][0]) / 2
        mid_y = (pos[edge[0]][1] + pos[edge[1]][1]) / 2
        angle = math.atan2(pos[edge[1]][1] - pos[edge[0]][1], pos[edge[0]][0] - pos[edge[1]][0])
        angle_deg = math.degrees(angle)

        if angle_deg < -90 or angle_deg > 90:
            angle_deg += 180
            angle_deg %= 360

        font = pygame.font.SysFont('Arial', 18)
        sub_font = pygame.font.SysFont('Arial', 14)

        if show_edge_labels:
            text = font.render(str(l_e), True, (0, 255, 0))  # GREEN
            text = pygame.transform.rotate(text, -angle_deg)
            text_rect = text.get_rect(center=(mid_x, mid_y))
            screen.blit(text, text_rect.topleft)

        if show_edge_sublabels:
            sub_text = sub_font.render(str(l_mod_7), True, (255, 0, 0))  # RED
            sub_text = pygame.transform.rotate(sub_text, -angle_deg)
            sub_text_rect = sub_text.get_rect(center=(mid_x, mid_y))
            if show_edge_labels:
                screen.blit(sub_text, (text_rect.right - 5, text_rect.bottom - 5))
            else:
                screen.blit(sub_text, sub_text_rect.topleft)

    for node in G.nodes():
        pygame.draw.circle(screen, (0, 0, 255), (int(pos[node][0]), int(pos[node][1])), 10)  # BLUE
        # Draw custom node labels with subscript
        node_label = "∞" if node == math.inf else str(node % 21)
        sub_label = "" if node == math.inf else str(node % 7)
        font = pygame.font.SysFont('Arial', 18)
        sub_font = pygame.font.SysFont('Arial', 14)

        if show_vertex_labels:
            text = font.render(node_label, True, (0, 0, 0))  # BLACK
            text_rect = text.get_rect()
            screen.blit(text, (pos[node][0] + 15, pos[node][1] - 10))  # Moved the label beside the node

        if show_vertex_sublabels and sub_label:
            sub_text = sub_font.render(sub_label, True, (255, 0, 0))  # RED
            if show_vertex_labels:
                screen.blit(sub_text, (pos[node][0] + 15 + text_rect.width - 5, pos[node][1] - 10 + text_rect.height - 5))
            else:
                screen.blit(sub_text, (pos[node][0] + 15, pos[node][1] - 10))

# Function to draw the boxes and charts for each graph
def draw_boxes_and_charts(screen, all_graph_data):
    edge_font = pygame.font.SysFont('Arial', 14)
    l_mod_7_font = pygame.font.SysFont('Arial', 14)
    chart_start_x, chart_start_y = MARGIN + 10, MARGIN + 140
    start_y = MARGIN

    for graph_data in all_graph_data:
        # Draw edge lengths grid
        pygame.draw.rect(screen, (0, 0, 0), (MARGIN, start_y, 120, 120), 2)  # Border for the edge length grid
        cell_width, cell_height = 40, 40
        start_x, box_start_y = MARGIN + 10, start_y + 10

        T = graph_data['T']
        grid = ["", "", "", "", "", "", "", "", ""]
        positions = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2), (1, 1)]

        for i, length in enumerate(T):
            if i < 6:
                row, col = positions[i]
                grid[row * 3 + col] = length
            elif i == 6:
                grid[7] = length

        for i in range(3):
            for j in range(3):
                text = edge_font.render(str(grid[i * 3 + j]), True, (0, 255, 0))  # GREEN
                screen.blit(text, (start_x + j * cell_width, box_start_y + i * cell_height))

        # Draw l_mod_7 chart
        headers = [8, 9, 10, '∞']
        chart_start_y = box_start_y + 130
        for i, header in enumerate(headers):
            text = l_mod_7_font.render(str(header), True, (0, 255, 0))  # GREEN
            screen.blit(text, (chart_start_x + i * cell_width, chart_start_y))
        # Draw continuous underline for headers
        line_start_x = MARGIN
        line_end_x = chart_start_x + cell_width * 4 - 10
        pygame.draw.line(screen, (0, 0, 0), (line_start_x, chart_start_y + 25), (line_end_x, chart_start_y + 25), 2)

        # Draw l_mod_7 values sorted below their respective headers
        l_mod_7_values = graph_data['l_mod_7_values']
        max_rows = max(len(l_mod_7_values[8]), len(l_mod_7_values[9]), len(l_mod_7_values[10]), len(l_mod_7_values['∞']))
        for i, header in enumerate(headers):
            values = sorted(l_mod_7_values[header])
            for j, value in enumerate(values):
                text = l_mod_7_font.render(str(value), True, (255, 0, 0))  # RED
                screen.blit(text, (chart_start_x + i * cell_width, chart_start_y + 30 + j * 20))

        start_y = chart_start_y + 30 + max_rows * 20 + 20

# Function to generate LaTeX code
def generate_latex(pos, G, output_dir, name, show_vertex_labels, show_vertex_sublabels, show_edge_labels, show_edge_sublabels):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    latex_code = "\\documentclass{standalone}\n\\usepackage{tikz}\n\\begin{document}\n\\begin{tikzpicture}[every node/.style={draw, circle, fill=black, minimum size=4pt, inner sep=0pt}]\n"
    
    for node, (x, y) in pos.items():
        node_label = "\infty" if node == math.inf else str(node % 21)
        sub_label = "" if node == math.inf else str(node % 7)
        y = DEFAULT_HEIGHT - y  # Reflect y-coordinate for LaTeX
        if show_vertex_labels and show_vertex_sublabels and sub_label:
            latex_code += f"\\node[fill=black, label=below:{{\\color{{black}}${node_label}_{{\\textcolor{{red}}{sub_label}}}$}}] (N{node}) at ({x/100:.2f},{y/100:.2f}) {{}};\n"
        elif show_vertex_labels:
            latex_code += f"\\node[fill=black, label=below:{{\\color{{black}}${node_label}$}}] (N{node}) at ({x/100:.2f},{y/100:.2f}) {{}};\n"
        elif show_vertex_sublabels and sub_label:
            latex_code += f"\\node[fill=black, label=below:{{\\color{{black}}$_{{\\textcolor{{red}}{sub_label}}}$}}] (N{node}) at ({x/100:.2f},{y/100:.2f}) {{}};\n"
        else:
            latex_code += f"\\node[fill=black] (N{node}) at ({x/100:.2f},{y/100:.2f}) {{}};\n"
    
    for edge in G.edges():
        x, y = edge
        l_e = "$\infty$" if x == math.inf or y == math.inf else min(abs(x - y), 21 - abs(x - y))
        if x == math.inf:
            l_mod_7 = y
        elif y == math.inf:
            l_mod_7 = x
        else:
            l_mod_7 = (x + y) % 7

        if show_edge_labels and show_edge_sublabels:
            latex_code += f"\\draw (N{x}) -- node[midway, sloped, above, draw=none, fill=none] {{\\textcolor{{green}}{{{l_e}}}$_{{\\textcolor{{red}}{{{l_mod_7}}}}}$}} (N{y});\n"
        elif show_edge_labels:
            latex_code += f"\\draw (N{x}) -- node[midway, sloped, above, draw=none, fill=none] {{\\textcolor{{green}}{{{l_e}}}}} (N{y});\n"
        elif show_edge_sublabels:
            latex_code += f"\\draw (N{x}) -- node[midway, sloped, above, draw=none, fill=none] {{$_{{\\textcolor{{red}}{{{l_mod_7}}}}}$}} (N{y});\n"
        else:
            latex_code += f"\\draw (N{x}) -- (N{y});\n"
    
    latex_code += "\\end{tikzpicture}\n\\end{document}"
    
    with open(os.path.join(output_dir, f"{name}.tex"), "w") as f:
        f.write(latex_code)
    
    print(f"LaTeX code saved to {os.path.join(output_dir, f'{name}.tex')}")

# Function to visualize multiple graphs using Pygame
def multivisualize(graphs, name):
    pygame.init()
    WIDTH, HEIGHT = DEFAULT_WIDTH, DEFAULT_HEIGHT
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Interactive Draggable Graphs")

    pos_list = [scale_pos(nx.spring_layout(G), WIDTH, HEIGHT) for G in graphs]
    left_tab_open = True
    right_tab_open = True

    show_vertex_labels = True
    show_vertex_sublabels = True
    show_edge_labels = True
    show_edge_sublabels = True

    all_graph_data = []
    for G, pos in zip(graphs, pos_list):
        edge_lengths = []
        l_mod_7_values = {8: [], 9: [], 10: [], '∞': []}

        for edge in G.edges():
            x, y = edge
            l_e = "∞" if x == math.inf or y == math.inf else min(abs(x - y), 21 - abs(x - y))
            if x == math.inf:
                l_mod_7 = y
            elif y == math.inf:
                l_mod_7 = x
            else:
                l_mod_7 = (x + y) % 7
            edge_lengths.append(l_e)
            if l_e in l_mod_7_values:
                l_mod_7_values[l_e].append(l_mod_7)

        T = ['8'] * len(l_mod_7_values[8]) + ['9'] * len(l_mod_7_values[9]) + ['10'] * len(l_mod_7_values[10]) + ['∞'] * len(l_mod_7_values['∞'])
        all_graph_data.append({'T': T, 'l_mod_7_values': l_mod_7_values})

    running = True
    selected_node = None
    selected_pos = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                pos_list = [scale_pos(nx.spring_layout(G), WIDTH, HEIGHT) for G in graphs]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if left_tab_open and LEFT_TAB_WIDTH - 20 < mouse_x < LEFT_TAB_WIDTH and HEIGHT // 2 - 20 < mouse_y < HEIGHT // 2 + 20:
                    left_tab_open = not left_tab_open
                elif not left_tab_open and 0 < mouse_x < 20 and HEIGHT // 2 - 20 < mouse_y < HEIGHT // 2 + 20:
                    left_tab_open = not left_tab_open
                elif right_tab_open and WIDTH - RIGHT_TAB_WIDTH < mouse_x < WIDTH - RIGHT_TAB_WIDTH + 20 and HEIGHT // 2 - 20 < mouse_y < HEIGHT // 2 + 20:
                    right_tab_open = not right_tab_open
                elif not right_tab_open and WIDTH - 20 < mouse_x < WIDTH and HEIGHT // 2 - 20 < mouse_y < HEIGHT // 2 + 20:
                    right_tab_open = not right_tab_open
                elif right_tab_open and WIDTH - RIGHT_TAB_WIDTH + MARGIN < mouse_x < WIDTH - RIGHT_TAB_WIDTH + MARGIN + 100 and 50 < mouse_y < 100:
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    output_dir = os.path.join(script_dir, name)
                    generate_latex(pos_list[0], graphs[0], output_dir, name, show_vertex_labels, show_vertex_sublabels, show_edge_labels, show_edge_sublabels)
                elif right_tab_open and WIDTH - RIGHT_TAB_WIDTH + MARGIN < mouse_x < WIDTH - RIGHT_TAB_WIDTH + MARGIN + 100:
                    if 120 < mouse_y < 170:
                        show_vertex_labels = not show_vertex_labels
                    elif 190 < mouse_y < 240:
                        show_vertex_sublabels = not show_vertex_sublabels
                    elif 260 < mouse_y < 310:
                        show_edge_labels = not show_edge_labels
                    elif 330 < mouse_y < 380:
                        show_edge_sublabels = not show_edge_sublabels
                else:
                    for pos in pos_list:
                        for node in pos:
                            node_x, node_y = pos[node]
                            if (node_x - mouse_x) ** 2 + (node_y - mouse_y) ** 2 < 10 ** 2:
                                selected_node = node
                                selected_pos = pos
                                break
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_node = None
            elif event.type == pygame.MOUSEMOTION and selected_node is not None:
                selected_pos[selected_node] = event.pos

        screen.fill((255, 255, 255))  # Clear the screen

        for G, pos in zip(graphs, pos_list):
            draw_graph(screen, G, pos, show_vertex_labels, show_vertex_sublabels, show_edge_labels, show_edge_sublabels)

        if left_tab_open:
            draw_boxes_and_charts(screen, all_graph_data)

        if right_tab_open:
            # Draw right tab with buttons
            pygame.draw.rect(screen, (200, 200, 200), (WIDTH - RIGHT_TAB_WIDTH, 0, RIGHT_TAB_WIDTH, HEIGHT))
            # Draw Save button
            pygame.draw.rect(screen, (0, 255, 0), (WIDTH - RIGHT_TAB_WIDTH + MARGIN, 50, 100, 50))
            save_text = pygame.font.SysFont('Arial', 20).render("Save", True, (0, 0, 0))  # BLACK
            screen.blit(save_text, (WIDTH - RIGHT_TAB_WIDTH + MARGIN + 50 - save_text.get_width() // 2, 75 - save_text.get_height() // 2))

            # Draw toggle buttons
            buttons = [
                {"label": "vertex labels", "state": show_vertex_labels, "pos": (WIDTH - RIGHT_TAB_WIDTH + MARGIN, 120)},
                {"label": "vertex subscript labels", "state": show_vertex_sublabels, "pos": (WIDTH - RIGHT_TAB_WIDTH + MARGIN, 190)},
                {"label": "edge labels", "state": show_edge_labels, "pos": (WIDTH - RIGHT_TAB_WIDTH + MARGIN, 260)},
                {"label": "edge subscript labels", "state": show_edge_sublabels, "pos": (WIDTH - RIGHT_TAB_WIDTH + MARGIN, 330)},
            ]

            for button in buttons:
                color = (0, 255, 0) if button["state"] else (255, 0, 0)
                text = f"{button['label']} {'on' if button['state'] else 'off'}"
                # Determine appropriate font size
                font_size = 20
                button_font = pygame.font.SysFont('Arial', font_size)
                button_text = button_font.render(text, True, (0, 0, 0))  # BLACK
                while button_text.get_width() > 100 and font_size > 10:  # Reduce font size if text is too wide
                    font_size -= 2
                    button_font = pygame.font.SysFont('Arial', font_size)
                    button_text = button_font.render(text, True, (0, 0, 0))
                pygame.draw.rect(screen, color, (*button["pos"], 100, 50))
                screen.blit(button_text, (button["pos"][0] + 50 - button_text.get_width() // 2, button["pos"][1] + 25 - button_text.get_height() // 2))

        # Draw tab toggle buttons
        tab_button_font = pygame.font.SysFont('Arial', 24)
        if left_tab_open:
            pygame.draw.rect(screen, (150, 150, 150), (LEFT_TAB_WIDTH - 20, HEIGHT // 2 - 20, 20, 40))
            tab_text = tab_button_font.render("<", True, (0, 0, 0))
            screen.blit(tab_text, (LEFT_TAB_WIDTH - 20 + 10 - tab_text.get_width() // 2, HEIGHT // 2 - 20 + 20 - tab_text.get_height() // 2))
        else:
            pygame.draw.rect(screen, (150, 150, 150), (0, HEIGHT // 2 - 20, 20, 40))
            tab_text = tab_button_font.render(">", True, (0, 0, 0))
            screen.blit(tab_text, (10 - tab_text.get_width() // 2, HEIGHT // 2 - 20 + 20 - tab_text.get_height() // 2))

        if right_tab_open:
            pygame.draw.rect(screen, (150, 150, 150), (WIDTH - RIGHT_TAB_WIDTH, HEIGHT // 2 - 20, 20, 40))
            tab_text = tab_button_font.render(">", True, (0, 0, 0))
            screen.blit(tab_text, (WIDTH - RIGHT_TAB_WIDTH + 10 - tab_text.get_width() // 2, HEIGHT // 2 - 20 + 20 - tab_text.get_height() // 2))
        else:
            pygame.draw.rect(screen, (150, 150, 150), (WIDTH - 20, HEIGHT // 2 - 20, 20, 40))
            tab_text = tab_button_font.render("<", True, (0, 0, 0))
            screen.blit(tab_text, (WIDTH - 10 - tab_text.get_width() // 2, HEIGHT // 2 - 20 + 20 - tab_text.get_height() // 2))

        pygame.display.flip()

    pygame.quit()