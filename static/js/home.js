const cardsContainer = document.getElementById("cardsContainer");

// function get the data form route AllCars
function getAllCars() {
    fetch("/AllCars")
    .then((res) => {
        return res.json();
    }).then((data) => {
        for (let index = 0; index < data.length; index++) {
            let element = data[index];
            console.log(element)
            // create the card container
            const cardContent = document.createElement("div");
            cardContent.className = "col mt-3 mb-3";
            cardsContainer.appendChild(cardContent);
          // create each card
            const card = document.createElement("div");
            card.className = "card h-100";
            cardContent.appendChild(card);
         //  create content of the card
            cardContent.innerHTML = `<div class="col mt-3 mb-3">
            <div class="card h-100">
            <div class="card-body">
            <div class="imgContainerCard">
            <img class="card-img-top cardImg" src="../static/images/${element.image}">
            </div>
            <div class="row">
            <div class="col-9">
            <a class="titleCardDelete" href="/carDetails/${element.id}">
            <h5 class="card-title py-3">${element.brand}</h5></a>
            </div>
            <div class="col-3 py-3 text-center">
            <a href="/edit/${element.id}">
            <img src="../static/images/edit.png" width="15"></a>
            </div>
            </div>
            <div class="btnCardContainer pb-3">
            <a class="btn btn-primary detailsBtn" href="/carDetails/${element.id}">Details</a>
           
            <!-- Button trigger modal -->
            <a type="button" class="btn btn-secondary deleteBtn" data-bs-toggle="modal" data-bs-target="#exampleModal_${element.id}">
              Delete
            </a>

            </div>
            </div>
            </div>
            </div>
            
            
          
            
            <!-- Modal -->
            <div class="modal fade " id="exampleModal_${element.id}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Confirm</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                   Do you want to delete ${element.brand}?
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <form  action="/delete/${element.id}" method="post" >
                    <button class="btn btn-danger" type="submit">Delete</button>
                    </form>
                  </div>
                </div>
              </div>
            </div>

            `

            cardsContainer.appendChild(cardContent);
             }
            })
    }


   


// call the function that get all cars from route in python
getAllCars();













