
class node:
    def __init__(self, song):
        self.song = song
        self.next = None

class playlist:
    def __init__(self):
        self.head = None

    def add(self, song):
        new = node(song)

        if not self.head:
            self.head = new
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new

    def show(self):
        cur = self.head

        while cur:
            print(cur.song, end=" -> ")
            cur = cur.next

        print("end")

p = playlist()
p.add("song a")
p.add("song b")
p.add("song c")
p.show()
