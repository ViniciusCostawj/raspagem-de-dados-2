from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
from datetime import datetime

def verificar_dominio(dominio):
    """Verifica a disponibilidade de um domínio no registro.br"""
    config = {
        "geckodriver_path": r"C:\drivers\geckodriver.exe",
        "firefox_path": r"C:\Program Files\Mozilla Firefox\firefox.exe"
    }
    
    # Configuração do WebDriver
    service = Service(config["geckodriver_path"])
    options = Options()
    options.binary_location = config["firefox_path"]
    options.add_argument("--headless")  # headless aqui
    driver = webdriver.Firefox(service=service, options=options)

    resultado = {
        "dominio": dominio,
        "disponivel": None,
        "mensagem": "",
        "detalhes": "",
        "data_consulta": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "url": ""
    }

    try:
        print(f"\nVerificando: {dominio}")
        
        # Acessa o site
        driver.get("https://registro.br")
        time.sleep(2)
        
        # campo de pesquisa
        search_box = driver.find_element(By.CSS_SELECTOR, 'input#is-avail-field')
        search_box.clear()
        search_box.send_keys(dominio)
        search_box.send_keys(Keys.RETURN)
        print("Pesquisa enviada...")
        
        # resultado
        time.sleep(3)
        page_text = driver.find_element(By.TAG_NAME, 'body').text
        resultado["url"] = driver.current_url
        
        # validando a resposta
        if "Domínio não disponível" in page_text:
            resultado["disponivel"] = False
            resultado["mensagem"] = "Domínio não disponível"
        elif "Domínio disponível" in page_text:
            resultado["disponivel"] = True
            resultado["mensagem"] = "Domínio disponível"
        else:
            resultado["mensagem"] = "Status indeterminado"
        
        # guardando detalhes adicionais
        linhas = [linha.strip() for linha in page_text.split('\n') 
                 if dominio.lower() in linha.lower() 
                 or 'domínio' in linha.lower()]
        resultado["detalhes"] = "\n".join(linhas)
        
        return resultado
    
    except Exception as e:
        resultado["erro"] = str(e)
        return resultado
    
    finally:
        driver.quit()
        print("Consulta concluída")

def salvar_json(resultados, arquivo="resultados_dominios.json"):
    """Salva os resultados em formato JSON"""
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    print(f"\nResultados salvos em {arquivo}")

# Exemplo 
if __name__ == "__main__":
    dominios = ["exemplo.com.br", "teste123.com.br", "google.com.br"]
    resultados = []
    
    for dominio in dominios:
        resultado = verificar_dominio(dominio)
        resultados.append(resultado)
        time.sleep(2)  # Intervalo entre consultas
    
    # Salvando os resultados
    salvar_json(resultados)
    
    # resumo
    print("\nResumo das verificações:")
    for r in resultados:
        status = "DISPONÍVEL" if r.get("disponivel") else "INDISPONÍVEL"
        print(f"{r['dominio']}: {status} - {r.get('mensagem', '')}")