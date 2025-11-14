from museum import artists, artwork


def main():
    artistName = input("write an artist for searching in chicago museum: ")

    artists_names = artists.get_artists(artistName, 3)
    artist_work = artwork.get_art_work(artistName, 3)

    for artist in artists_names:
        print(f". {artist}")

    for art_work in artist_work:
        print(f". {art_work}")


main()
