all: mergesort.cpp
	g++ -g -std=c++17 -Wall -Werror -pedantic -o mergesort mergesort.cpp
	g++ -g -std=c++17 -Wall -Werror -pedantic -o maxheap maxheap.cpp

clean:
	rm -rf mergesort
	rm -rf maxheap
