#%%
#Importanto a base de dados

import pandas as pd

df = pd.read_csv('base_CFM.csv')



#%%
#Análise da estrutura e qualidade dos dados

#Verificando dimensões do dataframe
df.shape

#Verificando colunas
df.columns

#removendo variável duplicada
df = df.drop(columns='avg_cars_at home(approx).1')


#Verificando dados duplicados
df.duplicated().sum()

#Verificando dados faltantes
df.isnull().sum()

#Verificando tipo dos dados
df.info()

#Verificando distribuição de valores únicos
df.nunique()

#%%
#Explarando tipos de variáveis
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Variáveis qualitativas
colunas_quali = df.select_dtypes(include=['object']).columns

#Criando dataframe apenas com variáveis qualitativas
df_quali = df.select_dtypes(include=['object'])

#Exploração inicial dados quali
for i in colunas_quali:
    print(f'\n Variável: {i} \n Valores únicos: {df[i].unique()}')

#Variáveis quantitativas
colunas_quant = df.select_dtypes(include = np.number).columns

#Criando dataframe apenas com variáveis quantitativas
df_quant = df.select_dtypes(include = np.number)

#Exploração inicial dos dados quanti
dados_colunas_quant = df.select_dtypes(exclude=['object']).describe().T

#Análise das variáveis qualitativas: Frequência absoluta
for variavel in df_quali:
    #ordena variáveis em ordem decrescente
    ordem = df_quali[variavel].value_counts().index
    plt.Figure(figsize=(20,10))
    sns.countplot(x=df_quali[variavel], order=ordem)
    plt.title(f'Frequência Absoluta - {variavel}')
    plt.xlabel(xlabel=f'{variavel}')
    plt.ylabel('Frequência')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()    

#criação de tabela de contigência por categoria de alimento
freq_rel_food_category = pd.crosstab(index=df_quali['food_category'], columns='Porcentagem', normalize=True).sort_values('Porcentagem' ,ascending = False)
freq_rel_food_category['Porcentagem'] = (freq_rel_food_category['Porcentagem']*100).round(2)
#configurando e gerando plot em barras
ax = sns.barplot(data=freq_rel_food_category,x='food_category',y='Porcentagem',hue='Porcentagem',palette='rocket')
ax.set_box_aspect(1/3)
for container in ax.containers: ax.bar_label(container, fmt='%.2f',padding = 3,fontsize=8, rotation=90)
plt.Figure(figsize=(20,6), dpi = 600)
plt.title('Categorias de alimento mais vendidas em promoção', fontsize=10)
plt.xlabel('Categorias', fontsize=8)
plt.ylabel('% das vendas em promoção', fontsize=8)
plt.xticks(fontsize=6)
plt.xticks(rotation=90)
plt.yticks(fontsize=6)
plt.legend(title="Porcentagem", fontsize=5, title_fontsize=12, loc="upper right")
plt.show()

#criação de tabela de contigência por tipo de mercado
freq_rel_store_type = pd.crosstab(index=df_quali['store_type'], columns='Porcentagem', normalize=True).sort_values('Porcentagem' ,ascending = False)
freq_rel_store_type['Porcentagem'] = (freq_rel_store_type['Porcentagem']*100).round(2)
#configurando e gerando plot em barras
ax1 = sns.barplot(data=freq_rel_store_type,x='store_type',y='Porcentagem',hue='Porcentagem',palette='rocket')
ax1.set_box_aspect(1/3)
for container in ax1.containers: ax1.bar_label(container, fmt='%.2f',padding = 3,fontsize=8)
plt.Figure(figsize=(20,6), dpi = 20)
plt.title('Distribuição das vendas em promoção por tipo de loja', fontsize=10)
plt.xlabel('Categorias', fontsize=8)
plt.ylabel('% das vendas em promoção', fontsize=8)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)
plt.legend(title="Porcentagem", fontsize=5, title_fontsize=12, loc="upper right")
plt.show()

