import random
from problem import MICROSERVICES, SERVERS, ANTI_AFFINITY, MAX_CAPACITY, is_valid

def local_cost(var, server, assignment):
    cost = 0
    for a, b in ANTI_AFFINITY:
        other = None
        if a == var:
            other = b
        elif b == var:
            other = a
        if other and other in assignment and assignment[other] == server:
            cost += 1

    count = sum(1 for v, s in assignment.items() if v != var and s == server)
    if count >= MAX_CAPACITY:
        cost += 1

    return cost
def local_search_icm(max_iter=100, max_restarts=10):

    for restart in range(max_restarts):
        assignment = {m: random.choice(SERVERS) for m in MICROSERVICES}

        for iteration in range(max_iter):
            changed = False
            for var in MICROSERVICES:
                current_server = assignment[var]
                best_server = current_server
                best_cost = local_cost(var, current_server, assignment)

                for server in SERVERS:
                    if server == current_server:
                        continue
                    c = local_cost(var, server, assignment)
                    if c < best_cost:
                        best_cost = c
                        best_server = server
                if best_server != current_server:
                    assignment[var] = best_server
                    changed = True
            if is_valid(assignment):
                return assignment
            if not changed:
                break
    return None