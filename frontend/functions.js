async function savetofs() {
  var a = document.getElementById("clientName").value;
  var b = document.getElementById("commDiff").value;
  var c = document.getElementById("grossDiff").value;
  var d = "11/05/2023"
  var e = "Pending approval"

  alert("Saving your data for Config: " + a);

  let ind = 1;
  var table = document.getElementById("portfolioTable");
  var row = table.insertRow(ind);

  var cell1 = row.insertCell(0); 
  var cell2 = row.insertCell(1); 
  var cell3 = row.insertCell(2); 
  var cell4 = row.insertCell(3); 
  var cell5 = row.insertCell(4); 
  var cell6 = row.insertCell(5);

  cell1.innerHTML = ind;
  cell2.innerHTML = a;
  cell3.innerHTML = b;
  cell4.innerHTML = c;
  cell5.innerHTML = d;
  cell6.innerHTML = e;

  var bu = document.createElement("button");
  bu.className = "bwt";
  bu.id = String(coin);
  bu.innerHTML = "Delete"
  bu.onclick = function() {
    deleteinstrument2(coin);
  }
  cell8.appendChild(bu);
  }

//display profit
async function display() {
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


}

display()

//delete instruments
function deleteinstrument2(coin) {
  var x = coin;
  
  alert("You're going to delete " + x);
  console.log(x);
}