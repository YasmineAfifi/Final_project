// validation for add car form when submit it 

const addCarForm = document.getElementById("addCarForm");
addCarForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const brand = document.getElementById("brand").value;
    const color = document.getElementById("color").value;
    const price = document.getElementById("price").value;
    const image = document.getElementById("image").value;
    const brandError = document.getElementById("brandError");
    const colorError = document.getElementById("colorError");
    const priceError =document.getElementById("priceError");
    const imageError =document.getElementById("imageError");

    if(brand.trim() == ""){
        brandError.innerText = "Brand Is Required";

    }else if(brand.length<3){
        brandError.innerText = "Brand must be more than 3 char ";
    }else{
        brandError.innerText ="";
    }


    if(color.trim() == ""){
        colorError.innerText = "Color Is Required";

    }else if(color.length<3){
        colorError.innerText = "color must be more than 3 char ";
    }else if(!(/^[a-zA-Z]+$/).test(color)){
        colorError.innerText ="Color accepts alphabets only";
    }else{
        colorError.innerText ="";
    }


    if(price.trim() == ""){
        priceError.innerText = "Price Is Required";

    }else if(!(/^[0-9]+$/).test(price)){
        priceError.innerText ="Price accepts Numbers only";
    }else{
        priceError.innerText ="";
    }

    if(image.trim() == ""){
        imageError.innerText = "Image Is Required";
    }else{
        imageError.innerText ="";
    }





if( brandError.innerText ==""&& colorError.innerText ==""&&priceError.innerText ==""&&imageError.innerText ==""){
    addCarForm.submit();
}



})

