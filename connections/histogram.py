from random import randint
import matplotlib.pyplot as pyplot
def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list
	

def compute_histogram_bins(data=[], bins=[]):
	def affectation_data_bins(element , bins):
			output = []
			if isinstance(element , int) or isinstance(element , float):
				for i in range(0,(len(bins) - 1)):
					if ((bins[i] < element) and (element <= bins[i+1])):
						output.append([element , bins[i+1]])
					elif (bins[i] == element) :
						output.append([element , bins[i]])
			return output

	resultats = list(map(lambda x : affectation_data_bins(x , bins) , data))
	resultats = sorted(flatten_list(resultats))
		
	lst = [[] for element in range(len(bins))]
	for i in range(0,(len(resultats) - 1)):
	    if (resultats[i][1] == resultats[i+1][1]):
		    lst[bins.index(resultats[i][1])].append(resultats[i][0])

	distributions = list(map(lambda x : len(x) , lst))
	distributions_bins = [[bin_element , distrib] for distrib , bin_element in zip(distributions , bins)]
		
	return distributions_bins
 




def plot_histogram(bins_count):
    Y = [bucket_bins[1] for bucket_bins in bins_count]
    X = range(0 , len(Y))
    
    pyplot.bar(X,Y, width = 0.5, color = 'blue')
    pyplot.xticks(range(0,len(X)), ['0-10', '10-20', '20-30', '30-40', '40-70' , '70-100' , '100+'])
    pyplot.savefig("connections.png")

if __name__ == "__main__":

    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
