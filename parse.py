from os import listdir, makedirs
from os.path import join
from bs4 import BeautifulSoup, Tag, NavigableString


def dive(current):
    if not current.parent or isinstance(current, NavigableString):
        return current
    if 'a' == current.name and 1 == len(current.contents) and isinstance(current.contents[0], NavigableString):
        return tree.new_string("[%s](%s)" % (current.contents[0].strip(), current['href']))
    elif 'span' == current.name and 1 == len(current.contents) and isinstance(current.contents[0], NavigableString):
        return current.contents[0]
    elif 'br' == current.name:
        return tree.new_string("\n\n")
    else:
        s = []
        for child in current.contents:
            s.append(dive(child))
        return s


def save(directory, name):
    if name in h2.string:
        with open(join(directory, name + '.md'), 'w+', encoding='utf-8') as fout:
            current = h2.nextSibling
            while current:
                if isinstance(current, (NavigableString, str)):
                    fout.write(current)
                elif isinstance(current, Tag):
                    if 'h2' == current.name:
                        break
                    result = dive(current)
                    if not result:
                        fout.write(current.prettify())
                    elif isinstance(result, Tag):
                        fout.write(result.prettify())
                    elif isinstance(result, list):
                        for item in result:
                            if isinstance(item, list):
                                for it in item:
                                    if it:
                                        fout.write(it)
                            elif item:
                                fout.write(item)
                            # if isinstance(item, (NavigableString, str)):
                            #     fout.write(item)
                            # else:
                            #     fout.write(item.prettify())
                current = current.nextSibling

i = 0

for file in listdir('loads'):
    with open(join('loads', file), 'r', encoding='utf-8') as fin:
        tree = BeautifulSoup(fin.read())
    headers = tree.find_all('h2')
    for h2 in tree.find_all('h2'):
        i += 1
        directory = join('themes', str(i))
        makedirs(directory)
        save(directory, 'Articles')
        save(directory, 'Libraries')
        save(directory, 'Screencasts')
