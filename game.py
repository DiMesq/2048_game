import random


def cria_coordenada(l, c):
    '''l: int, com valor compreendido entre 1 e 4 (inclusive)  
       c: int, com valor compreendido entre 1 e 4 (inclusive)
       retorna: tipo coordenada, tipo com duas entradas em que a primeira e l 
       (corresponde a linha do tabuleiro de uma certa posicao) e a segunda e 
       c (coluna)'''
    
    if isinstance(l, int) and isinstance(c, int) and 0<l<5 and 0<c<5:
        return (l, c)
    
    raise ValueError ("cria_coordenada: argumentos invalidos")

def coordenada_linha(coord):
    '''coord: coordenada, que define uma posicao no tabuleiro 4x4
       retorna: int, a linha do tabuleiro correspondente a posicao coord'''
    
    return coord[0]

def coordenada_coluna(coord):
    '''coord: coordenada, que define uma posicao no tabuleiro 4x4
       retorna: int, a coluna do tabuleiro correspondente a posicao coord'''
    
    return coord[1]

def e_coordenada(coord):
    '''coord: universal
       retorna: Bool, True caso coord seja do tipo coordenada e False caso
       contrario'''
    
    return isinstance(coord, tuple) and len(coord) == 2 and \
           isinstance(coord[0], int) and isinstance(coord[1], int) and \
           0<coord[0]<5 and 0<coord[1]<5

def coordenadas_iguais(coord1, coord2):
    '''coord1: coordenada
       coord2: coordenada9
       retorna: Bool, True caso coord1 e coord2 definam a mesma posicao no 
       tabuleiro e False caso contrario'''
    
    return coord1[0] == coord2[0] and coord1[1] == coord2[1]


def cria_tabuleiro():
    '''retorna: tipo tabuleiro, corresponde as posicoes de um tabuleiro 4x4, 
       onde todas contem o valor 0, e a uma pontuacao total, tambem com o valor 
       0'''
    
    tab = {}
    tab['totalScore'] = 0
    
    for lin in range(1,5):
        for col in range(1,5):
            tab[cria_coordenada(lin, col)] = 0
    return tab

def tabuleiro_posicao(tab, coord):
    '''tab: tabuleiro
       coord: coordenada
       retorna: int, valor coorrespondente a pontuacao na posicao do tabuleiro 
       tab definida pelas coordenadas coord'''
    
    if e_coordenada(coord):
        return tab[coord]
    
    raise ValueError ("tabuleiro_posicao:  argumentos invalidos")
    
    
def tabuleiro_pontuacao(tab):
    '''tab: tabuleiro
       retorna: int, correspondente a pontuacao total do tabuleiro'''
    
    return tab['totalScore']


def tabuleiro_posicoes_vazias(tab):
    '''tab: tabuleiro
       retorna: list, contendo as coordenadas de todas as posicoes vazias do 
       tabuleiro tab'''
    
    lst = []
    
    for c in tab:
        if tab[c] == 0 and c != 'totalScore':
            lst.append(c)
    return lst


def tabuleiro_preenche_posicao(tab, coord, v):
    '''tab: tabuleiro
       coord: coordenada
       valor: int
       retorna: tabuleiro, correspondente ao tab modificado, com o valor v
       colocado na posicao definida pelas coordenadas coord'''
    
    if e_coordenada(coord) and isinstance(v, int):
        
        tab[coord] = v
        return tab 
    
    raise ValueError ("tabuleiro_preenche_posicao: argumentos invalidos")
    


def tabuleiro_actualiza_pontuacao(tab, v):
    '''tab: tabuleiro
       v: int, que devera ser nao negativo e multiplo de 4
       retorna: tabuleiro, tabuleiro tab com a pontuacao respetiva acrescentada 
       v pontos'''
    
    if isinstance(v, int) and v >= 0 and v%4 == 0:
        
        tab['totalScore'] += v
        return tab
    
    raise ValueError ("tabuleiro_actualiza_pontuacao: argumentos invalidos")

