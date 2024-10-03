# 🌍 Global Temperature Analysis Project 🔥

Este projeto tem como objetivo analisar e visualizar dados históricos de temperatura global, explorando as variações de temperatura por país e ao longo dos anos. Utilizando ferramentas de visualização interativa e análise de dados, ele facilita a compreensão das mudanças climáticas globais.

## 📋 Funcionalidades

- **Visualização de temperaturas médias por país:**
  - Mapa interativo de cores (choropleth map), onde cada país é colorido de acordo com sua temperatura média.
  
- **Análise temporal da temperatura global:**
  - Gráfico de linha interativo mostrando a evolução das temperaturas médias globais anuais.
  - Inclusão de faixas de incerteza para ilustrar as variações na medição de temperatura.

## 🛠️ Tecnologias Utilizadas

- **Pandas:** Para manipulação e agregação de dados.
- **Plotly Express:** Para criar gráficos interativos, como o mapa de calor e gráficos de linha.
- **Seaborn:** (Opcional) Para visualizações adicionais.
- **NumPy:** Para operações matemáticas (uso leve).
- **Python:** Linguagem principal do projeto.

## 📂 Estrutura do Projeto

```bash
├── tabelas/                     # Diretório com os datasets CSV
│   ├── GlobalLandTemperaturesByCountry.csv
│   └── GlobalTemperatures.csv
├── main.py                      # Script principal para análise e visualização
├── README.md                    # Instruções do projeto
└── .venv/                       # Ambiente virtual Python (se necessário)
