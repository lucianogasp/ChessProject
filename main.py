#CHESS PROJECT

def chess_move(x, map_data, cont, en_passant, fen_list, move_list):
    alpha = 'abcdefgh'
    crv = []
    crd = []
    crd.append(alpha.find(x[-2]))
    crd.append(int(x[-1]) - 1)
    if map_data[crd[0]][crd[1]] != '_' and (not 'x' in x[1:] or (cont % 2 == 0 and map_data[crd[0]][crd[1]].islower()) or (cont % 2 != 0 and map_data[crd[0]][crd[1]].isupper())):
        return print('illegal move > occupied crd')

#   MOVE OF PIECES
    if x[0].islower():
        p = 'P'
        j = 1
        if cont%2 == 0:
            p = p.lower()
            j *= -1
        if not 'x' in x[1:]:
            for i in range(1, 3):
                if map_data[crd[0]][crd[1] - i*j] == p:
                    crv.append(crd[0])
                    crv.append(crd[1] - i*j)
                    break
                elif (cont%2 != 0 and crd[1] != 3) or (cont%2 == 0 and crd[1] != 4):
                    break
        elif map_data[crd[0]][crd[1]] != '_':
            if map_data[alpha.find(x[0])][crd[1] - 1*j] == p and (alpha.find(x[0]) + 1 == crd[0] or alpha.find(x[0]) - 1 == crd[0]):
                crv.append(alpha.find(x[0]))
                crv.append(crd[1] - 1*j)
            else:
                return print('illegal move > wrong notation')
        elif en_passant != '-' and en_passant == ''.join([x[-2], x[-1]]):
            if map_data[alpha.find(x[0])][crd[1] - 1*j] == p and (alpha.find(x[0]) + 1 == crd[0] or alpha.find(x[0]) - 1 == crd[0]):
                crv.append(alpha.find(x[0]))
                crv.append(crd[1] - 1*j)
                map_data[crd[0]][crd[1] - 1*j] = '_'
            else:
                return print('illegal move > en passant is not a possible move')
        else:
            return print('illegal move > wrong notation')

    elif x[0] == 'T':
        p = 'T'
        if cont%2 == 0:
            p = p.lower()
        r = len(map_data) - crd[0]
        for j in [1, -1]:
            for i in range(1, r):
                if map_data[crd[0] + i*j][crd[1]] == p:
                    crv.append(crd[0] + i*j)
                    crv.append(crd[1])
                    break
                elif map_data[crd[0] + i*j][crd[1]] != '_': break
            r = crd[0] + 1
        r = len(map_data[0]) - crd[1]
        for j in [1, -1]:
            for i in range(1, r):
                if map_data[crd[0]][crd[1] + i*j] == p:
                    crv.append(crd[0])
                    crv.append(crd[1] + i*j)
                    break
                elif map_data[crd[0]][crd[1] + i*j] != '_': break
            r = crd[1] + 1

    elif x[0] == 'B':
        p = 'B'
        if cont%2 == 0:
            p = p.lower()
        r = min(len(map_data) - crd[0], len(map_data[0]) - crd[1])
        for j in [1, -1]:
            for i in range(1, r):
                if map_data[crd[0] + i*j][crd[1] + i*j] == p:
                    crv.append(crd[0] + i*j)
                    crv.append(crd[1] + i*j)
                    break
                elif map_data[crd[0] + i*j][crd[1] + i*j] != '_': break
            r = min(crd[0] + 1, crd[1] + 1)
        r = min(len(map_data) - crd[0], crd[1] + 1)
        for j in [1, -1]:
            for i in range(1, r):
                if map_data[crd[0] + i*j][crd[1] - i*j] == p:
                    crv.append(crd[0] + i*j)
                    crv.append(crd[1] - i*j)
                    break
                elif map_data[crd[0] + i*j][crd[1] - i*j] != '_': break
            r = min(crd[0] + 1, len(map_data[0]) - crd[1])

    elif x[0] == 'D':
        p = 'D'
        if cont%2 == 0:
            p = p.lower()
        r = len(map_data) - crd[0]
        for j in [1, -1]:
            for i in range(1, r):
                if map_data[crd[0] + i*j][crd[1]] == p:
                    crv.append(crd[0] + i*j)
                    crv.append(crd[1])
                    break
                elif map_data[crd[0] + i*j][crd[1]] != '_': break
            r = crd[0] + 1
        r = len(map_data[0]) - crd[1]
        for j in [1, -1]:
            for i in range(1, r):
                if map_data[crd[0]][crd[1] + i*j] == p:
                    crv.append(crd[0])
                    crv.append(crd[1] + i*j)
                    break
                elif map_data[crd[0]][crd[1] + i*j] != '_': break
            r = crd[1] + 1
        r = min(len(map_data) - crd[0], len(map_data[0]) - crd[1])
        for j in [1, -1]:
            for i in range(1, r):
                if map_data[crd[0] + i*j][crd[1] + i*j] == p:
                    crv.append(crd[0] + i*j)
                    crv.append(crd[1] + i*j)
                    break
                elif map_data[crd[0] + i*j][crd[1] + i*j] != '_': break
            r = min(crd[0] + 1, crd[1] + 1)
        r = min(len(map_data) - crd[0], crd[1] + 1)
        for j in [1, -1]:
            for i in range(1, r):
                if map_data[crd[0] + i*j][crd[1] - i*j] == p:
                    crv.append(crd[0] + i*j)
                    crv.append(crd[1] - i*j)
                    break
                elif map_data[crd[0] + i*j][crd[1] - i*j] != '_': break
            r = min(crd[0] + 1, len(map_data[0]) - crd[1])

    elif x[0] == 'C':
        p = 'C'
        if cont%2 == 0:
            p = p.lower()
        row = [1, 2, -1, -2]
        col = [2, 1, 2, 1]
        for j in [1, -1]:
            for i in range(4):
                if crd[0] + row[i]*j not in range(8) or crd[1] + col[i]*j not in range(8):
                    continue
                elif map_data[crd[0] + row[i]*j][crd[1] + col[i]*j] == p:
                    crv.append(crd[0] + row[i]*j)
                    crv.append(crd[1] + col[i]*j)

    elif x[0] == 'R':
        p = 'R'
        if cont%2 == 0:
            p = p.lower()
        row = [0, 1, 1, 1]
        col = [1, 1, 0, -1]
        for j in [1, -1]:
            for i in range(4):
                if crd[0] + row[i]*j not in range(8) or crd[1] + col[i]*j not in range(8):
                    continue
                elif map_data[crd[0] + row[i]*j][crd[1] + col[i]*j] == p:
                    crv.append(crd[0] + row[i]*j)
                    crv.append(crd[1] + col[i]*j)

