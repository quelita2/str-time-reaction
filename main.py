import pygame
import random
import time

# Inicializando o Pygame
pygame.init()

# Definindo cores
AMARELO = (255, 255, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Mapeando teclas às cores
teclas_cores = {
    pygame.K_UP: AMARELO,
    pygame.K_DOWN: VERDE,
    pygame.K_LEFT: AZUL,
    pygame.K_RIGHT: VERMELHO
}

# Configurações da tela
tamanho_tela = (800, 600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Medidor de Tempo de Reação")

# Fonte
fonte = pygame.font.Font(None, 36)

def mostrar_instrucoes():
    '''Função para mostrar as instruções'''
    tela.fill(PRETO)
    instrucoes = [
        "",
        "Medidor de tempo de reação!",
        "",
        "Você terá 10 tentativas para responder.",
        "As teclas e cores associadas são:",
        "",
        "UP: Amarelo",
        "DOWN: Verde",
        "LEFT: AZUL",
        "RIGHT: Vermelho",
        "",
        "Aperte qualquer tecla para começar."
    ]
    for i, texto in enumerate(instrucoes):
        linha = fonte.render(texto, True, BRANCO)
        largura_texto = linha.get_width()
        tela.blit(linha, ((tamanho_tela[0] - largura_texto) // 2, 50 + i * 40))
    pygame.display.flip()

def mostrar_circulo(cor, posicao):
    '''Função para exibir um círculo em uma posição e cor aleatória'''
    pygame.draw.circle(tela, cor, posicao, 50)
    pygame.display.flip()
    
def jogo():
    '''Função principal do jogo'''
    tempos_reacao = []
    acertos = 0
    tentativas = 10

    for tentativa in range(tentativas):
        # Espera aleatória até 3 segundos antes de aparecer o círculo
        pygame.time.wait(random.randint(1000, 3000))
        
        # Seleciona uma cor e uma posição aleatória para o círculo
        cor_atual = random.choice(list(teclas_cores.values()))
        
        # Define limites para o círculo
        posicao_atual = (
            random.randint(100, 700),  # limite horizontal
            random.randint(150, 500)   # limite vertical
        )
        
        # Mostra o círculo na tela
        tela.fill(PRETO)  # Limpa a tela
        mostrar_circulo(cor_atual, posicao_atual)

        inicio_tempo = time.time()
        resposta_correta = False

        while not resposta_correta:
            # Verifica se o usuário pressionou alguma tecla
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    # Calcula o tempo de reação
                    tempo_reacao = time.time() - inicio_tempo
                    tempos_reacao.append(tempo_reacao)

                    # Verifica se a tecla pressionada corresponde à cor correta
                    if evento.key in teclas_cores and teclas_cores[evento.key] == cor_atual:
                        acertos += 1
                    
                    # Limpa a tela antes de mostrar o próximo círculo
                    tela.fill(PRETO)
                    resposta_correta = True
                    pygame.display.flip()  # Atualiza a tela após limpar
                    break

    # Cálculo do tempo médio de reação
    media_tempo = sum(tempos_reacao) / len(tempos_reacao) if tempos_reacao else 0

    # Mostra os resultados finais
    tela.fill(PRETO)
    resultado = f"Tempo medio de reação: {media_tempo:.2f} segundos"
    pontuacao = f"Acertos: {acertos} de {tentativas}"
    
    # Centraliza e exibe os resultados
    texto_resultado = fonte.render(resultado, True, BRANCO)
    texto_pontuacao = fonte.render(pontuacao, True, BRANCO)
    
    # Centralizando os textos
    largura_resultado = texto_resultado.get_width()
    largura_pontuacao = texto_pontuacao.get_width()
    
    tela.blit(texto_resultado, ((tamanho_tela[0] - largura_resultado) // 2, 200))
    tela.blit(texto_pontuacao, ((tamanho_tela[0] - largura_pontuacao) // 2, 250))
    pygame.display.flip()

    # Espera alguns segundos antes de fechar
    pygame.time.wait(5000)

def main():
    '''Função principal para rodar o jogo'''
    mostrar_instrucoes()
    
    # Espera até que uma tecla seja pressionada para iniciar
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                esperando = False
    
    # Iniciar o jogo
    jogo()

if __name__ == "__main__":
    '''Rodando o programa'''
    main()

# Encerrando o Pygame
pygame.quit()