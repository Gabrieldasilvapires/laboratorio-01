import threading
import time

saldo_conta = 0
NUM_OPERACOES = 100000

# Cria o mecanismo de bloqueio para proteger o saldo
lock_bancario = threading.Lock()

def depositar():
    global saldo_conta
    for _ in range(NUM_OPERACOES):
        # Secao critica protegida pelo Lock
        with lock_bancario:
            temp = saldo_conta
            temp = temp + 1
            saldo_conta = temp

def main():
    global saldo_conta

    inicio = time.time()

    print(f"[*] Saldo Inicial: {saldo_conta}")

    t1 = threading.Thread(target=depositar, name="Thread-Caixa-1")
    t2 = threading.Thread(target=depositar, name="Thread-App-2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    fim = time.time()

    saldo_esperado = NUM_OPERACOES * 2

    print(f"[*] Saldo Esperado: {saldo_esperado}")
    print(f"[!] Saldo Obtido: {saldo_conta}")
    print(f"[*] Tempo de Execucao: {fim - inicio:.6f} segundos")

    if saldo_conta == saldo_esperado:
        print("\n[OK] Resultado integro. Lock funcionou!")
    else:
        print("\n[ALERTA] Resultado incorreto.")

if __name__ == "__main__":
    main()
