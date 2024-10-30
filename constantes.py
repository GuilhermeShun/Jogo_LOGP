import pygame, pymunk

#inicialização do pygame
pygame.init()

#Criação da tela no pygame
LARGURA_DA_TELA = 1000  
ALTURA_DA_TELA = 750
tela = pygame.display.set_mode((LARGURA_DA_TELA, ALTURA_DA_TELA))
print(pygame.Surface.get_flags(tela))
pygame.display.set_caption("obliquum")


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
nivel = "Fácil"
borda_do_botao = 1
arremessos_totais = 0
arremessos_de_3 = 0
arremessos_totais_convertidos = 0
arremessos_de_3_convertidos = 0
distancia_linha_de_3 = 200

#cores

cores_padrao = {"jogador": (255, 255, 255), "cesta": (255, 255, 255), "fonte": (255, 255, 255), "linhas": (255, 255, 255)}
tema_azul = {"chao": (46, 108, 133), "background": (27, 170, 204), "botao": (46, 108, 133), "botao_hover": (17, 77, 108), "vetor": (28, 67, 82), "trajetoria": (0, 0,)}
tema_verde = {"chao": (53, 106, 0), "background": (101, 181, 30), "botao": (53, 106, 0), "botao_hover": (30, 60, 0), "vetor": (38, 76, 0)}
tema_vermelho = {"chao": (136, 0, 21), "background": (250, 18, 25), "botao": (136, 0, 21), "botao_hover": (70, 0, 11), "vetor": (77, 1, 11)}
tema_menu = {"background": (0, 0, 0), "botao": (135, 68, 1), "botao_hover": (92, 47, 1), "em_volta_dos_botoes": (255, 151, 0)}
