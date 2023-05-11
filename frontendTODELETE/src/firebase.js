import { initializeApp } from 'firebase/app';

const firebaseConfig = {
    apiKey: "AIzaSyDz2anWWf1kz3NZi8M4yvhP3jdvvmbstj0",
    authDomain: "bt3103-3103.firebaseapp.com",
    projectId: "bt3103-3103",
    storageBucket: "bt3103-3103.appspot.com",
    messagingSenderId: "351087976817",
    appId: "1:3510879 76817:web:24a1c948ef536f779d56d0"
  };

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig);
export default firebaseApp;