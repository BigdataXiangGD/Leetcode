

int toNumber(char c){
    switch(c){
    case 'I':  
        return 1;  
    case 'V':  
        return 5;  
    case 'X':  
        return 10;  
    case 'L':  
        return 50;  
    case 'C':  
        return 100;  
    case 'D':  
        return 500;  
    case 'M':  
        return 1000;  
    default:
        return;
    }
}


int romanToInt(char* s) {
    int res = 0;
    int N = strlen(s);
    for(int i=0; i<N; i++){
        if(i!=N-1){
        if (toNumber(s[i]) < toNumber(s[i+1])){
            res = res - toNumber(s[i]);
        } else {
            res = res + toNumber(s[i]);
        }
    }else{res = res + toNumber(s[N-1]);}
    }
    return res;
}
