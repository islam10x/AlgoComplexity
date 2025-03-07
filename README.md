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


