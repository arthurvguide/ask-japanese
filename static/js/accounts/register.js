// Script to customize the standard allauth register page
const signBtn = document.getElementsByTagName("button")[1];
const labelUsername = document.getElementsByTagName("label")[0];
const labelEmail = document.getElementsByTagName("label")[1];
const labelPass = document.getElementsByTagName("label")[2];
const labelPassAgain = document.getElementsByTagName("label")[3];
const usernameField = document.getElementsByTagName("input")[1];
const emailField = document.getElementsByTagName("input")[2];
const passField = document.getElementsByTagName("input")[3];
const passAgainField = document.getElementsByTagName("input")[4];

window.onload = () => {
    labelUsername.innerHTML = "";
    labelEmail.innerHTML = "";
    labelPassAgain.innerHTML = "";
    labelPass.innerHTML = "";
    usernameField.style.width = "250px";
    emailField.style.width = "250px";
    passField.style.width = "250px";
    passAgainField.style.width = "250px";
    signBtn.classList.add("btn");
};