#   CRV
    if len(crv) == 0:
        return print('illegal move > empty crv')

    elif len(crv) == 2:
        map_data[crv[0]][crv[1]] = '_'
        map_data[crd[0]][crd[1]] = p

    elif ('x' in x and len(x) == 6) or (not 'x' in x and len(x) == 5):
        if not (x[1].isalpha() and x[2].isdigit()):
            return print('illegal notation > there is no character for crv')
        if not alpha.find(x[1]) in crv[0::2] or not int(x[2]) - 1 in crv[1::2]:
            return print('illegal notation > the character for crv must be correct')
        map_data[alpha.find(x[1])][int(x[2]) - 1] = '_'
        map_data[crd[0]][crd[1]] = p

    else:
        if ('x' in x and len(x) <= 4) or (not 'x' in x and len(x) <= 3):
            return print('illegal notation > there is no character for crv')
        if x[1].isalpha() and alpha.find(x[1]) in crv[0::2]:
            n_columns = [i for i in crv[0::2] if i == alpha.find(x[1])]
            if len(n_columns) > 1:
                return print('illegal notation > a line is required to specify crv')
            else:
                select_line = [i + 1 for i in range(0, len(crv), 2) if crv[i] == alpha.find(x[1])]
                map_data[alpha.find(x[1])][crv[select_line[0]]] = '_'
        elif x[1].isdigit() and int(x[1]) - 1 in crv[1::2]:
            n_lines = [i for i in crv[1::2] if i == int(x[1]) - 1]
            if len(n_lines) > 1:
                return print('illegal notation > a column is required to specify crv')
            else:
                select_column = [i - 1 for i in range(1, len(crv), 2) if crv[i] == int(x[1]) - 1]
                map_data[crv[select_column[0]]][int(x[1]) - 1] = '_'
        else:
            return print('illegal move > the character for crv must be correct')
        map_data[crd[0]][crd[1]] = p

