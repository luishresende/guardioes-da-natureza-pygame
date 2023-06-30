import pygame
from pygame.locals import *
import random
pygame.mixer.init()


def vitoria():
    somVitoria.play()
    while True:
        screen.blit(quadroVitoria, ((fundo.get_width() - quadroVitoria.get_width()) / 2, 83))
        screen.blit(pygame.transform.rotate(medidor[acertos], -90), (443, 350))
        pygame.display.flip()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False


def derrota():
    somDerrota.play()
    while True:
        screen.blit(quadroDerrota, ((fundo.get_width() - quadroDerrota.get_width()) / 2, 83))
        screen.blit(pygame.transform.rotate(medidor[acertos], -90), (443, 350))
        pygame.display.flip()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False


def trocar_cartas(jogador):
    # Criando uma lista com todos os seus jogadores e suas cartas
    jogadoresDisponiveis = [{'jogador': 0, 'cartas': jogadores[0]['cartas']},
                          {'jogador': 1, 'cartas': jogadores[1]['cartas']},
                          {'jogador': 2, 'cartas': jogadores[2]['cartas']}]

    jogadorSolicitante = jogadoresDisponiveis[jogador] # Definindo o jogador solicitando com base no id passado por parâmetro
    jogadoresDisponiveis.pop(jogador) # Removendo o jogador solicitante da lista de disponíveis
    cartasTrocaRect = list() # Definindo a lista que receberá o Rect das imagens das cartas
    cartasTrocasDisponiveis = list() # Definindo a lista que receberá o Rect das imagens das cartas, e posteriormente adicionada a lista acima

    # Definindo váriaveis iniciais
    jogadorTroca = 0 #
    idCartaTrocada = 0
    cartaTrocada = 0
    idCartaSolicitada = 0
    cartaSolicitada = 0
    posicaoCartaTrocaX = 140
    etapa = 0


    screen.blit(quadroTrocas[etapa], (0, 13)) # Desenhando o quadro de trocas para o jogador solicitante
    for carta in jogadorSolicitante['cartas']:
        screen.blit(cartas[carta][1], (posicaoCartaTrocaX, 242)) # Desenhando a carta
        carta_rect = cartas[carta][1].get_rect() # Definindo o Rect
        carta_rect.x = posicaoCartaTrocaX # Definindo a posição X do Rect
        carta_rect.y = 229 # Definindo a posição Y do Recy
        cartasTrocasDisponiveis.append(carta_rect) # Adicionando o Rect da carta na lista de cartas disponíveis

        posicaoCartaTrocaX += cartas[carta][1].get_width() + 30 # Aumentando a posição X para serem desenhadas no local correto
        pygame.display.flip() # Atualizando a tela
        clock.tick(60) # Definindo a quantidade de quadros por segundo

    cartasTrocaRect.append(cartasTrocasDisponiveis) # Adicionando a lista de cartas disponíveis na lista de Rect

    # Etapa 0: Seleção da carta que irá trocar
    while etapa == 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Verifica se um botão do mouse foi pressionado
                if event.button == 1:  # Verifica se o botão esquerdo do mouse foi pressionado
                    somClick.play()
                    for i, carta in enumerate(cartasTrocaRect[0]):
                        if carta.collidepoint(event.pos):
                            cartaTrocada = jogadorSolicitante['cartas'][i] # Obtendo a carta que será trocada
                            idCartaTrocada = i # Obtendo a posição da carta na mão do dono
                            cartasTrocasDisponiveis.clear() # Limpando a lista de cartas de trocas disponíveis
                            cartasTrocaRect.clear() # Limpando a lista de Rect
                            etapa = 1 # Alterando a etapa

    # Redefinindo posições das cartas para o novo layout
    posicaoCartaTrocaX = 140
    posicaoCartaTrocaY = 119
    screen.blit(quadroTrocas[etapa], (0, 13)) # Desenhando o quadro onde irá ficar as cartas disponiveis

    for jogador in jogadoresDisponiveis:
        for carta in jogador['cartas']:
            screen.blit(cartas[carta][1], (posicaoCartaTrocaX, posicaoCartaTrocaY)) # Desenhando a carta
            carta_rect = cartas[carta][1].get_rect() # Definindo o Rect
            carta_rect.x = posicaoCartaTrocaX # Definindo a posição X do Rect
            carta_rect.y = posicaoCartaTrocaY # Definindo a posição Y do Rect
            cartasTrocasDisponiveis.append(carta_rect) # Adicionando o Rect da carta na lista de cartas disponíveis

            posicaoCartaTrocaX += cartas[carta][1].get_width() + 30 # Aumentando a posição X para serem desenhadas no local correto
            pygame.display.flip()  # Atualizando a tela
            clock.tick(60)  # Definindo a quantidade de quadros por segundo

        cartasTrocaRect.append(cartasTrocasDisponiveis) # Adicionando a lista de cartas disponíveis na lista de Rect
        cartasTrocasDisponiveis = list() # Redefinindo a lista
        posicaoCartaTrocaX = 140
        posicaoCartaTrocaY = 317

    while etapa == 1: # Etapa 1: Escolha da nova carta
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Verifica se um botão do mouse foi pressionado
                if event.button == 1:  # Verifica se o botão esquerdo do mouse foi pressionado
                    somClick.play()
                    for i, conjunto in enumerate(cartasTrocaRect):
                        for j, carta in enumerate(conjunto):
                            if carta.collidepoint(event.pos):

                                cartaSolicitada = jogadoresDisponiveis[i]['cartas'][j] # Obtendo o número da carta
                                jogadorTroca = i # Obtendo o id do jogador que irá ceder a carta
                                idCartaSolicitada = j # Obtendo a posição da carta na mão do jogador

                                # Limpando as listas
                                cartasTrocasDisponiveis.clear()
                                cartasTrocaRect.clear()
                                etapa = 0

    # Realizando a troca das cartas
    jogadores[jogadorSolicitante['jogador']]['cartas'][idCartaTrocada] = cartaSolicitada
    jogadores[jogadoresDisponiveis[jogadorTroca]['jogador']]['cartas'][idCartaSolicitada] = cartaTrocada

    jogadorSolicitante.clear()
    cartas_rect.clear()