#criação de tabela de contigência por tipo de cliente
freq_rel_member_card = pd.crosstab(index=df_quali['member_card'], columns='Porcentagem', normalize=True).sort_values('Porcentagem' ,ascending = False)
freq_rel_member_card['Porcentagem'] = (freq_rel_member_card['Porcentagem']*100).round(2)
#configurando e gerando plot em barras
ax2 = sns.barplot(data=freq_rel_member_card,x='member_card',y='Porcentagem',hue='Porcentagem',palette='rocket')
ax2.set_box_aspect(1/3)
for container in ax2.containers: ax2.bar_label(container, fmt='%.2f',padding = 3,fontsize=8)
plt.Figure(figsize=(20,6), dpi = 20)
plt.title('Distribuição das vendas em promoção por tipo de cliente', fontsize=10)
plt.xlabel('Categorias', fontsize=8)
plt.ylabel('% das vendas em promoção', fontsize=8)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)
plt.legend(title="Porcentagem", fontsize=5, title_fontsize=12, loc="upper right")
plt.show()

#criação de tabela de contigência por escolaridade
freq_rel_education = pd.crosstab(index=df_quali['education'], columns='Porcentagem', normalize=True).sort_values('Porcentagem' ,ascending = False)
freq_rel_education['Porcentagem'] = (freq_rel_education['Porcentagem']*100).round(2)
#configurando e gerando plot em barras
ax3 = sns.barplot(data=freq_rel_education,x='education',y='Porcentagem',hue='Porcentagem',palette='rocket')
ax3.set_box_aspect(1/3)
for container in ax3.containers: ax3.bar_label(container, fmt='%.2f',padding = 3,fontsize=8)
plt.Figure(figsize=(20,6), dpi = 20)
plt.title('Distribuição das vendas em promoção por escolaridade do cliente', fontsize=10)
plt.xlabel('Categorias', fontsize=8)
plt.ylabel('% das vendas em promoção', fontsize=8)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)
plt.legend(title="Porcentagem", fontsize=5, title_fontsize=12, loc="upper right")
plt.show()

#criação de tabela de contigência por renda
freq_rel_income = pd.crosstab(index=df_quali['avg. yearly_income'], columns='Porcentagem', normalize=True)
freq_rel_income['Porcentagem'] = (freq_rel_income['Porcentagem']*100).round(2)
#configurando e gerando plot em barras
ax4 = sns.barplot(data=freq_rel_income,x='avg. yearly_income',y='Porcentagem',hue='Porcentagem',palette='rocket',order=['$10K - $30K', '$30K - $50K', '$50K - $70K', '$70K - $90K', '$90K - $110K', '$110K - $130K', '$130K - $150K', '$150K +'])
ax4.set_box_aspect(1/3)
for container in ax4.containers: ax4.bar_label(container, fmt='%.2f',padding = 3,fontsize=8)
plt.Figure(figsize=(20,6), dpi = 20)
plt.title('Distribuição das vendas em promoção por renda do cliente', fontsize=10)
plt.xlabel('Categorias', fontsize=8)
plt.ylabel('% das vendas em promoção', fontsize=8)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)
plt.legend(title="Porcentagem", fontsize=5, title_fontsize=12, loc="upper right")
plt.show()

#Iniciando análise de variáveis quanti

#Criando função para remover outliers usando IQR
def remove_outliers(dataframe):
    for variavel in dataframe:
        #calculando IQR
        Q1 = dataframe[variavel].quantile(0.25)
        Q3 = dataframe[variavel].quantile(0.75)
        IQR = Q3 - Q1
        limite_sup = Q3 + 1.5*IQR
        limite_inf = Q1 - 1.5*IQR
        #criando array para definir posição dos outliers
        array_sup = dataframe[dataframe[variavel] >= limite_sup].index
        array_inf =dataframe[dataframe[variavel] <= limite_inf].index
        #removendo outliers
        dataframe = dataframe.drop(index=array_sup).drop(index=array_inf)
    return dataframe

#chamando função que remove outliers pelo método IQR
df_quant = remove_outliers(df_quant)

for variavel in df_quant:
    plt.Figure(figsize=(20,10))
    sns.displot(x=df_quant[variavel], kde= True)
    plt.title(f'Distribuição de valores - {variavel}')
    plt.xlabel(xlabel=f'{variavel}')
    plt.ylabel('Contagem')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
    plt.boxplot(df_quant[variavel], vert=False)
    plt.title(f'Boxplot - {variavel}')
    plt.ylabel('Amostra')
    plt.xlabel('Valor')
    plt.show()

