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

function appendNumber(number) {
    //append the number into calculation
    resultField.value += number;
    if (number!='%'){
        currentInput+=number;
    }
    else{
        currentInput+=' * 0.01';
    }
}

function appendOperator(operator) {
    //append the operator
    currentInput += operator;
    resultField.value = currentInput;

}

function calculateResult() {

    //calculate the result
    resultField.value =eval (currentInput);
    searchValue.value = resultField.value;
    currentOperator = null;
    resetField()
}


function clearAll() {
    //clear all
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
    //remove last entered data
  if(currentInput.length>0) {
  if(currentInput[-1]==' '){

    resultField.value=resultField.value.slice(0,currentInput.length-3);}
      
      else{
        resultField.value=resultField.value.slice(0,currentInput.length-1);
      }
  }}

function calcvisible(){
    //display calculator
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
    //display history block
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
    //insert favourite into the search and to select tag
    document.getElementById('option1').value = t;
    document.getElementById('option2').value = k;
    document.getElementById('option1').innerHTML = t;
    document.getElementById('option2').innerHTML = k;

}
