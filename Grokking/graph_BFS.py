graph = {}
graph["You"] = ["Alice", "Bob", "Claire"]
graph["Alice"] = ["Peggy"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Claire"] = ["Johnny", "Thom"]
graph["Anuj"] = []
graph["Peggy"] = []
graph["Johnny"] = []
graph["Thom"] = []

def is_mango_seller(name):
    return name[-1] == 'm'

from collections import deque

def search_queue_fun(name):
    search_queue = deque()
    search_queue += graph["You"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_mango_seller(person):
                return person + " is a mango seller!"
            else:
                search_queue += graph[person]
                searched.append(person)
    return "No mango sellers."

print(search_queue_fun("You"))