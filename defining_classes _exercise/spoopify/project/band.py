class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name not in [album.name for album in self.albums]:
            return f"Album {album_name} is not found."
        album = [album for album in self.albums if album.name == album_name][0]
        if album.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(album)
        return f"Album {album.name} has been removed."


        # album = [album for album in self.albums if album_name == album]
        # if album:
        #     album = album[0]
        #     if album.published == True:
        #         return "Album has been published. It cannot be removed."
        # if not album:
        #     return f"Album {album_name} is not found."
        # self.albums.remove(album)
        # return f"Album {album_name} has been removed."

    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += f" {album.details()}\n"
        return result