let numbers = prompt('enter');
for(let number = 1 ;number <= numbers; number++){
  let stars = '';
    for(let i = 0; i < number; i++){
        stars +='*';
    }

    console.log(stars);
} 