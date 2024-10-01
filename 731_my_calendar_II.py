class MyCalendarTwo(object):

    def __init__(self):
        self.split = [0, int(1e9+1)]
        self.tag = [0]

    def locate(self, pos):
        left = 0
        right = len(self.tag)
        cur = (left + right) // 2
        while True:
            if self.split[cur] > pos:
                right = cur
            elif self.split[cur+1] <= pos:
                left = cur
            else:
                break
            cur = (left + right) // 2
        return cur

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # locate start and end
        left_seg = self.locate(start)
        right_seg = self.locate(end)

        # check availability
        for i in range(left_seg, right_seg):
            if self.tag[i] == 2:
                return False
        right_overlap = self.split[right_seg] == end
        if (not right_overlap) and self.tag[right_seg] == 2:
            return False

        # change the status
        
        left_overlap = self.split[left_seg] == start
        if not left_overlap:
            self.tag.insert(left_seg+1, self.tag[left_seg])
            self.split.insert(left_seg+1, start)
        for i in range(left_seg, right_seg):
            self.tag[i+ 1 - int(left_overlap)] += 1
        if not right_overlap:
            self.tag.insert(right_seg+1+int(not left_overlap), self.tag[right_seg+int(not left_overlap)])
            self.tag[right_seg+int(not left_overlap)] += 1
            self.split.insert(right_seg+1+int(not left_overlap), end)
        return True
        
if __name__ == "__main__":
	books = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
	obj = MyCalendarTwo()
	for book in books:
		print(obj.book(book[0], book[1]))

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)