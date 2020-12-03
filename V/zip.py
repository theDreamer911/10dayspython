# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
# #
# # output wanted = [(1, 10), (2, 20), (3, 30)]
# # print(list(zip( list1,  list2)))
# print(list(zip('abc', list1, 'bac', list2)))


# browsing_section = []
# browsing_section.append(1)
# browsing_section.append(2)
# browsing_section.append(3)
# browsing_section.append(5)
# browsing_section.append(6)
# print(browsing_section)
# last = browsing_section.pop()
# print('removed:', last)
# print(browsing_section)

# print("redirect", browsing_section[-1])


from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(5)
queue.append(7)
queue.popleft()
print(queue)
if not queue:
    print('empty')
