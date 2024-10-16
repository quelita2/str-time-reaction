# ⏱️ Medidor de Tempo de Reação

Este é um mini-game em Python, utilizando a biblioteca Pygame, que mede o tempo de reação de um jogador ao pressionar a tecla correta, associada à cor de um círculo que aparece aleatoriamente na tela. O jogo é composto por 10 tentativas, e no final exibe a pontuação do jogador (acertos) e o tempo médio de reação.

## Como Funciona

1. **Instruções**: Ao iniciar o jogo, o jogador verá uma tela com as instruções das teclas associadas às cores:
   - Tecla **UP**: Amarelo
   - Tecla **DOWN**: Verde
   - Tecla **LEFT**: Laranja
   - Tecla **RIGHT**: Vermelho

2. **Jogo**: Em cada rodada, um círculo de uma cor aparecerá em uma posição aleatória da tela após um intervalo aleatório de até 3 segundos. O jogador deve pressionar a tecla correta, associada à cor do círculo. O tempo de reação será medido, e o círculo desaparecerá após a tecla ser pressionada.

3. **Pontuação**: Após 10 tentativas, o jogo exibirá o número de acertos e o tempo médio de reação.

## Instalação

### Pré-requisitos

- **Python 3.x** deve estar instalado.
- Instalar a biblioteca `pygame`. Para isso, execute:

```bash
pip install pygame
```

### Como Rodar

1. Faça o clone ou o download deste repositório.
2. No diretório do projeto, execute o arquivo `main.py`:

```bash
python main.py
```

## Estrutura do Código

- **Cores**: O jogo define quatro cores principais, associadas às teclas de setas (UP, DOWN, LEFT, RIGHT).
- **Teclas-Cores**: Há um dicionário que mapeia cada tecla para a respectiva cor.
- **Tela de Instruções**: Ao iniciar, uma tela com instruções é exibida, e o jogo só começa quando uma tecla é pressionada.
- **Jogo Principal**: O círculo aparece em posições aleatórias da tela. O tempo de reação é contado desde o momento que o círculo surge até o jogador pressionar uma tecla.
- **Resultados**: Ao final das 10 tentativas, o jogo exibe a média do tempo de reação e o número de acertos.

---

<p align="center">
  Feito com ♥ by Quelita Míriam :wave:
</p>
