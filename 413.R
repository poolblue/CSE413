setwd("./RPro")
data = read.csv("relationships.csv", header = T)
matrix_d = as.matrix(data)
library(igraph)
graph = graph.adjacency(matrix_d, mode = c("directed"), weighted = NULL)
data_rank = page.rank(graph, vids = V(graph), directed = T, damping = 0.85, personalized = NULL, weights = NULL, options = NULL)
data_vector = vector[["vector"]]
data_vector[order(data_vector, decreasing = T)]