#Algumas variáveis sofreram o problema de ponderação arbitrária
#corrigindo colunas no dataframe original
df[['recyclable_package', 'low_fat', 'coffee_bar', 'video_store','salad_bar','prepared_food','florist']] = df[['recyclable_package', 'low_fat', 'coffee_bar', 'video_store','salad_bar','prepared_food','florist']].replace({0: 'Não', 1: 'Sim'})
#Variáveis qualitativas
colunas_quali = df.select_dtypes(include=['object']).columns

#Criando dataframe apenas com variáveis qualitativas
df_quali = df.select_dtypes(include=['object'])

#passando variáveis quanti para quali

df_quali_adicionais = df_quant[['recyclable_package', 'low_fat', 'coffee_bar', 'video_store','salad_bar','prepared_food','florist']]
df_quali_adicionais = df_quali_adicionais.replace({0: 'Não', 1: 'Sim'})

for variavel in df_quali_adicionais:
    freq_rel = pd.crosstab(index=df_quali_adicionais[variavel], columns='Porcentagem', normalize=True).sort_values('Porcentagem' ,ascending = False)
    freq_rel['Porcentagem'] = (freq_rel['Porcentagem']*100).round(2)
    #configurando e gerando plot em barras
    ax5 = sns.barplot(data=freq_rel,x=variavel,y='Porcentagem',hue='Porcentagem',palette='rocket')
    ax5.set_box_aspect(1/3)
    for container in ax5.containers: ax5.bar_label(container, fmt='%.2f',padding = 3,fontsize=8)
    plt.Figure(figsize=(20,6), dpi = 20)
    plt.title(f'Frequência - {variavel}', fontsize=10)
    plt.xlabel('Categorias', fontsize=8)
    plt.ylabel('Porcentagem', fontsize=8)
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)
    plt.legend(title="Porcentagem", fontsize=5, title_fontsize=12, loc="upper right")
    plt.show()

#Análise Quanti x Quanti
plt.figure(figsize = (20,10))
sns.heatmap(df_quant.corr(), annot= True)
plt.title('Matriz de correlação')
plt.show()

#analise quanti x quali
    
import pandas as pd
from scipy.stats import kruskal

#Criando um dicionário para armazenar os resultados
kruskal_resultados = {}

#aplicando o teste de Kruskal-Wallis para cada variável qualitativa em relação ao custo
for var in colunas_quali:
    #Criando os grupos de "cost" para cada categoria na variável categórica
    grupos = [df[df[var] == categoria]["cost"] for categoria in df[var].unique()]
    print(grupos)
    H, p_valor = kruskal(*grupos)
    kruskal_resultados[var] = {"H": H, "p_valor": p_valor}

#Criando um DataFrame para visualizar os resultados
kruskal_df = pd.DataFrame.from_dict(kruskal_resultados, orient='index')
kruskal_significativo = kruskal_df[kruskal_df['p_valor']<=0.05]

#salvando variáveis significativas
colunas_kruskal = kruskal_significativo.index

for variavel in colunas_kruskal:
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=df[variavel], y=df['cost'], palette='coolwarm')
    plt.title(f'Distribuição do Custo por {variavel} (Violino)')
    plt.ylabel('Custo')
    plt.xlabel(variavel)
    plt.xticks(rotation=90)
    plt.show()

#%%

from sklearn.mixture import GaussianMixture
import numpy as np

#Ajustando um modelo GMM na distribuição de 'cost'
cost_values = df["cost"].values.reshape(-1, 1)
gmm = GaussianMixture(n_components=3, random_state=42).fit(cost_values)

#Gerando pontos para plotar a distribuição ajustada
x = np.linspace(df["cost"].min(), df["cost"].max(), 1000)
densidade = np.exp(gmm.score_samples(x.reshape(-1, 1)))

#Plotando a distribuição real e a ajustada pelo GMM
plt.figure(figsize=(10,6))
sns.histplot(df["cost"], bins=30, color="gray", kde=False, stat="density", alpha=0.6)
plt.plot(x, densidade, color="red", label="GMM Ajustado")
plt.title("Ajuste de Mistura Gaussiana - Custo")
plt.legend()
plt.show()

df["cluster_custo"] = gmm.predict(df["cost"].values.reshape(-1, 1))

