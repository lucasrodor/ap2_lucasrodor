## 📊 Sistema de Análise Financeira - AP2
Este é um sistema de análise financeira que auxilia investidores e analistas a tomarem decisões embasadas, utilizando dados reais e estratégias comprovadas. O projeto foi desenvolvido em **Python** com **Streamlit** para o frontend e backend.

## Participantes do Projeto

- Lucas Rodor
    Linkedin: [Lucas Rodor](https://www.linkedin.com/in/lucasrodor/)
    Github: [Lucas Rodor](https://github.com/lucasrodor)

- Bruno Ambrosio
    Linkedin: [Bruno Ambrosio](https://www.linkedin.com/in/brunobianco/)
    Github: [Bruno Ambrosio](https://github.com/BrunoAmbrosioAbs)

- Ludmila Guedes
    Linkedin: [Ludmila Guedes](https://www.linkedin.com/in/ludmila-guedes-810688302/)
    Github: [Ludmila Guedes](https://github.com/LudmilaGuedes) 

- Anna Clara Thimoteo
    Linkedin:[Anna Clara Thimoteo](https://www.linkedin.com/in/anna-clara-thimoteo-de-melo-3584a5323/)
    GitHub:[Anna Clara Thimoteo](https://github.com/AnnaClaraThimoteo)



### 📋 Funcionalidades
- **Exploração de Dados (Planilhão)**:
  - Acesse e filtre dados financeiros de diversas ações.
  - Filtre por setores específicos.
  - Selecione datas válidas (dias úteis) para análise.

- **Geração de Carteira (Estratégia)**:
  - Crie carteiras de investimento personalizadas utilizando a estratégia **Magic Formula**.
  - Escolha indicadores de rentabilidade e desconto.
  - Configure o número de ações na carteira.

- **Visualização de Gráficos**:
  - Compare o desempenho acumulado da sua carteira com o índice **Ibovespa**.
  - Gráficos interativos e visualmente claros.


### 🛠️ Tecnologias Utilizadas
- **Linguagem**: Python 3.11
- **Framework Frontend e Backend**: Streamlit
- **APIs**:
  - Laboratório de Finanças (para dados de ações e preços históricos).
- **Bibliotecas Principais**:
  - `pandas`: Manipulação de dados.
  - `matplotlib`: Visualização de gráficos.
  - `datetime`: Manipulação de datas.
  - `requests`: Consumo de APIs externas.


### 📂 Estrutura do Projeto

projeto_financeiro/
├── backend/
│   ├── views.py             # Funções principais do backend
│   ├── utils.py             # Funções utilitárias (ex.: validação de datas)
│   ├── apis.py              # Conexão com as APIs externas
│   └── config.py            # Configurações gerais e variáveis
├── frontend/
│   ├── inicio.py            # Página inicial
│   ├── planilhao.py         # Página do planilhão
│   ├── estrategia.py        # Página de estratégia
│   ├── graficos.py          # Página de gráficos
├── app.py                   # Arquivo principal para execução do Streamlit
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto



### 🚀 Como Executar o Projeto Localmente
Siga os passos abaixo para configurar e executar o projeto em sua máquina:

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/projeto-financeiro.git
   cd projeto-financeiro
   ```

2. **Crie e Ative um Ambiente Virtual**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # Linux/Mac
   .venv\Scripts\activate       # Windows
   ```

3. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o Arquivo `.env`**:
   - Visite o site [Laboratorio de Finanças](https://laboratoriodefinancas.com/), se registre e pegue o seu token de acesso
   - Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
     ```
     TOKEN=seu_token_da_api
     ```

5. **Execute o Projeto**:
   ```cmd
   streamlit run app.py
   ```

6. **Acesse no Navegador**:
   - O projeto estará disponível em: [http://localhost:8501](http://localhost:8501)


### 📊 Exemplos de Uso

#### 1. Planilhão
- Explore dados financeiros com filtros opcionais por setores.
- Certifique-se de selecionar datas válidas (dias úteis).

#### 2. Estratégia
- Configure os parâmetros para criar sua carteira:
  - Indicador de rentabilidade: `roe`, `roc`, `roic`.
  - Indicador de desconto: `earning_yield`, `dividend_yield`, `p_vp`.

#### 3. Gráficos
- Compare o desempenho acumulado da sua carteira com o Ibovespa em um período selecionado.
- Acesse gráficos anteriores armazenados no sistema.


### 📘 Sobre a Magic Formula
A **Magic Formula** é uma estratégia de investimento desenvolvida por Joel Greenblatt. Ela combina:
1. **Rentabilidade** (qualidade da empresa): Avalia a eficiência da empresa em gerar lucros.
2. **Desconto** (valuation): Mede o quão barata uma ação está em relação ao seu valor intrínseco.

#### **Vantagens:**
- Simples e eficaz.
- Baseada em princípios sólidos de finanças.
- Resultados historicamente superiores ao mercado.

---

### **📂 Planejamento para Futuras Funcionalidades**
1. **Indicadores Avançados**:
   - Adicionar métricas como volatilidade, Beta e Sharpe Ratio.

2. **Notificações**:
   - Alertas automáticos sobre mudanças nos preços ou no desempenho da carteira.

3. **Gráficos Interativos**:
   - Uso de bibliotecas como Plotly para maior interatividade.

4. **Relatórios Personalizados**:
   - Exportação de gráficos e tabelas em formatos como PDF e Excel.

---

### **📞 Suporte e Contribuições**
- **E-mail**: lucasgomessr10@gmail.com
- **Contribua no GitHub**: [Link para o repositório](https://github.com/seu-usuario/projeto-financeiro)

---

### **📄 Licença**
Este projeto está sob a licença MIT. Sinta-se à vontade para utilizá-lo e modificá-lo como desejar. 

---