#   OUTPUT (Graphic Position / FEN Notation)
    mapa = [[sublist[i] for sublist in map_data] for i in range(len(map_data[0]))]
    mapa = mapa[::-1]

#   FEN Coding
    fen = ''

    for sublist in mapa:    #Codificação da posição
        v_cont = 0
        fen_sublist = ''
        for j in sublist:
            if j == '_':
                v_cont += 1
            else:
                if v_cont > 0:
                    fen_sublist += str(v_cont)
                    v_cont = 0
                fen_sublist += j
        if v_cont > 0:
            fen_sublist += str(v_cont)
        fen += fen_sublist + '/'
    fen = fen.rstrip('/')    #Codificação da posição

    fen += ' b ' if cont%2 == 0 else ' p '    #Vez do jogador

    #   FEN De-coding for en_passant verification
    lines, _p, p_ = [[1, 2, 3], 'p', 'P'] if cont%2 == 0 else [[6, 5, 4], 'P', 'p']     #En_passant
    matrix = []
    fen_split = fen_list[-1].split()[0].split('/')
    for i in lines[::2]:
        lista = []
        for f in fen_split[i]:
            if f.isdigit():
                lista += ['_'] * int(f)
            else:
                lista += f
        matrix.append(lista)
    en_cont = 0
    for i in range(len(mapa)):
        if i == 0:
            j1, j2 = 1, -1
        elif i < 7:
            j1, j2 = 1, 1
        else:
            j1, j2 = -1, 1
        if mapa[lines[0]][i] == '_' and mapa[lines[1]][i] == '_' and mapa[lines[2]][i] == _p and (mapa[lines[2]][i + j1] == p_ or mapa[lines[2]][i - j2] == p_):
            if matrix[0][i] == _p and matrix[1][i] == '_':
                en_cont += 1
                fen += ''.join([alpha[i], str(6 if cont%2 == 0 else 3)]) + ' '
                en_passant = ''.join([alpha[i], str(6 if cont%2 == 0 else 3)])
    if en_cont == 0:
        fen += '- '
        en_passant = '-'

    fen += str(int(cont / 2) + 1)   #Lance

#   Setting Parametric Variables
    fen_list.append(fen)    #Lista de fen
    move_list.append(x)     #Lista de movimentos

#   Plot graphic position
    for i in range(len(mapa)): print(mapa[i])
    print(f'crd: {crd}\ncrv: {crv}\nfen: {fen}\nfen_list: {fen_list}')
    return en_passant

###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def chess_play():
#   FEN
    fen = 'tcbdrbct/pppppppp/8/8/8/8/PPPPPPPP/TCBDRBCT b - 1'
    x = input('___Start___: ')
    if x == 'fen':
        fen = input('Insira a notação fen: ')
    elif x == 'fen eng':
        fen = input('Insira a notação fen: ')
        split_fen = fen.split()
        split_fen[0] = split_fen[0].translate(str.maketrans('rnqkRNQK', 'tcdrTCDR'))
        split_fen[1] = split_fen[1].translate(str.maketrans('wb', 'bp'))
        fen = ' '.join(split_fen)
    if len(fen.split()) < 3: return print('illegal notation > fen is not correctly defined')

