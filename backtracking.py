from copy import deepcopy
from problem import is_valid, ANTI_AFFINITY, MAX_CAPACITY

def forward_check(domains, assignment):
    new_domains = deepcopy(domains)

    for (a, b) in ANTI_AFFINITY:
        if a in assignment:
            val = assignment[a]
            if b not in assignment and val in new_domains[b]:
                new_domains[b].remove(val)

        if b in assignment:
            val = assignment[b]
            if a not in assignment and val in new_domains[a]:
                new_domains[a].remove(val)

    counts = {}
    for s in assignment.values():
        counts[s] = counts.get(s, 0) + 1

    for server, count in counts.items():
        if count >= MAX_CAPACITY:
            for var in new_domains:
                if var not in assignment and server in new_domains[var]:
                    new_domains[var].remove(server)

    return new_domains

def select_unassigned(assignment, domains):
    for var in domains:
        if var not in assignment:
            return var
    return None


def backtracking(assignment, domains):
    if len(assignment) == len(domains):
        return assignment

    var = select_unassigned(assignment, domains)

    for value in domains[var]:
        new_assignment = assignment.copy()
        new_assignment[var] = value

        if is_valid(new_assignment):
            new_domains = forward_check(domains, new_assignment)

            if any(len(new_domains[v]) == 0 for v in new_domains if v not in new_assignment):
                continue

            result = backtracking(new_assignment, new_domains)
            if result:
                return result

    return None
