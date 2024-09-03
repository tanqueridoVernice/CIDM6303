# Follow the instructions for what to code in this file.
# Vernice Tanquerido

table1 = [18.1, 15.4, 19.0, 13.4, 10.2,
          13.1, 18.1, 14.4, 15.0, 10.8, 5.4, 12.2]
table2 = [0.7, 0.0, 0.7, 1.0, 1.1, 0.4, 0.0, 1.0, 2.3, 2.9, 1.3]

total_before = 0
total_after = 0
for x in table1:
    total_before += x
for x in table2:
    total_after += x

avg_before = total_before/len(table1)
avg_after = total_after/len(table2)
print(f"Average mortality rate before hand washing policy: {avg_before:.1f}")
print(f"Average mortality rate before hand washing policy: {avg_after:.1f}")
