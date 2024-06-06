data = """
4000.0,2.13472e+17,1.94066e+17,1.94065e+17,28893400000.0,1.94066e+16,0.000167,9.33162e-63,1.0
4999.99,1.70781e+17,1.55254e+17,1.55252e+17,1584990000000.0,1.55254e+16,5.37001,3.96712e-46,1.0
5999.99,1.42361e+17,1.29398e+17,1.29375e+17,23073700000000.0,1.29398e+16,5476.36,5.08183e-35,1.0
6999.99,1.22297e+17,1.11037e+17,1.10879e+17,157119000000000.0,1.11037e+16,776694.0,4.52444e-27,1.0
7999.99,1.08058e+17,9.76312e+16,9.69675e+16,663651000000000.0,9763120000000000.0,32128500.0,4.2599e-21,1.0
8999.99,9.89127e+16,8.80722e+16,8.60388e+16,2033340000000000.0,8807220000000000.0,587813295.0,1.9361e-16,1.00508
9999.99,9.50935e+16,8.19678e+16,7.70389e+16,4928900000000000.0,8196780000000000.0,6105000000.0,1.05071e-12,1.01292
11000.0,9.68395e+16,7.90221e+16,6.91069e+16,9915180000000000.0,7902170000000000.0,42053800000.0,1.20327e-09,1.0167
12000.0,1.03485e+17,7.85615e+16,6.14944e+16,1.70671e+16,7855940000000000.0,212423000000.0,4.25261e-07,1.01729
13000.0,1.12735e+17,7.92142e+16,5.36155e+16,2.55987e+16,7920580000000000.0,834141000000.0,5.98279e-05,1.01645
14000.0,1.21254e+17,7.94221e+16,4.55354e+16,3.38867e+16,7939580000000000.0,2625490000000.0,0.00396149,1.01618
15000.0,1.26437e+17,7.83607e+16,3.8127e+16,4.02337e+16,7829340000000000.0,6736550000000.0,0.137499,1.01755
16000.0,1.27546e+17,7.60783e+16,3.22326e+16,4.38457e+16,7593510000000000.0,14325100000000.0,2.71224,1.02048
17000.0,1.25438e+17,7.30564e+16,2.80062e+16,4.50502e+16,7279690000000000.0,25948500000000.0,33.1445,1.02436
18000.0,1.21511e+17,6.97866e+16,2.50828e+16,4.47039e+16,6937110000000000.0,41554700000000.0,276.488,1.02855
19000.0,1.16964e+17,6.65552e+16,2.28634e+16,4.36917e+16,6594030000000000.0,61482900000000.0,1752.14,1.04296
20000.0,1.12316e+17,6.34926e+16,2.11043e+16,4.23883e+16,6263420000000000.0,85845400000000.0,8942.71,1.06182
21000.0,1.07778e+17,6.06439e+16,1.96885e+16,4.09553e+16,5949980000000000.0,114407000000000.0,38123.9,1.07935
"""

lines = data.strip().split('\n')
dicts = []

for line in lines:
    values = line.split(',')
    T = float(values[0])
    rho = float(values[1])
    H = float(values[2])
    HI = float(values[3])
    HII = float(values[4])
    HeI = float(values[5])
    HeII = float(values[6])
    HeIII = float(values[7])
    b1 = float(values[8])

    dictionary = {
        'T': T,
        'rho': rho,
        'H': H,
        'HI': HI,
        'HII': HII,
        'HeI': HeI,
        'HeII': HeII,
        'HeIII': HeIII,
        'b1': b1
    }

    dicts.append(dictionary)

# Salida final en forma de diccionarios
for i, d in enumerate(dicts):
    print(f"T{i+1} = {d}")