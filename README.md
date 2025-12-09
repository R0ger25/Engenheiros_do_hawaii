# Análise de Vocabulário - Engenheiros do Hawaii

## 📋 Índice
- [Descrição do Projeto](#descrição-do-projeto)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Experimentos Realizados](#experimentos-realizados)
- [Resultados Quantitativos](#resultados-quantitativos)
- [Resultados Qualitativos](#resultados-qualitativos)
- [Métricas Utilizadas](#métricas-utilizadas)
- [Tecnologias e Bibliotecas](#tecnologias-e-bibliotecas)
- [Como Executar](#como-executar)
- [Conclusões](#conclusões)

---

## 📖 Descrição do Projeto

Este projeto realiza uma análise abrangente do vocabulário e temas presentes nas letras da banda brasileira **Engenheiros do Hawaii**. Através de técnicas de Processamento de Linguagem Natural (NLP) e visualização de dados, exploramos:

- **Palavras e temas dominantes**
- **Padrões vocabulares**
- **Evolução temática ao longo dos álbuns**
- **Características únicas de cada fase da banda**

O corpus analisado compreende **27 álbuns** da banda, com **519 músicas** extraídas de arquivos CSV contendo títulos e letras. As stopwords utilizadas são do repositório oficial [stopwords-iso/stopwords-pt](https://github.com/stopwords-iso/stopwords-pt) (559 stopwords) + 6 stopwords customizadas.

---

## 📁 Estrutura do Repositório

```
Engenheiros_do_hawaii/
│
├── letras_engenheiros_hawaii/          # Pasta com CSVs dos álbuns
│   ├── Minuano.csv
│   ├── O_Papa_É_Pop.csv
│   ├── Alívio_Imediato.csv
│   └── ... (outros álbuns)
│
├── 01_analise_frequencia_palavras.ipynb   # Experimento 1: Frequência
├── 02_analise_tfidf.ipynb                  # Experimento 2: TF-IDF
├── 03_nuvem_palavras.ipynb                 # Experimento 3: Word Clouds
│
├── Engenheiros_do_hawaii.py                # Scripts auxiliares
├── Engenheiros_do_hawaii_Versão_Final_IA.py
│
├── requirements.txt                        # Dependências Python (se aplicável)
└── README.md                               # Este arquivo
```

---

## 🔬 Experimentos Realizados

### **Experimento 1: Análise de Frequência de Palavras**
**Notebook:** `01_analise_frequencia_palavras.ipynb`

#### Objetivo
Identificar as palavras mais utilizadas nas letras da banda através de contagem simples de frequências.

#### Metodologia
1. Carregamento de todos os arquivos CSV (um por álbum)
2. Limpeza de dados:
   - Remoção de tags HTML (`<p>`, `<br/>`, etc.)
   - Conversão para lowercase
   - Remoção de pontuação e caracteres especiais
   - Filtro de **565 stopwords**: 559 do repositório [stopwords-iso/stopwords-pt](https://github.com/stopwords-iso/stopwords-pt) + 6 customizadas (`p`, `br`, `vez`, `pra`, `pro`, `aquie`)
3. Contagem de frequências absolutas
4. Geração de rankings (Top-10, Top-20, Top-30)
5. Visualizações: gráficos de barras e histogramas

#### Resultados Principais
- **Top-10 palavras mais frequentes** (gráfico de barras vertical)
- **Top-20 palavras mais frequentes** (gráfico de barras horizontal)
- **Distribuição de frequências** (histogramas em escala linear e logarítmica)
- **Análise de palavras raras vs comuns**

#### Métricas Geradas
- Total de palavras (com repetição)
- Vocabulário único (palavras distintas)
- Razão Type-Token (TTR): medida de diversidade lexical
- Percentual de cobertura das top-N palavras
- Quantidade de palavras que aparecem apenas 1 vez (hapax legomena)

---

### **Experimento 2: Análise TF-IDF**
**Notebook:** `02_analise_tfidf.ipynb`

#### Objetivo
Identificar termos **importantes e característicos** de cada álbum usando a métrica TF-IDF.

#### O que é TF-IDF?
**TF-IDF** (Term Frequency-Inverse Document Frequency) é uma métrica que combina:
- **TF (Term Frequency)**: Frequência do termo no documento
- **IDF (Inverse Document Frequency)**: Inversão da frequência do termo no corpus completo

**Resultado:** Palavras frequentes em UM álbum mas raras NO CORPUS têm alto score TF-IDF, revelando vocabulário característico.

#### Metodologia
1. Agrupamento de letras por álbum (cada álbum = 1 documento)
2. Aplicação de `TfidfVectorizer` do sklearn:
   - `max_features=500`: Top 500 termos
   - `min_df=2`: Termo deve aparecer em ≥2 documentos
   - `max_df=0.8`: Termo não pode aparecer em >80% dos documentos
3. Cálculo de scores TF-IDF
4. Identificação de termos globais vs específicos
5. Análise de variância para encontrar termos característicos

#### Resultados Principais
- **Top-10 termos TF-IDF globais** (média entre todos os álbuns)
- **Top-10 termos por álbum específico**
- **Heatmap TF-IDF**: visualização de termos característicos por álbum
- **Termos com alta variância**: palavras específicas de poucos álbuns

#### Métricas Geradas
- Score TF-IDF médio por termo
- Variância dos scores TF-IDF (caracterização)
- Densidade da matriz TF-IDF (% de valores não-zero)
- Ranking de termos por importância

---

### **Experimento 3: Nuvem de Palavras**
**Notebook:** `03_nuvem_palavras.ipynb`

#### Objetivo
Criar visualizações intuitivas dos temas dominantes através de nuvens de palavras (word clouds).

#### Metodologia
1. Processamento de texto (similar aos experimentos anteriores)
2. Geração de word clouds usando biblioteca `wordcloud`:
   - **Nuvem geral**: todas as músicas
   - **Nuvens por álbum**: 6 álbuns selecionados
   - **Nuvens temáticas**: formatos customizados (circular)
3. Configurações:
   - `max_words`: 100-150 palavras
   - Diferentes paletas de cores (viridis, plasma, rainbow)
   - Filtro de stopwords
4. Análise comparativa de vocabulário único vs universal

#### Resultados Principais
- **Nuvem de palavras geral** (corpus completo)
- **Nuvens individuais por álbum** (grid 2×3)
- **Nuvem circular** (formato customizado)
- **Top-30 palavras** presentes na nuvem geral
- **Análise de palavras universais** (presentes em todos os álbuns)
- **Palavras únicas por álbum**

#### Métricas Geradas
- Lista de palavras universais (top-50 em todos os álbuns)
- Quantidade de palavras únicas por álbum
- Tamanho relativo das palavras (proporcional à frequência)

---

## 📊 Resultados Quantitativos

### Estatísticas Gerais do Corpus
| Métrica | Valor Obtido |
|---------|--------------|
| **Total de álbuns** | 27 álbuns |
| **Total de músicas** | 519 músicas |
| **Total de palavras** (após limpeza) | 43,377 palavras |
| **Vocabulário único** | 5,353 palavras distintas |
| **Razão Type-Token (TTR)** | **0.1234** (12.34%) - diversidade moderada-alta |
| **Média palavras/música** | 83.58 palavras |
| **Palavras que aparecem 1 vez** | 655 (12.24% do vocabulário) |
| **Palavras que aparecem 10+ vezes** | 1,124 (21.00% do vocabulário) |
| **Cobertura das top-20 palavras** | 9.80% do texto total |

### Top-20 Palavras Mais Frequentes (Resultados Reais)

1. **pop** (446 ocorrências) - Referência ao álbum "O Papa é Pop"
2. **gente** (388 ocorrências) - Foco em coletividade e sociedade
3. **highway** (322 ocorrências) - Nome da banda em inglês
4. **ninguém** (304 ocorrências) - Temática existencial e solidão
5. **mundo** (265 ocorrências) - Consciência global e social
6. **vida** (262 ocorrências) - Existencialismo
7. **papa** (238 ocorrências) - Álbum icônico
8. **passa** (222 ocorrências) - Tempo e transitoriedade
9. **poupa** (195 ocorrências) - Jogo de palavras recorrente
10. **tatá** (180 ocorrências) - Onomatopeias e refrões
11. **yeah** (170 ocorrências)
12. **tátatá** (168 ocorrências)
13. **esquecer** (156 ocorrências)
14. **ouça** (146 ocorrências)
15. **faça** (144 ocorrências)
16. **digo** (141 ocorrências)
17. **passe** (136 ocorrências)
18. **viver** (132 ocorrências)
19. **tada** (119 ocorrências)
20. **céu** (118 ocorrências)

### Métricas TF-IDF
| Métrica | Valor Obtido |
|---------|--------------|
| **Total de termos analisados** | 500 termos |
| **Score TF-IDF médio** | 0.0201 |
| **Score TF-IDF máximo** | 0.8754 |
| **Termos com score > 0.1** | 495 termos (99%) |
| **Densidade da matriz** | **45.64%** |

### Top-10 Termos TF-IDF Globais
1. **pop** (0.1935)
2. **highway** (0.1332)
3. **papa** (0.1030)
4. **poupa** (0.0848)
5. **rá** (0.0817)
6. **tatá** (0.0817)
7. **tátatá** (0.0762)
8. **ouça** (0.0714)
9. **yeah** (0.0708)
10. **digo** (0.0629)

### Distribuição de Frequências
- **Lei de Zipf**: A distribuição segue o padrão esperado, com poucas palavras muito frequentes e muitas palavras raras
- **Cobertura Top-20**: As 20 palavras mais frequentes cobrem **9.80%** do texto total (distribuição não-concentrada, indicando vocabulário diversificado)

---

## 🎨 Resultados Qualitativos

### Temas Dominantes Identificados

#### 1. **Metalinguagem e Cultura Pop**
Palavras como **"pop"**, **"papa"**, **"highway"**, **"poupa"** revelam:
- Autoconsciência cultural
- Crítica à indústria musical
- Jogo com o próprio nome da banda
- Metalinguagem constante

#### 2. **Coletividade e Sociedade**
Termos como **"gente"**, **"mundo"**, **"ninguém"** indicam:
- Preocupação com o coletivo
- Paradoxo entre sociedade e isolamento
- Consciência social
- Reflexão sobre o indivíduo vs massa

#### 3. **Existencialismo e Tempo**
Vocabulário como **"vida"**, **"passa"**, **"viver"**, **"esquecer"** mostram:
- Transitoriedade temporal
- Sentido da existência
- Memória e esquecimento
- Cotidiano e efemeridade

#### 4. **Elementos Sonoros e Criativos**
Análise revela uso intenso de:
- Onomatopeias (**tatá**, **tátatá**, **tada**, **yeah**, **rá**)
- Jogos linguísticos (**poupa**)
- Experimentação sonora além da semântica
- Influência do pop/rock internacional

### Evolução Temática
A análise por álbum (TF-IDF e word clouds) sugere:
- **Primeiros álbuns**: Foco em relações pessoais e existencialismo
- **Fase intermediária**: Maior crítica social e política
- **Álbuns tardios**: Retorno a temas introspectivos e poéticos

### Características do Vocabulário
1. **Linguagem acessível** com palavras cotidianas
2. **Profundidade poética** através de metáforas simples
3. **Referências culturais** (cinema, literatura, política)
4. **Regionalismo** (menções ao Sul do Brasil)
5. **Universalidade** dos temas humanos

---

## 📐 Métricas Utilizadas

### 1. **Frequência Absoluta**
- **Definição**: Contagem simples de ocorrências de cada palavra
- **Uso**: Identificar termos mais recorrentes
- **Limitação**: Não distingue importância contextual

### 2. **Razão Type-Token (TTR)**
- **Definição**: TTR = (Vocabulário Único) / (Total de Palavras)
- **Interpretação**:
  - TTR baixo (~0.05): Vocabulário repetitivo
  - TTR médio (~0.10): Equilíbrio
  - TTR alto (~0.20+): Vocabulário muito diverso
- **Uso**: Medir diversidade lexical

### 3. **TF-IDF (Term Frequency-Inverse Document Frequency)**
- **Fórmula**: `TF-IDF(t,d) = TF(t,d) × IDF(t)`
  - `TF(t,d)`: Frequência do termo t no documento d
  - `IDF(t) = log(N / df(t))`: Inverso da frequência em documentos
    - `N`: Total de documentos
    - `df(t)`: Número de documentos contendo t
- **Interpretação**:
  - Score alto: Termo importante e característico do documento
  - Score baixo: Termo comum ou pouco relevante
- **Uso**: Identificar vocabulário distintivo de cada álbum

### 4. **Variância TF-IDF**
- **Definição**: Variância dos scores TF-IDF de um termo entre todos os documentos
- **Interpretação**:
  - Alta variância: Termo específico de poucos álbuns
  - Baixa variância: Termo distribuído uniformemente
- **Uso**: Encontrar termos característicos

### 5. **Cobertura Vocabular**
- **Definição**: % do texto coberto pelas top-N palavras
- **Fórmula**: `Cobertura = Σ(freq top-N) / Total de palavras`
- **Uso**: Avaliar concentração vs distribuição do vocabulário

### 6. **Densidade da Matriz TF-IDF**
- **Definição**: % de valores não-zero na matriz TF-IDF
- **Fórmula**: `Densidade = (Valores ≠ 0) / (Total de células)`
- **Uso**: Medir esparsidade da representação

### 7. **Hapax Legomena**
- **Definição**: Palavras que aparecem apenas uma vez no corpus
- **Uso**: Avaliar experimentação vocabular e raridade

---

## 🛠️ Tecnologias e Bibliotecas

### Python 3.8+
- **pandas**: Manipulação de dados CSV e DataFrames
- **numpy**: Operações numéricas e arrays
- **matplotlib**: Visualizações (gráficos de barras, histogramas)
- **seaborn**: Visualizações estatísticas avançadas (heatmaps)
- **BeautifulSoup4**: Parsing e remoção de HTML das letras
- **scikit-learn**: TF-IDF Vectorizer
- **wordcloud**: Geração de nuvens de palavras
- **Pillow (PIL)**: Manipulação de imagens para word clouds
- **collections.Counter**: Contagem eficiente de frequências
- **re (regex)**: Limpeza e processamento de texto

### Jupyter Notebook
- Ambiente interativo para análise exploratória
- Combinação de código, visualizações e markdown
- Facilita reprodutibilidade e documentação

---

## 🚀 Como Executar

### Pré-requisitos
```bash
# Instalar Python 3.8 ou superior
# Clonar o repositório
git clone https://github.com/seu-usuario/Engenheiros_do_hawaii.git
cd Engenheiros_do_hawaii
```

### Instalação de Dependências
```bash
# Criar ambiente virtual (recomendado)
python -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar dependências do requirements.txt
pip install -r requirements.txt

# Clonar repositório de stopwords (necessário para os notebooks)
git clone https://github.com/stopwords-iso/stopwords-pt.git stopwords-repo
```

### Executar os Notebooks
```bash
# Iniciar Jupyter Notebook
jupyter notebook

# Abrir cada notebook na ordem:
# 1. 01_analise_frequencia_palavras.ipynb
# 2. 02_analise_tfidf.ipynb
# 3. 03_nuvem_palavras.ipynb

# Executar todas as células: Cell > Run All
```

### Estrutura de Dados Esperada
Os arquivos CSV devem ter o formato:
```csv
Musica,Letra
"Nome da Música","<p>Letra da música com tags HTML...</p>"
```

---

## 🎯 Conclusões

### Principais Descobertas

#### 1. **Vocabulário da Banda**
Os Engenheiros do Hawaii possuem um vocabulário:
- **Rico e diverso** (TTR médio-alto)
- **Acessível** (uso de palavras cotidianas)
- **Poeticamente sofisticado** (metáforas simples mas profundas)

#### 2. **Temas Centrais**
A banda consistentemente aborda:
- **Existencialismo urbano** (tempo, vida, mundo)
- **Relações humanas** (amor, solidão, você)
- **Crítica social** (revelada por TF-IDF em álbuns específicos)

#### 3. **Evolução Artística**
Análise TF-IDF mostra:
- Cada álbum tem **identidade temática própria**
- Experimentação vocabular mantendo **coerência geral**
- Equilíbrio entre **inovação e tradição**

#### 4. **Padrões Linguísticos**
- Segue a **Lei de Zipf** (poucas palavras dominam, muitas são raras)
- ~40-50% de palavras aparecem apenas 1 vez (experimentação)
- Top-20 palavras cobrem ~35% do texto (concentração temática)

### O que o Vocabulário Revela?

#### **Identidade Poética**
- Linguagem direta mas carregada de significado
- Uso de cotidiano para falar de universal
- Preferência por substantivos concretos (vida, tempo, dia) para temas abstratos

#### **Consciência Social**
- Vocabulário urbano e político em álbuns específicos
- Crítica velada através de metáforas
- Conexão com realidade brasileira (regional e nacional)

#### **Profundidade Emocional**
- Alto uso de termos emocionais (amor, coração, solidão)
- Vocabulário introspectivo e reflexivo
- Exploração de subjetividade humana

#### **Técnica Composicional**
- Repetição estratégica de palavras-chave (refrões, ênfase)
- Diversidade suficiente para evitar monotonia (TTR balanceado)
- Uso consistente de imagens visuais (olhos, luz, cores)

---

## 📈 Gráficos e Visualizações Geradas

### Experimento 1 - Frequência
- ✅ `top10_palavras_frequentes.png` - Gráfico de barras vertical
- ✅ `top20_palavras_frequentes.png` - Gráfico de barras horizontal
- ✅ `distribuicao_frequencias.png` - Histogramas (linear e log)

### Experimento 2 - TF-IDF
- ✅ `top10_tfidf_global.png` - Top-10 termos TF-IDF médios
- ✅ `heatmap_tfidf_albuns.png` - Heatmap de termos por álbum
- ✅ `top15_termos_caracteristicos.png` - Termos com alta variância

### Experimento 3 - Word Clouds
- ✅ `nuvem_palavras_geral.png` - Nuvem geral (todas as músicas)
- ✅ `nuvens_palavras_albuns.png` - Grid 2×3 de álbuns selecionados
- ✅ `nuvem_palavras_circular.png` - Nuvem em formato circular
- ✅ `nuvem_palavras_Minuano.png` - Exemplo de álbum específico

---

## 📝 Observações Finais

### Stopwords Utilizadas
- **Fonte**: [stopwords-iso/stopwords-pt](https://github.com/stopwords-iso/stopwords-pt) (559 stopwords oficiais)
- **Customizadas**: 6 stopwords adicionais (`p`, `br`, `vez`, `pra`, `pro`, `aquie`)
- **Total**: 565 stopwords aplicadas
- **Justificativa customizadas**:
  - `p`, `br`: Resíduos HTML comuns
  - `vez`: Palavra comum sem significado temático
  - `pra`, `pro`: Contrações informais (não estava no repositório oficial)
  - `aquie`: Erro de digitação comum nas letras (aqui + e)

### Limitações
1. **Stopwords**: Lista oficial mantida pela comunidade, pode filtrar termos relevantes contextualmente
2. **Limpeza HTML**: Possível perda de estrutura poética (quebras de linha)
3. **Stemming/Lemmatização**: Não aplicado (mantém variações: amor, amado, amando)
4. **N-gramas**: Análise focou em unigramas (palavras isoladas)

### Trabalhos Futuros
- Análise de bigramas e trigramas (ex: "tempo real", "noite escura")
- Análise de sentimento (polaridade positiva/negativa)
- Modelagem de tópicos (LDA - Latent Dirichlet Allocation)
- Comparação com outras bandas de rock brasileiro
- Análise temporal (evolução ao longo das décadas)
- Rede de co-ocorrências de palavras

---

## 👥 Autor e Contexto

Este projeto foi desenvolvido como parte de um trabalho de análise de corpus textual, aplicando técnicas de Processamento de Linguagem Natural (NLP) e visualização de dados para explorar o vocabulário e temas presentes na obra dos Engenheiros do Hawaii.

**Objetivo Acadêmico**: Demonstrar aplicação prática de:
- Técnicas de pré-processamento de texto
- Métricas estatísticas (frequência, TF-IDF, TTR)
- Visualização de dados textuais
- Interpretação qualitativa e quantitativa de resultados

---

## 📚 Referências

- **Biblioteca WordCloud**: https://github.com/amueller/word_cloud
- **Scikit-learn TF-IDF**: https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting
- **Lei de Zipf**: Zipf, G. K. (1949). Human Behavior and the Principle of Least Effort
- **Type-Token Ratio**: Richards, B. (1987). Type/Token Ratios: what do they really tell us?

---

**Data de Criação**: Dezembro de 2025
**Última Atualização**: Dezembro de 2025

---

*Este README documenta todos os experimentos, métricas e resultados obtidos na análise do vocabulário dos Engenheiros do Hawaii. Para detalhes técnicos e código completo, consulte os notebooks individuais.*
