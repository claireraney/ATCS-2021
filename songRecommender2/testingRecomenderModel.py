import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import random
import csv

''' Load Data '''
data = pd.read_csv("spotify_taylorswift.csv")
x = data[["danceability", "tempo"]]

# gotten from stack overflow, does this work??
index = random.randint(1, 170)
print("Given song: ", data.iloc[index]["name"])

# Standardize data
scaler = StandardScaler().fit(x)
x = scaler.transform(x)

''' Create the Model '''
# based on number of albums
k = 9
km = KMeans(n_clusters=k).fit(x)

# Get the centroids and label values
centroids = km.cluster_centers_

labels = km.labels_
print(labels)

''' Visualize the Clusters '''
# set the size of the graph
plt.figure(figsize=(5,4))

# plot the data points for each of the k clusters
for i in range(k):
    # Get all the points x[n] where labels[n] == the label i
    cluster = x[labels == i]
    # Get the income and the spending values for each point in the cluster
    cluster_danceability = cluster[:, 0]
    cluster_tempo = cluster[:, 1]
    plt.scatter(cluster_danceability, cluster_tempo)

# Plot the centroids
centroids_danceability = centroids[:, 0]
centroids_tempo = centroids[:, 1]
plt.scatter(centroids_danceability, centroids_tempo, marker='X', s=100, c='r')
plt.show()

# scatter first and second row
plt.scatter(x[:, 0], x[:, 1])
plt.xlabel("Danceability")
plt.ylabel("Tempo")
plt.show()


# psuedocoding for finding song to reccomend based on the cluster of the song given
# cluster number of song given is labels[index]
for i in range(1,170):
    if labels[i] == labels[index] and i != index:
        print("Recommended song: ", data.iloc[i]["name"])
        break
# given song cluster variable
# get reccomendation by randomly picking one of the songs in the cluster that the given song comes from
# return song recommendation




