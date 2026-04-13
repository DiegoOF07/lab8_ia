import time
from problem import DOMAIN
from backtracking import backtracking
from beam_search import beam_search
from local_search import local_search_icm

def run_benchmark():
    resultados = {}

    start = time.perf_counter()
    sol_bt = backtracking({}, DOMAIN)
    elapsed_bt = time.perf_counter() - start
    resultados["Backtracking"] = {"solucion": sol_bt, "tiempo": elapsed_bt}

    K = 5
    start = time.perf_counter()
    sol_bs = beam_search(DOMAIN, k=K)
    elapsed_bs = time.perf_counter() - start
    resultados[f"Beam Search (K={K})"] = {"solucion": sol_bs, "tiempo": elapsed_bs}

    start = time.perf_counter()
    sol_icm = local_search_icm(max_iter=200, max_restarts=20)
    elapsed_icm = time.perf_counter() - start
    resultados["Local Search ICM"] = {"solucion": sol_icm, "tiempo": elapsed_icm}

    print("Task 2.4")

    for nombre, datos in resultados.items():
        sol = datos["solucion"]
        t   = datos["tiempo"]
        print(f"\n{nombre}")
        if sol:
            print(f"Solución: {sol}")
            print(f"Válida: True")
        else:
            print(f"Solución: No encontrada  *** FALLO ***")
            print(f"Válida: False")
        print(f"Tiempo: {t:.6f} segundos")

    print(f"\n{'Algoritmo':<22} {'¿Solución?':<12} {'Tiempo (s)'}")
    for nombre, datos in resultados.items():
        encontro = "Sí" if datos["solucion"] else "NO (falló)"
        print(f"{nombre:<22} {encontro:<12} {datos['tiempo']:.6f}")
