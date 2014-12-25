from os import listdir, makedirs
from os.path import join
from bs4 import BeautifulSoup, Tag


def save(directory, name):
        if name in h2.string:
            with open(join(directory, name + '.html'), 'w+', encoding='utf-8') as fout:
                current = h2.nextSibling
                while current:
                    if isinstance(current, Tag):
                        if 'h2' == current.name:
                            break
                        fout.write(str(current))
                    current = current.nextSibling

i = 0

for file in listdir('loads'):
    with open(join('loads', file), 'r', encoding='utf-8') as fin:
        tree = BeautifulSoup(fin.read())
    for h2 in tree.find_all('h2'):
        i += 1
        directory = join('themes', str(i))
        makedirs(directory)
        save(directory, 'Articles')
        save(directory, 'Libraries')
        save(directory, 'Screencasts')
