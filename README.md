# raspagem-de-dados-2
Este script em Python usa Selenium para verificar a disponibilidade de domínios no site registro.br. Ele consulta automaticamente, captura o status do domínio e salva os resultados em um arquivo JSON. Funciona no modo headless para maior eficiência, sendo ideal para quem deseja monitorar domínios sem acessar o site manualmente. 🚀

# Verificador de Domínios no Registro.br

Este script em Python utiliza **Selenium** para verificar a disponibilidade de domínios no **registro.br**.

## 📌 Funcionalidades

- Consulta a disponibilidade de domínios **.com.br**.
- Retorna um JSON com os resultados, incluindo detalhes da verificação.
- Opera no modo **headless**, sem abrir a interface do navegador.

## 🚀 Requisitos

- Python 3.8+
- Firefox instalado
- [Geckodriver](https://github.com/mozilla/geckodriver/releases) compatível com sua versão do Firefox

## 📦 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/verificador-dominios.git
   cd verificador-dominios
