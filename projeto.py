import pygame, pymunk, math, random

#inicialização do pygame
pygame.init()

#Criação da tela no pygame
LARGURA_DA_TELA = 1200
ALTURA_DA_TELA = 800
tela = pygame.display.set_mode((LARGURA_DA_TELA, ALTURA_DA_TELA))

COR_DE_FUNDO = (255, 255, 255)

#alta taxa de quadros por segundo para manter boa a simulação física
FPS = 200

#configurações do espaço físico do pymunk
space = pymunk.Space()
space.gravity = 0, 1000

class Cesta:
    #vide desenho ilustrando o significado das coordenadas, presente no documento
    def __init__(self, x1, x2, x3, y1, y2, y3, y4):
        self.P1 = [x1, y1]
        self.P2 = [x2, y1]
        self.P3 = [x1, y2]
        self.P4 = [x2, y2]
        self.P5 = [x3, y3]
        self.P6 = [x3, y1]
        self.P7 = [x3, y4]
        self.pontos = [self.P1, self.P2, self.P3, self.P4, self.P5, self.P6, self.P7]
        self.radius = 2
        self.pos1 = [self.P1, self.P3]
        self.pos2 = [self.P3, self.P4]
        self.pos3 = [self.P4, self.P2]
        self.pos4 = [self.P2, self.P6]
        self.pos5 = [self.P5, self.P7]
        self.shape1 = pymunk.Segment(space.static_body, self.pos1[0], self.pos1[1], self.radius)
        self.shape2 = pymunk.Segment(space.static_body, self.pos2[0], self.pos2[1], self.radius)
        self.shape3 = pymunk.Segment(space.static_body, self.pos3[0], self.pos3[1], self.radius)
        self.shape4 = pymunk.Segment(space.static_body, self.pos4[0], self.pos4[1], self.radius)
        self.shape5 = pymunk.Segment(space.static_body, self.pos5[0], self.pos5[1], self.radius)
        self.shape1.elasticity = 0.6
        self.shape2.elasticity = 0.6
        self.shape3.elasticity = 0.6      
        self.shape4.elasticity = 0.6      
        self.shape5.elasticity = 0.6      
        self.conjunto = [self.pos1, self.pos2, self.pos3, self.pos4, self.pos5]
        space.add(self.shape1, self.shape2, self.shape3, self.shape4, self.shape5)

    def desenhar(self):
        for linha in self.conjunto:
            pygame.draw.line(tela, (0, 0, 0), linha[0], linha[1], self.radius)

    #função que altera aleatoriamente, em um determinado intervalo, a posição da cesta
    def posicao_aleatoria(self):
        space.remove(self.shape1, self.shape2, self.shape3, self.shape4, self.shape5)
        variacao_horizontal = random.randint(-300, 100)
        variacao_vertical  = random.randint(-150, 150)
        self.P1_aleatorio = [self.P1[0] + variacao_horizontal, self.P1[1] + variacao_vertical]
        self.P2_aleatorio = [self.P2[0] + variacao_horizontal, self.P2[1] + variacao_vertical]
        self.P3_aleatorio = [self.P3[0] + variacao_horizontal, self.P3[1] + variacao_vertical]
        self.P4_aleatorio = [self.P4[0] + variacao_horizontal, self.P4[1] + variacao_vertical]
        self.P5_aleatorio = [self.P5[0] + variacao_horizontal, self.P5[1] + variacao_vertical]
        self.P6_aleatorio = [self.P6[0] + variacao_horizontal, self.P6[1] + variacao_vertical]
        self.P7_aleatorio = [self.P7[0] + variacao_horizontal, self.P7[1] + variacao_vertical]
        self.pos1 = [self.P1_aleatorio, self.P3_aleatorio]
        self.pos2 = [self.P3_aleatorio, self.P4_aleatorio]
        self.pos3 = [self.P4_aleatorio, self.P2_aleatorio]
        self.pos4 = [self.P2_aleatorio, self.P6_aleatorio]
        self.pos5 = [self.P5_aleatorio, self.P7_aleatorio]
        self.shape1 = pymunk.Segment(space.static_body, self.pos1[0], self.pos1[1], self.radius)
        self.shape2 = pymunk.Segment(space.static_body, self.pos2[0], self.pos2[1], self.radius)
        self.shape3 = pymunk.Segment(space.static_body, self.pos3[0], self.pos3[1], self.radius)
        self.shape4 = pymunk.Segment(space.static_body, self.pos4[0], self.pos4[1], self.radius)
        self.shape5 = pymunk.Segment(space.static_body, self.pos5[0], self.pos5[1], self.radius)
        self.conjunto = [self.pos1, self.pos2, self.pos3, self.pos4, self.pos5]
        space.add(self.shape1, self.shape2, self.shape3, self.shape4, self.shape5)

