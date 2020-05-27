'''
Deber 02: Generating random variables (discrete)
Responda por simulación:

El propietario de un puesto de periódicos recibe 50 ejemplares del periódico El Uninverso cada mañana. La cantidad de ejemplares demandados, X, varía al azar de acuerdo con la siguiente distribución de probabilidad:

f(x)=⎧⎩⎨⎪⎪⎪⎪145,130,133,x=35,36,...,49x=50,51,...59x=60,61,...70
Determine la probabilidad de que el propietario venda todos los ejemplares.
Determine el número esperado de ejemplares no vendidos por día.
Un ejemeplar cuesta 50 centavos y se vende a $1.00. Determine el ingreso neto esperado por día.
'''
import numpy as np

no_sell = 50 - np.array(range(35, 71))

no_sell[np.where(no_sell < 0)[0]] = 0

print(no_sell)

px = np.concatenate((np.ones(50-35)*1/45, np.ones(60-50)*1/30,
                    np.ones(71-60)*1/33))
print(px, np.sum(px), len(no_sell), len(px))

# unsold estimated value
np.sum(no_sell * px)

pos_all_sell = np.where(no_sell == 0)[0]
print(np.sum(px[pos_all_sell]))
np.sum(px[15:])


no_sell_sim = np.random.choice(no_sell, p=px)

Sold = 50 - no_sell_sim
no_sell_sim, Sold


# Una sola simulación, hay que repetir muchas veces y promediar
Sold*1 - 50*0.50  # Utilidad diaria