# Город состоит из n перекрестков. Некоторые перекрестки соединены направленными дорогами. Для дорог задана максимальная масса автомобиля, который может проехать по дороге, не повреждая дорожное покрытие.
# Для каждой пары вершин u, v требуется найти максимальную массу машины, которая может проехать от перекрестка u до перекрестка v.
# Если не существует пути между перекрестками, следует вывести 0. Если же нет ограничений на массу машины, то требуется вывести 
# 2000000023.
# Формат ввода
# В первой строке находится одно целое число 
# n(1≤n≤500) — количество перекрестков в городе.
# Далее записана матрица смежности города: n строк по n чисел gi,j(−1≤gi,j≤109) – максимальная масса машины, которая может проехать от перекрестка i до перекрестка j по прямой дороге. Если дороги между i-м и j-м перекрестком не существует, то gi,j=0. Если же нет ограничений на массу автомобиля, то gi,j=−1. Гарантируется, что на главой диагонали матрицы g все элементы нулевые.
# Формат вывода
# Выведите ответ на задачу в виде матрицы 
# ans(u,v), где ans(u,v) равно максимальной массе машины, которая может проехать от перекрестка u до перекрестка v.
# Если u=v или нет ограничений на массу машины, то будем считать ans(u,v)=2000000023. Если же проехать от перекрестка u до перекрестка v невозможно, следует вывести 0.

INF = 2000000023

n = int(input())
graph = [[0] * n for _ in range(n)]

# инициализируем матрицу смежности графа
for i in range(n):
    row = list(map(int, input().split()))
    for j, val in enumerate(row):
        if val == 0:
            graph[i][j] = -INF
        else:
            graph[i][j] = val

# алгоритм Флойда-Уоршелла
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = max(graph[i][j], min(graph[i][k], graph[k][j]))

# выводим результат
for i in range(n):
    for j in range(n):
        if i == j:
            print(INF, end=' ')
        elif graph[i][j] == -INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()