def reduz_coluna(tab, d, coluna):
    '''coluna: int, numero da coluna que quero reduzir
       retorna: tabuleiro, com a coluna reduzida'''
        
    flag = True
        
    if d == 'S':
        valorMax = 0
        valorMin = 3
        step = -1
    else:
        valorMax = 5
        valorMin = 2
        step = 1        
            
    for i in range(valorMin, valorMax, step):
            
        P_a_mover = cria_coordenada(i, coluna)
        valor_a_mover = tabuleiro_posicao(tab, P_a_mover)
                
        if valor_a_mover == 0:
            continue
                
        for k in range(valorMin - step, valorMax - step, step): 
                
            if k == i:
                break
                
            P_hipotese = cria_coordenada(k, coluna)
            valor_hipotese = tabuleiro_posicao(tab, P_hipotese)
                    
            if valor_hipotese == 0:
                tab = tabuleiro_preenche_posicao(tab, P_hipotese, \
                                                     valor_a_mover)
                                        
                tab = tabuleiro_preenche_posicao(tab, P_a_mover, 0)
                break                
                
            if k+step != i and tabuleiro_posicao(tab, cria_coordenada\
                                                     (k+step, coluna)) != 0:
                continue
                        
            if flag == True and \
                valor_a_mover == valor_hipotese:
                flag = False
                        
                soma = valor_a_mover + valor_hipotese
                tab = tabuleiro_preenche_posicao(tab, P_hipotese, \
                                                         soma)
                tab = tabuleiro_actualiza_pontuacao(tab, soma) 
                tab = tabuleiro_preenche_posicao(tab, P_a_mover,0)
                break
                        
            elif flag == False:
                flag = True
                        
                    
    return tab
    

def reduz_linha(tab, d, linha):
    '''linha: int, numero da linha que quero reduzir 
        retorna: tabuleiro, com a linha reduzida'''
    
    flag = True
    
    if d == 'E':
        valorMax = 0
        valorMin = 3
        step = -1
    else:
        valorMax = 5
        valorMin = 2
        step = 1        
            
    for i in range(valorMin, valorMax, step):
            
        P_a_mover = cria_coordenada(linha, i)
        valor_a_mover = tabuleiro_posicao(tab, P_a_mover)
                
        if valor_a_mover == 0:
            continue
            
        for k in range(valorMin - step, i, step): 
                
            P_hipotese = cria_coordenada(linha, k)
            valor_hipotese = tabuleiro_posicao(tab, P_hipotese)
                
            if valor_hipotese == 0:
                tab = tabuleiro_preenche_posicao(tab, P_hipotese, \
                                                     valor_a_mover)
                                            
                tab = tabuleiro_preenche_posicao(tab, P_a_mover, 0)
                break                    
                    
            if k+step != i and tabuleiro_posicao(tab, cria_coordenada\
                                                     (linha, k+step)) != 0:
                continue
                    
            if flag == True and valor_a_mover == valor_hipotese:
                    
                flag = False
                        
                soma = valor_a_mover + valor_hipotese
                tab = tabuleiro_preenche_posicao(tab, P_hipotese, \
                                                         soma)
                tab = tabuleiro_actualiza_pontuacao(tab, soma) 
                tab = tabuleiro_preenche_posicao(tab, P_a_mover,0)
                break
                        
            elif flag == False:
                flag = True
                        
                    
    return tab


def tabuleiro_reduz(tab, d):
    '''tab: tabuleiro 
       d: str, em particular deve ser: 'N', 'S', 'W', ou 'E'
       retorna: tabuleiro, tab modificado (reduzido na direcao d e pontuacao 
       atualizada)'''
    
    if d in ('N', 'S', 'W', 'E'):
        
        if d in ('W', 'E'):
            for lin in range(1, 5):
                tab = reduz_linha(tab, d, lin)
            return tab
    
        for col in range(1, 5):
            tab = reduz_coluna(tab, d, col)
        return tab
    
    raise ValueError ("tabuleiro_reduz:  argumentos invalidos") 


