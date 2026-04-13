from problem import DOMAIN
from backtracking import backtracking
from beam_search import beam_search
from local_search import local_search_icm


def print_solution(name, solution):
    print(f"\n{'='*10}  {name}{'='*10}")
    if solution:
        print("Solución válida encontrada:")
        for k, v in solution.items():
            print(f"    {k} -> {v}")
    else:
        print("No se encontró solución")


def main():
    #Task 2.1
    sol_bt = backtracking({}, DOMAIN)
    print_solution("Backtracking Search (Task 2.1)", sol_bt)

    #Task 2.2
    K = 5
    sol_bs = beam_search(DOMAIN, k=K)
    print_solution(f"Beam Search K={K} (Task 2.2)", sol_bs)

    #Task 2.3
    sol_icm = local_search_icm(max_iter=200, max_restarts=20)
    print_solution("Local Search (Task 2.3)", sol_icm)


if __name__ == "__main__":
    main()