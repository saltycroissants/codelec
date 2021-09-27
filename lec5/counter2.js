let count =0;
function counter(){
    count ++;
    document.querySelector('h1').innerHTML =count;

    if(count % 10 === 0){
        alert(`Count is now ${count}`)
    }
}

/* avoid mixing html with javascript*/
//functional programming - in javascript, we can pass a function as a variable
//when dom is loaded, 
document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').onclick = counter;
});