import khmer, sys, os
import gc
import glob

filename=sys.argv[1]
basename = os.path.basename(filename)
pmap_filename = sys.argv[2]

if not os.path.exists(filename):
    print '%s doesn\'t exist! dying.' % filename
    sys.exit(0)

# create a fake-ish ht; K matters, but not hashtable size.
ht = khmer.load_hashbits(basename + '.ht')
ht.load_tagset(basename + '.tagset')
ht.merge_subset_from_disk(pmap_filename)

# find singletons
n_singletons = ht.find_unpart(filename)
print 'found:', n_singletons

n_partitions = ht.output_partitions(filename, basename + '.unpart')

###

(n_partitions, n_singletons) = ht.count_partitions()

print 'output partitions:', n_partitions
print 'pmap partitions:', n_partitions
print 'singletons:', n_singletons
