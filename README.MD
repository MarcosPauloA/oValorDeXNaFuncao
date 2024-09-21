# Algoritmo Genético em Python

Este repositório contém uma implementação de um algoritmo genético em Python para otimização de uma função objetivo.

## Requisitos

- Python 3.x
- Bibliotecas: `random`, `numpy`

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/MarcosPauloA/oValorDeXNaFuncao
    cd oValorDeXNaFuncao
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install numpy
    ```

## Uso

Para executar o algoritmo genético, siga os passos abaixo:

1. Certifique-se de que você está no diretório do projeto.
2. Execute o script Python:
    ```bash
    python oValorDeXNaFuncao.py
    ```

## Código

### Função Objetivo

A função objetivo a ser otimizada é definida como:
```python
def f(x):
    return x**3 - 6*x + 14
