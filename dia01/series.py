#%%
import pandas as pd
# %%
# Isso é uma lista
idade = [11,54,23,69,52,23,20]
# A medida que a lista cresce, ela deixa de ser perfomática, além de não tem a finalidade analitica.
s_idade = pd.Series(idade)
#O pd.Series transforma a minha lista em series. O Que é mais recomendado para utilização analitica.
# %%
# Métodos das séries
s_idade.mean()
variancia = s_idade.var()
desvio_padrao = s_idade.std()
s_idade.describe()

# %%
## Series todos os objetos tem que ser do mesmo tipo