
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#include <cuComplex.h>

__global__ void do_stuff(int *a, int N)
{
    short i = threadIdx.x;
    if (i < N)
    {
        a[i] = a[i] * 1000;
    }
}
int main()
{
    int N = 100;
    int* h_a = (int*) malloc(N * sizeof(int));
    for (int i = 0; i < N; i++)
    {
        h_a[i] = i * i;
    }

    int* d_a;

    printf("Malloc memory to device\n");
    cudaMalloc((void**)&d_a, N * sizeof(int));


    printf("Copy memory to device\n");
    cudaMemcpy(d_a, h_a, N * sizeof(int), cudaMemcpyHostToDevice);

    dim3 grid_size(1); 
    dim3 block_size(N);

    printf("Run kernal\n");
    do_stuff<<<grid_size, block_size>>>(d_a, N);

    printf("Copy memory back\n");
    cudaMemcpy(h_a, d_a, N * sizeof(int), cudaMemcpyDeviceToHost);


    printf("Print results in the form of h_a\n");
    for (int i = 0; i < N; i++)
    {
        printf("%d: ", h_a[i]);
    }

    cudaFree(d_a);
    free(h_a);
}