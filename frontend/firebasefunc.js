
// Import the functions you need from the SDKs you need
//import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.6/firebase-app.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration

const firebaseConfig = {
    apiKey: "AIzaSyDz2anWWf1kz3NZi8M4yvhP3jdvvmbstj0",
    authDomain: "bt3103-3103.firebaseapp.com",
    projectId: "bt3103-3103",
    storageBucket: "bt3103-3103.appspot.com",
    messagingSenderId: "351087976817",
    appId: "1:3510879 76817:web:24a1c948ef536f779d56d0"
  };

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

var db = firebase.firestore();

//save to firestore
async function savetofs() {
  var a = document.getElementById("coinName").value;
  var b = document.getElementById("ticker").value;
  var c = document.getElementById("pricse").value;
  var d = document.getElementById("quantity").value;

  alert("Saving your data for Coin: " + a);
  try {
      const docRef = await setDoc(doc(db, "Portfolio", a), {
          Coin: a, 
          Ticker: b,
          Buy_Price: c,
          Buy_Quantity: d
      })
      console.log(docRef)
      document.getElementById('userForm').reset();
      this.$emit("added")
  }
  catch(error) {
      console.error("Error adding document: ", error);
  }
  }
/*
function savetofs() {
  var a = document.getElementById("coinName").value;
  var b = document.getElementById("ticker").value;
  var c = document.getElementById("price").value;
  var d = document.getElementById("quantity").value;

  alert("Saving your data for Coin: " + a);

  db.collection("Portfolio").doc(a).set({
    Coin: a,
    Ticker: b,
    Buy_Price: c,
    Buy_Quantity: d
  })
  .then((docRef) => {
    console.log(docRef);
    window.location.reload();
    //console.log("Document written with ID: ", docRef.id);
  })
  .catch((error) => {
    console.error("Error adding document: ", error);
  });
}*/

//display profit
async function display() {
  let z = await db.collection("Portfolio").get();

  let ind = 1;
  var tp = 0;

  z.forEach((docs) => {
    let yy = docs.data();
    var table = document.getElementById("portfolioTable");
    var row = table.insertRow(ind);

    var coin = (yy.Coin);
    var price = (yy.Buy_Price);
    var quantity = (yy.Buy_Quantity);
    var ticker = (yy.Ticker);

    var cell1 = row.insertCell(0); 
    var cell2 = row.insertCell(1); 
    var cell3 = row.insertCell(2); 
    var cell4 = row.insertCell(3); 
    var cell5 = row.insertCell(4); 
    var cell6 = row.insertCell(5);
    var cell7 = row.insertCell(6); 
    var cell8 = row.insertCell(7);

    cell1.innerHTML = ind;
    cell2.innerHTML = coin;
    cell3.innerHTML = ticker;
    cell4.innerHTML = price;
    cell5.innerHTML = quantity;
    cell6.innerHTML = 0;
    cell7.innerHTML = 0;

    cell7.className = "profits";

    var bu = document.createElement("button");
    bu.className = "bwt";
    bu.id = String(coin);
    bu.innerHTML = "Delete"
    bu.onclick = function() {
      deleteinstrument2(coin);
    }
    cell8.appendChild(bu);

    val(ticker);

    async function val(ticker) {
      let binance = new ccxt.binance();
      let x = await binance.fetch_ohlcv(ticker, "5m");
      cell6.innerHTML = x[499][4];
      cell7.innerHTML = Math.round(quantity * (-parseFloat(price) + parseFloat(cell6.innerHTML)));
      tp = tp + parseFloat(cell7.innerHTML);
      document.getElementById("totalProfit").innerHTML = ("Total Profit is: $" + String(tp));
    }
    ind += 1;
  })
}

display()

//delete instruments
function deleteinstrument2(coin) {
  var x = coin;
  
  alert("You're going to delete " + x);
  console.log(x);

  db.collection("Portfolio").doc(x).delete().then(() => {
    console.log("Document successfully deleted!", x);
    window.location.reload();
  })
  .catch((error) => {
    console.log("Error removing document: ", error);
  });
}