#   FEN De-coding
    fen_split = fen.split()[0].split('/')
    map_data_0 = []
    for i in range(8):
        sublist = []
        for f in fen_split[i]:
            if f.isdigit():
                sublist += ['_'] * int(f)
            else:
                sublist += f
        map_data_0.append(sublist)

#   PLOT START
    map_data_0 = map_data_0[::-1]
    map_data = [[sublist[i] for sublist in map_data_0] for i in range(len(map_data_0[0]))]
    for i in range(len(map_data_0) - 1, -1, -1): print(map_data_0[i])

#   PARAMETRIC VARIABLES
    cont = 2 * int(fen.split()[-1]) - 2 if fen.split()[-3] == 'b' else 2 * int(fen.split()[-1]) - 1
    en_passant = fen.split()[-2]
    fen_list = [fen]
    move_list = []

#   LOOP OF MOVES
    while True:
        x = input('Digite seu lance: ')
        if x == 'reset_move':
            cont -= 1
            continue

        elif x == 'reset_position':
            cont -= 1
            fen_list.pop()
            move_list.pop()
            en_passant = fen_list[-1].split()[-2]
            fen_split = fen_list[-1].split()[0].split('/')
            map_data_0 = []
            for i in range(8):
                sublist = []
                for f in fen_split[i]:
                    if f.isdigit():
                        sublist += ['_'] * int(f)
                    else:
                        sublist += f
                map_data_0.append(sublist)
            map_data_0 = map_data_0[::-1]
            map_data = [[sublist[i] for sublist in map_data_0] for i in range(len(map_data_0[0]))]
            for i in range(len(map_data_0) - 1, -1, -1): print(map_data_0[i])
            continue

        elif 'plot_move' in x:
            plot_move = ['...'] + move_list.copy() if fen_list[0].split()[-3] == 'p' else move_list.copy()
            if len(plot_move)%2 != 0: plot_move += ['...']
            plot_cont = int(fen_list[0].split()[-1])
            for i in range(0, len(plot_move), 2):
                print(f'{plot_cont + int(i/2)}. {plot_move[i]}     {plot_move[i + 1]}')
            continue

        elif 'plot_fen' in x:
            plot_fen = []
            plot_cont = int(fen_list[0].split()[-1])
            if 'eng' in x:
                for i in fen_list:
                    split_fen = []
                    split_fen = i.split()
                    split_fen[0] = split_fen[0].translate(str.maketrans('tcdrTCDR', 'rnqkRNQK'))
                    split_fen[1] = split_fen[1].translate(str.maketrans('bp', 'wb'))
                    plot_fen.append(' '.join(split_fen))
            else:
                plot_fen = fen_list.copy()
            if plot_fen[0].split()[-3] == 'b' or  plot_fen[0].split()[-3] == 'w':
                print(f'{plot_cont - 1}. {plot_fen[0]}')
                plot_fen = plot_fen[1:]
            if len(plot_fen)%2 != 0:
                plot_fen += ['...']
            for i in range(0, len(plot_fen), 2):
                print(f'{plot_cont + int(i/2)}. {plot_fen[i]}     {plot_fen[i + 1]}')
            continue

        elif 'find_fen' in x:
            plot_fen = fen_list[move_list.index(x.split()[-1]) + 1]
            plot_cont = int(plot_fen.split()[-1])
            if 'eng' in x:
                split_fen = plot_fen.split()
                split_fen[0] = split_fen[0].translate(str.maketrans('tcdrTCDR', 'rnqkRNQK'))
                split_fen[1] = split_fen[1].translate(str.maketrans('bp', 'wb'))
                plot_fen = ' '.join(split_fen)
                plot_fen = plot_fen + '     ...' if plot_fen.split()[-3] == 'w' else '...     ' + plot_fen
            else:
                plot_fen = plot_fen + '     ...' if plot_fen.split()[-3] == 'b' else '...     ' + plot_fen
            print(f'{plot_cont}. {plot_fen}')
            continue

        elif x == 'exit':
            break
        cont += 1
        en_passant = chess_move(x, map_data, cont, en_passant, fen_list, move_list)

chess_play()