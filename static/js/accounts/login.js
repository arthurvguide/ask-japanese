// Script to customize the standard allauth login page
const loginBtn = document.getElementsByClassName("primaryAction")[0];
const labelUsername = document.getElementsByTagName("label")[0];
const labelPass = document.getElementsByTagName("label")[1];
const usernameField = document.getElementsByTagName("input")[1];
const passwordField = document.getElementsByTagName("input")[2];

window.onload = () => {
    labelUsername.innerHTML = "";
    labelPass.innerHTML = "";
    loginBtn.classList.add("btn");
    usernameField.style.width = "250px";
    passwordField.style.width = "250px";
};


