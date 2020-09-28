class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        # tracks oldest item
        self.oldest = 0

    def append(self, item):
        # check if buffer isn't full yet
        if len(self.data) < self.capacity:
            # append the item
            self.data.append(item)
        # otherwise if the buff is full
        else:
            # delete oldest item
            del self.data[self.oldest]
            # insert item into location of oldest item
            self.data.insert(self.oldest, item)
            # check if oldest is last item in data
            if self.oldest == self.capacity-1:
                # Reset oldest to first item in data
                self.oldest = 0
            # otherwise if oldest is not yet last item in data
            else:
                # increase oldest placement by 1
                self.oldest += 1

    def get(self):
        # remove all None items from data
        no_none = [i for i in self.data if i]
        return no_none
