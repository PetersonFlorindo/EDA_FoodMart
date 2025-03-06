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
dados_colunas_quant = df.select_dtypes(exclude=['object']).describe()

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

#criação de tabela de contigência por tipo de mercado
freq_rel_member_card = pd.crosstab(index=df_quali['member_card'], columns='Porcentagem', normalize=True).sort_values('Porcentagem' ,ascending = False)
freq_rel_member_card['Porcentagem'] = (freq_rel_member_card['Porcentagem']*100).round(2)
#configurando e gerando plot em barras
ax2 = sns.barplot(data=freq_rel_member_card,x='member_card',y='Porcentagem',hue='Porcentagem',palette='rocket')
ax2.set_box_aspect(1/3)
for container in ax2.containers: ax2.bar_label(container, fmt='%.2f',padding = 3,fontsize=8)
plt.Figure(figsize=(20,6), dpi = 20)
plt.title('Distribuição das vendas em promoção por de cliente', fontsize=10)
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
freq_rel_income = pd.crosstab(index=df_quali['avg. yearly_income'], columns='Porcentagem', normalize=True).sort_values('Porcentagem' ,ascending = False)
freq_rel_income['Porcentagem'] = (freq_rel_income['Porcentagem']*100).round(2)
#configurando e gerando plot em barras
ax4 = sns.barplot(data=freq_rel_income,x='avg. yearly_income',y='Porcentagem',hue='Porcentagem',palette='rocket')
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
    #ordena variáveis em ordem decrescente
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

#Iniciando análise bivariada
df_quant_corrigido = df_quant.drop(columns=df_quali_adicionais.columns)
df_quant_corrigido = df_quant_corrigido.drop(columns='avg_cars_at home(approx).1')
#Análise Quanti x Quanti
plt.figure(figsize = (20,10))
sns.heatmap(df_quant_corrigido.corr(), annot= True)
plt.title('Matriz de correlação')
plt.show()

#analise quanti x quali
        