class Bola:
    def __init__(self):
        self.radius = 10
        self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, self.radius))
        self.body.position = 100, (ALTURA_DA_TELA-100-self.radius)
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.density = 1
        self.shape.elasticity = 0.8
        self.shape.friction = 0.5
        space.add(self.body, self.shape)

    def desenhar(self):
        self.x = int(self.body.position.x)
        self.y = int(self.body.position.y)
        pygame.draw.circle(tela, (255, 0, 0), (self.x, self.y), self.radius)

    #aplicação de impulso na bola para o lançamento
    def lancamento(self, velocidade_horizontal, velocidade_vertical):
        self.shape.friction = 0.5
        self.velocidade_horizontal = velocidade_horizontal
        self.velocidade_vertical = velocidade_vertical
        self.body.velocity = (self.velocidade_horizontal, self.velocidade_vertical)
        return

    def respawn(self):
        self.body.position = 100, (ALTURA_DA_TELA-100-self.radius)
        self.body.velocity = 0, 0
        self.shape.friction = 0
        

class Chao:
    def __init__(self):
        self.shape = pymunk.Segment(space.static_body, (-30, ALTURA_DA_TELA-95), (LARGURA_DA_TELA+30, ALTURA_DA_TELA-95), 5)
        self.shape.elasticity = 0.6
        self.shape.friction = 0.5
        space.add(self.shape)

    def desenhar(self):
        pygame.draw.line(tela, (0, 0, 0), (0, ALTURA_DA_TELA-100), (LARGURA_DA_TELA, ALTURA_DA_TELA-100))

class Paredes:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        self.shape = pymunk.Segment(space.static_body, self.inicio, self.fim, 1)
        self.shape.elasticity = 0.6
        self.shape.friction = 0.5
        space.add(self.shape)

    def desenhar(self):
        pygame.draw.line(tela, (0, 0, 0), self.inicio, self.fim)
        
