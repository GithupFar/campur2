#include <stdio.h>
#include <stdlib.h>

int countwalks(int graph[100][100], int u, int v, int k, int inputan){
	if(k == 0 && u == v)	return 1;
	if(k == 1 && graph[u][v])	return 1;
	if(k <= 0)	return 0;
	int count = 0;
	int i;
	for(i=0; i<inputan; i++){
		if(graph[u][i] == 1){
			count += countwalks(graph, i, v, k-1);
		}
	}
	return count;
}

int main(){
	int inputan, a, b;
	scanf("%d", &inputan)
	int graph[100][100];
	for(a=0;a<inputan;a++){
		for(b=0;b<inputan;b++){
			scanf("%d", &graph[a][b]);
		}
	}
	int u, v, k;
	scanf("%d %d %d", &u, &v, &k);
	printf("%d\n", countwalks(graph, u, v, k, inputan));
	return 0;
}