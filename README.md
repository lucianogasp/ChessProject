Este projeto é dedicado a desenvolver a lógica do jogo de xadrez em python, com planos futuros de implementar funcionalidades de frontend entre outras tecnologias para construir um aplicativo completo de xadrez.
Também tenho como objetivo tornar o backend versátil e independente o suficiente para que possa ser reutilizado no desenvolvimento de programas semelhantes como, por exemplo, outros jogos de tabuleiro.


>>> Disclaimer:

Como sou iniciante na programação e nunca tive experiência profissional, espero que compreendam os diversos erros e imprecisões cometidos ao longo do desenvolvimento desse meu projeto pessoal. É a primeira vez que trabalho num projeto tão grande como esse, também é minha primeira vez programando em POO. Sintam-se livres para levantar críticas a fim de melhorar o desenvolvimento do mesmo e realizar pull requests.


>>> Conteúdo de Apoio:

-> Notação algébrica de xadrez: https://pt.wikipedia.org/wiki/Nota%C3%A7%C3%A3o_alg%C3%A9brica_de_xadrez
-> Notação FEN de xadrez: https://pt.wikipedia.org/wiki/Nota%C3%A7%C3%A3o_Forsyth-Edwards#:~:text=Nota%C3%A7%C3%A3o%20Forsyth%2DEdwards%20ou%20FEN,para%20o%20uso%20em%20computadores.
-> Regras do xadrez (FIDE) (pdf): https://arbiters.fide.com/wp-content/uploads/Publications/VariousContributions/20230101-FIDE_Laws_2023-POR.pdf


>>> Como funciona:

    Versões

Atualmente o projeto teve duas versões principais. A versão 1.0 foi construída usando duas funções no formato de programação em script, onde a função chess_move() era responsável por realizar um único movimento de cada lance e a função chess_play() era responsável por inicializar o jogo e as variáveis necessárias para a realização dos movimentos, incluindo uma estrutura em loop para a chamada de chess_move().

A versão 2.0 (mais atualizada), e suas subversões derivadas, foram construídas com base no paradigma de programação orientada a objetos, facilitando muito no desenvolvimento do código e me fazendo perceber que programar todo um sistema complexo como esse em um único script é simplesmente loucura.

    Input

A dinâmica do sistema consiste em um loop que realiza um input para cada movimento, a entrada é um movimento de xadrez no formato algébrico oficial determinado pela FIDE (Federação Internacional de Xadrez). Além disso, esse mesmo input deve atuar como interface de usuário, onde comandos específicos possam ser lidos nesta entrada e realizar algumas funcionalidades como apresentar o histórico de movimentos realizados, apresentar a notação fen atual, entre outros, incluindo sair ou reiniciar o sistema.
(ver Notação algébrica de xadrez)

    Tabuleiro

O "core" do projeto, julgo eu, é como fazer o python entender o tabuleiro.
O tabuleiro é definido por uma matriz onde cada valor da matriz representa a presença ou ausência de uma peça específica e cada posição da matriz uma casa no xadrez. Cada sublista da matriz é uma coluna e cada index de uma sublista é uma linha. Assim, a casa da primeira coluna da primeira linha, ou 'matriz[0][0]', é a casa 'a1', e de forma análoga, a casa da oitava coluna da oitava linha, ou 'matriz[7][7]', é a casa 'h8'.

    Peças

Os valores da matriz são interpretados pelo programa como uma string. As peças no tabuleiro através da primeira letra do nome de cada uma, sendo maiúscula para peças brancas e minúiscula para peças pretas. As casas vazias pela string '_'.
No input, onde a notação algébrica do lance é utilizada, as peças são sempre referidas com a primeira letra do nome, maiúscula, com exceção do peão que é omitido da notação.
(ver Notação algébrica de xadrez)

Exemplo:

