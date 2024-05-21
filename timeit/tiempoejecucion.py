import timeit

def mi_funcion():
    for a in range(10000):
        a = a + 1
"""       
total_tiempo = timeit.timeit(mi_funcion, number=10000)
print(f"La funcion tomo{total_tiempo}segundos.")
print(f"La funcion tomo{total_tiempo*1000}milisegundos")
print(f"La funcion tomo{total_tiempo*1000000}microsegundos")
"""