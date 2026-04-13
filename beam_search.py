from problem import MICROSERVICES, SERVERS, ANTI_AFFINITY, MAX_CAPACITY, is_valid

def count_violations(assignment):
    violations = 0

    counts = {}
    for s in assignment.values():
        counts[s] = counts.get(s, 0) + 1
    for c in counts.values():
        if c > MAX_CAPACITY:
            violations += (c - MAX_CAPACITY)

    for a, b in ANTI_AFFINITY:
        if a in assignment and b in assignment:
            if assignment[a] == assignment[b]:
                violations += 1
    return violations

def beam_search(domains, k=3):
    variables = list(domains.keys())
    beam = [{}]

    for var in variables:
        successors = []
        for assignment in beam:
            for server in domains[var]:
                new_assignment = assignment.copy()
                new_assignment[var] = server
                successors.append(new_assignment)

        if not successors:
            return None

        successors.sort(key=lambda a: count_violations(a))
        beam = successors[:k]

    for assignment in beam:
        if is_valid(assignment):
            return assignment

    return None