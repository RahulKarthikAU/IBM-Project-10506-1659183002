const loginBtn = document.querySelector('.btn-login');
const signUpBtn = document.querySelector('.btn-signup');
const authBtn = document.querySelectorAll('.auth-header h3');
const formCnt = document.querySelectorAll('.auth-form-cnt');

loginBtn.addEventListener("click" ,(e) => {
    authBtn[0].classList.add("active");
    authBtn[1].classList.remove("active");
    formCnt[0].classList.remove("none");
    formCnt[1].classList.add("none");
});
signUpBtn.addEventListener("click", (e) => {
    authBtn[1].classList.add("active");
    authBtn[0].classList.remove("active");
    formCnt[1].classList.remove("none");
    formCnt[0].classList.add("none");
})