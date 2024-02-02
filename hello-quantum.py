# Nota: TAD = Tipo Abstrato de Dados

'''
TAD: celula
Para o tipo celula foi escolhida a seguinte representacao:
[val]
em que "val" representa o valor da celula (-1, 0 ou 1).
Operacoes basicas do tipo celula: 
-Construtor: cria_celula
-Seletor: obter_valor
-Modificador: inverte_estado
-Reconhecedor: eh_celula
-Teste: celulas_iguais
-Transformador: celula_para_str
'''

def cria_celula(val):
      """cria_celula: {-1,0,1} -> celula
      Funcao que cria uma celula com o valor que lhe foi introduzido."""
      if (val != -1 and val != 0 and val != 1) or type(val) != int:
            raise ValueError('cria_celula: argumento invalido.')
      return [val]

def obter_valor(cel):
      """obter_valor: celula -> {-1,0,1}
      Funcao que indica qual o valor da celula que lhe foi introduzida."""
      return cel[0]

def inverte_estado(cel):
      """inverte_estado: celula -> celula
      Funcao que devolve uma celula com o valor "inverso" ao da celula introduzida,
      mantendo valores de incerteza (-1) e invertendo os valores zero e um para
      um e zero, respetivamente."""
      cel.append(-1) if cel == [-1] else (cel.append(1) if cel == [0] else cel.append(0))
      del cel[0]
      return cel

def eh_celula(arg):
      """eh_celula: universal -> boolean
      Funcao que indica se o argumento que lhe foi fornecido e uma celula do
      jogo Hello Quantum."""
      return (arg == [-1] or arg == [0] or arg == [1]) and type(arg[0]) == int

def celulas_iguais(cel1, cel2):
      """celulas_iguais: celula x celula -> boolean
      Funcao que indica se as celulas que lhe sao introduzidas sao iguais (True)
      ou nao (False)."""
      return eh_celula(cel1) and eh_celula(cel2) and cel1 == cel2

def celula_para_str(cel):
      """celula_para_str: celula -> {'x','0','1'}
      Funcao que devolve uma string com o valor da celula que lhe foi introduzida.
      Estados incertos representam-se por 'x'."""
      return str(obter_valor(cel)) if obter_valor(cel) == 0 or obter_valor(cel) == 1 else 'x'


'''
TAD: coordenada
Para o tipo coordenada foi escolhida a seguinte representacao:
(l, c)
em que "l" representa a linha e "c" a coluna do tabuleiro que a coordenada
assinala. "l" e "c" podem assumir os valores 0, 1 ou 2, nao existindo a 
coordenada (2, 0) no jogo (Hello Quantum).
Operacoes basicas do tipo coordenada:
-Construtor: cria_coordenada
-Seletores: coordenada_linha, coordenada_coluna
-Reconhecedor: eh_coordenada
-Teste: coordenadas_iguais
-Transformador: coordenada_para_str
'''


def cria_coordenada(linha,col):
      """cria_coordenada: {0,1,2} x {0,1,2} -> coordenada
      Funcao que cria uma coordenada do tabuleiro do Jogo Hello Quantum
      coorrespondente a linha (1o argumento) e a coluna (2o argumento) que
      lhe sao fornecidas."""
      if linha not in [0,1,2] or col not in [0,1,2] or (linha,col) == (2,0) \
      or type(linha) != int or type(col) != int:
            raise ValueError('cria_coordenada: argumentos invalidos.') 
      return (linha,col)

def coordenada_linha(coor):
      """coordenada_linha: coordenada -> {0,1,2}
      Funcao que devolve o numero da linha da posicao que a coordenada assinala."""
      return coor[0]

def coordenada_coluna(coor):
      """coordenada_coluna: coordenada -> {0,1,2}
      Funcao que devolve o numero da coluna da posicao que a coordenada assinala."""
      return coor[1]

def eh_coordenada(arg):
      """eh_coordenada: universal -> boolean
      Funcao que indica se o argumento introduzido e uma coordenada valida
      de um tabuleiro do jogo Hello Quantum."""
      return type(arg) == tuple and len(arg) == 2 and arg[0] in \
             [0,1,2] and arg[1] in [0,1,2] and type(arg[0]) == int \
             and type(arg[1]) == int

