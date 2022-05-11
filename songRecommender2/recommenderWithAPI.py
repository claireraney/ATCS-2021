# by Claire Raney
# Program recommends song from given artist that resembles a given song based on danceability and tempo
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# authentication
client_id = "3f626ffc7e274c8ea070c3d2bf8f2b32"
client_secret = "765381053a9f497eb2ad1ce0f4c0ec58"
scope = "user-library-read"

# creating an object of spotipy
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri='http://127.0.0.1:9090', scope=scope))

# minimum number of songs required for cluster analysis
minSongs = 20

def main():

     # holds song data
     df1 = pd.DataFrame()

     # getting user data
     print("Welcome to my song recommender!")
     givenSong = input("Enter a song you want a recommendation based on: ")
     givenArtist = input("Enter the artist of your song: ")

     # calling methods
     # finds URI for given song
     songURI = searchForSong(givenSong, givenArtist)

     # finds attribute data for given song
     givenSongData = getFeaturesOfSong(songURI)

     # find attribute data for all songs from artist
     df1 = getAllSongsFromArtist(givenArtist)

     # confirms the artist has the minimum number of songs to perform analysis
     if len(df1) < minSongs:
         print("The artist doesn't have enough songs to provide a recommendation.")
         quit()

     # adds given song to end of the list
     df1.loc[len(df1.index)] = givenSongData

     # getting rid of duplicates (espicailly make sure the given song doesn't appear twice)
     df1.drop_duplicates(subset=['track'], keep='last', inplace=True)

     # converting data to csv
     df1.to_csv("songsFromArtist.csv")

     # performs sorting of songs to develop recommendation
     sortingSongs()


# searches for the song with the given artist and track, and returns its uri that is got from spotipy
def searchForSong(song, artist):

     # referred to this link: https://stackoverflow.com/questions/63290060/how-to-search-for-track-based-on-track-name-and-artist-in-spotipy
     toSearch = "track:" + song + "+artist:" + artist

     #spotipy library call
     results = sp.search(q=toSearch)
     songs = results["tracks"]["items"]

     #returns song URI from given song
     return songs[0]["uri"]

# gets the danceability and tempo of a song given the songURI
# referred to this link: https://stackoverflow.com/questions/58945197/extracting-audio-features-from-spotify-using-track-uris
def getFeaturesOfSong(songURI):

    artist = []
    track = []
    danceability = []
    tempo = []

    # spotipy API calls which extract audio features and track information of song
    # referred to this link: https://stackoverflow.com/questions/58945197/extracting-audio-features-from-spotify-using-track-uris
    x = sp.audio_features(songURI)
    y = sp.track(songURI)
    for audioFeatures in x:
         danceability.append(audioFeatures["danceability"])
         tempo.append(audioFeatures["tempo"])
    artist.append(y["album"]["artists"][0]["name"])
    track.append(y["name"])

    # creates row to be added to dataframe for song attributes
    row = (artist[0], track[0], danceability[0], tempo[0])

    return row

# identifies 300 songs for given artist and creates data frame of songs and attributes
def getAllSongsFromArtist(artist):

    # create dataframe
    df = pd.DataFrame(columns=["artist", "track", "danceability", "tempo"])

    # search term based on artist
    toSearch = "artist:" + artist

    # list of artists song URIs
    songURIs = []

    # spotipy API call which pulls 300 songs from artist
    for i in range(6):
        results = sp.search(q=toSearch, limit=50, offset=50*i)
        songs = results["tracks"]["items"]
        for song in songs:
            # builds song URI list
            songURIs.append(song["uri"])

    # for each song, adds row to dataframe with song attributes
    for uri in songURIs:
        row = getFeaturesOfSong(uri)
        df.loc[len(df.index)] = row

    return df

# clusters the songs to be reccomended based on K Means
def sortingSongs():
    ''' Load Data '''
    # reads the csv
    data = pd.read_csv("songsFromArtist.csv")
    x = data[["danceability", "tempo"]]

    # index of the given song
    index = len(data)-1

    # Standardize data
    scaler = StandardScaler().fit(x)
    x = scaler.transform(x)

    # Calculate internia for K = 1 to MINSONG
    inertias = []
    for k in range (1, minSongs):
        # Build and fit the model
        kmeanModel = KMeans(n_clusters=k).fit(x)
        # Store the inertias
        inertias.append(kmeanModel.inertia_)

    # Plot the inertias to find the elbow
    plt.plot(range(1, minSongs), inertias, 'bx-')
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
    # print(labels)

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
    #plt.show()

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
    for i in range(len(data)):
        if labels[i] == labels[index] and i != index:
            print("Recommended song: ", data.iloc[i]["track"])
            break

if __name__ == '__main__':
    main()