#Função main
def main(tela):
    lancamento = False
    angulo = 45
    velocidade = 0
    clock = pygame.time.Clock()
    cesta = Cesta(LARGURA_DA_TELA-250, LARGURA_DA_TELA-150, LARGURA_DA_TELA-140, 400, 425, 350, 412)
    bola = Bola()
    chao = Chao()
    parede_esquerda = Paredes((0, 0), (0, ALTURA_DA_TELA))
    parede_direita = Paredes((LARGURA_DA_TELA, 0), (LARGURA_DA_TELA, ALTURA_DA_TELA))
    pode_ajustar_o_angulo = True
    pode_ajustar_a_velocidade = True
    tempo_ao_ajustar = 0
    velocidade_horizontal = 0
    velocidade_vertical = 0
    velocidade_maxima = 2000
    velocidade_minima = 0

    while True:
        
        #relógio
        tempo = pygame.time.get_ticks()
        
        #verificador de teclas pressionadas
        key = pygame.key.get_pressed()

        #Event handler do pygame
        for event in pygame.event.get():
            #Botão de fechar a janela
            if event.type == pygame.QUIT:
                return

        #definição dos componentes da velocidade, que serão passados em bola.lancamento()
        velocidade_horizontal = velocidade*math.cos(math.radians(-angulo))
        velocidade_vertical = velocidade*math.sin(math.radians(-angulo))

        #realização do lançamento
        if key[pygame.K_SPACE] == True and lancamento == False:
            bola.lancamento(velocidade_horizontal, velocidade_vertical)
            lancamento = True
        
        #procedimentos enquanto a bola está no chão
        if lancamento == False:

            #controle de ângulo
            if key[pygame.K_UP] and not key[pygame.K_LSHIFT] and not key[pygame.K_LCTRL] and pode_ajustar_o_angulo == True:
                tempo_ao_ajustar = pygame.time.get_ticks()
                angulo = min(90, angulo + 1)  # Limita o ângulo máximo
                print("Ângulo", angulo)
            elif key[pygame.K_DOWN] and not key[pygame.K_LSHIFT] and not key[pygame.K_LCTRL] and pode_ajustar_o_angulo == True:
                tempo_ao_ajustar = pygame.time.get_ticks()
                angulo = max(0, angulo - 1)  # Limita o ângulo mínimo
                print("Ângulo", angulo)

            if key[pygame.K_UP] and key[pygame.K_LCTRL] and not key[pygame.K_LSHIFT] and pode_ajustar_o_angulo == True:
                tempo_ao_ajustar = pygame.time.get_ticks()
                angulo = min(90, angulo + 10)  # Limita o ângulo máximo
                print("Ângulo", angulo)

            elif key[pygame.K_DOWN] and key[pygame.K_LCTRL] and not key[pygame.K_LSHIFT] and pode_ajustar_o_angulo == True:
                tempo_ao_ajustar = pygame.time.get_ticks()
                angulo = max(0, angulo - 10)  # Limita o ângulo máximo
                print("Ângulo", angulo)
            
            #controle de tempo para regular o aumento do ângulo
            if tempo-tempo_ao_ajustar <= 100:
                pode_ajustar_o_angulo = False
            else:
                pode_ajustar_o_angulo = True

            #controle da velocidade do lançamento
            if key[pygame.K_UP] and key[pygame.K_LSHIFT] and not key[pygame.K_LCTRL] and pode_ajustar_a_velocidade == True:
                tempo_ao_ajustar = pygame.time.get_ticks()
                velocidade = min(velocidade_maxima, velocidade + 10)
                print("Velocidade:", velocidade)

            elif key[pygame.K_DOWN] and key[pygame.K_LSHIFT] and not key[pygame.K_LCTRL] and pode_ajustar_a_velocidade == True:
                tempo_ao_ajustar = pygame.time.get_ticks()
                velocidade = max(velocidade_minima, velocidade - 10)
                print("Velocidade:", velocidade)

            if key[pygame.K_UP] and key[pygame.K_LCTRL] and key[pygame.K_LSHIFT] and pode_ajustar_a_velocidade == True:
                tempo_ao_ajustar = pygame.time.get_ticks()
                velocidade = min(velocidade_maxima, velocidade + 100)
                print("Velocidade:", velocidade)

            elif key[pygame.K_DOWN] and key[pygame.K_LCTRL] and key[pygame.K_LSHIFT] and pode_ajustar_a_velocidade == True:
                tempo_ao_ajustar = pygame.time.get_ticks()
                velocidade = max(velocidade_minima, velocidade - 100)
                print("Velocidade:", velocidade)
                            
            #controle de tempo para regular o aumento da velocidade
            if tempo - tempo_ao_ajustar <=50:
                pode_ajustar_a_velocidade = False
            else: 
                pode_ajustar_a_velocidade = True

            #movimento para a esquerda
            if key[pygame.K_LEFT] == True and lancamento == False:
                bola.body.velocity = (-150, 0)

            #movimento para a direita
            elif key[pygame.K_RIGHT] == True and lancamento == False:
                bola.body.velocity = (150, 0)

            #a bola para
            else:
                bola.body.velocity = (0, 0)
        
        #se a bola estiver no chão, e com velocidade vertical 0, então o lançamento acabou
        elif lancamento == True and bola.body.velocity.y == 0 and bola.body.position.y>=ALTURA_DA_TELA-100-bola.radius:
            lancamento = False
        
        #se a bola sair da tela ou o jogador solicitar, é feito um respawn dela e a função cesta.posicao_aleatoria() é chamada, modificando sua posição aleatoriamente
        if bola.body.position.x > LARGURA_DA_TELA+50 or bola.body.position.x < -50 or (key[pygame.K_q] and tempo-tempo_ao_ajustar>=1000):
            tempo_ao_ajustar = pygame.time.get_ticks()
            bola.respawn()
            cesta.posicao_aleatoria()

        #Preenchimento da tela com a cor de fundo, para que a cada frame haja uma atualização do que é exibido
        tela.fill(COR_DE_FUNDO)

        #Exibição na tela dos elementos
        cesta.desenhar()
        bola.desenhar()
        chao.desenhar()
        parede_direita.desenhar()
        parede_esquerda.desenhar()

        #Se o lançamento não estiver acontecendo, o vetor que representa a velocidade de lançamento e o ângulo é desenhado
        if not lancamento:
            pygame.draw.line(tela, (0, 0, 200), (int(bola.body.position.x), int(bola.body.position.y)), (int(bola.body.position.x)+int(0.1*velocidade_horizontal), int(bola.body.position.y)+int(0.1*velocidade_vertical)), 4)
    
        #Taxa de FPS limitada 
        clock.tick(FPS)

        #Tempo para a atualização de física do pymunk ser atualizada
        space.step(1/FPS)

        pygame.display.update()


main(tela)

pygame.quit()