def coordenadas_iguais(coor1,coor2):
      """coordenadas_iguais: coordenada x coordenada -> boolean
      Funcao que indica se as coordenadas que lhe sao introduzidas sao iguais 
      (True) ou nao (False). """
      return eh_coordenada(coor1) and eh_coordenada(coor2) and coor1 == coor2

def coordenada_para_str(coor):
      """coordenada_para_str: coordenada -> str
      Funcao que devolve uma string com a coordenada (em notacao matematica)
      que lhe foi fornecida."""
      return str((coordenada_linha(coor),coordenada_coluna(coor)))


'''
TAD: tabuleiro
Para o tipo tabuleiro foi escolhida a seguinte representacao:
[[[cel,cel,cel], [cel,cel,cel], [cel,cel]]
em que cada "cel" representa cada celula do tabuleiro, por ordem crescente do
seu numero de coluna, e cada sub-lista do tabuleiro (que, por sua vez, e a 
lista maior) representa as suas linhas, por ordem crescente tambem.
Operacoes basicas do tipo tabuleiro:
-Construtores: tabuleiro_inicial, str_para_tabuleiro
-Seletores: tabuleiro_dimensao, tabuleiro_celula
-Modificadores: tabuleiro_substitui_celula, tabuleiro_inverte_estado
-Reconhecedor: eh_tabuleiro
-Teste: tabuleiros_iguais
-Transformador: tabuleiro_para_str
As operacoes de alto nivel associadas do tipo tabuleiro sao: porta_x, porta_z, 
porta_h.
'''


def tabuleiro_inicial():
      """tabuleiro_inicial: {} -> tabuleiro
      Funcao que devolve o tabuleiro inicial do jogo Hello Quantum."""
      return [[cria_celula(-1),cria_celula(-1),cria_celula(-1)], \
              [cria_celula(0),cria_celula(0),cria_celula(-1)], \
              [cria_celula(0),cria_celula(-1)]]

def str_para_tabuleiro(st):
      """str_para_tabuleiro: str -> tabuleiro
      Funcao que devolve o tabuleiro representado pela string que lhe foi fornecida,
      sendo que esta utiliza a representacao dos tabuleiros utilizada no primeiro
      projeto."""
      if type(st) != str or type(eval(st)) != tuple or len(eval(st)[0]) != 3 or not\
         (type(eval(st)[linha]) == tuple for linha in range(3)) or not\
         (len(eval(st)[linha]) == 3 for linha in [0,1]) or len(eval(st)[2]) != 2 or not\
         (eval(st)[linha][numero] in [-1,0,1] and type(eval(st)[linha][numero]) == int \
          for linha in range(3) for numero in range(len(eval(st)[linha]))):
            raise ValueError('str_para_tabuleiro: argumento invalido.')
      
      return [[cria_celula(eval(st)[0][0]), cria_celula(eval(st)[0][1]), cria_celula(eval(st)[0][2])], \
              [cria_celula(eval(st)[1][0]), cria_celula(eval(st)[1][1]), cria_celula(eval(st)[1][2])], \
              [cria_celula(eval(st)[2][0]), cria_celula(eval(st)[2][1])]]

def tabuleiro_dimensao(tab):
      """tabuleiro_dimensao: tabuleiro -> {3}
      Funcao que retorna a dimensao do tabuleiro que lhe foi fornecido (e sempre igual a 3)."""
      return 3

def tabuleiro_celula(tab, coor):
      """tabuleiro_celula: tabuleiro x coordenada -> celula
      Funcao que retorna a celula que esta presente numa coordenada e num tabuleiro
      especificos, sendo estes os seus argumentos."""
      return tab[coordenada_linha(coor)][coordenada_coluna(coor)] \
             if coordenada_linha(coor) in [0,1] else \
             tab[2][coordenada_coluna(coor) - 1]

def tabuleiro_substitui_celula(tab, cel, coor):
      """tabuleiro_substitui_celula: tabuleiro x celula x coordenada -> tabuleiro
      Funcao que retorna o tabuleiro que lhe foi fornecido, substituindo-lhe a
      celula presente na coordenada fornecida, pela celula que lhe foi introduzida."""
      if not (eh_tabuleiro(tab) and eh_celula(cel) and eh_coordenada(coor)):
            raise ValueError('tabuleiro_substitui_celula: argumentos invalidos.')
      if coordenada_linha(coor) in [0,1]:
            ajuste = 0
      else:
            ajuste = 1
      tab[coordenada_linha(coor)][coordenada_coluna(coor)-ajuste] = cel           
      return tab

