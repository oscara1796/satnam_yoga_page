console.log("Sanity check!");

var id_value= false
var submitBtn= null


function give_value_session_id(element) {
  id_value= element.value
}



// Get Stripe publishable key
fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
  var btns = document.querySelectorAll(".submitBtn")
  // new
  // Event handler

  console.log(btns)
  // let submitBtn = document.querySelector(".submitBtn");
  // let submitBtn_2 = document.querySelector(".submitBtn")[1];
  if (btns[0] !== null && btns[1] !== null) {

    var userSelection = document.getElementsByClassName('submitBtn mb-4 btn btn-primary');
    console.log(userSelection)
    for(let i = 0; i < userSelection.length; i++) {
      userSelection[i].addEventListener("click", function() {
        console.log(userSelection[i].value);
        fetch("/create-checkout-session/")
          .then((result) => { return result.json(); })
          .then((data) => {
            // console.log(data.session.line_items.data[0].price);
            console.log(userSelection[i].value);
            let final_id= data.session_subs_Id
            if (data.session_subs_Id.line_items.data[0].price.id == userSelection[i].value) {
              final_id= data.session_subs_Id.id
            } else {
              final_id= data.session_year_Id.id
            }
            return stripe.redirectToCheckout({sessionId: final_id})
            // Redirect to Stripe Checkout
          })
          .then((res) => {
            console.log(res);
          });
      })
    }

    // waitForIt(btns);

  }
});
