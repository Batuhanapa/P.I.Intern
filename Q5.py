
import numpy as np
import pandas as pd

Vac_Stats = pd.read_csv('country_vaccination_stats.csv')
Vac_Stats = pd.DataFrame(Vac_Stats)

Vac_Stats['daily_vaccinations'] = Vac_Stats['daily_vaccinations'].fillna(Vac_Stats.groupby('country')['daily_vaccinations'].transform("min"))
Vac_Stats['daily_vaccinations'].fillna(0,inplace = True)
Vac_Stats.groupby('country')['daily_vaccinations'].median().nlargest(3)





