# Laboratorio 8

Se tienen 8 microservicios (M1–M8) que deben asignarse a 3 servidores físicos (S1, S2, S3) respetando las siguientes restricciones

---

### Task 2.1 – Backtracking Search con Forward Checking

**Archivo:** `backtracking.py`

Implementa búsqueda por backtracking clásica con la técnica de **lookahead (Forward Checking)**. Después de cada asignación, se actualizan los dominios de las variables no asignadas eliminando valores que ya no son consistentes. Si algún dominio queda vacío, esa rama se abandona de inmediato sin seguir explorando.

---

### Task 2.2 – Beam Search

**Archivo:** `beam_search.py`

Implementa Beam Search, una búsqueda informada que mantiene únicamente los **K mejores candidatos** en cada nivel del árbol (uno por microservicio). En cada paso se expanden todos los candidatos del beam, se generan sus sucesores y se aplica **prune**: solo los K con menor número de violaciones pasan al siguiente nivel. `k` (Tamaño del beam) Se pasa directamente a la función `beam_search(domains, k)` y se define en `main.py`. Un `k` más grande explora más candidatos y tiene más probabilidad de encontrar solución.

---

### Task 2.3 – Local Search (ICM)

**Archivo:** `local_search.py`

Implementa **Iterated Conditional Modes (ICM)**, un algoritmo de búsqueda local que parte de una asignación completamente aleatoria y la mejora iterativamente.

---

### Task 2.4 - Benchmark

**Archivo:** `benchmark.py`

Realiza una comparación entre los tres algoritmos, dando como resultado lo siugiente:

```bash
Backtracking
Solución: {'M1': 'S1', 'M2': 'S2', 'M3': 'S1', 'M4': 'S2', 'M5': 'S2', 'M6': 'S1', 'M7': 'S3', 'M8': 'S3'}
Válida: True
Tiempo: 0.000083 segundos

Beam Search (K=5)
Solución: {'M1': 'S1', 'M2': 'S2', 'M3': 'S1', 'M4': 'S2', 'M5': 'S2', 'M6': 'S1', 'M7': 'S3', 'M8': 'S3'}
Válida: True
Tiempo: 0.000076 segundos

Local Search ICM
Solución: {'M1': 'S3', 'M2': 'S2', 'M3': 'S2', 'M4': 'S1', 'M5': 'S1', 'M6': 'S3', 'M7': 'S3', 'M8': 'S1'}
Válida: True
Tiempo: 0.000025 segundos

Algoritmo              ¿Solución?   Tiempo (s)
Backtracking           Sí           0.000083
Beam Search (K=5)      Sí           0.000076
Local Search ICM       Sí           0.000025
```

---

### Cómo Ejecutar

```bash
python main.py
```
