let arr = [1,2,3,3,4]
let arr2 = []
for (i=0;i<arr.length;i++){
    if(i in arr2){
        console.log('inside')
        arr2.push(i)
    }
}
console.log(arr2)