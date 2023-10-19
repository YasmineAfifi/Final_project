

function Func() {
    fetch("./static/json/cars.json")
        .then((res) => {
            return res.json();
        }).then((data) => {
            for (let index = 0; index < data.cars.length; index++) {
                let element = data.cars[index];
                console.log(element);
            }
        })
}

Func()


// create the card container
const cardsContainer = document.getElementById("cardsContainer");
const card = document.createElement("div");
card.className = "cards";
const image = document.createElement("div");
image.className = "image";
const cardImage = document.createElement("img");
cardImage.src = `../static/images/reservation.jpg`;
image.appendChild(cardImage);
card.appendChild(image);
const cardContent = document.createElement("div");
cardContent.className = "cardContent";
card.appendChild(cardContent);
const cardAnchor = document.createElement("a");
cardAnchor.innerText  ="hi";
cardAnchor.href = "/hello.html";
const cardTitle = document.createElement("p");
cardTitle.innerHTML="welcome"
cardAnchor.appendChild(cardTitle);
cardContent.appendChild(cardAnchor);
const cardDetailsBtn = document.createElement("Button")
cardDetailsBtn.innerText ="Details"
const cardReserveBtn = document.createElement("Button")
cardReserveBtn.innerText ="Reserve";
cardContent.appendChild(cardDetailsBtn);
cardContent.appendChild(cardReserveBtn);
cardsContainer.appendChild(card);

