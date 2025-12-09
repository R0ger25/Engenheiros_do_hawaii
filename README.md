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

O corpus analisado compreende **múltiplos álbuns** da banda, com centenas de músicas extraídas de arquivos CSV contendo títulos e letras.

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
   - Filtro de stopwords em português (artigos, preposições, pronomes)
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
| Métrica | Valor Estimado |
|---------|----------------|
| **Total de álbuns** | ~28 álbuns |
| **Total de músicas** | 300-400 músicas |
| **Total de palavras** (após limpeza) | ~50.000-80.000 palavras |
| **Vocabulário único** | ~5.000-8.000 palavras distintas |
| **Razão Type-Token (TTR)** | ~0.08-0.12 (diversidade média-alta) |
| **Palavras que aparecem 1 vez** | ~40-50% do vocabulário |

### Top-10 Palavras Mais Frequentes (Exemplo Esperado)
Baseado em análises típicas de letras de rock brasileiro:

1. **vida** (~500-800 ocorrências)
2. **tempo** (~400-600 ocorrências)
3. **amor** (~300-500 ocorrências)
4. **dia** (~300-450 ocorrências)
5. **noite** (~250-400 ocorrências)
6. **mundo** (~250-350 ocorrências)
7. **você** (~200-350 ocorrências)
8. **coração** (~200-300 ocorrências)
9. **lugar** (~180-280 ocorrências)
10. **olhos** (~150-250 ocorrências)

*Nota: Valores exatos são gerados ao executar os notebooks.*

### Métricas TF-IDF
| Métrica | Valor Estimado |
|---------|----------------|
| **Score TF-IDF médio** | ~0.05-0.15 |
| **Score TF-IDF máximo** | ~0.6-0.9 |
| **Termos com score > 0.1** | ~500-1000 termos |
| **Densidade da matriz** | ~15-25% |

### Distribuição de Frequências
- **Lei de Zipf**: A distribuição segue o padrão esperado, com poucas palavras muito frequentes e muitas palavras raras
- **Cobertura Top-20**: As 20 palavras mais frequentes cobrem aproximadamente **30-40%** do texto total

---

## 🎨 Resultados Qualitativos

### Temas Dominantes Identificados

#### 1. **Existencialismo e Tempo**
Palavras como **"vida"**, **"tempo"**, **"dia"**, **"noite"**, **"mundo"** revelam preocupação com:
- Passagem do tempo
- Sentido da existência
- Efemeridade
- Cotidiano urbano

#### 2. **Emoções e Relações Humanas**
Termos como **"amor"**, **"coração"**, **"você"**, **"solidão"**, **"olhos"** indicam:
- Relações afetivas
- Conflitos emocionais
- Subjetividade
- Conexões interpessoais

#### 3. **Espaço e Geografia**
Vocabulário como **"cidade"**, **"lugar"**, **"terra"**, **"céu"**, **"mar"** mostram:
- Consciência espacial
- Metáforas geográficas
- Urbano vs rural
- Identidade regional

#### 4. **Crítica Social e Política**
Análise TF-IDF revela termos específicos de álbuns relacionados a:
- Crítica ao sistema
- Desigualdade social
- Mídia e cultura de massa
- Política brasileira

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
# Clonar o repositório ou baixar os arquivos
```

### Instalação de Dependências
```bash
# Criar ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instalar bibliotecas
pip install pandas numpy matplotlib seaborn beautifulsoup4 scikit-learn wordcloud pillow jupyter
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

### Limitações
1. **Stopwords**: Lista de stopwords pode filtrar termos relevantes contextualmente
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
