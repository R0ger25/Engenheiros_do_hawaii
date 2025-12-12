# Análise de Similaridade de Letras - Engenheiros do Hawaii

## Descrição

Este projeto realiza uma análise completa de similaridade temática entre as letras de músicas dos Engenheiros do Hawaii utilizando técnicas avançadas de Processamento de Linguagem Natural (NLP).

## Arquivo Principal

**`analise_similaridade_letras.ipynb`** - Notebook Jupyter completo com todas as análises

## Objetivos

1. Gerar embeddings semânticos das letras usando sentence-transformers
2. Calcular similaridade cosseno entre todas as músicas
3. Visualizar resultados através de gráficos e mapas interativos
4. Identificar clusters temáticos nas músicas
5. Exportar resultados para análise posterior

## Requisitos

### Python
- Python 3.8 ou superior
- Conexão com internet (para download automático de pacotes na primeira execução)

### Bibliotecas (Instaladas Automaticamente)

O notebook instala automaticamente todos os pacotes necessários! Você não precisa instalar nada manualmente.

#### Pacotes Obrigatórios (instalados automaticamente):
- pandas
- numpy
- sentence-transformers
- scikit-learn
- matplotlib
- seaborn
- plotly
- beautifulsoup4

#### Pacotes Opcionais (instalados automaticamente se possível):
- umap-learn (para redução dimensional UMAP)
- networkx (para visualização de grafos)

## Instalação

### Opção 1: Execução Direta (Recomendado)

**O notebook é autossuficiente!** Simplesmente abra e execute:

```bash
jupyter notebook analise_similaridade_letras.ipynb
```

A primeira célula do notebook instalará automaticamente todos os pacotes necessários.

### Opção 2: Instalação Manual (Opcional)

Se preferir instalar os pacotes manualmente antes de executar:

```bash
pip install pandas numpy sentence-transformers scikit-learn matplotlib seaborn plotly beautifulsoup4 umap-learn networkx
```

