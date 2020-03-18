import argparse
parser = argparse.ArgumentParser()
parser.add_argument("Base", type = int , help= "The Base ")
parser.add_argument("Exponent", type = int , nargs = '?' , default = 2 , help = "The Exponent" )
parser.add_argument("-v", "--verbosity" , action = "count", default = 0)
args = parser.parse_args()
args_1 = vars(parser.parse_args())
print args_1
ans = args.Base**args.Exponent
if args.verbosity >= 3 :
	print "Running {} ".format(__file__)
if args.verbosity >= 2 :
	print " This Program Prints the value of x^y where x and y are entered by the user "
	print " Note : The value of y is taken to be 2 unless provided explicitly"
if args.verbosity >= 1 :
	print "{}^{} = {}".format(args.Base,args.Exponent,ans)
print ans
