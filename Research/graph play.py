import pygame
import networkx as nx

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Draggable Graph")

# Fonts
FONT = pygame.font.SysFont('Arial', 18)
SUB_FONT = pygame.font.SysFont('Arial', 14)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create a NetworkX graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

# Initialize node positions
pos = nx.spring_layout(G)

# Scale positions to fit the screen
def scale_pos(pos, width, height):
    for node in pos:
        x, y = pos[node]
        pos[node] = ((x + 1) / 2 * width, (1 - (y + 1) / 2) * height)
    return pos

pos = scale_pos(pos, WIDTH, HEIGHT)

# Function to draw the graph with labels
def draw_graph(screen, G, pos):
    screen.fill(WHITE)
    for edge in G.edges():
        pygame.draw.line(screen, GRAY, pos[edge[0]], pos[edge[1]], 2)
        # Calculate edge label
        x, y = edge
        l_e = min(abs(x - y), 21 - abs(x - y))
        edge_label = f"{l_e}_{{{l_e % 7}}}"
        mid_x = (pos[edge[0]][0] + pos[edge[1]][0]) / 2
        mid_y = (pos[edge[0]][1] + pos[edge[1]][1]) / 2
        text = FONT.render(str(l_e), True, GREEN)
        sub_text = SUB_FONT.render(str(l_e % 7), True, RED)
        text_rect = text.get_rect()
        screen.blit(text, (mid_x, mid_y))
        screen.blit(sub_text, (mid_x + text_rect.width - 5, mid_y + text_rect.height - 5))
    for node in G.nodes():
        pygame.draw.circle(screen, BLUE, (int(pos[node][0]), int(pos[node][1])), 10)
        # Draw custom node labels with subscript
        mod_21 = node % 21
        mod_7 = node % 7
        node_label = f"{mod_21}"
        sub_label = f"{mod_7}"
        text = FONT.render(node_label, True, BLACK)
        sub_text = SUB_FONT.render(sub_label, True, RED)
        text_rect = text.get_rect()
        screen.blit(text, (pos[node][0] + 10, pos[node][1] - 10))
        screen.blit(sub_text, (pos[node][0] + 10 + text_rect.width - 5, pos[node][1] - 10 + text_rect.height - 5))
    pygame.display.flip()

# Main loop
running = True
selected_node = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
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