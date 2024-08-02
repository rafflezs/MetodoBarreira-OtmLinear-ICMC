import numpy as np

class Barreira:
    def __init__(self, modelo: any) -> None:
        self.modelo = modelo
        self.x = []
        self.y = []
        self.s = []
        self.log = []

    def get_solucao(self) -> tuple[np.array, np.array, np.array]:
        return self.x, self.y, self.s, self.modelo.get_coeficiente()

    def get_log(self) -> tuple[list]:
        return self.log

    def barreira(self, tol=1e-8, max_iter=100) -> tuple[np.array, np.array, np.array, list]:
        """
        @about
        Codigo drive do solver.
        Implementa o metodo da barreira, realizando a chamada das funcoes operacionais.

        @param
        tol: float, opt
            Tolerancia de convergencia do sistema. O padrao e 1e-8.
        max_iter: int, opt
            Numero maximo de iteracoes do sistema. O padrao e 100

        @return
        self.x: np.array
            Vetor contendo o valor final das variaveis de decisao do sistema
        self.y: np.array
            Vetor contendo o valor final das variaveis de Lagrange do sistema
        self.s: np.array
            Vetor contendo o valor final das variaveis de folga do sistema
        self.log: list of tuples
            Lista de tuplas contendo o historico de (self.x, self.y, self.s) em cada iteracao.
        """
        A, b, c = self.modelo.get_data()
        m, n = A.shape
        
        self.x = np.ones(n)
        self.y = np.zeros(m)
        self.s = np.ones(n)

        for _ in range(max_iter):
            self.log.append((self.x.copy(), self.y.copy(), self.s.copy())) 
            res = self.KKT(A, b, c)
            if np.linalg.norm(res) < tol:
                break
            
            delta_x, delta_y, delta_s = self.passo_newton(A, b, c)
            
            alpha = 1
            while np.any(self.x + alpha * delta_x <= 0) or np.any(self.s + alpha * delta_s <= 0):
                alpha *= 0.5
            
            self.x += alpha * delta_x
            self.y += alpha * delta_y
            self.s += alpha * delta_s

    def grad_f(self, c: np.array) -> np.array:
        """
        @About
        Realiza o calculo do gradiente da funcao objetivo.

        @param
        self.x: np.array, req
            Vetor contendo o valor atual das variaveis de decisao no espaco.
        c: np.array, req
            Vetor de coeficientes da funcao objetivo.

        @return
        c + np.sum(1 / self.x) [gradiente]: np.array
            Gradiente da funcao objetivo em termos de barreira.
        """
        return c + np.sum(1 / self.x)

    def hessian_f(self) -> np.array:
        """
        @about
        Realiza o calculo da matriz Hessiana.

        @param
        self.x: np.array, req
            Vetor contendo o valor atual das variaveis de decisao no espaco.

        @return
        np.diag(1 / (self.x ** 2)) [Matriz Hessiana]: np.array
            Matriz Hessiana.
        """
        return np.diag(1 / (self.x ** 2))
    
    def KKT(self, A: np.array, b: np.array, c: np.array) -> np.array:
        """
        @about
        Constroi o sistema KKT para verificacao das condicoes do sistema.

        @param
        A: np.array, req
            Matriz de coeficiente das restricoes do problema.
        b: np.array, req
            Vetor de recursos do problema (lado direito).
        self.x: np.array, req
            Vetor contendo o valor atual das variaveis de decisao no espaco.
        c: np.array, req
            Vetor de coeficientes da funcao objetivo.
        self.y: np.array, req
            Vetor de multiplicadores de Lagrange.
        self.s: np.array, req
            Vetor de variaveis de folga do problema.

        @return
        [sistema KKT]: np.array
            Sistema de condicoes KKT concatenado.
        """
        return np.concatenate([A.T @ self.y + self.s - c,
                            A @ self.x - b,
                            self.x * self.s])
    
    def passo_newton(self, A: np.array, b: np.array, c: np.array) -> np.array:
        """
        @about
        Calcula o passo de Newton para solucao do sistema KKT.

        @param
        A: np.array, req
            Matriz de coeficiente das restricoes do problema.
        b: np.array, req
            Vetor de recursos do problema (lado direito).
        c: np.array, req
            The coefficients of the linear objective function.
        self.x: np.array, req
            The current point in the space of decision variables.
        self.y: np.array, req
            Vetor de multiplicadores de Lagrange.
        self.s: np.array, req
            Vetor de variaveis de folga do problema.

        @return
        delta_x: np.array
            Passo de Newton aplicado as variaveis de decisao.
        delta_y: np.array
            Passo de Newton aplicado as variaveis de Lagrange.
        delta_s: np.array
            Passo de Newton aplicado as variaveis de folga.
        """
        m, n = A.shape
        #X_inv = np.diag(1 / self.x)
        #S_inv = np.diag(1 / self.s)
        
        KKT_matrix = np.block([
            [np.zeros((n, n)), A.T, np.eye(n)],
            [A, np.zeros((m, m)), np.zeros((m, n))],
            [np.diag(self.s), np.zeros((n, m)), np.diag(self.x)]
        ])
        
        KKT_rhs = -self.KKT(A, b, c)
        
        delta = np.linalg.solve(KKT_matrix, KKT_rhs)
        return delta[:n], delta[n:n + m], delta[n + m:]