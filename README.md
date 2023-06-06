# Projeto Python FATEC
Projeto desenvolvido para a matéria Tópicos Especiais em Informática.

## Sobre a aplicação:

### A aplicação em si é um sistema de Biblioteca.

### O Usuário tem como opção de entrada realizar o 'Login', realizar o 'Cadastro' de um Login Novo, a opção Sobre a aplicação e Sair do Sistema.

### Além disso realizamos a criação de um 'Menu' específico para quando realizar o acesso pelas credenciais do Administrador do Sistema. Nele conterá algumas opções diferentes como: Importar os dados do Banco de Dados para um arquivo JSON compactado, Exportar o Banco de dados (BKP), Importar um Banco de Dados, realizar a liberação do Usuário (Após a criação, o usuários não está autorizado a acessar o Sistema até que haja a confirmação do Administrador) e Realizar a importação de Dados WEB (será registrado no banco de dados os dados 'pegos').

### Após a realização de um login não administrador, esse terá acesso ao Menu principal da aplicação, onde poderá realizar operações como: Cadastro de Livros, de Leitores, realizar retirada de Livros, devoluções/renovações, e tem a possibilidade de realizar a importação de dados como os livros registrados, os leitores, uma listagem das retiradas (pode-se denominar como a área de relatórios). Também no menu traz a opção de informação do Sistema, 'Sobre'.

### Para finalizar estamos contentes com o resultado, por mais que não colocamos nenhuma interface complexa, mas algo simples e que cumpriu com todos os requisitos necessários passados pelo Professor.

## Bibliotecas utilizadas:
### Abaixo será listados bibliotecas que foram úteis para a realização do nosso Sistema. É válido deixar evidente que são essenciais para o funcionamento do nosso sistema, além de que desenvolvemos na ferramenta VSCode o qual ajudou muito para chegarmos ao resultado mostrado nesse projeto.

### Banco de dados: 
* SGBD SQLite3: pip install sqlite3

### Destacamos que para a validação utilizamos o Try Except e para que o erro específico para cada situação fosse mostrado, utilizamos o sqlite3.Error para capturar esse erro e mostrar no console.
### Para o VSCode utilizamos uma extensão para melhor visualizar o Banco de Dados produzido de forma visual e fácil de manuseá-lo.

### Dando início as bibliotecas utilizadas mais a fundo do sistema citamos:

* import os (realizar manipulação do Sistema/console)
* from click import pause (realizar uma pausa até pressionar alguma tecla)
* import time (realizar uma pausa ‘time.sleep(tempo de espera)’)
* from datetime import datetime, timedelta (realizar a manipulação de data/dias)
* from tqdm import tqdm (realizar uma visualização de carregamento de arquivo no início)
* from getpass import getpass (ocultar a senha)
* import requests (pegar os dados da página)
* from lxml import html (Para realizar na conversão da página em TXT)
* import json (realizar a manipulação de arquivos JSON)
* import zipfile (realizar a manipulação de arquivos ZIP)
* import xlsxwriter (realizar a manipulação de arquivos XLSX)

Projeto Desenvolvido por Álifi Augusto Estevam dos Santos e Rafael Augusto Pereira Rodrigues.