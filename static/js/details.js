// set the values of the user that stored in a local storage in the Reserve Car hidden inputs form

const userIdInput = document.getElementById("userId");
const userNameInput =document.getElementById("userName");
if(localStorage.getItem("userId")!=null && localStorage.getItem("userName")!=null ){
    const userId =   localStorage.getItem("userId");
    const userName = localStorage.getItem("userName");
    // set hidden value with local storage value
    if( userNameInput!=null && userIdInput!=null){
        userNameInput.value = userName;
        userIdInput.value = userId;
    }
}


// validation for reservation form when submit it 
const reserveForm = document.getElementById("reserveForm");
reserveForm.addEventListener("submit",function(e)
{
e.preventDefault();
const dateFrom = document.getElementById("dateFrom").value;
const dateTo = document.getElementById("dateTo").value;
const dateFromError = document.getElementById("dateFromError");
const dateToError = document.getElementById("dateToError");

    if(dateFrom == ""){
        dateFromError.innerText = "Date Is Required";
    }else{
        dateFromError.innerText = "";
    }
    
    if(dateTo == ""){
        dateToError.innerText = "Date Is Required";
    }else{
        dateToError.innerText = "";
    }
    
    if(dateFromError.innerText == "" && dateToError.innerText == "")
    {
        reserveForm.submit();
    }


})







