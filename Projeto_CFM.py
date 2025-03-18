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

# Criar um dicionário para armazenar os resultados
kruskal_results = {}

# Aplicar o teste de Kruskal-Wallis para cada variável qualitativa em relação ao custo
for var in colunas_quali:
    # Criar os grupos de "cost" para cada categoria na variável categórica
    grupos = [df[df[var] == categoria]["cost"] for categoria in df[var].unique()]
    print(grupos)
    H, p_valor = kruskal(*grupos)
    kruskal_results[var] = {"H": H, "p_valor": p_valor}

# Criar um DataFrame para visualizar os resultados
kruskal_df = pd.DataFrame.from_dict(kruskal_results, orient='index')
kruskal_significativo = kruskal_df[kruskal_df['p_valor']<=0.05]

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

# Ajustar um modelo GMM na distribuição de 'cost'
cost_values = df["cost"].values.reshape(-1, 1)
gmm = GaussianMixture(n_components=3, random_state=42).fit(cost_values)

# Gerar pontos para plotar a distribuição ajustada
x = np.linspace(df["cost"].min(), df["cost"].max(), 1000)
densidade = np.exp(gmm.score_samples(x.reshape(-1, 1)))

# Plotar a distribuição real e a ajustada pelo GMM
plt.figure(figsize=(10,6))
sns.histplot(df["cost"], bins=30, color="gray", kde=False, stat="density", alpha=0.6)
plt.plot(x, densidade, color="red", label="GMM Ajustado")
plt.title("Ajuste de Mistura Gaussiana ao Custo")
plt.legend()
plt.show()

df["cost_cluster"] = gmm.predict(df["cost"].values.reshape(-1, 1))

# Ver a distribuição de custo por cluster identificado
sns.boxplot(x="cost_cluster", y="cost", data=df)
plt.title("Boxplot do Custo por Cluster GMM")
plt.show()

pd.crosstab(df["cost_cluster"], df["media_type"], normalize="index") * 100
pd.crosstab(df["cost_cluster"], df["promotion_name"], normalize="index") * 100

import scipy.stats as stats

# Criar tabela de contingência (cross-tabulação)
contingencia = pd.crosstab(df["cost_cluster"], df["media_type"])

# Aplicar teste qui-quadrado
chi2, p, dof, expected = stats.chi2_contingency(contingencia)

# Exibir resultados
print(f"Estatística Qui-Quadrado: {chi2:.4f}")
print(f"Valor-p: {p:.4f}")

# Interpretar resultado
if p < 0.05:
    print("Existe associação significativa entre cost_cluster e media_type.")
else:
    print("Não há evidências suficientes para associação entre cost_cluster e media_type.")
    
df_contingencia = pd.crosstab(df["cost_cluster"], df["media_type"])


# Criar tabela de contingência entre promoção e categoria de custo
contingencia = pd.crosstab(df["cost_category"], df["promotion_name"])

# Aplicar teste qui-quadrado
chi2, p, dof, expected = stats.chi2_contingency(contingencia)

# Exibir resultado
print(f"Estatística Qui-Quadrado: {chi2:.4f}")
print(f"Valor-p: {p:.4f}")

# Interpretar
if p < 0.05:
    print("Existe associação significativa entre cost_category e promotion_name.")
else:
    print("Não há evidências suficientes para associação entre cost_category e promotion_name.")

df["cost_cluster"] = df["cost_cluster"].replace({0: 'Alto', 1: 'Baixo', 2: 'Médio'})
df_contingencia_media = pd.crosstab(df["cost_cluster"], df["media_type"]).T
df_contingencia_promotion = pd.crosstab(df["cost_cluster"], df["promotion_name"]).T

# Normalizar os valores (transformar em porcentagem por linha)
df_contingencia_media = df_contingencia_media.div(df_contingencia_media.sum(axis=1), axis=0) * 100
df_contingencia_promotion = df_contingencia_promotion.div(df_contingencia_promotion.sum(axis=1), axis=0) * 100

# Criar tabelas de contingência normalizadas
df_contingencia_media = pd.crosstab(df["cost_cluster"], df["media_type"])
df_contingencia_promotion = pd.crosstab(df["cost_cluster"], df["promotion_name"])

# Normalizar os valores (transformar em porcentagem por linha)
df_contingencia_media = df_contingencia_media.div(df_contingencia_media.sum(axis=1), axis=0) * 100
df_contingencia_promotion = df_contingencia_promotion.div(df_contingencia_promotion.sum(axis=1), axis=0) * 100


