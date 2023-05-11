<template>
    <h1 id="Current" class="header"> Current Portfolio </h1>

        <table id="table" class="auto-index">
            <tr> 
                <th> S.No </th> 
                <th> Coin </th>
                <th> Ticker </th>
                <th> Buy_Price </th>
                <th> Buy_Quantity </th>
                <th> Current_Price </th>
                <th> Profit </th>
                <th> Options </th>
            </tr>
        </table> <br>

        <h2 id="totalProfit" class="header"> Your Total Profit is: XX$ </h2>
</template>

<script>

import ccxt from "ccxt"
import firebaseApp from '../firebase.js';
import { getFirestore } from "firebase/firestore";
import { collection, getDocs, doc, deleteDoc } from "firebase/firestore";
import { getAuth } from 'firebase/auth';

const db = getFirestore(firebaseApp);

export default {
    mounted() {
    const auth = getAuth();
    async function display(user) {
        let z = await getDocs(collection(db, user));
        let ind = 1;
        var tp = 0;

        z.forEach((docs) => {
            let yy = docs.data();
            var table = document.getElementById("table");
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
            console.log("TP is", tp)
            document.getElementById("totalProfit").innerHTML = ("Total Profit is: $" + String(tp));
        }
        ind += 1;
        })
    }
    display(auth.currentUser.email)

    //delete instruments
    async function deleteinstrument2(coin) {
        var x = coin;
        alert("You're going to delete " + x);

        await deleteDoc(doc(db, auth.currentUser.email, x))
        console.log("Document successfully deleted!", x);

        let tb = document.getElementById("table")
        while (tb.rows.length > 1) {
            tb.deleteRow(1)
        }
        document.getElementById("totalProfit").innerHTML=""
        display(auth.currentUser.email)
    }
    }
}

</script>

<style>

.header {
    text-align: center;
    background-color: #ABEAF7;
    margin: 10px 10px 10px 10px;
    border: 3px solid darkblue;
    border-radius: 25px;
    padding: 10px 0px 10px 0px;
    display: block;
}

table {
    border-collapse: collapse;
    font-family: arial, sans-serif;
    width: 99%;
    background-color: beige;
    margin: 10px 10px 10px 10px;
    border-radius: 25px;
}

th, td {
    border: 3px solid darkgoldenrod;
    text-align: center;
    padding: 5px 5px 5px 5px;
}

.bwt {
    color: white;
    background-color: black;
}
</style>
