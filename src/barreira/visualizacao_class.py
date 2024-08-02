import os
import numpy as np
import matplotlib.pyplot as plt

class Visualizacao:

    def __init__(self, solucao: any) -> None:
        self.solucao = solucao

    def print_val_solucao(self) -> None:
        x, y, s, c = self.solucao.get_solucao()
        print("Valores de X: ", x)
        print("Valores de Y: ", y)
        print("Valores de S: ", s)
        print("Valor Total da FO: ", np.dot(c, x)) 

    def plot_evolucao_sol(self, output_path: str, fig_title: str, A: np.array, b: np.array) -> None:
        """
        @about
        Plota a evolucao do sistema (somente bidimensional).

        @param
        A: np.array, req
            Matriz de coeficiente das restricoes do problema.
        b: np.array, req
            Vetor de recursos do problema (lado direito).
        evolucao_log: list of tuples, req
            Lista de tuplas contendo o historico de (x, y, s) em cada iteracao.

        @return
        None

        @raises
        Exception: se o sistema nao e bidimensional, nao e realizado plot.
        """
        evolucao_log = self.solucao.get_log()
        if len(evolucao_log[0][0]) - len(b) != 2:
            raise Exception("O sistema nao e bidimensional (2 variaveis de decisao), portanto nao sera realizada plotagem.")

        x1_vals = np.linspace(-5, 10, 400)
        x2_vals = np.linspace(-5, 10, 400)
        x1, x2 = np.meshgrid(x1_vals, x2_vals)

        constraints = []
        for i in range(A.shape[0]):
            constraint = b[i] - A[i, 0] * x1 - A[i, 1] * x2
            constraints.append(constraint)

        plt.figure(figsize=(10, 6))
        for constraint in constraints:
            plt.contour(x1, x2, constraint, levels=[0], colors=['blue'])

        plt.xlabel('$x_1$')
        plt.ylabel('$x_2$')

        evolucao_log_x1 = [h[0][0] for h in evolucao_log]
        evolucao_log_x2 = [h[0][1] for h in evolucao_log]
        plt.plot(evolucao_log_x1, evolucao_log_x2, marker='o', color='red')

        plt.title('Região Factível e Evolução da Solução')
        plt.xlim([-5, 10])
        plt.ylim([-5, 10])

        if output_path:
            os.makedirs(output_path, exist_ok=True)
            file_path = os.path.join(output_path, f"{fig_title}.png")
            plt.savefig(file_path)
            print(f"Plot saved to {file_path}")
        else:
            plt.show()