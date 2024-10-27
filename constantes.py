import pygame, pymunk

#inicialização do pygame
pygame.init()

#Criação da tela no pygame
LARGURA_DA_TELA = 1200
ALTURA_DA_TELA = 700
tela = pygame.display.set_mode((LARGURA_DA_TELA, ALTURA_DA_TELA))
print(pygame.Surface.get_flags(tela))

COR_DE_FUNDO = (27, 170, 204)

clock = pygame.time.Clock()

fonte = pygame.font.SysFont('arial', 20, True, False)

#alta taxa de quadros por segundo para manter boa a simulação física
FPS = 200

#configurações do espaço físico do pymunk
space = pymunk.Space()
space.gravity = 0, 1000

mouse_clicado = False
cor_do_botao = (0, 0, 0)
lancamento = False