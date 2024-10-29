import pygame, pymunk, random
from constantes import *

def exibir_texto(tela, texto, x, y, tamanho, cor, fonte_nome="comicsans"):
    fonte = pygame.font.SysFont(fonte_nome, tamanho)
    texto_surface = fonte.render(texto, True, cor)
    return texto_surface


class Cesta:
    
    #vide desenho ilustrando o significado das coordenadas, presente no documento
    def __init__(self, nivel, x1=LARGURA_DA_TELA-250, x2=LARGURA_DA_TELA-150, x3=LARGURA_DA_TELA-140, y1=ALTURA_DA_TELA-400, y2=ALTURA_DA_TELA-350, y3=ALTURA_DA_TELA-550, y4=ALTURA_DA_TELA-388):
    #Cesta(LARGURA_DA_TELA-250, LARGURA_DA_TELA-150, LARGURA_DA_TELA-140, 400, 475, 250, 412)
        self.P1 = [x1, y1]
        self.P2 = [x2, y1]
        self.P3 = [x1, y2]
        self.P4 = [x2, y2]
        self.P5 = [x3, y3]
        self.P6 = [x3, y1]
        self.P7 = [x3, y4]
        self.largura = x2 - x1
        self.altura = y2 - y1
        self.pontos = [self.P1, self.P2, self.P3, self.P4, self.P5, self.P6, self.P7]
        self.radius = 2
        self.cor = cores_padrao["cesta"]
        self.extremidades = {"aro_esquerdo": [self.P1, self.P1], "rede_esquerda": [self.P1, self.P3], "rede_direita": [self.P2, self.P4], "rede_baixo": [self.P3, self.P4], "ponte": [self.P2, self.P6], "tabela": [self.P5, self.P7]}
        
        self.extremidades_aro_esquerdo = [self.P1, self.P1]
        self.extremidades_rede_esquerda = [self.P1, self.P3]
        self.extremidades_rede_baixo = [self.P3, self.P4]
        self.extremidades_rede_direita = [self.P4, self.P2]
        self.extremidades_ponte = [self.P2, self.P6]
        self.extremidades_tabela = [self.P5, self.P7]
        
        self.aro_esquerdo_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.rede_esquerda_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.rede_direita_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.rede_baixo_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.ponte_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.tabela_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        
        self.rede_esquerda_body.position = self.extremidades["aro_esquerdo"][0]
        self.rede_esquerda_body.position = self.extremidades["rede_esquerda"][0]
        self.rede_direita_body.position = self.extremidades["rede_direita"][0]
        self.rede_baixo_body.position = self.extremidades["rede_baixo"][0]
        self.ponte_body.position = self.extremidades["ponte"][0]
        self.tabela_body.position = self.extremidades["tabela"][0]

        self.aro_esquerdo_shape = pymunk.Segment(self.aro_esquerdo_body, (0, 0), (0, 5), self.radius)
        self.rede_esquerda_shape = pymunk.Segment(self.rede_esquerda_body, (0, 0), (0, y2-y1), self.radius)
        self.rede_direita_shape = pymunk.Segment(self.rede_direita_body, (0, 0), (0, y2-y1), self.radius)
        self.rede_baixo_shape = pymunk.Segment(self.rede_baixo_body, (0, 0), (x2-x1, 0), self.radius)
        self.ponte_shape = pymunk.Segment(self.ponte_body, (0, 0), (x3-x2, 0), self.radius)
        self.tabela_shape = pymunk.Segment(self.tabela_body, (0, 0), (0, y4-y3), self.radius)

        self.aro_esquerdo_shape.elasticity = 0.8
        self.rede_esquerda_shape.elasticity = 0
        self.rede_baixo_shape.elasticity = 0
        self.rede_direita_shape.elasticity = 0     
        self.ponte_shape.elasticity = 0.8
        self.tabela_shape.elasticity = 0.5

        self.aro_esquerdo_shape.friction = 0
        self.rede_esquerda_shape.friction = 0
        self.rede_baixo_shape.friction = 0
        self.rede_direita_shape.friction = 0      
        self.ponte_shape.friction = 0      
        self.tabela_shape.friction = 0
        
        self.conjunto_bodies = [self.aro_esquerdo_body, self.rede_esquerda_body, self.rede_direita_body, self.rede_baixo_body, self.ponte_body, self.tabela_body]  
        self.conjunto_shapes = [self.aro_esquerdo_shape, self.rede_esquerda_shape, self.rede_direita_shape, self.rede_baixo_shape, self.ponte_shape, self.tabela_shape] 
        
        if not nivel == "Fácil":
            self.posicao_aleatoria()

        if nivel == "Difícil":
            for body in self.conjunto_bodies:
                body.velocity = (-50, 0)

        self.conjunto_segmentos = [self.extremidades_aro_esquerdo, self.extremidades_rede_esquerda, self.extremidades_rede_baixo, self.extremidades_rede_direita, self.extremidades_ponte, self.extremidades_tabela]
        for body in self.conjunto_bodies:
            space.add(body)

        for shape in self.conjunto_shapes:
            space.add(shape)
        for body in self.conjunto_bodies:
            body.velocity = (0, 0)

    def desenhar(self):
        #shape.a se refere ao ponto inicial e shape.b ao ponto final do shape
        for shape in self.conjunto_shapes:
            p1 = shape.a + shape.body.position
            p2 = shape.b + shape.body.position

            pygame.draw.line(tela, self.cor, p1, p2, self.radius)

    #função que altera aleatoriamente, em um determinado intervalo, a posição da cesta
    def posicao_aleatoria(self):
        variacao_vertical = random.randint(-150, 150)
        #Evita que o range da variação vertical seja definido a partir da posição atual da cesta, garantindo que ela esteja sempre no máximo 150 pixels acima ou abaixo da posição inicial
        self.aro_esquerdo_body.position = self.extremidades["aro_esquerdo"][0]
        self.rede_esquerda_body.position = self.extremidades["rede_esquerda"][0]
        self.rede_direita_body.position = self.extremidades["rede_direita"][0]
        self.rede_baixo_body.position = self.extremidades["rede_baixo"][0]
        self.ponte_body.position = self.extremidades["ponte"][0]
        self.tabela_body.position = self.extremidades["tabela"][0]

        for body in self.conjunto_bodies:
            body.position += (0, variacao_vertical)

    def sentido_do_movimento_horizontal(self):
        if self.aro_esquerdo_body.velocity.x == 0:
            return "Parado"
        elif self.aro_esquerdo_body.velocity.x > 0:
            return "Direita"
        elif self.aro_esquerdo_body.velocity.x < 0:
            return "Esquerda"
       
    def movimento_horizontal(self):
        if self.sentido_do_movimento_horizontal()=="Parado":
            for body in self.conjunto_bodies:
                body.velocity = (-50, 0)
        if self.sentido_do_movimento_horizontal()=="Esquerda" and self.aro_esquerdo_body.position.x <= self.extremidades["aro_esquerdo"][0][0]-100:
            for body in self.conjunto_bodies:
                body.velocity = (50, 0)
        if self.sentido_do_movimento_horizontal()=="Direita" and self.aro_esquerdo_body.position.x >= self.extremidades["aro_esquerdo"][0][0]+100:
            for body in self.conjunto_bodies:
                body.velocity = (-50, 0)

    def remover_do_pymunk(self):
        for body in self.conjunto_bodies:
            space.remove(body)
        
        for shape in self.conjunto_shapes:
            space.remove(shape)
                          
    

