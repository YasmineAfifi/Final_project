const welcomeUser = document.getElementById("welcomeUser");
const logOutBtn = document.getElementById("logOutBtn");
welcomeUser.innerText = "welcome " + localStorage.getItem("userName");

// function Func() {
//     fetch("./static/json/cars.json")
//         .then((res) => {
//             return res.json();
//         }).then((data) => {
//             for (let index = 0; index < data.cars.length; index++) {
//                 let element = data.cars[index];
//                 // create the card container
//                 const allCardsContainer = document.getElementById("allCardsContainer");
//                 const cardsContainer = document.getElementById("cardsContainer");
//                 const cardContent = document.createElement("div");
//                 cardContent.className = "col mt-3 mb-3";
//                 cardsContainer.appendChild(cardContent);
//                 // create each card
//                 const card = document.createElement("div");
//                 card.className = "card h-100";
//                 cardContent.appendChild(card);
//                 // create image
//                 const imgContainerDiv = document.createElement("div");
//                 const image = document.createElement("img");
//                 imgContainerDiv.className = "imgContainerCard"
//                 image.className="card-img-top cardImg";
//                 image.src = `../static/images/${element.image}`;
//                 imgContainerDiv.appendChild(image);

//                 // create card body 
//                 const cardbody = document.createElement("div");
//                 cardbody.className="card-body";
//                 card.appendChild(cardbody);
//                 cardbody.appendChild(imgContainerDiv);
//                 // create text for car brand
//                 const titleAnchorDetails = document.createElement("a");
//                 titleAnchorDetails.className="titleCardDetails"
//                 titleAnchorDetails.href =`/carDetails/${element.id}`;
//                 const carBrand = document.createElement("h5");
//                 titleAnchorDetails.appendChild(carBrand);
//                 carBrand.className="card-title py-3";
//                 carBrand.innerText=element.brand;
//                 const btnCardContainer = document.createElement("div");
//                 // create the card buttons
//                btnCardContainer.className="btnCardContainer pb-3";
//                 const reserveBtn = document.createElement("button");
               
//                 const DetailsBtn = document.createElement("button");
//                 DetailsBtn.onclick = function redirctToUrl() {
//                     window.location.href = `/carDetails/${element.id}`;
//                 };
//                 cardbody.appendChild(titleAnchorDetails);
//                 cardbody.appendChild(reserveBtn);
//                 cardbody.appendChild(DetailsBtn);
//                 reserveBtn.className="btn btn-primary reserveBtn";
//                 reserveBtn.innerHTML = "Reserve"
//                 DetailsBtn.className="btn btn-secondary detailsBtn";
//                 DetailsBtn.innerHTML = "Details"
              
//                 btnCardContainer.appendChild(reserveBtn);
//                 btnCardContainer.appendChild(DetailsBtn);

//                 cardbody.appendChild(btnCardContainer);
//                 allCardsContainer.appendChild(cardsContainer);





//                 // console.log(element);
//             }
//         })
// }





function getAllCars() {
        fetch("/AllCars")
            .then((res) => {
                return res.json();
            }).then((data) => {
                for (let index = 0; index < data.length; index++) {
                    let element = data[index];
                    // create the card container
                    const allCardsContainer = document.getElementById("allCardsContainer");
                    const cardsContainer = document.getElementById("cardsContainer");
                    const cardContent = document.createElement("div");
                    cardContent.className = "col mt-3 mb-3";
                    cardsContainer.appendChild(cardContent);
                    // create each card
                    const card = document.createElement("div");
                    card.className = "card h-100";
                    cardContent.appendChild(card);
                    // create image
                    const imgContainerDiv = document.createElement("div");
                    const image = document.createElement("img");
                    imgContainerDiv.className = "imgContainerCard"
                    image.className="card-img-top cardImg";
                    image.src = `../static/images/${element.image}`;
                    imgContainerDiv.appendChild(image);
    
                    // create card body 
                    const cardbody = document.createElement("div");
                    cardbody.className="card-body";
                    card.appendChild(cardbody);
                    cardbody.appendChild(imgContainerDiv);
                    // create text for car brand
                    const titleAnchorDetails = document.createElement("a");
                    titleAnchorDetails.className="titleCardDetails"
                    titleAnchorDetails.href =`/carDetails/${element.id}`;
                    const carBrand = document.createElement("h5");
                    titleAnchorDetails.appendChild(carBrand);
                    carBrand.className="card-title py-3";
                    carBrand.innerText=element.brand;
                    const btnCardContainer = document.createElement("div");
                    // create the card buttons
                   btnCardContainer.className="btnCardContainer pb-3";
                    const reserveBtn = document.createElement("button");
                   
                    const DetailsBtn = document.createElement("button");
                    DetailsBtn.onclick = function redirctToUrl() {
                        window.location.href = `/carDetails/${element.id}`;
                    };
                    cardbody.appendChild(titleAnchorDetails);
                    cardbody.appendChild(reserveBtn);
                    cardbody.appendChild(DetailsBtn);
                    reserveBtn.className="btn btn-primary reserveBtn";
                    reserveBtn.innerHTML = "Reserve"
                    DetailsBtn.className="btn btn-secondary detailsBtn";
                    DetailsBtn.innerHTML = "Details"
                  
                    btnCardContainer.appendChild(reserveBtn);
                    btnCardContainer.appendChild(DetailsBtn);
    
                    cardbody.appendChild(btnCardContainer);
                    allCardsContainer.appendChild(cardsContainer);
    
    
    
    
    
                    // console.log(element);
                }
            })
    }






// logout function to clear data from local storage
function logOut(){
    localStorage.clear();
    window.location.href = "http://127.0.0.1:5000/login"
}
// call the function that get all cars from route in python 
getAllCars()

logOutBtn.addEventListener("click",logOut)








