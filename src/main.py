from barreira import barreira_class, modelo_class, visualizacao_class
import numpy as np

def exemplo_1():
    A = np.array([
        [1, 1, 1, 0, 0],
        [1, -1, 0, 1, 0],
        [-1, 1, 0, 0, 1]
    ])
    b = np.array([6, 4, 4])
    c = np.array([-1, -2, 0, 0, 0])

    modelo = modelo_class.Modelo(A=A, b=b, c=c)
    solver = barreira_class.Barreira(modelo=modelo)
    solver.barreira()

    ploter = visualizacao_class.Visualizacao(solucao=solver)
    ploter.print_val_solucao()
    ploter.plot_evolucao_sol(output_path="output", fig_title="exemplo1", A=A, b=b)

def exemplo_2():
    A = np.array([
        [1, 1, 1, 0, 0],
        [1, -1, 0, 1, 0],
        [-1, 1, 0, 0, 1]
    ])
    b = np.array([6, 4, 4])
    c = np.array([-1, -1, 0, 0, 0])

    modelo = modelo_class.Modelo(A=A, b=b, c=c)
    solver = barreira_class.Barreira(modelo=modelo)
    solver.barreira()

    ploter = visualizacao_class.Visualizacao(solucao=solver)
    ploter.print_val_solucao()
    ploter.plot_evolucao_sol(output_path="output", fig_title="exemplo2", A=A, b=b)

def exemplo_3():
    """
    Exemplo Ilimitado
    """
    A = np.array([
    [1, -1, 1, 0],
    [-1, 1, 0, 1]
    ])
    b = np.array([4, 4])
    c = np.array([-1, -1, 0, 0])

    modelo = modelo_class.Modelo(A=A, b=b, c=c)
    solver = barreira_class.Barreira(modelo=modelo)
    solver.barreira()

    ploter = visualizacao_class.Visualizacao(solucao=solver)
    ploter.print_val_solucao()
    ploter.plot_evolucao_sol(output_path="output", fig_title="exemplo3", A=A, b=b)

def exemplo_4():
    A = np.array([
        [0.5, 0.3, 1, 0, 0],
        [0.1, 0.2, 0, 1, 0],
        [0.4, 0.5, 0, 0, 1],
    ])
    b = np.array([3, 1, 3])
    c = np.array([-1, -1, 0, 0, 0])

    modelo = modelo_class.Modelo(A=A, b=b, c=c)
    solver = barreira_class.Barreira(modelo=modelo)
    solver.barreira()

    ploter = visualizacao_class.Visualizacao(solucao=solver)
    ploter.print_val_solucao()
    ploter.plot_evolucao_sol(output_path="output", fig_title="exemplo4", A=A, b=b)

if __name__ == "__main__":
    exemplo_1()
    exemplo_2()
    exemplo_3()
    exemplo_4()