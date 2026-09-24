# Laboratório 01 — Concorrência, Threads e Race Conditions

## Disciplina
Sistemas Operacionais — ADS 2026.2

## Objetivo

O objetivo deste laboratório foi compreender o funcionamento de threads, concorrência e condições de corrida, além de aplicar um mecanismo de sincronização utilizando `Lock`.

## Parte 1 — Condição de Corrida

Na primeira parte foi desenvolvido o arquivo `conta_bancaria_insegura.py`.

O programa utiliza duas threads para realizar 100.000 operações de depósito cada uma. O saldo esperado ao final é de 200.000.

A operação de atualização do saldo não é atômica, pois envolve leitura, modificação e escrita:

```python
temp = saldo_conta
temp = temp + 1
saldo_conta = temp

