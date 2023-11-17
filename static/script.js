// // include api for currency change 
// //https://v6.exchangerate-api.com/v6/376be693fc1bbb5111dfcee0/latest/USD another api
// //http://api.exchangeratesapi.io/v1/latest?access_key=aa54007b6c5e6136b3eba5cf93f4a9a9
// //https://api.exchangerate-api.com/v4/latest/USD in case of problem


var display_his = 0;
var his = document.getElementById('historyBlock');
var calcOption = document.getElementById('calcOption');
var calculator = document.getElementById('calculator');
let resultField = document.getElementById('result');
let currentInput = '';
let currentOperator = null;
let shouldResetField = false;
let firstOperand = null;
let secondOperand = null;
var fromCurrecy=document.querySelector('.from');
var toCurrecy = document.querySelector('.to');
var display = 0;
var searchValue = document.getElementById('oamount');

//for options tag
// const optionMenu = document.querySelector(".select-menu"),
//        selectBtn = optionMenu.querySelectorAll(".select-btn"),
//        options = optionMenu.querySelectorAll(".option"),
//        sBtn_text = optionMenu.querySelector(".sBtn-text");

// selectBtn.addEventListener("click", () => optionMenu.classList.toggle("active"));       

// options.forEach(option =>{
//     option.addEventListener("click", ()=>{
//         let selectedOption = option.querySelector(".option-text").innerText;
//         sBtn_text.innerText = selectedOption;

//         optionMenu.classList.remove("active");
//     });
// });
function clearVal() { 

    window.location.reload(); 

    document.getElementsByClassName("finalValue").innerHTML = ""; 
};


function appendNumber(number) {
    
    resultField.value += number;
    if (number!='%'){
        currentInput+=number;
    }
    else{
        currentInput+=' * 0.01';
    }
}

function appendOperator(operator) {

    currentInput += operator;
    resultField.value = currentInput;

}

function calculateResult() {

    
    resultField.value =eval (currentInput);
    searchValue.value = resultField.value;
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

function calcvisible(){
    
    if(display==1){
        calculator.style.display='block';
        display = 0;
        his.style.display='none';
        display_his=1;

    }
    else{
        calculator.style.display='none';
        display =1;
    }
}
function historyShow(){
    if(display_his==1){
        his.style.display='block';
        calculator.style.display='none';
        display =1;
        display_his=0;
    }
    else{
        his.style.display='none';
        display_his=1;
    }
}
function favShow(t,k){
    document.getElementById('option1').value = t;
    document.getElementById('option2').value = k;
    document.getElementById('option1').innerHTML = t;
    document.getElementById('option2').innerHTML = k;

}
