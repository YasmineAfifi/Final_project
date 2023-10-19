
const userIdInput = document.getElementById("userId");
const userNameInput =document.getElementById("userName");
const userId =   localStorage.getItem("userId");
const userName = localStorage.getItem("userName");
// set hidden value with local storage value
userNameInput.value = userName;
userIdInput.value = userId;



// function Func() { 
//     fetch("./static/json/cars.json") 
//         .then((res) => { 
//         return res.json(); 
//     }).then((data) => {
//             for (let index = 0; index < data.cars.length; index++) {
//                 let element = data.cars[index];
//                 console.log(element);
//             }
//         })

//     // .then(({cars} = data) => {
//     //     console.log(cars)
//     //     for (let index = 0; index < cars.length; index++) {
//     //         let element = cars[index];
//     //         console.log(element);
            
//     //     }
//     // })
// }

// Func()





