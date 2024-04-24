import interfaces
from interfaces import Token


class GroupeDavidStrategy(interfaces.Strategy):

    """
    Strategy that plays a valid random move for each play.
    """



    def authors(self) -> str:
        return "Alexis Rosenfeld , David Simonet"

    def play(self, b: interfaces.Board, t: interfaces.Token) -> int:
        r = Token.RED
        y = Token.YELLOW
        e = Token.EMPTY
        # playable_columns = [index for index in range(current_board.width) if
        #                     interfaces.Token.EMPTY in current_board.column(index)]
        # secrets.choice(playable_columns)
        m_b = [[b.column(j)[i] for i in range(b.height)] for j in range(b.width)]

        def reverse_nested_list(arr):
            reversed_arr = [sub_arr[::-1] for sub_arr in arr]
            return reversed_arr

        # Reverse each sub-array (row) in the nested list
        m_b = reverse_nested_list(m_b)

        width = len(m_b[0])
        height = len(m_b)

        # print(m_b[0][0])
        # print(m_b[2][0])
        # print(m_b[2][1])

        nr = 0
        ny = 0
        ne = 0

        # Parcourir chaque tableau dans la matrice m_b
        for sous_array in m_b:
            for valeur in sous_array:
                # Incrémenter le compteur correspondant à la valeur
                if valeur == r:
                    nr += 1
                elif valeur == y:
                    ny += 1
                elif valeur == e:
                    ne += 1

        positions_r = []
        positions_y = []
        positions_e = []

        # Parcourir chaque sous-array dans la matrice m_b
        for i, sous_array in enumerate(m_b):
            for j, valeur in enumerate(sous_array):
                # Vérifier la valeur et ajouter la position à la liste correspondante
                if valeur == r:
                    positions_r.append((i, j))
                elif valeur == y:
                    positions_y.append((i, j))
                elif valeur == e:
                    positions_e.append((i, j))

        # print(b)
        # print(nr)
        # print(ny)
        # print(ne)
        # print(positions_r)

        def create_series_matrix(m_b, width, height, win):
            # Initialisation de la matrice mat avec des zéros
            mat = [[0] * width for _ in range(height)]

            # Parcourir chaque élément de la matrice m_b
            for i in range(height):
                for j in range(width):
                    # Calcul du nombre de séries passant par m_b[i][j]
                    horizontal_series = min(win, j + 1) + min(win, width - j)
                    vertical_series = min(win, i + 1) + min(win, height - i)
                    diagonal1_series = min(win, i + 1, j + 1) + min(win, height - i, width - j)
                    diagonal2_series = min(win, i + 1, width - j) + min(win, height - i, j + 1)

                    # Somme des séries horizontales, verticales et diagonales
                    mat[i][j] = horizontal_series + vertical_series + diagonal1_series + diagonal2_series - 3

            return mat


        # Exemple d'utilisation
        width = 4
        height = 4
        win = 3
        m_b = [
            ['r', 'y', 'r', 'e'],
            ['e', 'y', 'e', 'r'],
            ['r', 'y', 'y', 'y'],
            ['e', 'r', 'r', 'e']
        ]

        mat = create_series_matrix(m_b, width, height, win)

        # Affichage de la matrice mat
        for row in mat:
            print(row)



        return int(1)

