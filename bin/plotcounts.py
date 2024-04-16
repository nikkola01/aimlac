"""Plot word counts."""
import argparse
import pandas as pd
import matplotlib.pyplot as plt
def main(args):
    """Run the command line program."""
    word_counts = count_words(args.infile)
    util.collection_to_csv(word_counts, num=args.num)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Plot word counts")
	parser.add_argument('infile', type=argparse.FileType('r'),
                    nargs='?', default='-',
                       help='Word count csv file name')
	parser.add_argument('--xlim', type=float, nargs=2,
                    metavar=('XMIN', 'XMAX'),
                    default=None, help='X-axis limits')
	parser.add_argument('--outfile', type=str,
                    default='plotcounts.png',
                    help='Output image file name')
	args = parser.parse_args()

	df = pd.read_csv(args.infile, header=None,
                 names=('word', 'word_frequency'))
	df['rank'] = df['word_frequency'].rank(ascending=False,
                                       method='max')
	df['inverse_rank'] = 1 / df['rank']
	ax = df.plot.scatter(x='word_frequency',
                     y='inverse_rank',
                     figsize=[12, 6],
                     grid=True,
                     xlim=args.xlim)

	plt.savefig(args.outfile)
	main(args)