# Definir constantes
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600

somCerto = pygame.mixer.Sound("audios/certo.mp3")
somErrado = pygame.mixer.Sound("audios/errado.mp3")
somVitoria = pygame.mixer.Sound("audios/vitoria.mp3")
somDerrota = pygame.mixer.Sound("audios/derrota.mp3")
somClick = pygame.mixer.Sound("audios/click.mp3")

icone = pygame.image.load("imagens/icone.png")
cartaProblema = pygame.image.load("imagens/outros/verso-carta-problema.png")
fundo = pygame.image.load("imagens/fundos/fundo.png")

quadro = pygame.image.load("imagens/fundos/quadro.png")
quadroVitoria = pygame.image.load("imagens/quadros/quadro-vitoria.png")
quadroDerrota = pygame.image.load("imagens/quadros/quadro-derrota.png")
quadroTrocas = [pygame.image.load("imagens/quadros/quadro-troca1.png"),
                pygame.image.load("imagens/quadros/quadro-troca2.png")]

botaoTroca = pygame.image.load("imagens/outros/troca.png")

medidor = [
    pygame.image.load("imagens/medidor/0.png"),
    pygame.image.load("imagens/medidor/1.png"),
    pygame.image.load("imagens/medidor/2.png"),
    pygame.image.load("imagens/medidor/3.png"),
    pygame.image.load("imagens/medidor/4.png"),
    pygame.image.load("imagens/medidor/5.png"),
    pygame.image.load("imagens/medidor/6.png"),
    pygame.image.load("imagens/medidor/7.png"),
    pygame.image.load("imagens/medidor/8.png"),
    pygame.image.load("imagens/medidor/9.png"),
    pygame.image.load("imagens/medidor/10.png")
]

