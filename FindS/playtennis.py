import csv
with open('playgame.csv','r') as f:
	reader=csv.reader(f)
	your_list=list(reader)
	k=0
	h=[['0','0','0','0','0','0']]
	for i in your_list:
		print("for the training sample",(k))
		if i[-1]=="TRUE":
			j=0
			for x in i:
				if x != "TRUE":
					if x!=h[0][j] and h[0][j]=='0':
						h[0][j]=x
					if x!=h[0][j] and h[0][j]!='0':
						h[0][j]='?'
				j=j+1
		k+=1
		print("the hypothesis is:",h)
print("maximally specific hypothesis is",h)
                    