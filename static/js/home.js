const welcomeUser = document.getElementById("welcomeUser");
welcomeUser.innerText = "welcome " + localStorage.getItem("userName");

function Func() {
    fetch("./static/json/cars.json")
        .then((res) => {
            return res.json();
        }).then((data) => {
            for (let index = 0; index < data.cars.length; index++) {
                let element = data.cars[index];
                // create the card container

                const cardsContainer = document.getElementById("cardsContainer");
                const card = document.createElement("div");
                card.className = "cards";
                // create image div
                const image = document.createElement("div");
                image.className = "imageCard";
                const cardImage = document.createElement("img");
                cardImage.src = `../static/images/${element.image}`;
                image.appendChild(cardImage);
                card.appendChild(image);
                // create card content
                const cardContent = document.createElement("div");
                cardContent.className = "cardContent";
                card.appendChild(cardContent);
                // create the anchor title for the brand
                const cardAnchor = document.createElement("a");
                cardAnchor.innerText = element.brand;
                cardAnchor.href = `/carDetails/${element.id}`;
                const cardTitle = document.createElement("p");
                cardTitle.className = "cardTitle";
                cardTitle.appendChild(cardAnchor)
                cardContent.appendChild(cardTitle);
                // create the button for the card
                const cardDetailsBtn = document.createElement("Button")
                cardDetailsBtn.innerText = "Details"
                cardDetailsBtn.className = "detailsBtn";
                const cardReserveBtn = document.createElement("Button")
                cardReserveBtn.innerText = "Reserve";
                cardReserveBtn.className = "reserveBtn";
                cardDetailsBtn.onclick = function redirctToUrl() {
                    window.location.href = `/carDetails/${element.id}`;
                };
                cardContent.appendChild(cardDetailsBtn);
                cardContent.appendChild(cardReserveBtn);
                cardsContainer.appendChild(card);
                // create container for card button

                const btnContainer = document.createElement("div");
                btnContainer.className="cardsBtn";
                btnContainer.appendChild(cardDetailsBtn);
                btnContainer.appendChild(cardReserveBtn);
                card.appendChild(btnContainer);

                // console.log(element);
            }
        })
}

Func()