matriz = [
    ['T', 'P', '_', '_', '_', '_', 'p', 't'],
    ['C', 'P', '_', '_', '_', '_', 'p', 'c'],
    ['B', 'P', '_', '_', '_', '_', 'p', 'b'],
    ['D', 'P', '_', '_', '_', '_', 'p', 'd'],
    ['R', 'P', '_', '_', '_', '_', 'p', 'r'],
    ['B', 'P', '_', '_', '_', '_', 'p', 'b'],
    ['C', 'P', '_', '_', '_', '_', 'p', 'c'],
    ['T', 'P', '_', '_', '_', '_', 'p', 't'],
]

    Notação FEN

A notação fen, ou Forsyth-Edwards Notation, no contexto do jogo de xadrez é um tipo de codificação que descreve como está a posição do jogo. O arranjo das peças em relação ao tabuleiro, a cor que tem a vez no lance, as possibilidades da execução dos movimentos de roque, a possibilidade da execução do movimento 'en passant', o valor 'half move clock' indicando um empate pela regra dos 50 lances e a quantidade de lances realizados são informações explícitas na notação fen, que são atualizadas a cada movimento.
(ver Notação FEN de xadrez)
Esta notação será armazenada como atributo de classe do programa como uma variável do tipo dicionário, onde cada chave representará uma informação diferente da notação.

    Regex

Para validar os inputs do usuário no formato algébrico da notação oficial dos lances de xadrez, um mecanismo de expressão regular foi implementado.
Inicialmente o input passa por uma validação mais genérica, através de um padrão 'regex_generic', que garantirá uma sintaxe correta. Então, uma segunda avaliação sobre coerência e coesão dos valores do input é aplicada através de um padrão 'regex_context' ou de simples blocos de código com tratamentos de exceção. Esta necessita uma análise sobre o contexto, ou seja, sobre o estado atual das variáveis presentes na matriz do tabuleiro, na notação fen e até nos próprios valores do input.
Se o input não passar pela validação o programa executará um 'raise Exception' indicando um erro na formatação.

Por exemplo: O lance 'K&fgh35-lYm' não possui sintaxe adequada para o regex_generic. Já o lance 'Cbxf8=D' possui sintaxe adequada, mas sem coerência nem coesão, pois um lance de Cavalo como este não pode promover Dama, nem conseguir saltar para um casa tão distante do tabuleiro, e ainda precisaríamos verificar o tabuleiro para garantir que o caracter 'x', expressando captura, foi corretamente utilizado.
(ver Notação algébrica de xadrez)

O 'regex_generic' assume um padrão de entrada do seguinte tipo:

                       | Nome da peça | CRV | Captura | CRD | Especial 1 | Especial 2 |
Exemplo A: Cc3xe2+     | C            | c3  | x       | e2  |            | +          |
Exemplo B: Te1         | T            |     |         | e1  |            |            |
Exemplo C: e8=D#       |              |     |         | e8  | =D         | #          |
Exemplo D: cxd5++      |              | c   | x       | d5  |            | ++         |

*Opcional / Obrigatório| Opc          | Opc | Opc     | Obr | Opc        | Opc        |

Padrão do regex_generic: rf'^(?:[{piece_names}][a-h]?[1-8]?x?|[a-h]x)?[a-h][1-8](?:=[A-Z])?(?:\+|\+\+|#)?$'

O padrão dessa expressão regular envolve uma 'raw/f-string', necessária para incluir a variável 'piece_name', definida no arquivo main.py, uma string contendo o nome de todas as peças que serão usadas no jogo (com exceção do peão que não é referido pelo nome e sim pela sua ausência).

    CRD / CRV

Para a continuidade da explicação do programa serão necessários entender dois conceitos.
CRD (abreviação de 'coordenadas') refere-se a uma variável do tipo lista que contém dois valores, o primeiro indicando a coluna e o segundo indicando a linha em que se encontra a casa de destino do movimento realizado localizada na matriz.
CRV (abreviação de 'coordenadas de verificação') refere-se a uma variável do tipo lista que armazena tuplas de dois valores, os primeiros indicando as colunas e os segundos indicando as linhas em que se encontram as possíveis casas onde a peça do movimento realizado se origina, casas que precisam ser verificadas antes dos valores da matriz serem atualizados.