#Distribuição de custo por cluster identificado
sns.boxplot(x="cost_cluster", y="cost", data=df)
plt.title("Boxplot do Custo por Cluster GMM")
plt.show()

df["cluster_custo"] = df["cluster_custo"].replace({0: 'Alto', 1: 'Baixo', 2: 'Médio'})


#%%

import scipy.stats as stats

#Criando um dicionário para armazenar os resultados
resultados_chi2 = {}

for var in colunas_kruskal:
    #criando tabela d contigência
    contingencia = pd.crosstab(df["cluster_custo"], df[var])
    # Aplicar teste qui-quadrado
    chi2, p_valor, dof, expected = stats.chi2_contingency(contingencia)
    resultados_chi2[var] = {"chi2": chi2, "p_valor": p_valor}

#Criando um DataFrame para visualizar os resultados
chi2_df = pd.DataFrame.from_dict(resultados_chi2, orient='index')
chi2_significativo = chi2_df[kruskal_df['p_valor']<=0.05]

#salvando variáveis significativas
colunas_chi2 = chi2_significativo.index

#faixas de custo
custos = ["Baixo", "Médio", "Alto"]
dic_cor = {"Baixo": "green", "Médio": "orange", "Alto": "red"}

for var in colunas_chi2:
    #criando tabela de contigência
    contingencia = pd.crosstab(df["cluster_custo"], df[var]).T
    #normalizando valores
    contingencia = contingencia.div(contingencia.sum(axis=1), axis=0) * 100
    for custo in custos:
        contingencia = contingencia.sort_values(by=custo, ascending = False)
         #Gráfico 1: Linha mostrando variação da porcentagem do cluster "Baixo" por promotion_name
        plt.figure(figsize=(14, 6))
        plt.plot(contingencia.index, contingencia[custo], marker="o", linestyle="-", color=dic_cor[custo], label=f"Cluster {custo}")
        plt.title(f"Variação da Porcentagem do Cluster {custo} por {var}")
        plt.ylabel("Percentual (%)")
        plt.xticks(rotation=90)
        plt.legend()
        plt.grid(True)
        plt.show()
    

for var in colunas_chi2:
    # Criando tabela de contingência
    contingencia = pd.crosstab(df["cluster_custo"], df[var]).T

    # Normalizando valores (percentual dos clusters por categoria)
    contingencia = contingencia.div(contingencia.sum(axis=1), axis=0) * 100

    # Criando DataFrame com percentual das categorias
    percentual_categoria = df[var].value_counts(normalize=True) * 100

    for custo in custos:
        # Ordenando pela porcentagem do cluster
        contingencia = contingencia.sort_values(by=custo, ascending=False)
        percentual_categoria = percentual_categoria.reindex(contingencia.index)

        # Criando a figura com dois eixos
        fig, ax1 = plt.subplots(figsize=(14, 6))

        # Gráfico de linha - Variação da porcentagem por categoria
        ax1.plot(contingencia.index, contingencia[custo], marker="o", linestyle="-", color=dic_cor[custo], label=f"Cluster {custo}")
        ax1.set_ylabel("Percentual Cluster (%)", color=dic_cor[custo])
        ax1.tick_params(axis='y', labelcolor=dic_cor[custo])
        ax1.legend(loc="upper left")
        ax1.grid(True)

        # Criando um segundo eixo y para o countplot percentual
        ax2 = ax1.twinx()

        # Countplot percentual - Percentual das categorias
        sns.barplot(x=contingencia.index, y=percentual_categoria, ax=ax2, color="gray", alpha=0.3, label="Percentual (%)")

        ax2.set_ylabel("Percentual (%)", color="gray")
        ax2.tick_params(axis='y', labelcolor="gray")

        # **Garantindo que os dois eixos comecem no zero e tenham a mesma escala**
        ax1.set_ylim(0, max(contingencia[custo].max(), percentual_categoria.max()) * 1.1)
        ax2.set_ylim(0, max(contingencia[custo].max(), percentual_categoria.max()) * 1.1)

        # Ajustando rótulos e título
        plt.title(f"Variação da Porcentagem do Cluster {custo} por {var} com Percentual das Categorias")
        ax1.set_xticklabels(contingencia.index, rotation=90)

        # Adicionando legenda
        ax2.legend(loc="upper right")

        # Exibir gráfico
        plt.show()


