MICROSERVICES = [f"M{i}" for i in range(1, 9)]
SERVERS = ["S1", "S2", "S3"]

DOMAIN = {m: SERVERS.copy() for m in MICROSERVICES}

ANTI_AFFINITY = [
    ("M1", "M2"),
    ("M3", "M4"),
    ("M5", "M6"),
    ("M1", "M5"),
]

MAX_CAPACITY = 3

# Checar si la asignación respeta la capacidad
def capacity_ok(assignment):
    counts = {}
    for s in assignment.values():
        counts[s] = counts.get(s, 0) + 1
        if counts[s] > MAX_CAPACITY:
            return False
    return True

# Checar si la asignación respeta las restricciones de anti-affinity
def anti_affinity_ok(assignment):
    for a, b in ANTI_AFFINITY:
        if a in assignment and b in assignment:
            if assignment[a] == assignment[b]:
                return False
    return True

# Checar si la asignación es consistente con todas las restricciones
def is_valid(assignment):
    return capacity_ok(assignment) and anti_affinity_ok(assignment)

# Función de peso para la búsqueda informada
def weight(assignment):
    return 1 if is_valid(assignment) else 0