class Bola:
    def __init__(self):
        self.cor = cores_padrao["jogador"]
        self.radius = 10
        self.body = pymunk.Body()
        self.body.position = 400, (ALTURA_DA_TELA-100-self.radius)
        self.body.velocity = (0, 0)
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.density = 10
        self.shape.elasticity = 0.8
        self.shape.friction = 0
        self.lista = []
        space.add(self.body, self.shape)

    def desenhar(self):
        self.x = int(self.body.position.x)
        self.y = int(self.body.position.y)
        pygame.draw.circle(tela, self.cor, (self.x, self.y), self.radius)

    #aplicação de impulso na bola para o lançamento
    def lancamento(self, velocidade_horizontal, velocidade_vertical):
        self.posicao_horizontal_ao_lancar = self.body.position.x
        self.shape.friction = 0.5
        self.velocidade_horizontal = velocidade_horizontal
        self.velocidade_vertical = velocidade_vertical
        self.body.velocity = (self.velocidade_horizontal, self.velocidade_vertical)
        

    def respawn(self):
        self.body.position = 400, (ALTURA_DA_TELA-100-self.radius)
        self.body.velocity = (0, 0)
        self.shape.friction = 0
        self.body.angular_velocity = 0
        self.lista.clear()
    
    def desenhar_rastro(self, lista, nivel):
        self.lista = lista
        if nivel == "Fácil":
            for ponto in self.lista:
                if(100+3*self.lista.index(ponto))<=255:
                    pygame.draw.circle(tela, (50+3*self.lista.index(ponto), 50+3*self.lista.index(ponto), 100+3*self.lista.index(ponto)), ponto, int(self.radius/2.8))
                elif(50+3*self.lista.index(ponto))<=255:
                    pygame.draw.circle(tela, (50+3*self.lista.index(ponto), 50+3*self.lista.index(ponto), 255), ponto, int(self.radius/2.8))
                else:
                    pygame.draw.circle(tela, (255, 255, 255), ponto, int(self.radius/2.8))
        if nivel == "Médio":
            for ponto in self.lista:
                if(70+4*self.lista.index(ponto))<=255:
                    pygame.draw.circle(tela, (50+3*self.lista.index(ponto), 70+4*self.lista.index(ponto), 50+3*self.lista.index(ponto)), ponto, int(self.radius/2.8))
                elif(50+3*self.lista.index(ponto))<=255:
                    pygame.draw.circle(tela, (50+3*self.lista.index(ponto), 255, 50+3*self.lista.index(ponto)), ponto, int(self.radius/2.8))
                else:
                    pygame.draw.circle(tela, (255, 255, 255), ponto, int(self.radius/2.8))

        if nivel == "Difícil":
            for ponto in self.lista:
                if(80+3*self.lista.index(ponto))<=255:
                    pygame.draw.circle(tela, (80+3*self.lista.index(ponto), 0+3*self.lista.index(ponto), 0+3*self.lista.index(ponto)), ponto, int(self.radius/2.8))
                elif(0+3*self.lista.index(ponto))<=255:
                    pygame.draw.circle(tela, (255, 0+3*self.lista.index(ponto), 0+3*self.lista.index(ponto)), ponto, int(self.radius/2.8))
                else:
                    pygame.draw.circle(tela, (255, 255, 255), ponto, int(self.radius/2.8))

    def remover_do_pymunk(self):
        space.remove(self.shape, self.body)
                                          
    def tocando_o_chao(self):
        if self.body.position.y >= ALTURA_DA_TELA - 100.5 - self.radius:
            return True
        else:
            return False
                
