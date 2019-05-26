
#recursive
int fib(int N){
    if(N == 0){
        return 0;
    }
    else if(N == 1){
        return 1;
    }
    else{
        return fib(N - 1) + fib(N - 2);
    }

}




#iterative
int fib(int N){
    if(N == 0){
        return 0;
    }
    else if(N == 1){
        return 1;
    }
    int pre1 = 1;
    int pre2 = 0;
    int res = 0;
    for(int i = 2; i <= N; i++){
        res = pre1 + pre2;
        pre2 = pre1;
        pre1 = res;
    }return res;
}
