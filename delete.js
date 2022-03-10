function begum(arr, num){
    for(var i = 0; i < arr.length; i++){
        arr[i] = arr[i]*num 
    }
    console.log(arr);
    return arr
}
a = [2, 4, 10, 16]
b = begum(a,5)