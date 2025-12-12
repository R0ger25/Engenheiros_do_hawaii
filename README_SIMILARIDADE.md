# 🎵 Análise de Similaridade - Engenheiros do Hawaii

## 🚀 Início Rápido (3 Passos)

### 1. Abra o Notebook
```bash
jupyter notebook analise_similaridade_letras.ipynb
```

### 2. Execute a Primeira Célula
A primeira célula (Seção 0) instala **automaticamente** todos os pacotes necessários.

### 3. Execute o Resto
Clique em `Cell > Run All` ou execute célula por célula com `Shift + Enter`.

---

## ✨ Características

- **100% Autossuficiente**: Instala todas as dependências automaticamente
- **Sem configuração manual**: Não precisa instalar pacotes manualmente
- **Análise completa**: Embeddings, similaridade, clusters e visualizações
- **Visualizações interativas**: Gráficos PNG + HTML interativos
- **Exporta resultados**: CSV, gráficos e embeddings salvos

## 📋 O que você precisa

- ✅ Python 3.8+
- ✅ Jupyter Notebook ou JupyterLab
- ✅ Conexão com internet (primeira execução)
- ✅ Pasta `letras_engenheiros_hawaii/` com os CSVs

**Só isso!** O resto é instalado automaticamente.

## ⏱️ Tempo de Execução

**Primeira vez**: 15-30 minutos
- Instalação de pacotes: 5-10 min
- Download do modelo NLP: 3-5 min
- Análise completa: 5-15 min

**Próximas vezes**: 3-8 minutos
- Pacotes já instalados ✓
- Modelo em cache ✓

## 📊 Resultados Gerados

### Arquivos CSV
- `matriz_similaridade.csv` - Similaridade entre todas as músicas
- `top20_pares_similares.csv` - 20 pares mais similares
- `analise_clusters.csv` - Músicas agrupadas por tema
- `letras_processadas.csv` - Dataset processado

### Visualizações PNG
- Heatmap de similaridade
- Distribuições estatísticas
- Scatter plot 2D
- Clusters temáticos
- Top 20 pares
- Método do cotovelo
- Network de similaridade

### Visualizações Interativas HTML
- `mapa_interativo_similaridade.html` - Explore as músicas
- `clusters_interativos.html` - Clusters navegáveis

### Modelo
- `embeddings_letras.pkl` - Embeddings reutilizáveis

## 🎯 O que o Notebook Faz

1. **Instala dependências** automaticamente
2. **Carrega** todas as letras dos CSVs
3. **Limpa** o texto (remove HTML)
4. **Gera embeddings** usando NLP avançado
5. **Calcula similaridade** entre todas as músicas
6. **Identifica clusters** temáticos
7. **Cria visualizações** profissionais
8. **Exporta resultados** para análise

## 🔧 Pacotes Instalados Automaticamente

**Obrigatórios**:
- pandas, numpy
- sentence-transformers (modelo NLP)
- scikit-learn
- matplotlib, seaborn, plotly
- beautifulsoup4

**Opcionais** (se disponível):
- umap-learn (redução dimensional)
- networkx (grafos)

## 📖 Documentação Completa

Para instruções detalhadas, veja: `INSTRUCOES_SIMILARIDADE.md`

## ❓ Dúvidas Comuns

**P: Preciso instalar pacotes manualmente?**
R: Não! A primeira célula faz isso automaticamente.

**P: E se não tiver internet?**
R: Instale os pacotes antes (veja `INSTRUCOES_SIMILARIDADE.md`)

**P: Posso reutilizar os embeddings?**
R: Sim! Eles são salvos em `embeddings_letras.pkl`

**P: Como ajustar o número de clusters?**
R: Na Seção 7, altere a variável `n_clusters`

**P: Demora muito?**
R: Primeira vez: 15-30 min. Depois: 3-8 min.

## 🎨 Personalização

Você pode facilmente:
- Ajustar número de clusters
- Mudar threshold do network graph
- Adicionar stopwords personalizadas
- Usar modelos NLP alternativos

Tudo está documentado no próprio notebook!

---

**Pronto para começar?** Abra o notebook e execute! 🚀
