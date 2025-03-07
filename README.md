//create the team struct
team{name: string,strength:int}

Algorithm championsLeague()
	teams<-Initializeteams()
	while length(teams)>1 Do
		teams<-simulateround(teams)
	end while
	display "the champion is :",teams[1]
end algo

algorithm initializeteams()
	//read the size of the array
	repeat
		read(N)
	until(test(N))
	//fill the array
	for i from 1 to N
		team.name<-'T',i
		team.strength<-random(1,100)
		team[i]<-team
	end for
	return teams
end algo

algorithm Simulateround(teams)
	winners<-[]
	N<-length(teams)
	for i from 1 to Ndiv2
		winner<-simulatematch(teams[i],teams[N+1-i])
		winners[i]<-winner
	end for
	return winners
end algo

algorithm simulatematch(T1,T2)
	rand<-random(1,100)
	if (40<=rand<=60)
		if(T1.strength<T2.strength)
			return T2
		else
			return T1
	else
		if(T1.strength<T2.strength)
			return T2
		else
			return T1
	end if
end algo

Algorithm test (N)

	while(N mod 2 = 0)
		N<-N div 2
	end while
	if N =1		
		return True
	else 
		return false
end algo

Complexity :
	O(1) :simulatematch()
	O(log(n)):Test(n)
	O(n):Initializeteams()
total complexity : 1+ log(n) + n
Final Complexity is O(n)


Sorting Algorithm Performance Analysis

Overview

This repository contains an analysis of the performance of different sorting algorithms, including:

Bubble Sort

Selection Sort

Python's Built-in `` (Timsort)

The goal is to compare execution times and understand the efficiency of each algorithm for different dataset sizes.

Execution Time Comparison

Small Dataset (50 elements):

✅ Bubble Sort took 0.001000 seconds.✅ Selection Sort took 0.000000 seconds.

Large Dataset (10,000 elements):

⚠️ Bubble Sort took 5.852864 seconds.✅ Selection Sort took 2.510549 seconds.🚀 Python Built-in Sort took 0.002001 seconds.

Key Observations

Selection Sort performs slightly better than Bubble Sort but is still inefficient for large datasets.

**Python's Built-in **`` (Timsort) is significantly faster than both, making it the preferred choice for large-scale sorting.

Complexity Analysis

Algorithm

Time Complexity (Best)

Time Complexity (Worst)

Bubble Sort

O(n)

O(n²)

Selection Sort

O(n²)

O(n²)

Python sort() (Timsort)

O(n log n)

O(n log n)

Real-World Implications

Using inefficient sorting methods can lead to:

Longer processing times in large datasets.

Higher computational costs due to increased CPU usage.

Poor user experience in applications requiring real-time sorting.

Scalability issues as data size grows.

Conclusion

For practical applications, Timsort (Python's ``) should be used due to its superior efficiency. Algorithms like Merge Sort, Quick Sort, or Radix Sort also offer better performance compared to Bubble Sort and Selection Sort.
