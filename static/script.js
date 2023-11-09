// // include api for currency change 
// //https://v6.exchangerate-api.com/v6/376be693fc1bbb5111dfcee0/latest/USD another api
// //http://api.exchangeratesapi.io/v1/latest?access_key=aa54007b6c5e6136b3eba5cf93f4a9a9
// //https://api.exchangerate-api.com/v4/latest/USD in case of problem

// var api = "https://api.exchangerate-api.com/v4/latest/USD"; 


// // for selecting different controls 

// var search = document.querySelector(".searchBox"); 

// var convert = document.querySelector(".convert"); 

// var fromCurrecy = document.querySelector(".from"); 
// console.log(fromCurrecy);
// var toCurrecy = document.querySelector(".to"); 

// var finalValue = document.getElementById("bamount"); 

// var finalAmount = document.getElementById("finalAmount"); 

// var resultFrom; 

// var resultTo; 

// var searchValue; 

  
// // Event when currency is changed 

// fromCurrecy.addEventListener('change',fromcurr);


  
// // Event when currency is changed 

// toCurrecy.addEventListener('change', (event) => { 

//     resultTo = `${event.target.value}`; 
// }); 

  

// search.addEventListener('input', updateValue); 

  
// // function for updating value 

// function updateValue(e) { 

//     searchValue = e.target.value; 
// } 

  
// // when user clicks, it calls function getresults  

// convert.addEventListener("click", getResults); 

  
// // function getresults 

// function getResults() { 

//     fetch(`${api}`).then(currency => { 
            
//             return currency.json(); 

//         }).then(displayResults); 
        
// } 

  
// // display results after convertion 

// function displayResults(currency) { 
//     console.log(currency);
//     let fromRate = currency.rates[resultFrom]; 

//     let toRate = currency.rates[resultTo]; 

//     finalValue.innerHTML =  

//        ((toRate / fromRate) * searchValue).toFixed(2); 

//     finalAmount.style.display = "block"; 
// } 

  
// // when user click on reset button 

// function clearVal() { 

//     window.location.reload(); 

//     document.getElementsByClassName("finalValue").innerHTML = ""; 
// };
// function fromcurr(){
//     resultTo = `${event.target.value}`; 
// }
// include api for currency change 
//https://v6.exchangerate-api.com/v6/376be693fc1bbb5111dfcee0/latest/USD another api
//http://api.exchangeratesapi.io/v1/latest?access_key=aa54007b6c5e6136b3eba5cf93f4a9a9
//https://api.exchangerate-api.com/v4/latest/USD in case of problem

var api = "https://api.exchangerate-api.com/v4/latest/USD"; 


// for selecting different controls 

var search = document.querySelector(".searchBox"); 

var convert = document.querySelector(".convert"); 

var fromCurrecy = document.querySelector(".from"); 

var toCurrecy = document.querySelector(".to"); 

var finalValue = document.getElementById("bamount"); 

var intialValue = document.getElementById('oamount')
var resultFrom; 

var resultTo; 

var searchValue; 

  console.log(fromCurrecy.value);
// Event when currency is changed 

fromCurrecy.addEventListener('change', (event) => { 

    resultFrom = `${event.target.value}`; 
}); 

  
// Event when currency is changed 

toCurrecy.addEventListener('change', (event) => { 

    resultTo = `${event.target.value}`; 
}); 

  

search.addEventListener('input', updateValue); 

  
// function for updating value 

function updateValue(e) { 

    searchValue = e.target.value; 
} 

  
// when user clicks, it calls function getresults  

convert.addEventListener("click", getResults); 

  
// function getresults 

function getResults() { 

    fetch(`${api}`).then(currency => { 
            
            return currency.json(); 

        }).then(displayResults); 
        
} 

  
// display results after convertion 

function displayResults(currency) { 
    console.log(currency);
    let fromRate = currency.rates[resultFrom]; 

    let toRate = currency.rates[resultTo]; 

    finalValue.innerHTML =  

       ((toRate / fromRate) * searchValue).toFixed(3); 


} 

  
// when user click on reset button 

function clearVal() { 

    window.location.reload(); 

    document.getElementsByClassName("finalValue").innerHTML = ""; 
};




var calcOption = document.getElementById('calcOption');
var calculator = document.getElementById('calc');
let resultField = document.getElementById('result');
let currentInput = '';
let currentOperator = null;
let shouldResetField = false;
let firstOperand = null;
let secondOperand = null;



function appendNumber(number) {

    currentInput += number;
    resultField.value = currentInput;
}

function appendOperator(operator) {
    currentInput += operator;
    resultField.value = currentInput;

}

function calculateResult() {
    let operands = resultField.value.split(' ');

    
    resultField.value =eval (resultField.value);
    intialValue.value = resultField.value;
    searchValue = resultField.value;
    getResults();
    
    currentOperator = null;
    resetField()
}


function clearAll() {
    currentInput = '';
    currentOperator = null;
    shouldResetField = false;
    firstOperand = null;
    secondOperand = null;
    resultField.value = '';
}

function resetField() {
    currentInput = '';
}
function backspace() {
  if(currentInput.length>0) {
  if(currentInput[-1]==' '){

    resultField.value=resultField.value.slice(0,currentInput.length-3);}
      
      else{
        resultField.value=resultField.value.slice(0,currentInput.length-1);
      }
  }}

function favStore(){
    
}
fetch(URL, {
    method: 'POST',
    credentials: 'same-origin',
    headers:{
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
        'X-CSRFToken': csrftoken,
},
    body: JSON.stringify({'post_data':'Data to post'}) //JavaScript object of data to POST
})
.then(response => {
        return response.json() //Convert response to JSON
})
.then(data => {
//Perform actions with the response data from the view
})