Se, depois do movimento realizado, o crv for um valor vazio, então o movimento é ilegal; se continver uma única tupla, então o movimento é válido e direto; se contiver mais de uma tupla, então o movimento é ambíguo e seu input necessita de alguma especificação da casa de origem da peça. Caracteriza-se um caso de 'Multiplicidade de Crv'. Por exemplo, considere a seguinte posição:

8.| _ _ _ _ _ D _ _ |
7.| _ _ _ _ _ _ _ _ |
6.| _ _ _ _ _ D _ D |
5.| _ _ _ _ _ _ _ _ |
4.| T _ _ _ _ _ _ T |
3.| _ _ _ _ _ _ _ _ |
2.| C _ _ _ _ _ _ _ |
1.| _ _ _ C _ _ _ _ |
    a b c d e f g h

O lance 'Cc3' é ambíguo e necessita que seja especificado a linha ou coluna (por conveção a coluna) do Cavalo que realizará o movimento.
O lance 'Te4' é ambíguo e necessita que seja especificado a coluna, apenas, da Torre que realizará o movimento.
O lance 'Dh8' é ambíguo e necessita que seja especificado ambos coluna e linha da Dama que realizará o movimento.

    O cálculo da movimentação das peças

Enquanto que o crd é um valor dado especialmente pelo input, o crv é um valor que depende da posição do tabuleiro, da peça especificada no input e do crd. A lógica é a seguinte:

Quando um lance é realizado, uma peça é selecionada e a partir de sua posição atual os movimentos possívies para aquela peça específica 'desenham' no tabuleiro todas as casas que podem se tornar crd, ou seja, casa de destino da peça. Se aplicarmos esse mesmo raciocínio a partir da casa crd, podemos encontrar todas as casas possívies de onde ela surgiu, ou seja, candidatos a crv's.
O algoritmo que descreve a movimentação, esse 'desenho' projetado por todo o tabuleiro a partir da casa de origem da peça, depende de 3 parâmetros, denominados de atributos de movimentação. Todos compõe um conjunto de cálculos que resultam em novas coordenadas para a matriz, ou uma casa canditada a crv. Esse processo aplicado a uma estrutra de iterações demonstra a movimentação completa da peça pelo tabuleiro e captura as coordenadas de todos os crv's. Para que uma nova coordenada seja denominada uma nova tupla de valores para o crv, é preciso verificar se o valor da matriz nesta nova coordenada é igual ao valor que corresponde ao nome da peça especificado no input do movimento. Enquanto o valor da nova coordenada for igual a string '_' ou diferente do nome da peça especificado no input, a estrutura deverá continuar iterando.

O cálculo é o seguinte:

for direction in piece.direction:
    for sense in piece.sense:
        step = 0
        while step < piece.distancing:
            step += 1

            crv0 = crd[0] + step*sense*direction[0]
            crv1 = crd[1] + step*sense*direction[1]

            '''lógica para verificar o valor da matriz na posição matriz[crv0][crv1]'''
            '''caso o valor seja diferente da string '_' ou do nome da peça que está efetuando o lance, executa-se um comando break e a iteração continua, a movimentação muda de sentido e/ou direção'''

