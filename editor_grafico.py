# !/usr/bin/python
# -*- coding: utf8 -*-

"""
Explicação
----------
Dada uma matriz de tamanho MxN na qual cada elemento represente um pixel, crie
um programa que leia uma sequência de comandos e os interprete manipulando a
matriz de acordo com a descrição abaixo de cada comando.

Comandos
--------
I M N
Cria uma nova matriz MxN. Todos os pixels são brancos (O).

C
Limpa a matriz. O tamanho permanece o mesmo. Todos os pixels ficam brancos (O).

L X Y C
Colore um pixel de coordenadas (X,Y) na cor C.

V X Y1 Y2 C
Desenha um segmento vertical na coluna X nas linhas de Y1 a Y2 (intervalo
inclusivo) na cor C.

H X1 X2 Y C
Desenha um segmento horizontal na linha Y nas colunas de X1 a X2 (intervalo
inclusivo) na cor C.

K X1 Y1 X2 Y2 C
Desenha um retangulo de cor C. (X1,Y1) é o canto superior esquerdo e (X2,Y2) o
canto inferior direito.

F X Y C
Preenche a região com a cor C. A região R é definida da seguinte forma:
O pixel (X,Y) pertence Ã  região. Outro pixel pertence Ã  região, se e somente
se, ele tiver a mesma cor que o pixel (X,Y) e tiver pelo menos um lado em comum
com um pixel pertencente Ã  região.

S name
Escreve a imagem em um arquivo de nome name.

X
Encerra o programa.

ConsideraÃ§Ãµes
-------------
Comandos diferentes de I, C, L, V, H, K, F, S e X devem ser ignorados

Testes
------

Entrada 01:

I 5 6
L 2 3 A
S one.bmp
G 2 3 J
V 2 3 4 W
H 3 4 2 Z
F 3 3 J
S two.bmp
X

Saida 01:

one.bmp
OOOOO
OOOOO
OAOOO
OOOOO
OOOOO
OOOOO

two.bmp
JJJJJ
JJZZJ
JWJJJ
JWJJJ
JJJJJ
JJJJJ

Entrada 02:

I 10 9
L 5 3 A
G 2 3 J
V 2 3 4 W
H 1 10 5 Z
F 3 3 J
K 2 7 8 8 E
F 9 9 R
S one.bmp
X

Saida 02:

one.bmp
JJJJJJJJJJ
JJJJJJJJJJ
JWJJAJJJJJ
JWJJJJJJJJ
ZZZZZZZZZZ
RRRRRRRRRR
REEEEEEERR
REEEEEEERR
RRRRRRRRRR
"""
import cmd
from canvas import Canvas


class EditorGrafico(cmd.Cmd):
    """Interface em linha de comando para o editor grafico"""

    def do_I(self, line):
        M, N = (int(x) for x in line.split(' '))
        self.canvas = Canvas(M, N)

    def do_print(self, line):
        print(self.canvas.area)

    def do_X(self, line):
        return True

    def do_C(self, line):
        self.canvas.clear_canvas()
        print("Matriz limpa")

    def do_L(self, line):
        X, Y, C = line.split(' ')
        X = int(X) - 1
        Y = int(Y) - 1
        self.canvas.set_pixel(X, Y, C)

    def do_V(self, line):
        X, Y1, Y2, C = line.split(' ')
        self.canvas.vertical_line(int(X) - 1, int(Y1) - 1, int(Y2) - 1, C)

    def do_H(self, line):
        X1, X2, Y, C = line.split(' ')
        self.canvas.horizontal_line(int(X1) - 1, int(X2) - 1, int(Y) - 1, C)

    def do_K(self, line):
        X1, Y1, X2, Y2, C = line.split(' ')
        self.canvas.rectangle(int(X1)-1, int(Y1) - 1,
                              int(X2) - 1, int(Y2) - 1, C)

    def do_F(self, line):
        X, Y, C = line.split(' ')
        self.canvas.paint_region(int(X) - 1, int(Y) - 1, C)

    def do_S(self, line):
        with open(line, 'w') as output:
            for linha in self.canvas.area:
                for pixel in linha:
                    output.write(pixel)
                output.write("\n")
            output.close()


def main():
    EditorGrafico().cmdloop()

if __name__ == '__main__':
    main()
