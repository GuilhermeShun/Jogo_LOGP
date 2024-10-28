import pygame, math
from constantes import *
from funcoes import *


'''
Significados dos códigos de retorno:
0: fechar o jogo
1: voltar para a tela inicial
2: reiniciar o jogo

'''

def tela_inicial(tela):
    global mouse_clicado, space, lancamento, nivel

    texto_start = exibir_texto(tela, "Iniciar", 0,0, 30, (255, 255, 255))
    texto_options = exibir_texto(tela, "Opções", 0, 0, 30, (255, 255, 255))
    texto_exit = exibir_texto(tela, "Sair", 0, 0, 30, (255, 255, 255))        
    start_button = Botao(tema_menu["botao"], {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA / 2 - 100, "coordenada_vertical": ALTURA_DA_TELA / 2 - 150})
    options_button = Botao(tema_menu["botao"], {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA / 2 - 100, "coordenada_vertical": ALTURA_DA_TELA / 2 - 75})
    exit_button = Botao(tema_menu["botao"], {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA / 2 - 100, "coordenada_vertical": ALTURA_DA_TELA / 2})
    botoes_menu = [start_button, options_button, exit_button]
    COR_DE_FUNDO = tema_menu["background"]
    RETANGULO_DOS_BOTOES = pygame.Rect(LARGURA_DA_TELA/2 - 200, ALTURA_DA_TELA/2 - 200, 400, 300)
   
    botao_nivel_facil = Botao(cor_do_botao, {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": 300, "coordenada_vertical": ALTURA_DA_TELA-100})
    botao_nivel_medio = Botao(cor_do_botao, {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": 550, "coordenada_vertical": ALTURA_DA_TELA-100})
    botao_nivel_dificil = Botao(cor_do_botao, {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": 800, "coordenada_vertical": ALTURA_DA_TELA-100})

    texto_botao_nivel_facil = exibir_texto(tela, "Fácil", 0,0, 30, (255, 255, 255))
    texto_botao_nivel_medio = exibir_texto(tela, "Médio", 0,0, 30, (255, 255, 255))
    texto_botao_nivel_dificil = exibir_texto(tela, "Difícil", 0,0, 30, (255, 255, 255))
    texto_nivel = exibir_texto(tela, "Nível: ", 0, 0, 30, (255, 255, 255))
    botoes_dificuldade = [botao_nivel_facil, botao_nivel_medio, botao_nivel_dificil]
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
        

        
        if start_button.clicado(mouse_clicado):
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

        if exit_button.clicado(mouse_clicado):
            mouse_clicado = False
            return
        if options_button.clicado(mouse_clicado):
            mouse_clicado = False
            if configuracoes(tela) == False:
                return

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

        start_button.desenhar()
        options_button.desenhar()
        exit_button.desenhar()

        tela.blit(texto_start, texto_start.get_rect(center=(start_button.posicao_x + start_button.largura / 2, start_button.posicao_y + start_button.altura / 2)))
        tela.blit(texto_options, texto_options.get_rect(center=(options_button.posicao_x + options_button.largura / 2, options_button.posicao_y + options_button.altura / 2)))
        tela.blit(texto_exit, texto_exit.get_rect(center=(exit_button.posicao_x + exit_button.largura / 2, exit_button.posicao_y + exit_button.altura / 2)))

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

        tela.blit(texto_nivel, pygame.Rect(100, ALTURA_DA_TELA-100, 150, 50))
        tela.blit(texto_botao_nivel_facil, texto_botao_nivel_facil.get_rect(center=(botao_nivel_facil.posicao_x + botao_nivel_facil.largura / 2, botao_nivel_facil.posicao_y + botao_nivel_facil.altura / 2)))
        tela.blit(texto_botao_nivel_medio, texto_botao_nivel_medio.get_rect(center=(botao_nivel_medio.posicao_x + botao_nivel_medio.largura / 2, botao_nivel_medio.posicao_y + botao_nivel_medio.altura / 2)))
        tela.blit(texto_botao_nivel_dificil, texto_botao_nivel_dificil.get_rect(center=(botao_nivel_dificil.posicao_x + botao_nivel_dificil.largura / 2, botao_nivel_dificil.posicao_y + botao_nivel_dificil.altura / 2)))

        clock.tick(FPS)

        pygame.display.update()

def configuracoes(tela):
    global mouse_clicado, lancamento, nivel
    botao_retornar = Botao(cor_do_botao, {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": 30, "coordenada_vertical": 20})

    texto_botao_retornar = exibir_texto(tela, "Retornar", 0,0, 30, (255, 255, 255))
    botoes = [botao_retornar]
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
        

        
        if botao_retornar.clicado(mouse_clicado):
            mouse_clicado = False
            return True
        
        tela.fill((60, 60, 60))

        for botao in botoes:
            if botao.mouse_sobre():
                botao.cor = (25, 25, 25)
            else:
                botao.cor = (0, 0, 0)   

        botao_retornar.desenhar()
 

        tela.blit(texto_botao_retornar, texto_botao_retornar.get_rect(center=(botao_retornar.posicao_x + botao_retornar.largura / 2, botao_retornar.posicao_y + botao_retornar.altura / 2)))

        clock.tick(FPS)

        pygame.display.update()

def pausa(tela):
    global mouse_clicado
    botao_retornar = Botao(cor_do_botao, {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": LARGURA_DA_TELA / 2 - 50, "coordenada_vertical": ALTURA_DA_TELA / 2})

    texto_botao_retornar = exibir_texto(tela, "Retornar", 0,0, 30, (255, 255, 255))
    botoes = [botao_retornar]
    tempo_inicial = pygame.time.get_ticks()
    while True:
        tempo = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:                    
                    mouse_clicado = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:                    
                    mouse_clicado = False   
        
 
        
        tempo_decorrido_na_pausa = tempo - tempo_inicial
        
        if botao_retornar.clicado(mouse_clicado):
            mouse_clicado = False
            return tempo_decorrido_na_pausa

        tela.fill((255, 100, 100))
        for botao in botoes:
            if botao.mouse_sobre():
                botao.cor = (25, 25, 25)
            else:
                botao.cor = (0, 0, 0)  

        botao_retornar.desenhar()

        tela.blit(texto_botao_retornar, texto_botao_retornar.get_rect(center=(botao_retornar.posicao_x + botao_retornar.largura / 2, botao_retornar.posicao_y + botao_retornar.altura / 2)))

        clock.tick(FPS)

        pygame.display.update()

#Função jogo
def jogo(tela):

    global mouse_clicado, tempo_de_pausa, arremessos_de_3, arremessos_de_3_convertidos, arremessos_totais, arremessos_totais_convertidos, pontuacao
    botao_retornar = Botao((3, 13, 67), {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": 10, "coordenada_vertical": 10})
    texto_botao_retornar = exibir_texto(tela, "Retornar", 0,0, 30, (255, 255, 255))
    botao_pausar = Botao((3, 13, 67), {"largura": 200, "altura": 50}, tela, {"coordenada_horizontal": 10, "coordenada_vertical": 80})
    texto_botao_pausar = exibir_texto(tela, "Pausar", 0,0, 30, (255, 255, 255))
    botoes = [botao_retornar, botao_pausar]
    lancamento = False
    cesta = Cesta(nivel)
    bola = Bola()
    chao = Chao()
    parede_esquerda = Paredes((0, 0), (0, ALTURA_DA_TELA))
    parede_direita = Paredes((LARGURA_DA_TELA, 0), (LARGURA_DA_TELA, ALTURA_DA_TELA))
    tempo_ao_ajustar = 0
    velocidade_horizontal = 0
    velocidade_vertical = 0
    velocidade_maxima = 1500
    velocidade_minima = 10
    pontos_trajetoria = []
    contador = 0
    pode_fazer_ponto = True
    acertou = False
    pontuacao = 0
    distancia_linha_de_3 = 300
    largura_linha_de_3 = 6
    tempo_ao_iniciar = pygame.time.get_ticks()
    tempo_limite = 30000
    tempo_de_pausa = 0
    tempo_total_pausado = 0
    tempo_faltando = tempo_limite
    arremessos_totais = 0
    arremessos_de_3 = 0
    arremessos_totais_convertidos = 0
    arremessos_de_3_convertidos = 0

    if nivel == "Fácil":
        COR_DE_FUNDO = tema_azul["background"]
        COR_DO_CHAO = tema_azul["chao"]
        COR_DO_VETOR = tema_azul["vetor"]
        COR_DO_BOTAO = tema_azul["botao"]
        COR_DO_BOTAO_HOVER = tema_azul["botao_hover"]
        #COR_INICIAL_TRAJETORIA = 

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
            return True
        if botao_pausar.clicado(mouse_clicado):
            mouse_clicado = False
            resultado_da_pausa = pausa(tela)
            if resultado_da_pausa == False:
                return False
            else:
                tempo_total_pausado += resultado_da_pausa
        if tempo_faltando <= 0 and lancamento == False:
            pygame.time.delay(1000)
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
        if mouse_clicado and not botao_retornar.clicado(mouse_clicado) and not botao_pausar.clicado(mouse_clicado) and not lancamento:

            lancamento = True
            bola.lancamento(5*velocidade_horizontal, 5*velocidade_vertical)
            arremessos_totais += 1    
            if bola.posicao_horizontal_ao_lancar < distancia_linha_de_3-largura_linha_de_3/2:
                arremessos_de_3 += 1        
        #se a bola sair da tela ou o jogador solicitar, é feito um respawn dela e a função cesta.posicao_aleatoria() é chamada, modificando sua posição aleatoriamente
        #if (bola.body.position.x > LARGURA_DA_TELA+50 or bola.body.position.x < -50):
        if (bola.body.position.x > LARGURA_DA_TELA+50 or bola.body.position.x < -50 or (key[pygame.K_q] and tempo-tempo_ao_ajustar>=1000 and tempo_faltando >= 0)):

            acertou = False
            pode_fazer_ponto = True
            bola.respawn()
                       
            tempo_ao_ajustar = pygame.time.get_ticks()

        if retangulo.collidepoint(bola.body.position):
            acertou = True
        if acertou == True and pode_fazer_ponto == True:
            if not nivel == "Fácil":
                cesta.posicao_aleatoria()
            #No basquete, caso o jogador pise na linha, a cesta é de 2 pontos. 
            #Como no pygame a largura da linha é considerada para os dois lados a partir do seu centro, então a distância da linha de 3 deve ser considerada somada à metade da largura da linha
            arremessos_totais_convertidos += 1
            if bola.posicao_horizontal_ao_lancar < distancia_linha_de_3-largura_linha_de_3/2:
                arremessos_de_3_convertidos += 1
                pontuacao += 3
            elif bola.posicao_horizontal_ao_lancar >= distancia_linha_de_3-largura_linha_de_3/2:
                pontuacao += 2
            pode_fazer_ponto = False
            lancamento = False


            bola.respawn()
            acertou = False
            pode_fazer_ponto = True
         

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
        botao_pausar.desenhar()
        tela.blit(texto_botao_retornar, texto_botao_retornar.get_rect(center=(botao_retornar.posicao_x + botao_retornar.largura / 2, botao_retornar.posicao_y + botao_retornar.altura / 2)))
        tela.blit(texto_botao_pausar, texto_botao_pausar.get_rect(center=(botao_pausar.posicao_x + botao_pausar.largura / 2, botao_pausar.posicao_y + botao_pausar.altura / 2)))
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
        pygame.draw.arc(tela, (255, 255, 255), pygame.Rect(distancia_linha_de_3-2, ALTURA_DA_TELA-219, 400, 240), math.radians(180), math.radians(250), 5)
        '''
        
        if key[pygame.K_t]:
            pygame.draw.line(tela, (255, 255, 255), (distancia_linha_de_3, ALTURA_DA_TELA-100), (distancia_linha_de_3, ALTURA_DA_TELA), largura_linha_de_3)
     
        
        if key[pygame.K_t]:
            pygame.draw.line(tela, (255, 255, 255), (distancia_linha_de_3+170, ALTURA_DA_TELA), (LARGURA_DA_TELA, ALTURA_DA_TELA), 2*largura_linha_de_3+3)
        '''

        #Se o lançamento não estiver acontecendo, o vetor que representa a velocidade de lançamento e o ângulo é desenhado
        if not lancamento:
            pontos_trajetoria.clear()
            pygame.draw.line(tela, COR_DO_VETOR, (int(bola.body.position.x), int(bola.body.position.y)), (int(bola.body.position.x)+int(velocidade_horizontal), int(bola.body.position.y)+int(velocidade_vertical)), 4)
    
        #Taxa de FPS limitada 
        clock.tick(FPS)

        #Tempo para a atualização de física do pymunk ser atualizada
        space.step(1/FPS)

        pygame.display.update()

def fim_de_jogo(tela):
    botao_jogar_novamente = Botao((0, 255, 255), {"largura": 300, "altura": 50}, tela, {"coordenada_horizontal": 400, "coordenada_vertical": 300})
    botao_voltar_a_tela_inicial = Botao((0, 255, 255), {"largura": 300, "altura": 50}, tela, {"coordenada_horizontal": 400, "coordenada_vertical": 370})
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
        tela.blit(exibir_texto(tela, f'Arremessos: {arremessos_totais_convertidos}/{arremessos_totais}. Porcentagem: {(100*arremessos_totais_convertidos/arremessos_totais):.0f}%', LARGURA_DA_TELA/2-300, ALTURA_DA_TELA/2+150, 30, (255, 255, 255)), pygame.Rect(LARGURA_DA_TELA/2-300, ALTURA_DA_TELA/2+150, 300, 50))
        tela.blit(exibir_texto(tela, f'Arremessos de 3: {arremessos_de_3_convertidos}/{arremessos_de_3}. Porcentagem: {(100*arremessos_de_3_convertidos/arremessos_de_3):.0f}%', LARGURA_DA_TELA/2-300, ALTURA_DA_TELA/2+200, 30, (255, 255, 255)), pygame.Rect(LARGURA_DA_TELA/2-300, ALTURA_DA_TELA/2+200, 300, 50))
        tela.blit(exibir_texto(tela, f'Pontos: {pontuacao}', LARGURA_DA_TELA/2-300, ALTURA_DA_TELA/2+250, 30, (255, 255, 255)), pygame.Rect(LARGURA_DA_TELA/2-300, ALTURA_DA_TELA/2+250, 300, 50))
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