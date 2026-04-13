
# 🧠 TextMind — Analisador Inteligente de Texto

O **TextMind** é uma ferramenta de linha de comando (CLI) desenvolvida em Python para processamento de linguagem natural (PLN). Ele permite analisar artigos, logs e mensagens, extraindo métricas estatísticas, sentimentos e gerando resumos executivos de forma automatizada.

## 🚀 Funcionalidades

- **Métricas de Texto:** Contagem de palavras totais e únicas.
- **Extração de Keywords:** Identificação das palavras mais relevantes utilizando filtragem de *stopwords* (NLTK).
- **Análise de Sentimento:** Detecção de polaridade textual (Positivo, Negativo ou Neutro).
- **Resumo Inteligente:** Algoritmo de resumo extrativo baseado em saliência de sentenças e distribuição espacial, garantindo que o resumo tenha início, meio e fim.
- **Interface Profissional:** CLI moderna e organizada utilizando a biblioteca `Rich`.

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**
- **NLTK:** Processamento de linguagem natural e tokenização.
- **TextBlob:** Análise de sentimentos.
- **Rich:** Formatação e interface visual no terminal.
- **Regex:** Limpeza e padronização de dados.

## 📦 Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/BrunoRS17/text-mind.git
   cd text-mind
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Baixe os recursos do NLTK:**
   ```bash
   python -m textblob.download_corpora
   python -c "import nltk; nltk.download('stopwords')"
   ```

## 📋 Como Usar

Existem duas formas de utilizar o TextMind:

### Modo Interativo
Basta rodar o comando e colar o texto no terminal:
```bash
python main.py
```
*No Windows, pressione `Ctrl+Z` e `Enter` para finalizar a entrada. No Linux/Mac, `Ctrl+D`.*

### Argumento de Linha de Comando
Para textos curtos, você pode passar o texto diretamente:
```bash
python main.py "O Python é uma linguagem fantástica e muito poderosa para dados."
```


Para este projeto, foquei em resolver dois problemas comuns em análise de texto:
1. **Filtragem de Ruído:** Implementei o uso de *Stopwords* do NLTK para garantir que as palavras-chave fossem semânticas e não apenas conectivos (como "de", "e", "para").
2. **Coesão no Resumo:** Em vez de selecionar apenas as frases com maior pontuação, o algoritmo divide o texto em segmentos (início, meio e fim) e extrai a frase mais relevante de cada parte, preservando a linha narrativa original.

Desenvolvido por Bruno Ribeiro - https://www.linkedin.com/in/bruno-ribeiro-778243264/
```
