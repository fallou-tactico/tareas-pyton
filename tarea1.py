import time


def obtener_guardar_y_sumar_primos(limite, archivo_salida):
    print(f"Calculando números primos del 1 al {limite:,}...")
    inicio = time.time()

    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False

    for i in range(2, int(limite**0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False

    primos = [num for num, primo in enumerate(es_primo) if primo]

    suma_total = sum(primos)

    print("Guardando resultados en el archivo...")
    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        for numero in primos:
            archivo.write(f"{numero}\n")

    fin = time.time()
    tiempo_total = fin - inicio

    print(f"Suma total de los primos:    {suma_total:,}")
    print(f"Archivo guardado como:       {archivo_salida}")


if __name__ == "__main__":
    LIMITE = 2_000_000
    NOMBRE_ARCHIVO = "primos_2M.txt"
    obtener_guardar_y_sumar_primos(LIMITE, NOMBRE_ARCHIVO)