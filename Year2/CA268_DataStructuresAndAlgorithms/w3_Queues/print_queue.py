def print_queue(lst, front, back):
    stuff = []
    while front != back:
        item = lst[front]
        stuff.append(item)
        front = (front + 1) % len(lst)
    return stuff
