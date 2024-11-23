import random
import curses

# Inicialização do terminal
screen = curses.initscr()
altura, largura = screen.getmaxyx()
janela = curses.newwin(altura, largura, 0, 0)

# Configurações iniciais
curses.curs_set(False)
janela.keypad(True)
janela.nodelay(True)

# Desenhar bordas
for pos in range(0, largura - 1):
    janela.addch(0, pos, '#')
    janela.addch(altura - 1, pos, '#')

for pos in range(0, altura - 1):
    janela.addch(pos, 0, '#')
    janela.addch(pos, largura - 1, '#')

# Configuração inicial da cobra
cobra = [[2, 4], [2, 3], [2, 2]]
for segmento in cobra:
    janela.addch(segmento[0], segmento[1], '#')

posicao_cabeca = [2, 4]

# Configuração inicial da maçã
maca = [5, 5]
janela.addch(maca[0], maca[1], '*')

# Configurações de controle
tecla = -1
tecla_nova = curses.KEY_RIGHT
ultima_posicao = 'r'

# Pontuação e velocidade
pontuacao = 0
velocidade_movimento = 100

# Loop principal
while True:
    tecla_nova = janela.getch()
    tecla = tecla if tecla_nova == -1 else tecla_nova

    # Controle de direção
    if tecla == curses.KEY_DOWN and ultima_posicao != 'u':
        ultima_posicao = 'd'
    elif tecla == curses.KEY_UP and ultima_posicao != 'd':
        ultima_posicao = 'u'
    elif tecla == curses.KEY_LEFT and ultima_posicao != 'r':
        ultima_posicao = 'l'
    elif tecla == curses.KEY_RIGHT and ultima_posicao != 'l':
        ultima_posicao = 'r'

    # Movimentação da cobra
    if ultima_posicao == 'r':
        posicao_cabeca[1] += 1
    elif ultima_posicao == 'l':
        posicao_cabeca[1] -= 1
    elif ultima_posicao == 'u':
        posicao_cabeca[0] -= 1
    elif ultima_posicao == 'd':
        posicao_cabeca[0] += 1

    # Verifica colisão com a maçã
    if posicao_cabeca == maca:
        pontuacao += 1
        maca = [random.randint(1, altura - 2), random.randint(1, largura - 2)]
        janela.addch(maca[0], maca[1], '*')
        velocidade_movimento = max(5, velocidade_movimento - 10)
    # Verifica colisão com as bordas ou com o próprio corpo
    elif (
        posicao_cabeca[0] == 0 or posicao_cabeca[0] == altura - 1 or
        posicao_cabeca[1] == 0 or posicao_cabeca[1] == largura - 1 or
        posicao_cabeca in cobra
    ):
        break
    else:
        # Remove a cauda da cobra
        cauda = cobra.pop()
        janela.addch(cauda[0], cauda[1], ' ')

    # Atualiza a posição da cobra
    cobra.insert(0, list(posicao_cabeca))
    janela.addch(posicao_cabeca[0], posicao_cabeca[1], '#')

    # Atualiza a tela
    curses.napms(velocidade_movimento)
    janela.refresh()

# Exibir a pontuação final
janela.addnstr(int(altura / 2), int(largura / 2.5), f"Pontuação: {pontuacao}")
janela.refresh()
curses.napms(2000)
curses.endwin()
