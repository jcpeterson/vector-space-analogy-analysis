# Save a mapping of each AB pair to the corresponding relation

import cPickle

# Read the AB pairs
paradigmsFileName = '../../word2vec-tests/data/analogy/SemEval-2012-Complete-Data-Package/subcategories-paradigms-edited2.txt'
rev_rels = ['1a', '1e', '2a', '2b', '10c']

AB_rel_dict = {}
with open(paradigmsFileName, 'r') as paradigmsFile:
    for line in paradigmsFile:
        line = line.strip()
        parts = line.split(', ')
        # The short name for the relation (e.g., "1a")
        relation = parts[0] + parts[1]
    	AB_pairs = [pair.split(':') for pair in parts[4:]]
        for pair in AB_pairs:
            if relation in rev_rels:
                AB = (pair[1], pair[0])
            else:
                AB = tuple(pair)
            AB_rel_dict[AB] = relation

with open('AB_rel_dict.pickle', 'wb') as dictFile:
    cPickle.dump(AB_rel_dict, dictFile, cPickle.HIGHEST_PROTOCOL)