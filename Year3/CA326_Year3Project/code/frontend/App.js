import React from "react";
import Providers from "./navigation/"


const App = () => {
  
  // Setting up Navigation To Navigate Around the Pages
  // If User is Not Authenticated, He Will be Put in RootStackScreen,
  // Where The SignIn/SignUp Screens Are Located
  return (
    <Providers/>
  )
}

export default App;