cartas = [
    [0, pygame.image.load("imagens/problemas/solucoes/proteger-animais.png")],
    [1, pygame.image.load("imagens/problemas/solucoes/praticar-reciclagem.png")],
    [2, pygame.image.load("imagens/problemas/solucoes/dimuir-emicao-poluentes.png")],
    [3, pygame.image.load("imagens/problemas/solucoes/reflorestar.png")],
    [4, pygame.image.load("imagens/problemas/solucoes/proteger-animais2.png")],
    [5, pygame.image.load("imagens/problemas/solucoes/dimuir-emicao-poluentes2.png")],
    [6, pygame.image.load("imagens/problemas/solucoes/consiencia-ambiental.png")],
    [7, pygame.image.load("imagens/problemas/solucoes/consiencia-ambiental2.png")],
    [8, pygame.image.load("imagens/problemas/solucoes/consiencia-ambiental3.png")],
    [9, pygame.image.load("imagens/problemas/solucoes/dimuir-emicao-poluentes3.png")],
    [10, pygame.image.load("imagens/problemas/solucoes/dimuir-emicao-poluentes4.png")],
    [11, pygame.image.load("imagens/problemas/solucoes/reflorestar2.png")],
    [12, pygame.image.load("imagens/problemas/solucoes/proteger-animais3.png")],
    [13, pygame.image.load("imagens/problemas/solucoes/habitos-sustentaveis.png")],
    [14, pygame.image.load("imagens/problemas/solucoes/praticar-reciclagem2.png")]]

biomas = [
    {
        'imagem': pygame.image.load("imagens/biomas/artico.png"),


        'problemas': [
            pygame.image.load("imagens/problemas/artico/artico1.png"),
            pygame.image.load("imagens/problemas/artico/artico2.png"),
            pygame.image.load("imagens/problemas/artico/artico3.png"),
            pygame.image.load("imagens/problemas/artico/artico4.png"),
            pygame.image.load("imagens/problemas/artico/artico5.png")
        ],

        'solucoes': [
            [2, 5, 9, 10], [2, 5, 9, 10], [0, 4, 12], [0, 4, 12], [2, 5, 9, 10]
        ]
    },

    {
        'imagem': pygame.image.load("imagens/biomas/floresta.png"),
        'problemas' : [
            pygame.image.load("imagens/problemas/floresta/floresta1.png"),
            pygame.image.load("imagens/problemas/floresta/floresta2.png"),
            pygame.image.load("imagens/problemas/floresta/floresta3.png"),
            pygame.image.load("imagens/problemas/floresta/floresta4.png"),
            pygame.image.load("imagens/problemas/floresta/floresta5.png"),
        ],
        'solucoes': [
            [3, 11], [6, 7, 8], [3, 11], [6, 7, 8], [0, 4, 12]
        ]
    },


    {
        'imagem': pygame.image.load("imagens/biomas/cidade.png"),
        'problemas': [
            pygame.image.load("imagens/problemas/cidade/cidade1.png"),
            pygame.image.load("imagens/problemas/cidade/cidade2.png"),
            pygame.image.load("imagens/problemas/cidade/cidade3.png"),
            pygame.image.load("imagens/problemas/cidade/cidade4.png"),
            pygame.image.load("imagens/problemas/cidade/cidade5.png"),
        ],
        'solucoes': [
            [2, 5, 9, 10], [1, 14], [1, 14], [13], [6, 7, 8]
        ]
    }
]
posicaoBiomas = [86, 38] # Posição padrão do bioma

# Inicialização do Pygame
pygame.init()
pygame.display.set_icon(icone)
pygame.display.set_caption("Guardiões do Meio Ambiente")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fonte = pygame.font.Font(None, 36)