'crv0' é o valor da nova coordenada que representará a coluna na matriz (derivada do cálculo envolvendo crd[0], o valor coluna da matriz em crd), 'crv1' é o valor da nova coordenada que representará a linha na matriz (derivada do cálculo envolvendo crd[1], o valor linha da matriz em crd).
'step' é uma variável que representará o passo do movimento em relação ao tabuleiro, a cada iteração esse valor é incrementado em +1 para aumentar o alcance da peça numa determinada direção e sentido, além disso, também servirá como flag da própria estrutura de iteração.
'distancing' é o parâmetro de movimentação que define o limite de quantos passos serão realizados numa determinada direção e sentido em relação ao tabuleiro.
'sense' é o parâmetro de movimentação do tipo iterável que representa o sentido do movimento em relação ao tabuleiro, a cada iteração o sentido do movimento inverte.
'direction' é o parâmetro de movimentação do tipo iterável que representa a direção do movimento em relação ao tabulerio, a cada iteração a direção do movimento rotaciona.

Os valores exatos dos atributos de movimentação para cada peça são os seguintes:

                 |Dama                              |Torre            |Bispo             |Rei                               |Peão     |Cavalo
self.direction   |((1, 0), (0, 1), (1, 1), (1, -1)) |((1, 0), (0, 1)) |((1, 1), (1, -1)) |((1, 0), (0, 1), (1, 1), (1, -1)) |((0, 1)) |((1, 2), (2, 1), (1, -2), (2, -1))
self.sense       |(1, -1)                           |(1, -1)          |(1, -1)           |(1, -1)                           |(-1, 1)* |(1, -1)
self.distancing  |float('inf')                      |float('inf')     |float('inf')      |1                                 |1**      |1

*1 Para peão de cor branca; -1 para peão de cor preta
**Sujeito a incrementação em +1 em casos de movimento inicial do peão de salto duplo.

    Arquivos

Os arquivos do projeto foram divididos em main.py, responsável pela importação e chamada das classes, execução e configuração da inicialização do jogo. Borad.py contendo a classe Board, responsável por tudo que referencia o tabuleiro do jogo (incluindo a configuração das peças no tabuleiro definidas pelo atributo matrix). Fen.py contendo a classe Fen, responsável por tudo que referencia a notação fen que se estenderá do início ao fim do jogo. Move.py contendo a classe Move, responsável pela execução de cada lance do jogo. E Piece.py, contendo as classes das peças, responsáveis por instanciar um objeto que representará a peça na execução de cada movimento para cada lance.

Os arquivos na pasta 'backup-code', armazenam arquivos de código e anotações de versões passadas do projeto. Os arquivos da pasta 'notes', contém anotações da versão atual do projeto (com uma lista de problemas a serem resolvidos) e um código para testes de regex usando inputs aleatórios (tentativa de solução do problema regex da classe Move - veja 'lista de problemas a serem resolvidos'). Além disso, existe um arquivo test.py para realizar testes locais.


>>> Script:

O arquivo main.py é o script onde os módulos contendo todas as classes são importados e onde o programa é executado. As linhas de cógido seguem o seguinte programa:

# Default Settings
Onde variáveis relacionadas a construção da notação fen inicial e procedimentos iniciais relacionados são configurados

# FEN Settings
Onde a notação fen é definida

# Matrix Settings
Onde a matriz do tabuleiro é definida

# Plot Matrix
Onde a configuração inicial das peças no tabuleiro é impressa

# Move
Onde o input dos movimentos são executados. O loop é inicializado.
O padrão regex_generic é aplicado para validação.
O CRD é definido pelo input.
Uma estrutura de controle if else instancia uma peça a sua respectiva classe, definindo nome, cor e atributos de movimentação da peça.
O cáculo de movimentação das peças é executado.
O CRV é verificado.

# Update Matrix
A matriz do tabulerio é atualizada.

# Update Fen
As informações da notação fen é atualizada.

# Reset attributes
Os atributos modificados na execução do movimento são resetados.


>>> Resalvas:

    Lógica ainda não conceitualizada

-> Regex_context para 'Especial 1' e 'Especial 2' do padrão de expressão regular
-> Interface do usuário
-> Movimento En-passant
-> Mecânicas de roque, cheque, cheque-mate, empate

    Erros / Imprecisões

-> Regex impreciso >> possibilitando entradas com caracteres especificados sem necessidade em movimentos ambíguos.
