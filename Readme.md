Este projeto consiste em um sistema simples de **Monitoramento de Teclas (Keylogger)** composto por um cliente que captura as entradas do teclado e um servidor Flask que recebe e exibe esses dados.

---

# ⌨️ Keylogger Client-Server System

Este repositório contém uma ferramenta de monitoramento educacional para captura de teclas em tempo real com envio para um servidor centralizado via requisições HTTP POST.

## 📂 Estrutura do Projeto

* **`flask.py`**: O servidor backend que recebe os logs e os exibe no console.
* **`keylogger.py`**: O script Python cliente que captura o teclado e envia os dados.
* **`key.bat`**: Arquivo executável Windows para instalar dependências e iniciar o cliente automaticamente.



---

## 🚀 Passo a Passo de Configuração

### 1. Preparação do Ambiente

Certifique-se de ter o **Python 3.x** instalado em sua máquina.

### 2. Configuração do Servidor (Onde os dados chegam)

O servidor deve ser iniciado **antes** do cliente para que possa escutar as conexões.

1. Abra um terminal ou CMD na pasta do projeto.
2. Instale o Flask caso não o tenha:
```bash
pip install flask

```


3. Inicie o servidor:
```bash
python flask.py

```


4. O console exibirá: `--- SERVIDOR AGUARDANDO DADOS ---`. O servidor ficará rodando no endereço `http://0.0.0.0:5000`.

### 3. Configuração do Cliente (Onde as teclas são capturadas)

Existem duas formas de iniciar o cliente:

* **Via Arquivo BAT (Recomendado no Windows):**
Basta dar um duplo clique em `key.bat`. Ele tentará instalar as bibliotecas `pynput` e `requests` automaticamente e iniciará o monitoramento.


* **Via Python Manualmente:**
1. Instale as bibliotecas: `pip install pynput requests`.
2. Execute: `python keylogger.py`.



---

---

## 🛠️ Detalhes Técnicos

| Componente | Função |
| --- | --- |
| **Captura** | Utiliza a biblioteca `pynput` para ouvir eventos do teclado. |
| **Buffer** | As teclas são acumuladas localmente e enviadas em intervalos para evitar sobrecarga de rede. |
| **Envio** | O envio é feito via `threading` (em segundo plano) para não travar a captura enquanto comunica com o servidor. |
| **Servidor** | O Flask recebe os dados via rota `/receber_dados` e imprime no console com carimbo de data/hora. |

> [!IMPORTANT]
> **Aviso Ético:** Este software deve ser utilizado exclusivamente para fins educacionais ou de diagnóstico em máquinas de sua propriedade. O monitoramento de terceiros sem autorização expressa é ilegal e antiético.