for var in colunas_chi2:
    # Criando tabela de contingência
    contingencia = pd.crosstab(df["cluster_custo"], df[var]).T

    # Normalizando valores (percentual dos clusters por categoria)
    contingencia = contingencia.div(contingencia.sum(axis=1), axis=0) * 100

    # Criando DataFrame com percentual das categorias (para ordenar)
    percentual_categoria = df[var].value_counts(normalize=True) * 100

    # Ordenando as categorias pela frequência geral
    ordenacao_categorias = percentual_categoria.index

    for custo in custos:
        # Aplicando a ordenação pela frequência das categorias
        contingencia = contingencia.reindex(ordenacao_categorias)
        percentual_categoria = percentual_categoria.reindex(ordenacao_categorias)

        # Criando a figura com dois eixos
        fig, ax1 = plt.subplots(figsize=(14, 6))

        # Gráfico de linha - Variação da porcentagem por categoria
        ax1.plot(contingencia.index, contingencia[custo], marker="o", linestyle="-", color=dic_cor[custo], label=f"Cluster {custo}")
        ax1.set_ylabel("Percentual Cluster (%)", color=dic_cor[custo])
        ax1.tick_params(axis='y', labelcolor=dic_cor[custo])
        ax1.legend(loc="upper left")
        ax1.grid(True)

        # Criando um segundo eixo y para o countplot percentual
        ax2 = ax1.twinx()

        # Countplot percentual - Percentual das categorias
        sns.barplot(x=contingencia.index, y=percentual_categoria, ax=ax2, color="gray", alpha=0.3, label="Percentual (%)")

        ax2.set_ylabel("Percentual (%)", color="red")
        ax2.tick_params(axis='y', labelcolor="red")

        # **Garantindo que os dois eixos comecem no zero**
        ax1.set_ylim(0, max(contingencia[custo].max(), percentual_categoria.max()) * 1.1)
        ax2.set_ylim(0, max(contingencia[custo].max(), percentual_categoria.max()) * 1.1)

        # Ajustando rótulos e título
        plt.title(f"Variação da Porcentagem do Cluster {custo} por {var} (Categorias Ordenadas por Frequência)")
        ax1.set_xticklabels(contingencia.index, rotation=90)

        # Adicionando legenda
        ax2.legend(loc="upper right")

        # Exibir gráfico
        plt.show()

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 10))  # Normalizando entre 0 e 10

for var in colunas_chi2:
    # Criando tabela de contingência
    contingencia = pd.crosstab(df["cluster_custo"], df[var]).T

    # Normalizando valores (percentual dos clusters por categoria)
    contingencia = contingencia.div(contingencia.sum(axis=1), axis=0) * 100

    # Criando DataFrame com percentual das categorias no total (para calcular os índices)
    percentual_categoria = df[var].value_counts(normalize=True) * 100

    # Calculando os índices para "Baixo" e "Alto"
    contingencia["Indice_Baixo"] = contingencia["Baixo"] / percentual_categoria
    contingencia["Indice_Alto"] = contingencia["Alto"] / percentual_categoria

    # Removendo possíveis valores NaN e infinito antes da normalização
    contingencia.replace([np.inf, -np.inf], np.nan, inplace=True)
    contingencia.dropna(subset=["Indice_Baixo", "Indice_Alto"], inplace=True)

    # Aplicando normalização
    contingencia[["Indice_Baixo", "Indice_Alto"]] = scaler.fit_transform(contingencia[["Indice_Baixo", "Indice_Alto"]])

    # Ordenando os dados separadamente para os dois índices
    contingencia_baixo = contingencia.sort_values(by="Indice_Baixo", ascending=False)
    contingencia_alto = contingencia.sort_values(by="Indice_Alto", ascending=False)

    # Gráfico 1: Índice para "Baixo"
    plt.figure(figsize=(14, 6))
    plt.plot(contingencia_baixo.index, contingencia_baixo["Indice_Baixo"], marker="o", linestyle="-", color="blue", label="Índice Baixo (Normalizado)")
    plt.ylabel("Índice Baixo (0-10)")
    plt.xticks(rotation=90)
    plt.title(f"Índice Normalizado do Cluster 'Baixo' por {var}")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Gráfico 2: Índice para "Alto"
    plt.figure(figsize=(14, 6))
    plt.plot(contingencia_alto.index, contingencia_alto["Indice_Alto"], marker="o", linestyle="-", color="red", label="Índice Alto (Normalizado)")
    plt.ylabel("Índice Alto (0-10)")
    plt.xticks(rotation=90)
    plt.title(f"Índice Normalizado do Cluster 'Alto' por {var}")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
