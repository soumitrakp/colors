import pandas as pd

df = pd.read_csv("color_map.csv")

primary = df[df['primary']==1]
secondary = df[df['primary']!=1]

print primary
print secondary

with open("color_map.R", "w") as f:
  maps = []
  for i, row in primary.iterrows():
    maps.append("'{}' = '{}'".format(row['key'], row['value']))
  f.write("primary_colors = c(%s)\n" % ',\n\t'.join(maps))
  maps = []
  for i, row in secondary.iterrows():
    maps.append("'{}' = '{}'".format(row['key'], row['value']))
  f.write("cateogory_colors = c(%s)\n" % ',\n\t'.join(maps))

with open("color_map.tex", "w") as f:
  maps = []
  for i, row in primary.iterrows():
    maps.append("\\def\\col{}{{{}}}".format(row['key'], row['value'][1:]))
  f.write("%s\n" % '\n'.join(maps))
  maps = []
  for i, row in secondary.iterrows():
    maps.append("\\definecolor{{col{}}}{{HTML}}{{\\col{}}}".format(row['key'], row['value']))
  f.write("%s\n" % '\n'.join(maps))