Ou use o ambiente virtual:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Instalar pacotes
pip install pandas numpy sentence-transformers scikit-learn matplotlib seaborn plotly beautifulsoup4 umap-learn networkx
```

## Estrutura de Arquivos Necessária

```
Engenheiros_do_hawaii/
├── analise_similaridade_letras.ipynb    # Notebook principal
├── letras_engenheiros_hawaii/           # Pasta com CSVs
│   ├── Album1.csv
│   ├── Album2.csv
│   └── ...
└── INSTRUCOES_SIMILARIDADE.md          # Este arquivo
```

### Formato dos Arquivos CSV

Cada CSV deve conter duas colunas:
- `Musica`: Nome da música
- `Letra`: Letra da música (pode conter HTML)

## Como Executar

### 1. Abrir o Notebook

```bash
jupyter notebook analise_similaridade_letras.ipynb
```

Ou use o JupyterLab:
```bash
jupyter lab analise_similaridade_letras.ipynb
```

### 2. Executar a Primeira Célula (Instalação Automática)

**IMPORTANTE**: Execute a primeira célula (Seção 0) para instalar automaticamente todas as dependências.

- Esta célula verifica quais pacotes estão instalados
- Instala automaticamente os pacotes faltantes
- Mostra o progresso da instalação
- Na primeira vez, pode demorar 5-10 minutos

### 3. Executar as Demais Células

Após a instalação, execute as células sequencialmente usando **Shift + Enter** ou clicando em "Run All" no menu.

### 4. Tempo de Execução Total

- **Primeira execução completa**: 15-30 minutos
  - Instalação de pacotes: 5-10 minutos
  - Download do modelo sentence-transformers (~500MB): 3-5 minutos
  - Processamento de todas as letras: 5-15 minutos

- **Execuções posteriores**: 3-8 minutos
  - Pacotes já instalados (verificação rápida)
  - Modelo já está em cache local
  - Pode reutilizar embeddings salvos

## Seções do Notebook

### Seção 0: Instalação Automática de Dependências
- **EXECUTE ESTA CÉLULA PRIMEIRO!**
- Verificação automática de pacotes instalados
- Instalação automática de pacotes faltantes
- Mensagens de progresso e status

### Seção 1: Setup e Importações
- Importação de bibliotecas
- Verificação de versões
- Configuração do ambiente

### Seção 2: Carregamento de Dados
- Leitura de todos os CSVs
- Consolidação em DataFrame único
- Limpeza inicial (remoção de nulos e duplicatas)
- Estatísticas do dataset

### Seção 3: Pré-processamento de Texto
- Remoção de tags HTML
- Normalização de texto
- Análise exploratória (palavras mais frequentes)
- Estatísticas das letras

### Seção 4: Geração de Embeddings
- Carregamento do modelo `paraphrase-multilingual-mpnet-base-v2`
- Geração de embeddings (768 dimensões)
- Salvamento para reutilização

### Seção 5: Cálculo de Similaridade
- Matriz de similaridade cosseno
- Identificação de músicas similares
- Top 20 pares mais similares
- Exportação de resultados

### Seção 6: Visualizações
- Heatmap de similaridade
- Distribuição de similaridades
- Redução dimensional (UMAP/t-SNE)
- Scatter plot 2D
- Mapa interativo
- Network graph
- Visualização dos top 20 pares

### Seção 7: Análise de Clusters
- Método do cotovelo (escolha de k)
- K-Means clustering
- Visualização de clusters
- Análise de características
- Palavras-chave por cluster

### Seção 8: Insights e Conclusões
- Relatório final
- Interpretação dos clusters
- Sugestões para análises futuras

## Arquivos Gerados

### CSVs
- `matriz_similaridade.csv` - Matriz completa de similaridade entre músicas
- `top20_pares_similares.csv` - Lista dos 20 pares mais similares
- `analise_clusters.csv` - Análise detalhada dos clusters
- `letras_processadas.csv` - Dataset processado com estatísticas

### Modelo
- `embeddings_letras.pkl` - Embeddings salvos (reutilizável)

### Visualizações (PNG)
- `distribuicao_estatisticas_letras.png`
- `top20_palavras_frequentes_similaridade.png`
- `heatmap_similaridade_amostra.png`
- `distribuicao_similaridades.png`
- `scatter_2d_letras.png`
- `network_similaridade.png`
- `top20_pares_similares_viz.png`
- `metodo_cotovelo.png`
- `clusters_kmeans_2d.png`

### Visualizações Interativas (HTML)
- `mapa_interativo_similaridade.html`
- `clusters_interativos.html`

## Personalização

### Ajustar Número de Clusters
```python
n_clusters = 8  # Altere este valor na Seção 7
```

### Alterar Threshold do Network Graph
```python
threshold = 0.70  # Valores entre 0.6-0.8 recomendados
```

### Usar Modelo Diferente
```python
# Na Seção 4, altere o modelo:
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')  # Mais leve
# ou
model = SentenceTransformer('distiluse-base-multilingual-cased-v2')  # Alternativa
```

### Adicionar Stopwords Personalizadas
```python
# Na Seção 7, adicione palavras ao conjunto:
stopwords_pt.update({'palavra1', 'palavra2', 'palavra3'})
```

## Resolução de Problemas

### Erro: "Pasta não encontrada"
- Verifique se a pasta `letras_engenheiros_hawaii` está no mesmo diretório do notebook
- Ou ajuste o caminho na Seção 2:
  ```python
  data_folder = Path('caminho/para/letras_engenheiros_hawaii')
  ```

### Erro: "Out of Memory"
- Reduza o batch_size na geração de embeddings:
  ```python
  embeddings = model.encode(letras_list, batch_size=16)  # era 32
  ```
- Ou processe em lotes menores

### Modelo demora muito para baixar
- O modelo é baixado apenas uma vez
- Fica salvo em: `~/.cache/torch/sentence_transformers/`
- Tamanho: ~500MB
- Alternativa: use modelo mais leve (veja Personalização)

### UMAP/NetworkX não disponível
- O notebook continua funcionando sem estas bibliotecas
- UMAP → usa t-SNE automaticamente
- NetworkX → pula visualização de rede

## Interpretação dos Resultados

### Similaridade
- Valores próximos a 1.0: Músicas muito similares tematicamente
- Valores próximos a 0.5: Similaridade moderada
- Valores < 0.3: Músicas temáticas diferentes

### Clusters
- Cada cluster agrupa músicas com temas semelhantes
- Analise as palavras-chave para interpretar o tema
- Compare com os álbuns para ver evolução temporal

### Visualizações
- **Heatmap**: Padrões de blocos indicam grupos temáticos
- **Scatter 2D**: Proximidade = similaridade temática
- **Network**: Conexões mostram músicas fortemente relacionadas

## Próximos Passos

1. Execute o notebook completo
2. Analise os resultados gerados
3. Explore os arquivos HTML interativos
4. Ajuste parâmetros conforme necessário
5. Investigue músicas similares específicas

## Análises Futuras Sugeridas

- Análise temporal (evolução temática)
- Análise de sentimentos
- Topic Modeling (LDA)
- Comparação com outros artistas
- Análise de rimas e estrutura poética
- Word2Vec específico do artista

## Suporte

Se encontrar problemas:
1. Verifique se todas as dependências estão instaladas
2. Confirme a estrutura de arquivos
3. Consulte a seção "Resolução de Problemas"
4. Revise os comentários no código do notebook

## Créditos

- **Modelo NLP**: sentence-transformers (paraphrase-multilingual-mpnet-base-v2)
- **Dados**: Letras dos Engenheiros do Hawaii
- **Tecnologias**: Python, Scikit-learn, Plotly, Matplotlib, Seaborn

---

**Desenvolvido para análise acadêmica e educacional**

**Última atualização**: Dezembro 2025