# Ordenar promotions em ordem decrescente pela porcentagem do cluster "Baixo"
df_contingencia_promotion = df_contingencia_promotion.sort_values(by="Baixo", ascending=False)

# Gráfico 1: Linha mostrando variação da porcentagem do cluster "Baixo" por promotion_name
plt.figure(figsize=(14, 6))
plt.plot(df_contingencia_promotion.index, df_contingencia_promotion["Baixo"], marker="o", linestyle="-", color="blue", label="Cluster Baixo")
plt.title("Variação da Porcentagem do Cluster 'Baixo' por Promotion Name")
plt.ylabel("Percentual (%)")
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.show()

# Gráfico 2: Heatmap mostrando apenas a coluna 'Baixo'
plt.figure(figsize=(14, 6))
sns.heatmap(df_contingencia_promotion[["Baixo"]], cmap="Blues", annot=True, fmt=".1f")
plt.title("Heatmap da Porcentagem do Cluster 'Baixo' por Promotion Name")
plt.xlabel("Cluster Baixo")
plt.ylabel("Promotion Name")
plt.show()

# Ordenar promotions em ordem decrescente pela porcentagem do cluster "Baixo"
df_contingencia_promotion = df_contingencia_promotion.sort_values(by="Alto", ascending=False)

# Gráfico 1: Linha mostrando variação da porcentagem do cluster "Baixo" por promotion_name
plt.figure(figsize=(14, 6))
plt.plot(df_contingencia_promotion.index, df_contingencia_promotion["Alto"], marker="o", linestyle="-", color="blue", label="Cluster Alto")
plt.title("Variação da Porcentagem do Cluster 'Alto' por Promotion Name")
plt.ylabel("Percentual (%)")
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.show()

# Gráfico 2: Heatmap mostrando apenas a coluna 'Baixo'
plt.figure(figsize=(14, 6))
sns.heatmap(df_contingencia_promotion[["Alto"]], cmap="Blues", annot=True, fmt=".1f")
plt.title("Heatmap da Porcentagem do Cluster 'Baixo' por Promotion Name")
plt.xlabel("Cluster Alto")
plt.ylabel("Promotion Name")
plt.show()

# Ordenar promotions em ordem decrescente pela porcentagem do cluster "Baixo"
df_contingencia_promotion = df_contingencia_promotion.sort_values(by="Médio", ascending=False)

# Gráfico 1: Linha mostrando variação da porcentagem do cluster "Baixo" por promotion_name
plt.figure(figsize=(14, 6))
plt.plot(df_contingencia_promotion.index, df_contingencia_promotion["Médio"], marker="o", linestyle="-", color="blue", label="Cluster Médio")
plt.title("Variação da Porcentagem do Cluster 'Médio' por Promotion Name")
plt.ylabel("Percentual (%)")
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.show()

# Gráfico 2: Heatmap mostrando apenas a coluna 'Baixo'
plt.figure(figsize=(14, 6))
sns.heatmap(df_contingencia_promotion[["Médio"]], cmap="Blues", annot=True, fmt=".1f")
plt.title("Heatmap da Porcentagem do Cluster 'Baixo' por Promotion Name")
plt.xlabel("Cluster Médio")
plt.ylabel("Promotion Name")
plt.show()

# Ordenar promotions em ordem decrescente pela porcentagem do cluster "Baixo"
df_contingencia_media= df_contingencia_media.sort_values(by="Baixo", ascending=False)

# Gráfico 1: Linha mostrando variação da porcentagem do cluster "Baixo" por promotion_name
plt.figure(figsize=(14, 6))
plt.plot(df_contingencia_media.index, df_contingencia_media["Baixo"], marker="o", linestyle="-", color="blue", label="Cluster Baixo")
plt.title("Variação da Porcentagem do Cluster 'Baixo' por Media")
plt.ylabel("Percentual (%)")
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.show()

# Gráfico 2: Heatmap mostrando apenas a coluna 'Baixo'
plt.figure(figsize=(14, 6))
sns.heatmap(df_contingencia_media[["Baixo"]], cmap="Blues", annot=True, fmt=".1f")
plt.title("Heatmap da Porcentagem do Cluster 'Baixo' por Media")
plt.xlabel("Cluster Baixo")
plt.ylabel("Media")
plt.show()