def tabuleiro_inverte_estado(tab, coor):
      """tabuleiro_inverte_estado: tabuleiro x coordenada -> tabuleiro
      Funcao que retorna o tabuleiro que lhe foi fornecido, com o valor da celula
      presente na coordenada que lhe e introduzida invertido."""
      if not (eh_tabuleiro(tab) and eh_coordenada(coor)):
            raise ValueError('tabuleiro_inverte_estado: argumentos invalidos.')
      if coordenada_linha(coor) in [0,1]:
            ajuste = 0
      else:
            ajuste = 1
      tab[coordenada_linha(coor)][coordenada_coluna(coor)-ajuste] = \
      inverte_estado(tab[coordenada_linha(coor)][coordenada_coluna(coor)-ajuste])            
      return tab

def eh_tabuleiro(arg):
      """eh_tabuleiro: universal -> boolean
      Funcao que indica se o argumento introduzido e um tabuleiro valido do 
      jogo Hello Quantum."""
      return type(arg) == list and len(arg) == 3 and all(type(e) == list for e in arg) \
             and all(len(arg[e]) == 3 for e in [0,1]) and len(arg[2]) == 2 \
             and all(eh_celula(arg[linha][cel]) for linha in range(3) \
                     for cel in range(len(arg[linha])))

def tabuleiros_iguais(t1, t2):
      return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2

def tabuleiro_para_str(tab):
      """tabuleiro_para_str: tabuleiro -> str
      Funcao que devolve uma representacao, na forma de string, do tabuleiro que 
      lhe foi fornecido."""
      def aux(tab, coor): #Funcao que serve como abreviatura de "obter_valor de tabuleiro_celula"
            return obter_valor(tabuleiro_celula(tab, coor))
      st =  '+-------+\n'
      st += '|...{}...|\n'.format(aux(tab, cria_coordenada(0,2)))
      st += '|..{}.{}..|\n'.format(aux(tab, cria_coordenada(0,1)), aux(tab, cria_coordenada(1,2)))
      st += '|.{}.{}.{}.|\n'.format(aux(tab, cria_coordenada(0,0)),aux(tab, cria_coordenada(1,1)), aux(tab, cria_coordenada(2,2)))
      st += '|..{}.{}..|\n'.format(aux(tab, cria_coordenada(1,0)), aux(tab, cria_coordenada(2,1)))
      st += '+-------+'
      return st.replace('-1', 'x')

def t_i_e(tab, coor):
      """t_i_e: tabuleiro x coordenada -> tabuleiro
      A funcao "t_i_e" e utilizada pelas funcoes das portas x e z, como 
      abreviatura da expressao "tabuleiro_inverte_estado". Serve apenas para 
      melhorar a legibilidade do codigo."""      
      return tabuleiro_inverte_estado(tab,coor)

def porta_x(tab, side):
      """porta_x: tabuleiro x {'E','D'} -> tabuleiro
      Funcao que retorna o tabuleiro introduzido, com a aplicacao da porta X ao
      lado Esquerdo ou Direito deste, conforme lhe e especificado."""
      if not (eh_tabuleiro(tab) and side in ['E','D']):
            raise ValueError('porta_x: argumentos invalidos.')
      return t_i_e(t_i_e(t_i_e(tab, cria_coordenada(1,2)), cria_coordenada(1,1)), \
                   cria_coordenada(1,0)) if side == 'E' else \
             t_i_e(t_i_e(t_i_e(tab, cria_coordenada(0,1)), cria_coordenada(1,1)), \
                   cria_coordenada(2,1))

def porta_z(tab, side):
      """porta_z: tabuleiro x {'E','D'} -> tabuleiro
      Funcao que retorna o tabuleiro introduzido, com a aplicacao da porta Z ao
      lado Esquerdo ou Direito deste, conforme lhe e especificado."""
      if not (eh_tabuleiro(tab) and side in ['E','D']):
            raise ValueError('porta_z: argumentos invalidos.')
      return t_i_e(t_i_e(t_i_e(tab, cria_coordenada(0,2)), cria_coordenada(0,1)), \
                   cria_coordenada(0,0)) if side == 'E' else \
             t_i_e(t_i_e(t_i_e(tab, cria_coordenada(0,2)), cria_coordenada(1,2)), \
                   cria_coordenada(2,2))

