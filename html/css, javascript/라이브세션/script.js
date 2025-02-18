//유저가 버튼을 클릭했을 때 특정한 동작이 실행되도록 만들고 싶다.
const btn = document.querySelector('#button')
const number = document.querySelector('#number')
console.log(btn);
console.log(number);
btn.addEventListener('click', function() {
    number.textContent = console.log('버튼 클릭!');
})
