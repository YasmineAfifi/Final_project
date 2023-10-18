let userIdInput = document.getElementById("userId");
let userNameInput =document.getElementById("userName");
let userId =   localStorage.getItem("userId");
let userName = localStorage.getItem("userName");

// set hidden value with local storage value
userNameInput.value = userName;
userIdInput.value = userId