def e_tabuleiro(tab):
    '''tab: universal
       retorna: Bool, True caso tab seja do tipo tabuleiro e False caso
       contrario'''
    
    if isinstance(tab, dict) : 
        for key in tab:
            if key != 'totalScore':
                
                if not (e_coordenada(key) and tab[key] >= 0 and \
                        tab[key]%2 == 0):
                    
                    return False
            
        return tabuleiro_pontuacao(tab)%4 == 0
    
    return False


def tabuleiro_terminado(tab):
    '''tab: tabuleiro
       retorna: Bool, True caso o tabuleiro tab esteja terminado (nao existam
       movimentos possiveis) e False em caso contrario'''
    
    if tabuleiro_posicoes_vazias(tab) != []:
        return False
    
    for d in ('N', 'S', 'E', 'W'):
        
        tab_mod = tab.copy()
        if not tabuleiros_iguais(tabuleiro_reduz(tab_mod, d), tab):
            return False
        
    return True

def tabuleiros_iguais(tab1, tab2):
    '''tab1: tabuleiro
       tab2: tabuleiro
       retorna: Bool, True caso tab1 e tab2 tenham a mesma configuracao e a 
       mesma pontuacao'''
    
    return tab1 == tab2


def escreve_tabuleiro(tab):
    '''tab: tabuleiro 
       retorna: nao retorna nada. Apenas faz print para o ecra a representacao
       externa de um tabuleiro de 2048'''
    
    if e_tabuleiro(tab):
        
        for lin in range(1,5):
            for col in range(1,5):
                
                if col != 4:
                    end = ''
                else:
                    end = '\n'
                    
                print ('[ ' + str(tabuleiro_posicao\
                                  (tab, cria_coordenada(lin, col))) + ' ] ',\
                       end = end)                    
                    
        print('Pontuacao: ' + str(tabuleiro_pontuacao(tab)))
        return 
        
    raise ValueError ("escreve_tabuleiro:  argumentos invalidos")
    
    
def pede_jogada():
    '''pede_jogada pede uma direcao (N, S, E ou W) ao utilizador 
       retorna: str, correspondente a direcao escolhida'''
   
    d = input('Introduza uma jogada (N, S, E, W): ')
    
    while not (d in ('N', 'S', 'W', 'E')):
        print('Jogada invalida.')
        d = input('Introduza uma jogada (N, S, E, W): ')
        
    return d

def preenche_posicao_aleatoria(tab):
    '''tab: tabuleiro
       retorna: tabuleiro, corresponde ao tab acrescentado de um 2 ou um 4 numa
       das posicoes vazias. Sera acrescentado um 2 oitenta por cento das vezes
       e um 4 das restantes vezes'''
    
    posVazias = tabuleiro_posicoes_vazias(tab)
    
    tab = tabuleiro_preenche_posicao(tab, random.choice(posVazias), \
                                     random.choice([2, 2, 2, 2, 4]))
    return tab

def copia_tabuleiro(tab):
    '''tab: tabuleiro
       retorna: tabuleiro, copia do tabuleiro tab'''
    
    tab_copy = cria_tabuleiro()
    tab_copy = tabuleiro_actualiza_pontuacao(tab_copy, tabuleiro_pontuacao(tab))
    
    for lin in range(1,5):
        for col in range(1,5):
            c = cria_coordenada(lin, col)
            tab_copy = tabuleiro_preenche_posicao(tab_copy, c, \
                                                  tabuleiro_posicao(tab, c))
            
    return tab_copy
    

def jogo_2048():
    '''Permite a um utilizador jogar o jogo 2048'''
    
    
    tab = preenche_posicao_aleatoria(cria_tabuleiro())
    escreve_tabuleiro(tab)
   
    while not tabuleiro_terminado(tab):
        
        tab_copia = copia_tabuleiro(tab)
        d = pede_jogada() 
        
        while tabuleiros_iguais(tab_copia, tabuleiro_reduz(tab, d)):
            
            print('Jogada invalida.')
            d = pede_jogada()
            tab = tabuleiro_reduz(tab, d)
            
        else:
            tab = preenche_posicao_aleatoria(tab)
            escreve_tabuleiro(tab)
    return
        
        
        
    
       
        
   
    
        
        
        
    
    
    
    
    
    
    
    

    
        
        
       