def porta_h(tab, side):
      """porta_h: tabuleiro x {'E','D'} -> tabuleiro
      Funcao que retorna o tabuleiro introduzido, com a aplicacao da porta H ao
      lado Esquerdo ou Direito deste, conforme lhe e especificado."""
      if not (eh_tabuleiro(tab) and side in ['E','D']):
            raise ValueError('porta_h: argumentos invalidos.')
      
      def t_s_c(tab, cel, coor):
            """t_s_c: tabuleiro x celula x coordenada -> tabuleiro
            A funcao "t_s_c" e utilizada pela funcao da porta h, como 
            abreviatura da expressao "tabuleiro_substitui_celula". Serve apenas 
            para melhorar a legibilidade do codigo.""" 
            return tabuleiro_substitui_celula(tab, cel, coor)

      c1 = tabuleiro_celula(tab, cria_coordenada(0,0))
      c2 = tabuleiro_celula(tab, cria_coordenada(0,1))
      c3 = tabuleiro_celula(tab, cria_coordenada(0,2))
      c4 = tabuleiro_celula(tab, cria_coordenada(1,0))
      c5 = tabuleiro_celula(tab, cria_coordenada(1,1))
      c6 = tabuleiro_celula(tab, cria_coordenada(1,2))
      c7 = tabuleiro_celula(tab, cria_coordenada(2,1))
      c8 = tabuleiro_celula(tab, cria_coordenada(2,2))
      
      if side == 'E':
            #Para reescrever a linha 0 do tabuleiro:
            t_s_c(tab, c4, cria_coordenada(0,0))
            t_s_c(tab, c5, cria_coordenada(0,1))
            t_s_c(tab, c6, cria_coordenada(0,2))
            #Para reescrever a linha 1 do tabuleiro:
            t_s_c(tab, c1, cria_coordenada(1,0))
            t_s_c(tab, c2, cria_coordenada(1,1))
            t_s_c(tab, c3, cria_coordenada(1,2))
      else:
      #Para reescrever a coluna 1 do tabuleiro:
            t_s_c(tab, c3, cria_coordenada(0,1))
            t_s_c(tab, c6, cria_coordenada(1,1))
            t_s_c(tab, c8, cria_coordenada(2,1))
      #Para reescrever a coluna 2 do tabuleiro:
            t_s_c(tab, c2, cria_coordenada(0,2))
            t_s_c(tab, c5, cria_coordenada(1,2))
            t_s_c(tab, c7, cria_coordenada(2,2))
      return tab

def hello_quantum(string):
      """hello_quantum: str -> boolean
      Funcao que permite jogar um jogo de Hello Quantum, aceitando um tabuleiro
      objetivo e um numero maximo de jogadas, e devolvendo True se o jogador
      alcanca esse tabuleiro nao ultrapassando o numero de jogadas estabelecido,
      ou False caso contrario. O jogo acaba se o jogador ultrapassar esse numero
      limite de jogadas."""
      tab_objetivo, jogadas_objetivo = string.split(':')
      print('Bem-vindo ao Hello Quantum!\nO seu objetivo e chegar ao tabuleiro:')
      print(tabuleiro_para_str(str_para_tabuleiro(tab_objetivo)))
      print('Comecando com o tabuleiro que se segue:')
      print(tabuleiro_para_str(tabuleiro_inicial()))

      jogadas_feitas = 0
      tab = tabuleiro_inicial()
      while tab != str_para_tabuleiro(tab_objetivo) and jogadas_feitas < eval(jogadas_objetivo):
            porta = str(input('Escolha uma porta para aplicar (X, Z ou H): '))
            side = str(input('Escolha um qubit para analisar (E ou D): '))
            porta_x(tab, side) if porta == 'X' else (porta_z(tab, side) \
            if porta == 'Z' else porta_h(tab, side))
            print(tabuleiro_para_str(tab))
            jogadas_feitas += 1
            
      if tabuleiros_iguais(tab, str_para_tabuleiro(tab_objetivo)):
            print('Parabens, conseguiu converter o tabuleiro em' , jogadas_feitas, 'jogadas!') 
      return jogadas_feitas <= int(jogadas_objetivo)
      