# Pytest

Esse repositório tem como objetivo explorar e estudar o desenvolvimento orientado ao TDD (Test-driven development) assim como suas boas utilizando o Pytest.

## Sumário

- [Material de Apoio](#material-de-apoio)
- [Como instalar](#material-de-apoio)
- [Anotações](#minhas-anotações)

## Material de Apoio

A seguir estará disponibilizado algumas das fontes que eu utilizei para criar este repositório:

**Documentação Oficial do Pytest**
- [Docs Pytest](https://docs.pytest.org/en/8.0.x/)

**Lives do Eduardo Mendes**
- [Pytest: Uma introdução - Live de Python #167](https://www.youtube.com/watch?v=MjQCvJmc31A)

**Repositório do Edurado Mendes**
- [Live 168](https://github.com/dunossauro/live-de-python/tree/main/codigo/Live168)

## Como instalar

1. **Clone o Repositório:** No terminal, use o comando `git clone` seguido do URL do repositório do GitHub:
   ```bash
   git clone https://github.com/Jojojmo/pytest-studies.git
   ```


3. **Crie e Ative um Ambiente Virtual:**
   ```bash
   python -m venv .env
   ```
   Em seguida, ative o ambiente virtual:
   - No Windows:
     ```bash
     .env\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source .env/bin/activate
     ```

4. **Instale as Dependências:** Use o `pip` para instalar as dependências listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

Após seguir esses passos, o repositório estará instalado e suas dependências Python estarão configuradas no ambiente virtual, se você optou por utilizá-lo.

Caso queria rodar os testes, escreva o comando `pytest` em seu terminal, também é possível utilizar certas flags, então leia o que elas fazem no [pytest.ini](pytest.ini)

## Minhas Anotações 

Você pode encontrar minhas anotações assim como alguns usos desse repositório [aqui](stuffs/Studies.md)