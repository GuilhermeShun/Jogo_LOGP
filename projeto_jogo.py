import pygame
from math import radians 
from constantes_e_globais import *
from funcoes_e_classes import *

'''
Significados dos códigos de retorno:
0: fechar o jogo
1: voltar para a tela inicial
2: reiniciar o jogo
'''

def tela_inicial(tela):
    global mouse_clicado, space, lancamento, nivel

    texto_botao_iniciar = exibir_texto(tela, "Iniciar", 0,0, 30, (255, 255, 255))
    texto_botao_opcoes = exibir_texto(tela, "Controles", 0, 0, 30, (255, 255, 255))
    texto_botao_sair = exibir_texto(tela, "Sair", 0, 0, 30, (255, 255, 255))       
    texto_botao_sobre_as_fases_e_objetivo = exibir_texto(tela, "Níveis", 0, 0, 30, (255, 255, 255))   

    botao_iniciar = Botao(tema_menu["botao"], {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA / 2 - 100, "coordenada_vertical": ALTURA_DA_TELA / 2 - 150})
    botao_opcoes = Botao(tema_menu["botao"], {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA / 2 - 100, "coordenada_vertical": ALTURA_DA_TELA / 2 - 75})
    botao_sobre_as_fases_e_objetivo = Botao(tema_menu["botao"], {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA / 2 - 100, "coordenada_vertical": ALTURA_DA_TELA / 2})
    botao_sair = Botao(tema_menu["botao"], {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA / 2 - 100, "coordenada_vertical": ALTURA_DA_TELA / 2 + 75})
    botoes_menu = [botao_iniciar, botao_opcoes, botao_sair, botao_sobre_as_fases_e_objetivo]
    COR_DE_FUNDO = tema_menu["background"]
    RETANGULO_DOS_BOTOES = pygame.Rect(LARGURA_DA_TELA/2 - 180, ALTURA_DA_TELA/2 - 190, 360, 360)
   
    botao_nivel_facil = Botao(cor_do_botao, {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA/2 - 350, "coordenada_vertical": ALTURA_DA_TELA-125})
    botao_nivel_medio = Botao(cor_do_botao, {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA/2 - 100, "coordenada_vertical": ALTURA_DA_TELA-125})
    botao_nivel_dificil = Botao(cor_do_botao, {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA/2 + 150, "coordenada_vertical": ALTURA_DA_TELA-125})

    texto_botao_nivel_facil = exibir_texto(tela, "Fácil", 0,0, 30, (255, 255, 255))
    texto_botao_nivel_medio = exibir_texto(tela, "Médio", 0,0, 30, (255, 255, 255))
    texto_botao_nivel_dificil = exibir_texto(tela, "Difícil", 0,0, 30, (255, 255, 255))

    botoes_dificuldade = [botao_nivel_facil, botao_nivel_medio, botao_nivel_dificil]

    nome_do_jogo = pygame.image.load('Nome.png')

    while True:
        
        tela.fill(COR_DE_FUNDO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_clicado = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_clicado = False    
        

        
        if botao_iniciar.clicado(mouse_clicado):
            mouse_clicado = False
            for shape in space.shapes:
                space.remove(shape)
            for body in space.bodies:
                space.remove(body)

            while True:
                # Chama a função do jogo
                resultado_jogo = jogo(tela)

                if resultado_jogo == 0:
                    return  # Fechar o jogo
                elif resultado_jogo == 1:
                    break  # Voltar para a tela inicial
                elif resultado_jogo == 2:
                    continue  # Reiniciar o jogo


        if botao_sair.clicado(mouse_clicado):
            mouse_clicado = False
            return
        if botao_opcoes.clicado(mouse_clicado):
            mouse_clicado = False
            if controles(tela) == False:
                return
        if botao_sobre_as_fases_e_objetivo.clicado(mouse_clicado):
            mouse_clicado = False
            if niveis(tela) == False:
                return

        tela.fill(tema_menu["background"])
        tela.blit(nome_do_jogo, (-10, 10))

        pygame.draw.rect(tela, tema_menu["em_volta_dos_botoes"], RETANGULO_DOS_BOTOES)
        
        for botao in botoes_menu:
            if botao.mouse_sobre():
                botao.cor = tema_menu["botao_hover"]
            else:
                botao.cor = tema_menu["botao"]

        for botao in botoes_dificuldade:
            if botao.mouse_sobre():
                botao.cor = (25, 25, 25)
            else:
                botao.cor = (0, 0, 0)   

        botao_iniciar.desenhar()
        botao_sobre_as_fases_e_objetivo.desenhar()
        botao_opcoes.desenhar()
        botao_sair.desenhar()

        tela.blit(texto_botao_iniciar, texto_botao_iniciar.get_rect(center=(botao_iniciar.posicao_x + botao_iniciar.largura / 2, botao_iniciar.posicao_y + botao_iniciar.altura / 2)))
        tela.blit(texto_botao_sobre_as_fases_e_objetivo, texto_botao_sobre_as_fases_e_objetivo.get_rect(center=(botao_sobre_as_fases_e_objetivo.posicao_x + botao_sobre_as_fases_e_objetivo.largura / 2, botao_sobre_as_fases_e_objetivo.posicao_y + botao_sobre_as_fases_e_objetivo.altura / 2)))
        tela.blit(texto_botao_opcoes, texto_botao_opcoes.get_rect(center=(botao_opcoes.posicao_x + botao_opcoes.largura / 2, botao_opcoes.posicao_y + botao_opcoes.altura / 2)))
        tela.blit(texto_botao_sair, texto_botao_sair.get_rect(center=(botao_sair.posicao_x + botao_sair.largura / 2, botao_sair.posicao_y + botao_sair.altura / 2)))

        if botao_nivel_facil.clicado(mouse_clicado):
            mouse_clicado = False
            nivel = "Fácil"
        if botao_nivel_medio.clicado(mouse_clicado):
            mouse_clicado = False
            nivel = "Médio"
        if botao_nivel_dificil.clicado(mouse_clicado):
            mouse_clicado = False
            nivel = "Difícil"
    
        if nivel == "Fácil":
            pygame.draw.rect(tela, (255, 255, 255), pygame.Rect(botao_nivel_facil.posicao_x - borda_do_botao, botao_nivel_facil.posicao_y - borda_do_botao, botao_nivel_facil.largura+2*borda_do_botao, botao_nivel_facil.altura+2*borda_do_botao))

        if nivel == "Médio":
            pygame.draw.rect(tela, (255, 255, 255), pygame.Rect(botao_nivel_medio.posicao_x - borda_do_botao, botao_nivel_medio.posicao_y - borda_do_botao, botao_nivel_medio.largura+2*borda_do_botao, botao_nivel_medio.altura+2*borda_do_botao))

        if nivel == "Difícil":
            pygame.draw.rect(tela, (255, 255, 255), pygame.Rect(botao_nivel_dificil.posicao_x - borda_do_botao, botao_nivel_dificil.posicao_y - borda_do_botao, botao_nivel_dificil.largura+2*borda_do_botao, botao_nivel_dificil.altura+2*borda_do_botao))
        

        botao_nivel_facil.desenhar()
        botao_nivel_dificil.desenhar()
        botao_nivel_medio.desenhar()

        tela.blit(texto_botao_nivel_facil, texto_botao_nivel_facil.get_rect(center=(botao_nivel_facil.posicao_x + botao_nivel_facil.largura / 2, botao_nivel_facil.posicao_y + botao_nivel_facil.altura / 2)))
        tela.blit(texto_botao_nivel_medio, texto_botao_nivel_medio.get_rect(center=(botao_nivel_medio.posicao_x + botao_nivel_medio.largura / 2, botao_nivel_medio.posicao_y + botao_nivel_medio.altura / 2)))
        tela.blit(texto_botao_nivel_dificil, texto_botao_nivel_dificil.get_rect(center=(botao_nivel_dificil.posicao_x + botao_nivel_dificil.largura / 2, botao_nivel_dificil.posicao_y + botao_nivel_dificil.altura / 2)))

        clock.tick(FPS)

        pygame.display.update()

def controles(tela):
    global mouse_clicado, lancamento, nivel
    botao_retornar = Botao(cor_do_botao, {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": 30, "coordenada_vertical": 20})

    texto_botao_retornar = exibir_texto(tela, "Retornar", 0,0, 30, (255, 255, 255))
    botoes = [botao_retornar]

    #Imagem de tutorial
    tutorial = pygame.image.load('Tutorial.png')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:                    
                    mouse_clicado = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:                    
                    mouse_clicado = False   
        
        tela.blit(tutorial, (0, 0))
        
        if botao_retornar.clicado(mouse_clicado):
            mouse_clicado = False
            return True
        

        for botao in botoes:
            if botao.mouse_sobre():
                botao.cor = (25, 25, 25)
            else:
                botao.cor = (0, 0, 0)   

        botao_retornar.desenhar()
 

        tela.blit(texto_botao_retornar, texto_botao_retornar.get_rect(center=(botao_retornar.posicao_x + botao_retornar.largura / 2, botao_retornar.posicao_y + botao_retornar.altura / 2)))

        clock.tick(FPS)

        pygame.display.update()

def niveis(tela):
    global mouse_clicado, lancamento, nivel
    botao_retornar = Botao(cor_do_botao, {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": 30, "coordenada_vertical": 20})

    texto_botao_retornar = exibir_texto(tela, "Retornar", 0,0, 30, (255, 255, 255))
    botoes = [botao_retornar]

    #Imagem dos níveis de dificuldade e do objetivo do jogo
    niveis = pygame.image.load('Niveis.png')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:                    
                    mouse_clicado = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:                    
                    mouse_clicado = False   
        
        tela.blit(niveis, (-12, 0))
        
        if botao_retornar.clicado(mouse_clicado):
            mouse_clicado = False
            return True
        

        for botao in botoes:
            if botao.mouse_sobre():
                botao.cor = (25, 25, 25)
            else:
                botao.cor = (0, 0, 0)   

        botao_retornar.desenhar()
 

        tela.blit(texto_botao_retornar, texto_botao_retornar.get_rect(center=(botao_retornar.posicao_x + botao_retornar.largura / 2, botao_retornar.posicao_y + botao_retornar.altura / 2)))

        clock.tick(FPS)

        pygame.display.update()

def pausa(tela, tempo_restante, pontos):
    global mouse_clicado
    botao_retornar = Botao(tema_menu["botao"], {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA / 2 - 100, "coordenada_vertical": ALTURA_DA_TELA / 2 - 35})
    botao_tela_inicial = Botao(tema_menu["botao"], {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA / 2 - 100, "coordenada_vertical": ALTURA_DA_TELA / 2 + 35})

    texto_botao_retornar = exibir_texto(tela, "Retomar", 0,0, 30, (255, 255, 255))
    texto_botao_tela_inicial = exibir_texto(tela, "Tela inicial", 0,0, 30, (255, 255, 255))
    RETANGULO_DOS_BOTOES = pygame.Rect(LARGURA_DA_TELA/2 - 200, ALTURA_DA_TELA/2 - 75, 400, 200)

    botoes = [botao_retornar, botao_tela_inicial]
    tempo_inicial = pygame.time.get_ticks()
    while True:
        tempo = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:                    
                    mouse_clicado = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:                    
                    mouse_clicado = False   
        
 
        
        tela.fill(tema_menu["background"])
        tempo_decorrido_na_pausa = tempo - tempo_inicial
        
        if botao_retornar.clicado(mouse_clicado):
            mouse_clicado = False
            return tempo_decorrido_na_pausa
        
        if botao_tela_inicial.clicado(mouse_clicado):
            mouse_clicado = False
            return 1
        
        for botao in botoes:
            if botao.mouse_sobre():
                botao.cor = tema_menu["botao_hover"]
            else:
                botao.cor = tema_menu["botao"]

        pygame.draw.rect(tela, tema_menu["em_volta_dos_botoes"], RETANGULO_DOS_BOTOES)
        botao_retornar.desenhar()
        botao_tela_inicial.desenhar()

        tela.blit(texto_botao_retornar, texto_botao_retornar.get_rect(center=(botao_retornar.posicao_x + botao_retornar.largura / 2, botao_retornar.posicao_y + botao_retornar.altura / 2)))
        tela.blit(texto_botao_tela_inicial, texto_botao_tela_inicial.get_rect(center=(botao_tela_inicial.posicao_x + botao_tela_inicial.largura / 2, botao_tela_inicial.posicao_y + botao_tela_inicial.altura / 2)))
        exibir_pontuacao(pontos)
        exibir_tempo(tempo_restante)
        clock.tick(FPS)

        pygame.display.update()

#Função jogo
def jogo(tela):

    global mouse_clicado, tempo_de_pausa, arremessos_de_3, arremessos_de_3_convertidos, arremessos_totais, arremessos_totais_convertidos, pontuacao, distancia_linha_de_3
    botao_retornar = Botao((3, 13, 67), {"largura": 120, "altura": 40}, tela, {"coordenada_horizontal": 25, "coordenada_vertical": 25})
    botao_reiniciar = Botao((3, 13, 67), {"largura": 120, "altura": 40}, tela, {"coordenada_horizontal": 305, "coordenada_vertical": 25})
    texto_botao_reiniciar = exibir_texto(tela, "Reiniciar", 0,0, 22, (255, 255, 255))
    texto_botao_retornar = exibir_texto(tela, "Retornar", 0,0, 22, (255, 255, 255))
    botao_pausar = Botao((3, 13, 67), {"largura": 120, "altura": 40}, tela, {"coordenada_horizontal": 165, "coordenada_vertical": 25})
    texto_botao_pausar = exibir_texto(tela, "Pausar", 0,0, 22, (255, 255, 255))
    botoes = [botao_retornar, botao_pausar, botao_reiniciar]
    lancamento = False
    cesta = Cesta(nivel)
    bola = Bola()
    chao = Chao()
    parede_esquerda = Paredes((0, -ALTURA_DA_TELA), (0, ALTURA_DA_TELA))
    parede_direita = Paredes((LARGURA_DA_TELA, -ALTURA_DA_TELA), (LARGURA_DA_TELA, ALTURA_DA_TELA))
    velocidade_horizontal = 0
    velocidade_vertical = 0
    velocidade_maxima = 1500
    velocidade_minima = 10
    pontos_trajetoria = []
    contador = 0
    pode_fazer_ponto = True
    acertou = False
    pontuacao = 0
    largura_linha_de_3 = 6
    tempo_ao_iniciar = pygame.time.get_ticks()
    tempo_limite = 60000 #tempo em milissegundos
    tempo_de_pausa = 0
    tempo_total_pausado = 0
    tempo_faltando = tempo_limite
    arremessos_totais = 0
    arremessos_de_3 = 0
    arremessos_totais_convertidos = 0
    arremessos_de_3_convertidos = 0
    quiques = 0
    verificador_de_quiques = pygame.Rect(0, ALTURA_DA_TELA - 100 - 20, LARGURA_DA_TELA, 15)
    quique_contabilizado = True
    tempo_ao_acertar = pygame.time.get_ticks()
    tempo_ao_lancar = tempo_limite + 1000
    if nivel == "Fácil":
        COR_DE_FUNDO = tema_azul["background"]
        COR_DO_CHAO = tema_azul["chao"]
        COR_DO_VETOR = tema_azul["vetor"]
        COR_DO_BOTAO = tema_azul["botao"]
        COR_DO_BOTAO_HOVER = tema_azul["botao_hover"]

    elif nivel == "Médio":
        COR_DE_FUNDO = tema_verde["background"]
        COR_DO_CHAO = tema_verde["chao"]
        COR_DO_VETOR = tema_verde["vetor"]
        COR_DO_BOTAO = tema_verde["botao"]
        COR_DO_BOTAO_HOVER = tema_verde["botao_hover"]

    elif nivel == "Difícil":
        COR_DE_FUNDO = tema_vermelho["background"]
        COR_DO_CHAO = tema_vermelho["chao"]
        COR_DO_VETOR = tema_vermelho["vetor"]
        COR_DO_BOTAO = tema_vermelho["botao"]
        COR_DO_BOTAO_HOVER = tema_vermelho["botao_hover"]        

    while True:
        retangulo = pygame.Rect(cesta.rede_esquerda_body.position.x, cesta.rede_esquerda_body.position.y+cesta.altura-bola.radius-5, cesta.largura, 2*bola.radius)

        contador += 1

        #relógio
        tempo = pygame.time.get_ticks()
        
        #verificador de teclas pressionadas
        key = pygame.key.get_pressed()

        #Event handler do pygame
        for event in pygame.event.get():
            #Botão de fechar a janela
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_clicado = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_clicado = False   
        
        
        if botao_retornar.clicado(mouse_clicado):
            mouse_clicado = False
            return 1
        if botao_reiniciar.clicado(mouse_clicado):
            mouse_clicado = False
            pygame.time.delay(50)
            #remoção dos objetos físicos do espaço do pymunk para evitar erros no carregamento do próximo jogo
            cesta.remover_do_pymunk()
            bola.remover_do_pymunk()
            parede_direita.remover_do_pymunk()
            parede_esquerda.remover_do_pymunk()
            chao.remover_do_pymunk()
            return 2
        if botao_pausar.clicado(mouse_clicado):
            mouse_clicado = False
            resultado_da_pausa = pausa(tela, tempo_faltando, pontuacao)
            if resultado_da_pausa == 0:
                return 0
            elif resultado_da_pausa == 1:
                return 1
            else:
                tempo_total_pausado += resultado_da_pausa
                
        if tempo_faltando <= 0 and lancamento == False:
            pygame.time.delay(1000)
            
            #remoção dos objetos físicos do espaço do pymunk para evitar erros no carregamento do próximo jogo
            cesta.remover_do_pymunk()
            bola.remover_do_pymunk()
            parede_direita.remover_do_pymunk()
            parede_esquerda.remover_do_pymunk()
            chao.remover_do_pymunk()
            resultado_tela_fim_de_jogo = fim_de_jogo(tela)
            
            if resultado_tela_fim_de_jogo == 0:
                return 0                            #Fechar o jogo                           
            elif resultado_tela_fim_de_jogo == 1:
                return 1                            #Ir para a tela inicial
            elif resultado_tela_fim_de_jogo == 2:
                return 2                            #Reiniciar o jogo

        #realização do lançamento
        if mouse_clicado and not botao_retornar.clicado(mouse_clicado) and not botao_pausar.clicado(mouse_clicado) and not lancamento and tempo_ao_lancar - tempo_faltando >= 1000:

            lancamento = True
            tempo_ao_lancar = tempo_faltando
            bola.lancamento(5*velocidade_horizontal, 5*velocidade_vertical)
            arremessos_totais += 1    
            if bola.posicao_horizontal_ao_lancar < distancia_linha_de_3-largura_linha_de_3/2:
                arremessos_de_3 += 1        

        #se a bola sair da tela, quicar a partir de 3 vezes, estiver parada na cesta ou o tempo após o lançamento exceder 10 segundos, é feito um respawn dela
        if (bola.body.position.x > LARGURA_DA_TELA+50 or bola.body.position.x < -50 or quiques >= 4 or tempo_ao_lancar - tempo_faltando >= 10000):
            acertou = False
            pode_fazer_ponto = True
            quiques = 0
            quique_contabilizado = False
            bola.respawn(None, bola.body.position.x)

        if retangulo.collidepoint(bola.body.position):
            acertou = True

        if tempo_ao_lancar - tempo_faltando >= 10000 or (bola.body.velocity.y == 0 and verificador_de_quiques.collidepoint(bola.body.position)):
            lancamento = False
            bola.respawn(None, bola.body.position.x)

        if not verificador_de_quiques.collidepoint(bola.body.position):
            quique_contabilizado = False 
        if verificador_de_quiques.collidepoint(bola.body.position) and not quique_contabilizado:
            quiques += 1
            quique_contabilizado = True
        if acertou == True:
            if pode_fazer_ponto == True:
                #No basquete, caso o jogador pise na linha, a cesta é de 2 pontos. 
                #Como no pygame a largura da linha é considerada para os dois lados a partir do seu centro, então a distância da linha de 3 deve ser considerada somada à metade da largura da linha
                arremessos_totais_convertidos += 1
                if bola.posicao_horizontal_ao_lancar < distancia_linha_de_3-largura_linha_de_3/2:
                    arremessos_de_3_convertidos += 1
                    pontuacao += 3
                elif bola.posicao_horizontal_ao_lancar >= distancia_linha_de_3-largura_linha_de_3/2:
                    pontuacao += 2
                tempo_ao_acertar = tempo_faltando

                pode_fazer_ponto = False

            if tempo_faltando <= 0:
                lancamento = False
                pygame.time.delay(500)

            if tempo_ao_acertar - tempo_faltando >= 500:
                if not nivel == "Fácil":
                    cesta.posicao_aleatoria()
                lancamento = False
                acertou = False

                bola.respawn(randint(-100, 150), None)
                pode_fazer_ponto = True
                quiques = 0
                quique_contabilizado = False

        if nivel == "Difícil":
            cesta.movimento_horizontal()

        #procedimentos enquanto a bola está no chão
        if lancamento == False:
            #movimento para a esquerda
            if key[pygame.K_a] == True and lancamento == False:
                bola.body.velocity = (-250, 0)

            #movimento para a direita
            elif key[pygame.K_d] == True and lancamento == False:
                bola.body.velocity = (250, 0)

            #a bola para
            else:
                bola.body.velocity = (0, 0)

            posicao_mouse = pygame.mouse.get_pos()
            velocidade_vertical =  (int(posicao_mouse[1]) - int(bola.body.position.y))
            if velocidade_vertical <= -velocidade_maxima/5:
                velocidade_vertical = -velocidade_maxima/5
            if velocidade_vertical>= -velocidade_minima:
                velocidade_vertical = -velocidade_minima

            velocidade_horizontal = (int(posicao_mouse[0]) - int(bola.body.position.x))
            if velocidade_horizontal >= velocidade_maxima/5:
                velocidade_horizontal = velocidade_maxima/5
            if velocidade_horizontal <= -velocidade_maxima/5:
                velocidade_horizontal = -velocidade_maxima/5

        #se a bola estiver no chão, e com velocidade vertical 0, então o lançamento acabou
        elif lancamento == True and bola.body.velocity.y == 0 and bola.body.position.y>=ALTURA_DA_TELA-100-bola.radius:
            lancamento = False
            acertou = False
            pode_fazer_ponto = True
            quiques = 0
            quique_contabilizado = False
     
        #Preenchimento da tela com a cor de fundo, para que a cada frame haja uma atualização do que é exibido
        tela.fill(COR_DE_FUNDO)
        
        #pygame.draw.rect(tela, (200, 200, 200),retangulo) #visualização do hitbox da cesta

        #Exibição na tela dos elementos
        
        if lancamento:
            if contador%5 == 0:
                pontos_trajetoria.append((int(bola.body.position.x), int(bola.body.position.y)))
            bola.desenhar_rastro(pontos_trajetoria, nivel)
        for botao in botoes:
            if botao.mouse_sobre():
                botao.cor = COR_DO_BOTAO_HOVER
            else:
                botao.cor = COR_DO_BOTAO

        botao_retornar.desenhar()
        botao_reiniciar.desenhar()
        botao_pausar.desenhar()
        tela.blit(texto_botao_retornar, texto_botao_retornar.get_rect(center=(botao_retornar.posicao_x + botao_retornar.largura / 2, botao_retornar.posicao_y + botao_retornar.altura / 2)))
        tela.blit(texto_botao_pausar, texto_botao_pausar.get_rect(center=(botao_pausar.posicao_x + botao_pausar.largura / 2, botao_pausar.posicao_y + botao_pausar.altura / 2)))
        tela.blit(texto_botao_reiniciar, texto_botao_reiniciar.get_rect(center=(botao_reiniciar.posicao_x + botao_reiniciar.largura / 2, botao_reiniciar.posicao_y + botao_reiniciar.altura / 2)))
        cesta.desenhar()
        bola.desenhar()
        chao.desenhar(COR_DO_CHAO)
        parede_direita.desenhar()
        parede_esquerda.desenhar()
        exibir_pontuacao(pontuacao)
        tempo_decorrido = tempo - tempo_ao_iniciar - tempo_total_pausado
        tempo_faltando = tempo_limite - tempo_decorrido
        if tempo_faltando <= 0:
            tempo_faltando = 0
        exibir_tempo(tempo_faltando)
        pygame.draw.arc(tela, (255, 255, 255), pygame.Rect(distancia_linha_de_3-2, ALTURA_DA_TELA-219, 400, 240), radians(180), radians(250), 5)

        #Se o lançamento não estiver acontecendo, o vetor que representa a velocidade de lançamento e o ângulo é desenhado
        if not lancamento and tempo_faltando>0:
            pontos_trajetoria.clear()
            pygame.draw.line(tela, COR_DO_VETOR, (int(bola.body.position.x), int(bola.body.position.y)), (int(bola.body.position.x)+int(velocidade_horizontal), int(bola.body.position.y)+int(velocidade_vertical)), 4)
    
        #Taxa de FPS limitada 
        clock.tick(FPS)

        #Tempo para a atualização de física do pymunk ser atualizada
        space.step(1/FPS)

        pygame.display.update()

def fim_de_jogo(tela):
    botao_jogar_novamente = Botao((0, 255, 255), {"largura": 300, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA/2 - 150, "coordenada_vertical": ALTURA_DA_TELA - 225})
    botao_voltar_a_tela_inicial = Botao((0, 255, 255), {"largura": 300, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA/2 - 150, "coordenada_vertical": ALTURA_DA_TELA - 150})
    botoes = [botao_jogar_novamente, botao_voltar_a_tela_inicial]
    texto_botao_jogar_novamente = exibir_texto(tela, "Jogar novamente", 0,0, 30, (255, 255, 255))
    texto_botao_voltar_a_tela_inicial = exibir_texto(tela, "Tela inicial", 0,0, 30, (255, 255, 255))
    mouse_clicado = False

    while True:
        tela.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicado = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_clicado = False   
        
        for botao in botoes:
            if botao.mouse_sobre():
                botao.cor = (25, 25, 25)
            else:
                botao.cor = (0, 0, 0)   
        
        botao_jogar_novamente.desenhar()
        botao_voltar_a_tela_inicial.desenhar()
        
        tela.blit(texto_botao_jogar_novamente, texto_botao_jogar_novamente.get_rect(center=(botao_jogar_novamente.posicao_x + botao_jogar_novamente.largura / 2, botao_jogar_novamente.posicao_y + botao_jogar_novamente.altura / 2)))        
        tela.blit(texto_botao_voltar_a_tela_inicial, texto_botao_voltar_a_tela_inicial.get_rect(center=(botao_voltar_a_tela_inicial.posicao_x + botao_voltar_a_tela_inicial.largura / 2, botao_voltar_a_tela_inicial.posicao_y + botao_voltar_a_tela_inicial.altura / 2)))        
        if arremessos_totais != 0:
            tela.blit(exibir_texto(tela, f'Arremessos: {arremessos_totais_convertidos}/{arremessos_totais} ({(100*arremessos_totais_convertidos/arremessos_totais):.0f}%)', LARGURA_DA_TELA/2 -300, ALTURA_DA_TELA/2+150, 30, (255, 255, 255), 'verdana'),pygame.Rect(LARGURA_DA_TELA/2-187, ALTURA_DA_TELA/2-100, 600, 50))
        elif arremessos_totais == 0:
            tela.blit(exibir_texto(tela, f'Arremessos: {arremessos_totais_convertidos}/{arremessos_totais} ({0:.0f}%)', LARGURA_DA_TELA/2-0, ALTURA_DA_TELA/2+150, 30, (255, 255, 255), 'verdana'), pygame.Rect(LARGURA_DA_TELA/2-187, ALTURA_DA_TELA/2-100, 600, 50))
        
        if arremessos_de_3 != 0:
            tela.blit(exibir_texto(tela, f'Arremessos de 3: {arremessos_de_3_convertidos}/{arremessos_de_3} ({(100*arremessos_de_3_convertidos/arremessos_de_3):.0f}%)', LARGURA_DA_TELA/2-300, ALTURA_DA_TELA/2+200, 30, (255, 255, 255), 'verdana'), pygame.Rect(LARGURA_DA_TELA/2-264, ALTURA_DA_TELA/2-50, 600, 50))
        elif arremessos_de_3 == 0:
            tela.blit(exibir_texto(tela, f'Arremessos de 3: {arremessos_de_3_convertidos}/{arremessos_de_3} ({0:.0f}%)', LARGURA_DA_TELA/2-200, ALTURA_DA_TELA/2+200, 30, (255, 255, 255), 'verdana'), pygame.Rect(LARGURA_DA_TELA/2-264, ALTURA_DA_TELA/2-50, 600, 50))
        
        tela.blit(exibir_texto(tela, f'Pontos: {pontuacao}', LARGURA_DA_TELA/2-150, ALTURA_DA_TELA/2-170, 50, (255, 255, 255), 'verdana'), pygame.Rect(LARGURA_DA_TELA/2-180, ALTURA_DA_TELA/2-170, 600, 50))

        if botao_voltar_a_tela_inicial.clicado(mouse_clicado):
            mouse_clicado = False

            return 1
        
        if botao_jogar_novamente.clicado(mouse_clicado):
            mouse_clicado = False
            return 2
        
        clock.tick(FPS)
            
        pygame.display.update()


tela_inicial(tela)

pygame.quit()