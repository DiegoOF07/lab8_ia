from problem import DOMAIN
from backtracking import backtracking

def main():
    solution = backtracking({}, DOMAIN)

    if solution:
        print("Solución válida encontrada:")
        for k, v in solution.items():
            print(f"{k} -> {v}")
    else:
        print("No se encontró solución")


if __name__ == "__main__":
    main()