class Chao:
    def __init__(self):
        self.shape = pymunk.Segment(space.static_body, (-30, ALTURA_DA_TELA-95), (LARGURA_DA_TELA+30, ALTURA_DA_TELA-95), 5)
        self.shape.elasticity = 0.7
        self.shape.friction = 0.5

        space.add(self.shape)

    def desenhar(self, cor):
        pygame.draw.rect(tela, cor, pygame.Rect(0, ALTURA_DA_TELA-100, LARGURA_DA_TELA, 100))
        pygame.draw.line(tela, cores_padrao["linhas"], (0, ALTURA_DA_TELA-100), (LARGURA_DA_TELA, ALTURA_DA_TELA-100))

    def remover_do_pymunk(self):
        space.remove(self.shape)

class Paredes:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
        self.shape = pymunk.Segment(space.static_body, self.inicio, self.fim, 1)
        self.shape.elasticity = 0.6
        self.shape.friction = 0.5
        self.cor = cores_padrao["linhas"]
        space.add(self.shape)

    def desenhar(self):
        pygame.draw.line(tela, self.cor, self.inicio, self.fim)

    def remover_do_pymunk(self):
        space.remove(self.shape)

class Botao:
    def __init__(self, cor, medidas, tela, posicao):
        self.cor = cor
        self.posicao_x = posicao["coordenada_horizontal"]
        self.posicao_y = posicao["coordenada_vertical"]
        self.largura = medidas["largura"]
        self.altura = medidas["altura"]
        self.limite_superior = self.posicao_y + self.altura
        self.limite_inferior = self.posicao_y
        self.limite_esquerdo = self.posicao_x
        self.limite_direito = self.posicao_x + self.largura
        self.surface = tela
        
    def desenhar(self):
        pygame.draw.rect(self.surface, self.cor, pygame.Rect(self.posicao_x, self.posicao_y, self.largura, self.altura))
        
    def mouse_sobre(self):
        (x_mouse, y_mouse) = pygame.mouse.get_pos()
        if self.limite_esquerdo <= x_mouse <= self.limite_direito and self.limite_inferior <= y_mouse <= self.limite_superior:
            pygame.draw.rect(tela, (255, 255, 255), pygame.Rect(self.posicao_x - borda_do_botao, self.posicao_y - borda_do_botao, self.largura+2*borda_do_botao, self.altura+2*borda_do_botao))
            return True
        else:
            return False


        
    def clicado(self, estado_do_mouse):
        (x_mouse, y_mouse) = pygame.mouse.get_pos()
        if estado_do_mouse and self.limite_esquerdo <= int(x_mouse) <= self.limite_direito and self.limite_inferior <= int(y_mouse) <= self.limite_superior: 
            pygame.time.delay(50)
            return True
        else:
            return False
        
def exibir_pontuacao(pontos):
    #Texto de pontuação
    mensagem = f'pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    tela.blit(texto_formatado, (25, ALTURA_DA_TELA - 50))

def exibir_tempo(tempo_em_milissegundos):
    #Texto de pontuação
    tempo_em_segundos = tempo_em_milissegundos*0.001 
    mensagem = f'tempo: {tempo_em_segundos:.3f} s'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    tela.blit(texto_formatado, (LARGURA_DA_TELA - 200, ALTURA_DA_TELA - 50))