# Definição da carta problema e seu Rect
cartaProblema_rect = cartaProblema.get_rect()
cartaProblema_rect.x = 736
cartaProblema_rect.y = 64
acertos = 4

# Misturando a lista de cartas e biomas
random.shuffle(cartas)
random.shuffle(biomas)

# Definindo os jogadores
jogador1 = {
    'cartas': [0, 1, 2, 3, 4],
    'bioma': biomas[0]
}

jogador2 = {
    'cartas': [5, 6, 7, 8, 9],
    'bioma': biomas[1]
}

jogador3 = {
    'cartas': [10, 11, 12, 13, 14],
    'bioma': biomas[2]
}

# Definindo a lista de jogadores
jogadores = [jogador1, jogador2, jogador3]
cartas_rect = [] # Lista de rect

# Definindo botão de troca de cartas
troca_rect = botaoTroca.get_rect()
troca_rect.x = 914
troca_rect.y = 451

clock = pygame.time.Clock()
# Loop principal do jogo
running = True
jogada = 0
troca = 0
problema = 0
while running:
    # Eventos do Pygame
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Verifica se um botão do mouse foi pressionado
            if event.button == 1:  # Verifica se o botão esquerdo do mouse foi pressionado
                somClick.play()
                if troca_rect.collidepoint(event.pos): # Se botão de troca for pressionado
                    trocar_cartas(jogada) # Chamada de função passando como parâmetro o jogador da vez
                    troca = 0 # Definindo troca = 0 para ser atualizado os Rect
                    cartas_rect.clear()

                if problema == 1:
                    for i, carta in enumerate(cartas_rect):
                        if carta.collidepoint(event.pos):
                            if cartas[jogadores[jogada]['cartas'][i]][0] in jogadores[jogada]['bioma']['solucoes'][0]:
                                somCerto.play()
                                acertos += 1
                            else:
                                somErrado.play()
                                acertos -= 1

                            print(cartas[jogadores[jogada]['cartas'][i]])
                            print(jogadores[jogada]['bioma']['solucoes'][0])

                            jogadores[jogada]['cartas'].pop(i)
                            jogadores[jogada]['bioma']['problemas'].pop(0)
                            jogadores[jogada]['bioma']['solucoes'].pop(0)

                            if acertos == 10:
                                running = vitoria()
                            elif acertos == 0:
                                running = derrota()

                            if len(jogadores[2]['bioma']['problemas']) == 0:
                                print('problemas esgotadas')
                                running = derrota()

                            troca = 0
                            problema = 0
                            if jogada < 2:
                                jogada += 1
                            else:
                                jogada = 0
                            cartas_rect.clear()
                            break
                else:
                    if cartaProblema_rect.collidepoint(event.pos):
                        problema = 1


    # Desenho o quadro na tela
    screen.blit(fundo, (0, 0))
    screen.blit(quadro, (70, 26))

    # Desenha o botão de troca
    screen.blit(botaoTroca, (914, 451))

    # Desenho o medidor na tela
    screen.blit(medidor[acertos], (990, 350))

    # Desenho na tela o bioma do jogador 1
    screen.blit(jogadores[jogada]['bioma']['imagem'], (posicaoBiomas[0], posicaoBiomas[1]))

    #Desenho na tela a carta problema
    if problema == 0:
        screen.blit(cartaProblema, (736, 64))
    else:
        screen.blit(jogadores[jogada]['bioma']['problemas'][0], (685, 53))

    # Desenho na tela as cartas do jogador
    posicaoCartaX = 36
    for carta in jogadores[jogada]['cartas']:
        screen.blit(cartas[carta][1], (posicaoCartaX, 393))
        if troca == 0:
            carta_rect = cartas[carta][1].get_rect()
            carta_rect.x = posicaoCartaX
            carta_rect.y = 393
            cartas_rect.append(carta_rect)
        posicaoCartaX += 176

    troca = 1
    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

