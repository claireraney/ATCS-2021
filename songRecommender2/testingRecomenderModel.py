# by Claire Raney
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import random
import csv

''' Load Data '''
data = pd.read_csv("spotify_taylorswift.csv")
x = data[["danceability", "tempo"]]

# choosing a random song from the csv to use as the given song
index = random.randint(1, 170)
print("Given song: ", data.iloc[index]["name"])

# Standardize data
scaler = StandardScaler().fit(x)
x = scaler.transform(x)


# Calculate internia for K = 1 to 20
inertias = []
for k in range (1, 20):
    # Build and fit the model
    kmeanModel = KMeans(n_clusters=k).fit(x)
    # Store the inertias
    inertias.append(kmeanModel.inertia_)

# Plot the inertias to find the elbow
plt.plot(range(1, 20), inertias, 'bx-')
plt.xlabel("Values of K")
plt.ylabel("Inertia")
plt.show()

''' Create the Model '''
# based on the elbow method
k = 5
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
    # Get the danceability and the tempo values for each point in the cluster
    cluster_danceability = cluster[:, 0]
    cluster_tempo = cluster[:, 1]
    plt.scatter(cluster_danceability, cluster_tempo)
# plt.show()

# cluster based on the dancibility and tempo for each album
albums = data["album"].unique()
for i in range (len(albums)):
    cluster = data.loc[data['album'] == albums[i]]
    cluster_danceability = cluster["danceability"]
    cluster_tempo = cluster["tempo"]
    plt.scatter(cluster_danceability, cluster_tempo)

# cluster based on the dancibility and tempo for each album
albums = data["album"].unique()
for i in range (len(albums)):
    cluster = data.loc[data['album'] == albums[i]]
    cluster_danceability = cluster["danceability"]
    cluster_tempo = cluster["tempo"]
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


# recommending based on being in the same cluster
for i in range(1,170):
    if labels[i] == labels[index] and i != index:
        print("Recommended song: ", data.iloc[i]["name"])
        break





