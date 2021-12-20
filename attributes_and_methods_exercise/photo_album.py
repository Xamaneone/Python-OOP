class PhotoAlbum:
    def __init__(self, pages):
        self.pages = int(pages)
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(int(photos_count / 4))

    def add_photo(self, label):
        counter = -1
        for page in self.photos:
            counter += 1
            if len(page) == 4:
                continue
            self.photos[counter].append(label)
            return f"{label} photo added successfully on page {counter + 1} slot {len(self.photos[counter])}"
        return 'No more free spots'

    def display(self):
        result = ''
        for row in self.photos:
            result += f"-----------\n"
            if len(row) > 0:
                result += f"{' '.join(['[]' for el in row])}\n"
            else:
                result += '\n'
        result += f"-----------\n"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())




import unittest


class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free spots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------\n")


if __name__ == "__main__":
    unittest.main()