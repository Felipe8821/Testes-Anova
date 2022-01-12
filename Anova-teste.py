#Primeiro passo: importar libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

#Segundo passo: montar a df com dados de tricomas
df = pd.DataFrame(
    {   "MT": [2,3,42,96,12],
        "MTMeJa": [2,3,40,145,9]},
    index = [1,3,5,6,7])

mod = ols('MT ~ MTMeJa', data = df).fit()
aov_table=sm.stats.anova_lm(mod, type=2)

print(aov_table)
