n_classes = 3
plot_colors = "ryb"

for i, color in zip(range(n_classes), plot_colors):
    print(i, color)

for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]):
    print(pairidx, pair)