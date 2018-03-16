#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int graph[100][100], count[100][100][100];

int countwalks(int u, int v, int k){
	if(count[u][v][k] != -1)	return count[u][v][k]
	if(k == 0 && u == v)	return 1;
	if(k == 1 && graph[u][v])	return 1;
	if(k <= 0)	return 0;
	int counts = 0;
	int i;
	for(i=0; i<inputan; i++){
		if(graph[u][i] == 1){
			counts += countwalks(i, v, k-1);
			count[i][v][k-1] = count;
		}
	}
	return count[u][v][k];
}

int main(){
	memset(arr, -1, sizeof(arr));
	int inputan, a, b, u, v, k;

	scanf("%d", &inputan);

	for(a=0;a<inputan;a++){
		for(b=0;b<inputan;b++){
			scanf("%d", &graph[a][b]);
		}
	}

	scanf("%d %d %d", &u, &v, &k);

	printf("%d\n", countwalks(u, v, k));
	return 0;
}