<template>
      <div class="container">
          <form id="myform">
            <h1 id="header"> Add Coins </h1>

            <div class="formli">
                <label for="coin1"> Coin Name: </label>
                <input type="text" id="coin1" required="" placeholder="Enter Coin"> <br><br>
                <label for="ticker"> Ticker: </label>
                <input type="text" id="ticker" required="" placeholder="Valid Ticker"> <br><br>
                <label for="buy1"> Buy Price: </label>
                <input type="number" id="buy1" required="" placeholder="Enter Buy Price"> <br><br>
                <label for="quant1"> Buy Quantity: </label>
                <input type="number" id="quant1" required="" placeholder="Enter Buy Quantity"> <br><br>
                
                <div class ="save">
                    <button id="saveButton" type="button" v-on:click="savetofs()"> Save </button>
                </div>
            </div>
        </form>
      </div>
</template>

<script>
import firebaseApp from '../firebase.js';
import { getFirestore } from 'firebase/firestore';
import { doc, setDoc } from 'firebase/firestore';
import { getAuth } from '@firebase/auth';

const db = getFirestore(firebaseApp);

export default {
    data() {
        return {
            a:"", b:"", c:"", d:"", email:""
        }
    },
    methods: {
        async savetofs() {
            const auth = getAuth();
            this.email = auth.currentUser.email;
            this.a = document.getElementById("coin1").value;
            this.b = document.getElementById("ticker").value;
            this.c = document.getElementById("buy1").value;
            this.d = document.getElementById("quant1").value;

            alert("Saving your data for Coin: " + this.a);
            try {
                const docRef = await setDoc(doc(db, this.email, this.a), {
                    Coin: this.a, 
                    Ticker: this.b,
                    Buy_Price: this.c,
                    Buy_Quantity: this.d
                })
                console.log(docRef)
                document.getElementById('myform').reset();
                this.$emit("added")
            }
            catch(error) {
                console.error("Error adding document: ", error);
            }
            }
    }
}
</script>

<style scoped>
h1 {
    background-color: #ABEAF7;
    text-align: center;
    margin: 10px 10px 10px 10px;
    border: 3px solid darkblue;
    border-radius: 25px;
    padding: 10px 0px 10px 0px;
}

form {
    text-align: center;   
    align-items: center;
    margin: auto;  
}

.formli {
    text-align: right;
    display: inline-block;
    background: beige;
    margin: 10px 10px 10px 10px;
    border: 3px solid darkgoldenrod;
    border-radius: 25px;
    padding: 15px 550px 15px 550px;
}


input:hover {
    box-shadow: 3px 3px orange;
    border-radius: 5px
}

.save{
    text-align: center;
}

button.bwt {
    color: white;
    background-color: black;
}

.bwt:hover {
    box-shadow: 3px 3px orange;
    border-radius: 1px;
    outline: darkorange;
}
</style>