scaler = MinMaxScaler(feature_range=(0, 10))  # Normalizando entre 0 e 10

for var in colunas_chi2:
    # Criando tabela de contingência
    contingencia = pd.crosstab(df["cluster_custo"], df[var]).T

    # Normalizando valores (percentual dos clusters por categoria)
    contingencia = contingencia.div(contingencia.sum(axis=1), axis=0) * 100

    # Criando DataFrame com percentual das categorias no total (para calcular os índices)
    percentual_categoria = df[var].value_counts(normalize=True) * 100

    # Calculando os índices para "Baixo" e "Alto"
    contingencia["Indice_Baixo"] = contingencia["Baixo"] / percentual_categoria
    contingencia["Indice_Alto"] = contingencia["Alto"] / percentual_categoria

    # Removendo possíveis valores NaN e infinito antes da normalização
    contingencia.replace([np.inf, -np.inf], np.nan, inplace=True)
    contingencia.dropna(subset=["Indice_Baixo", "Indice_Alto"], inplace=True)

    # Aplicando normalização
    contingencia[["Indice_Baixo", "Indice_Alto"]] = scaler.fit_transform(contingencia[["Indice_Baixo", "Indice_Alto"]])

    # Ordenando os dados pelo Índice "Baixo"
    contingencia = contingencia.sort_values(by="Indice_Baixo", ascending=False)

    # Criando o gráfico com os dois índices
    plt.figure(figsize=(14, 6))
    plt.plot(contingencia.index, contingencia["Indice_Baixo"], marker="o", linestyle="-", color="blue", label="Índice Baixo (Normalizado)")
    plt.plot(contingencia.index, contingencia["Indice_Alto"], marker="o", linestyle="-", color="red", label="Índice Alto (Normalizado)")

    plt.ylabel("Índice Normalizado (0-10)")
    plt.xticks(rotation=90)
    plt.title(f"Índice Normalizado dos Clusters 'Baixo' e 'Alto' por {var}")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
# Definir número de desvios padrão para exclusão
num_desvios = 1  

