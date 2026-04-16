import pygame
import random

pygame.init()

# Tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Configurações
tamanho_bloco = 10
velocidade = 15

clock = pygame.time.Clock()

def desenhar_cobra(tamanho, lista_cobra):
    for bloco in lista_cobra:
        pygame.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho, tamanho])

def jogo():
    while True:  # loop que permite reiniciar o jogo

        fim = False
        game_over = False

        x = largura / 2
        y = altura / 2

        x_mudanca = 0
        y_mudanca = 0

        cobra_lista = []
        comprimento = 1

        comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
        comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0

        while not fim:

            # 🔁 Estado de morte
            while game_over:
                pygame.time.delay(1000)  # espera 1 segundo
                break  # reinicia o jogo

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        x_mudanca = -tamanho_bloco
                        y_mudanca = 0
                    elif evento.key == pygame.K_RIGHT:
                        x_mudanca = tamanho_bloco
                        y_mudanca = 0
                    elif evento.key == pygame.K_UP:
                        y_mudanca = -tamanho_bloco
                        x_mudanca = 0
                    elif evento.key == pygame.K_DOWN:
                        y_mudanca = tamanho_bloco
                        x_mudanca = 0

            x += x_mudanca
            y += y_mudanca

            # Colisão com parede
            if x >= largura or x < 0 or y >= altura or y < 0:
                game_over = True

            tela.fill(preto)

            # Desenhar comida
            pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

            # Atualizar cobra
            cabeca = [x, y]
            cobra_lista.append(cabeca)

            if len(cobra_lista) > comprimento:
                del cobra_lista[0]

            # Colisão com o próprio corpo
            for bloco in cobra_lista[:-1]:
                if bloco == cabeca:
                    game_over = True

            desenhar_cobra(tamanho_bloco, cobra_lista)

            pygame.display.update()

            # Comer comida
            if x == comida_x and y == comida_y:
                comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
                comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0
                comprimento += 1

            clock.tick(velocidade)

jogo()