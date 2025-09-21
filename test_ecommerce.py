# Importa as bibliotecas necessárias
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time # Usaremos para pequenas pausas visuais

# --- Fixture: Uma preparação que roda antes de cada teste ---
# Esta fixture cria o "driver" (o navegador) para cada teste e o fecha no final.
# Assim, não precisamos repetir o código de abrir/fechar o navegador em todas as funções.
@pytest.fixture
def driver():
    # Inicializa o WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5) # Espera implícita para elementos aparecerem
    
    # "yield" entrega o driver para a função de teste
    yield driver
    
    # O código após o "yield" roda no final do teste para limpeza
    driver.quit()

# --- Suíte de Testes para o E-commerce ---

# Teste 1: Login com Sucesso (Caminho Feliz)
def test_login_com_sucesso(driver):
    """Verifica se o login com credenciais válidas funciona."""
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verificação: Checa se o título da página de produtos está visível
    titulo_da_pagina = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo_da_pagina == "Products"

# Teste 2: Login com Usuário Bloqueado (Caminho Triste)
def test_login_com_usuario_bloqueado(driver):
    """Verifica se a mensagem de erro correta aparece para um usuário bloqueado."""
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verificação: Checa se a mensagem de erro esperada é exibida
    mensagem_erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Sorry, this user has been locked out" in mensagem_erro

# Teste 3: Login com Senha Inválida (Caminho Triste)
def test_login_com_senha_invalida(driver):
    """Verifica se a mensagem de erro correta aparece para uma senha incorreta."""
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("senha_errada")
    driver.find_element(By.ID, "login-button").click()

    # Verificação: Checa se a mensagem de erro esperada é exibida
    mensagem_erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Username and password do not match any user in this service" in mensagem_erro

# Teste 4: Adicionar um Item ao Carrinho (Caminho Feliz)
def test_adicionar_item_ao_carrinho(driver):
    """Verifica se é possível adicionar um item e se o ícone do carrinho atualiza."""
    # Passo 1: Fazer login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Passo 2: Adicionar a mochila ao carrinho
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Verificação: Checa se o ícone do carrinho mostra o número 1
    icone_carrinho = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert icone_carrinho == "1"

# Teste 5: Remover um Item do Carrinho (Caminho Feliz)
def test_remover_item_do_carrinho(driver):
    """Verifica se um item pode ser removido da página do carrinho."""
    # Passo 1: Fazer login e adicionar um item (pré-condições)
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    # Passo 2: Ir para a página do carrinho
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Passo 3: Remover o item
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    
    # Verificação: Checa se o item removido não está mais na lista do carrinho.
    # Se a lista de itens do carrinho estiver vazia, o `find_elements` retornará uma lista vazia.
    itens_no_carrinho = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(itens_no_carrinho) == 0