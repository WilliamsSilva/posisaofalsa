import math

# função f(x) = cos(x) - x


def f(x):
    return math.cos(x) - x


def falsa_posicao(a, b, tol=1e-6, max_iter=100):

    if f(a) * f(b) >= 0:
        print("O método pode falhar: f(a) e f(b) devem ter sinais opostos.")
        return None

    # Valor inicial x0 como a metade do intervalo
    x0 = (a + b) / 2
    print(f"Iteração 0: x0 = {x0:.6f}, f(x0) = {f(x0):.6f}")

    # Loop principal do método
    for i in range(1, max_iter + 1):
        # Fórmula da posição falsa para estimar a raiz
        xr = b - (f(b) * (a - b)) / (f(a) - f(b))
        fr = f(xr)

        print(f"Iteração {i}: xr = {xr:.6f}, f(xr) = {fr:.6f}")

        # Critério de parada: quando o valor de f(xr) for suficientemente próximo de zero
        if abs(fr) < tol:
            print("Convergência atingida.")
            return xr

        # Atualização do intervalo com base no sinal de f(xr)
        if f(a) * fr < 0:
            b = xr  # A raiz está entre a e xr
        else:
            a = xr  # A raiz está entre xr e b

    print("Número máximo de iterações atingido.")
    return xr


raiz = falsa_posicao(0, 1)

# Resultado final
if raiz is not None:
    print(f"\nRaiz aproximada encontrada: {raiz:.6f}")