for var in colunas_chi2:
    # Criar tabela de contingência
    contingencia = pd.crosstab(df["cluster_custo"], df[var]).T

    # Calcular a contagem total das categorias
    total_categoria = df[var].value_counts()

    # Calcular média e desvio padrão da frequência das categorias
    media_frequencia = total_categoria.mean()
    desvio_frequencia = total_categoria.std()

    # Definir limite de exclusão (excluir apenas categorias na cauda esquerda, ou seja, abaixo de 1 desvio padrão)
    limite_exclusao = media_frequencia - num_desvios * desvio_frequencia
    categorias_validas = total_categoria[total_categoria >= limite_exclusao].index  # Agora incluímos a média

    # Aplicar filtro para manter apenas categorias acima do limite inferior
    contingencia = contingencia.loc[categorias_validas]

    # Normalizar valores (percentual dos clusters por categoria)
    contingencia = contingencia.div(contingencia.sum(axis=1), axis=0) * 100

    # Criar DataFrame com percentual das categorias no total (para calcular os índices)
    percentual_categoria = total_categoria / total_categoria.sum() * 100
    percentual_categoria = percentual_categoria.loc[categorias_validas]

    # Calcular os índices para "Baixo" e "Alto" sem normalização
    contingencia["Indice_Baixo"] = contingencia["Baixo"] / percentual_categoria
    contingencia["Indice_Alto"] = contingencia["Alto"] / percentual_categoria

    # Ordenar categorias pelo Índice "Baixo"
    contingencia = contingencia.sort_values(by="Indice_Baixo", ascending=False)

    # Criar gráfico com os dois índices
    plt.figure(figsize=(14, 6))
    plt.plot(contingencia.index, contingencia["Indice_Baixo"], marker="o", linestyle="-", color="blue", label="Índice Baixo")
    plt.plot(contingencia.index, contingencia["Indice_Alto"], marker="o", linestyle="-", color="red", label="Índice Alto")

    plt.ylabel("Índice (Sem Normalização)")
    plt.xticks(rotation=90)
    plt.title(f"Índice do Cluster 'Baixo' e 'Alto' por {var} (Excluindo Categorias na Cauda Esquerda)")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
    for var in colunas_chi2:
        # Criar tabela de contingência
        contingencia = pd.crosstab(df["cluster_custo"], df[var]).T
    
        # Normalizar valores (percentual dos clusters por categoria)
        contingencia = contingencia.div(contingencia.sum(axis=1), axis=0) * 100
    
        # Criar DataFrame com percentual das categorias no total (para calcular os índices)
        total_categoria = df[var].value_counts()
        percentual_categoria = total_categoria / total_categoria.sum() * 100
    
        # Calcular a média e o desvio padrão global de cada cluster
        media_cluster = contingencia.mean()
        desvio_cluster = contingencia.std()
    
        # Calcular o Índice Z-Score para "Baixo" e "Alto"
        contingencia["Indice_Baixo_Z"] = (contingencia["Baixo"] - media_cluster["Baixo"]) / desvio_cluster["Baixo"]
        contingencia["Indice_Alto_Z"] = (contingencia["Alto"] - media_cluster["Alto"]) / desvio_cluster["Alto"]
    
        # Ordenar categorias pelo Índice "Baixo"
        contingencia = contingencia.sort_values(by="Indice_Baixo_Z", ascending=False)
    
        # Criar gráfico com os dois índices Z-Score
        plt.figure(figsize=(14, 6))
        plt.plot(contingencia.index, contingencia["Indice_Baixo_Z"], marker="o", linestyle="-", color="blue", label="Índice Z - Baixo")
        plt.plot(contingencia.index, contingencia["Indice_Alto_Z"], marker="o", linestyle="-", color="red", label="Índice Z - Alto")
    
        plt.ylabel("Índice Z-Score")
        plt.xticks(rotation=90)
        plt.title(f"Índice Z-Score do Cluster 'Baixo' e 'Alto' por {var}")
        plt.legend()
        plt.grid(True)
        plt.show()
    
for var in colunas_chi2:
    # Criar tabela de contingência
    contingencia = pd.crosstab(df["cluster_custo"], df[var]).T

    # Normalizar valores (percentual dos clusters por categoria)
    contingencia = contingencia.div(contingencia.sum(axis=1), axis=0) * 100

    # Criar DataFrame com percentual das categorias no total (para calcular os índices)
    total_categoria = df[var].value_counts()
    percentual_categoria = total_categoria / total_categoria.sum() * 100

    # Calcular a média e o desvio padrão global de cada cluster
    media_cluster = contingencia.mean()
    desvio_cluster = contingencia.std()

    # Calcular o Índice Z-Score para "Baixo" e "Alto"
    contingencia["Indice_Baixo_Z"] = (contingencia["Baixo"] - media_cluster["Baixo"]) / desvio_cluster["Baixo"]
    contingencia["Indice_Alto_Z"] = (contingencia["Alto"] - media_cluster["Alto"]) / desvio_cluster["Alto"]

    # Calcular a diferença direta entre os Z-Scores (sem valor absoluto)
    contingencia["Indice_Comparativo_Z"] = contingencia["Indice_Baixo_Z"] - contingencia["Indice_Alto_Z"]

    # Ordenar categorias pelo Índice Comparativo Z (valores positivos primeiro)
    contingencia = contingencia.sort_values(by="Indice_Comparativo_Z", ascending=False)

    # Criar gráfico mostrando a diferença de Z-Score entre os clusters
    plt.figure(figsize=(14, 6))
    plt.plot(contingencia.index, contingencia["Indice_Comparativo_Z"], marker="o", linestyle="-", color="blue", label="Índice Comparativo Z")

    plt.axhline(0, color="black", linestyle="--")  # Linha central para diferenciar positivo e negativo
    plt.ylabel("Comparação Z-Score (Baixo - Alto)")
    plt.xticks(rotation=90)
    plt.title(f"Índice Comparativo Z entre Cluster 'Baixo' e 'Alto' por {var}")
    plt.legend()
    plt.grid(True)
    plt.show()