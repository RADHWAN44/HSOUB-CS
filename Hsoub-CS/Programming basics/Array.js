let numbers = [1, 2, 3, 4, 5];


function reverse(array){
    for(let i in array)
    array.splice(i, 0, array.pop());
return array;
}
console.log(reverse(numbers));