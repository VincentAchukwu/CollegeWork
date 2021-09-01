import React, {useEffect} from 'react';
import {
    NavigationContainer,
    DefaultTheme as NativeDefaultTheme,
    DarkTheme as NativeDarkTheme } from "@react-navigation/native";
    import {
    Provider as PaperProvider,
    DarkTheme as PaperDarkTheme,
    DefaultTheme as PaperDefaultTheme } from "react-native-paper";

import AppStack from "./AppStack"
import Splash from "../screens/Splash"
const Providers = () => {

    const [isDarkTheme, setIsDarkTheme] = React.useState(false);

    const CustomDefaultTheme = {
        ... NativeDefaultTheme,
        ... PaperDefaultTheme,
        colors: {
        ... NativeDefaultTheme.colors,
        ... PaperDefaultTheme.colors,
        background: "#ffffff",
        text: "#000000",
        placeholder: "#818181",
        }
    }

    const CustomDarkTheme = {
        ... NativeDarkTheme,
        ... PaperDarkTheme,
        colors: {
        ... NativeDarkTheme.colors,
        ... PaperDarkTheme.colors,
        background: "#555555",
        text: "#ffffff",
        placeholder: "#C4C4C3",
        }
    }

    const theme = isDarkTheme ? CustomDarkTheme : CustomDefaultTheme;

    // The Functions that Check For Authentication,
    // Passing an Empty Array So That it Doesnt Run Everytime
    // We Render Our Screen
    const authContext = React.useMemo( () => ({
        toggleTheme: () => {
        setIsDarkTheme( isDarkTheme => !isDarkTheme )
        }
    }), []);

    // Setting up Navigation To Navigate Around the Pages
    // If User is Not Authenticated, He Will be Put in RootStackScreen,
    // Where The SignIn/SignUp Screens Are Located
    return (
        <PaperProvider theme= { theme }>
            <NavigationContainer>
                <AppStack/>
            </NavigationContainer>
        </PaperProvider>
  );
}

export default Providers;