from threading import Thread
from time import sleep

def slice(text, chunk_size):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks


def count_letters(text, letter, threads):
    TOTALS = []

    def count_chunk(chunk, letter):
        TOTALS.append(sum([c == letter for c in chunk]))

    length = len(text)
    chunk_size = length // threads
    chunks = slice(text, chunk_size)
    for chunk in chunks:
        p = Thread(target=count_chunk, args=(chunk, letter)).start()

    while len(TOTALS) != len(chunks):
        sleep(0.01)

    return sum(TOTALS)

if __name__ == '__main__':
    print(count_letters("there are so many letter e here", "e",8))
