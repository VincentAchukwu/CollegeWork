import React, { useEffect } from "react";
import Icon from "react-native-vector-icons/Ionicons"
import { createDrawerNavigator } from "@react-navigation/drawer";
import { createStackNavigator } from '@react-navigation/stack';

import Splash from "../screens/Splash";
import Information from "../screens/Information";
import AboutUs from "../screens/AboutUs";
import Support from "../screens/Support";
import MainTabs from "../components/MainTabs";
import { DrawerContent } from "../components/DrawerContent";


const AppStack = () => {
    const AddToFavouritesStack = createStackNavigator();
    const AboutUsStack = createStackNavigator();
    const SupportStack = createStackNavigator();
    const SplashStack = createStackNavigator();

    const SplashStackScreen = ({ navigation }) => (
        <SplashStack.Navigator
            screenOptions={{
                headerShown: false
            }}
        >

        <SplashStack.Screen name="Splash" component= { Splash }/>

        </SplashStack.Navigator>
    );

    const AddToFavouritesStackScreen = ({ navigation }) => (
        <AddToFavouritesStack.Navigator
            screenOptions={{
                headerTitleAlign: "center",
                headerStyle: { backgroundColor: "#1E90FF", },
                headerTintColor: "#ffffff",
                fontWeight: "bold"
            }}
        >

        <AddToFavouritesStack.Screen name="Information" component= { Information } options={{
            headerLeft: () => (
                <Icon.Button name="ios-menu" size={ 25 }
                    backgroundColor= "#1E90FF" onPress={() => 
                    navigation.openDrawer()
                }></Icon.Button>
                )
        }}/>

        </AddToFavouritesStack.Navigator>
    );

    const AboutUsStackScreen = ({ navigation }) => (
        <AboutUsStack.Navigator
            screenOptions={{
                headerTitleAlign: "center",
                headerStyle: { backgroundColor: "#1E90FF", },
                headerTintColor: "#ffffff",
                fontWeight: "bold"
            }}
        >

        <AboutUsStack.Screen name="AboutUs" component= { AboutUs } options={{
            headerLeft: () => (
                <Icon.Button name="ios-menu" size={ 25 }
                    backgroundColor= "#1E90FF" onPress={() => 
                    navigation.openDrawer()
                }></Icon.Button>
                )
        }}/>

        </AboutUsStack.Navigator>
    );

    const SupportStackScreen = ({ navigation }) => (
        <SupportStack.Navigator
            screenOptions={{
                headerTitleAlign: "center",
                headerStyle: { backgroundColor: "#1E90FF", },
                headerTintColor: "#ffffff",
                fontWeight: "bold"
            }}
        >
    
        <SupportStack.Screen name="Support" component= { Support } options={{
            headerLeft: () => (
                <Icon.Button name="ios-menu" size={ 25 }
                    backgroundColor= "#1E90FF" onPress={() => 
                    navigation.openDrawer()
                }></Icon.Button>
                )
        }}/>

        </SupportStack.Navigator>
    );

    const Drawer = createDrawerNavigator();

    return (
        <Drawer.Navigator 
            drawerContent={ props => <DrawerContent { ... props }/>}
        >
                <Drawer.Screen name="Splash" component={ SplashStackScreen }/>
                <Drawer.Screen name="HomeDrawer" component={ MainTabs }/>
                <Drawer.Screen name="Information" component={ AddToFavouritesStackScreen }/>
                <Drawer.Screen name="AboutUs" component={ AboutUsStackScreen }/>
                <Drawer.Screen name="Support" component={ SupportStackScreen }/>
        </Drawer.Navigator>
    )
}

export default AppStack;