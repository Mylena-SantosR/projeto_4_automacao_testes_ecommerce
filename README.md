# Projeto de Testes Automatizados para E-commerce com Selenium e Pytest

Este projeto demonstra a criação de uma suíte de testes automatizados para um site de e-commerce fictício, utilizando Python, Selenium e o framework Pytest.

O site alvo para os testes é o [Sauce Demo](https://www.saucedemo.com/), uma aplicação web feita para praticar automação.

## Tecnologias Utilizadas

* **Linguagem:** Python
* **Automação de Navegador:** Selenium
* **Framework de Testes:** Pytest
* **Gerenciamento de Drivers:** webdriver-manager

## Casos de Teste Cobertos

A suíte de testes atual cobre as seguintes funcionalidades:

1.  **`test_login_com_sucesso`**: Verifica o login com credenciais válidas.
2.  **`test_login_com_usuario_bloqueado`**: Verifica a mensagem de erro para usuários bloqueados.
3.  **`test_login_com_senha_invalida`**: Verifica a mensagem de erro para senhas incorretas.
4.  **`test_adicionar_item_ao_carrinho`**: Verifica se o ícone do carrinho é atualizado após adicionar um produto.
5.  **`test_remover_item_do_carrinho`**: Verifica se um produto pode ser removido com sucesso da página do carrinho.

## Como Executar os Testes

Siga os passos abaixo para rodar a suíte de testes localmente.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    cd nome-do-repositorio
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a suíte de testes:**
    ```bash
    pytest
    ```
O Pytest encontrará e executará todos os testes automaticamente, exibindo o resultado no terminal.
