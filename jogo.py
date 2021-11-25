import pygame
import time
import random
pygame.init()
largura = 800
altura = 600
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("FutImed - felix")
icone = pygame.image.load("assets/bola.png")
pygame.display.set_icon(icone)
jogador = pygame.image.load("assets/jogador.png")
largurajogador = 80
fundo = pygame.image.load("assets/estadio.png")
cartao = pygame.image.load("assets/cartao.png")
juiz = pygame.image.load("assets/cartao-vermelho.png")
apitoSound = pygame.mixer.Sound("assets/apito.mp3")
cartaovPosicaoX = largura*0.40
cartaovPosicaoY = altura*0.81


apitoSound.set_volume(0.2)
def mostraVermelho(x, y):
    gameDisplay.blit(juiz,(x,y))
    pygame.display.update(juiz(x,y))
    dead()
def mostraJogador(x, y):
    gameDisplay.blit(jogador, (x, y))
def mostracartao(x, y):
    gameDisplay.blit(cartao, (x, y))
def text_objects(texto, font):
    textSurface = font.render(texto, True, white)
    return textSurface, textSurface.get_rect()
def escreverTela(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    TextSurf, TextRect = text_objects(texto, fonte)
    TextRect.center = ((largura/2, altura/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    game()
def escreverPlacar(contador):
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render("Pontos: "+str(contador), True, white)
    gameDisplay.blit(texto, (10, 10))
def dead():
    pygame.mixer.Sound.play(apitoSound)
    pygame.mixer.music.stop()
    escreverTela("Você foi expulso!")
     
def game():
    pygame.mixer.music.load("assets/futebol_som.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    jogadorPosicaoX = largura*0.40
    jogadorPosicaoY = altura*0.81
    movimentoX = 0
    velocidade = 10
    cartaoAltura = 86
    cartaoLargura = 85
    cartaoVelocidade = 2
    cartaoX = random.randrange(0, largura)
    cartaoY = -200
    desvios = 0
    
    while True:
        # pega as ações da tela. Ex.: fechar, click de uma tecla ou do mouse
        acoes = pygame.event.get()  # devolve uma lista de ações
        keys = pygame.key.get_pressed()                  
        if keys[pygame.K_LEFT] and jogadorPosicaoX > velocidade:              
            jogadorPosicaoX -= velocidade          
        if keys[pygame.K_RIGHT] and jogadorPosicaoX < 1400 - velocidade - jogadorPosicaoX:               
            jogadorPosicaoX += velocidade
        # [ini] mapeando as ações
        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()
            if acao.type == pygame.KEYDOWN:
                if acao.key == pygame.K_LEFT:
                    movimentoX = velocidade*-1
                elif acao.key == pygame.K_RIGHT:
                    movimentoX = velocidade
            if acao.type == pygame.KEYUP:
                movimentoX = 0
        # [end] mapeando as ações
        # definindo o fundo do game
        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (0, 0))
        # definindo o fundo do game]
        escreverPlacar(desvios)
        cartaoY = cartaoY + cartaoVelocidade
        mostracartao(cartaoX, cartaoY)
        if cartaoY > altura:
            cartaoY = -200
            cartaoX = random.randrange(0, largura)
            desvios = desvios+1
            cartaoVelocidade += 1

        jogadorPosicaoX += movimentoX
        if jogadorPosicaoX < 0:
            jogadorPosicaoX = 0
        elif jogadorPosicaoX > largura-largurajogador:
            jogadorPosicaoX = largura-largurajogador
        # analise de colisão com o jogador
        if jogadorPosicaoY < cartaoY + cartaoAltura:
            if jogadorPosicaoX < cartaoX and jogadorPosicaoX+largurajogador > cartaoX or cartaoX+cartaoLargura > jogadorPosicaoX and cartaoX+cartaoLargura < jogadorPosicaoX+largurajogador:
                dead()
            
                
                
        # analise de colisão com o jogador
        mostraJogador(jogadorPosicaoX, jogadorPosicaoY)
        pygame.display.update()
        
        clock.tick(60)  # faz com que o while execute 60x por segundo
game()
