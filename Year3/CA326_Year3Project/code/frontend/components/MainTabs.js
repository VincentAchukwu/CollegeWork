// This File is Mainly For The Bottom Tab Navigation But Also Sets Up The HeadBar
// Where The Drawer Menu Is Situated

import React from "react";
import { createStackNavigator } from '@react-navigation/stack';
import Icon from "react-native-vector-icons/Ionicons"
import { createMaterialBottomTabNavigator } from '@react-navigation/material-bottom-tabs';


import Home from "../screens/Home";
import Graph from "../screens/Graph";
import Rates from "../screens/Rates";
import Currencies from "../screens/Currencies";

// Initialising The Stack Navigotor Screens
const HomeStack = createStackNavigator();
const GraphStack = createStackNavigator();
const RatesStack = createStackNavigator();
const CurrenciesStack = createStackNavigator();

// 
const HomeStackScreen = ({ navigation }) => (
    <HomeStack.Navigator
        screenOptions={{
            headerTitleAlign: "center",
            headerStyle: { backgroundColor: "#1E90FF", },
            headerTintColor: "#ffffff",
            fontWeight: "bold"
        }}
    >
  
        <HomeStack.Screen name="Home" component={ Home } options={{
            headerLeft: () => (
                <Icon.Button name="ios-menu" size={ 25 }
                    backgroundColor= "#1E90FF" onPress={() => 
                    navigation.openDrawer()
                }></Icon.Button>
                )
        }}/>

    </HomeStack.Navigator>
);
  
const GraphStackScreen = ({ navigation }) => (
    <GraphStack.Navigator
        screenOptions={{
            headerTitleAlign: "center",
            headerStyle: { backgroundColor: "#1E90FF",},
            headerTintColor: "#ffffff",
            fontWeight: "bold"
        }}
    >

        <GraphStack.Screen name="Graph" component={ Graph } options={{
            headerLeft: () => (
                <Icon.Button name="ios-menu" size={ 25 }
                backgroundColor= "#1E90FF" onPress={() => 
                    navigation.openDrawer()
                }></Icon.Button>
            )
        }}/>

    </GraphStack.Navigator>
);

const RatesStackScreen = ({ navigation }) => (
    <RatesStack.Navigator
        screenOptions={{
            headerTitleAlign: "center",
            headerStyle: { backgroundColor: "#1E90FF", },
            headerTintColor: "#ffffff",
            fontWeight: "bold"
        }}
    >

        <RatesStack.Screen name="Rates" component={ Rates } options={{
            headerLeft: () => (
                <Icon.Button name="ios-menu" size={ 25 }
                backgroundColor= "#1E90FF" onPress={() => 
                    navigation.openDrawer()
                }></Icon.Button>
            )
        }}/>

    </RatesStack.Navigator>
);

const CurrenciesStackScreen = ({ navigation }) => (
    <CurrenciesStack.Navigator
        screenOptions={{
            headerTitleAlign: "center",
            headerStyle: { backgroundColor: "#1E90FF", },
            headerTintColor: "#ffffff",
            fontWeight: "bold"
        }}
    >
  
        <CurrenciesStack.Screen name="Currencies" component={ Currencies } options={{
            headerLeft: () => (
                <Icon.Button name="ios-menu" size={ 25 }
                    backgroundColor= "#1E90FF" onPress={() => 
                    navigation.openDrawer()
                }></Icon.Button>
                )
        }}/>

    </CurrenciesStack.Navigator>
);

const Tab = createMaterialBottomTabNavigator();

const MainTabs = () => {
    return(
        <Tab.Navigator
            initialRouteName="Home"
            activeColor="#ffffff"
            shifting= { true }
        >
            <Tab.Screen
                name="Home"
                component={ HomeStackScreen }
                options={{
                    tabBarLabel: 'Home',
                    tabBarColor: "#1E90FF",
                    tabBarIcon: ({ color }) => (
                        <Icon name="ios-home" color={color} size={26} />
                    ),
                }}
            />
            <Tab.Screen
                name="Graph"
                component={ GraphStackScreen }
                options={{
                    tabBarLabel: 'Graph',
                    tabBarColor: "#1E90FF",
                    tabBarIcon: ({ color }) => (
                        <Icon name="analytics-outline" color={color} size={26} />
                    ),
                }}
            />
            <Tab.Screen
                name="Rates"
                component={ RatesStackScreen }
                options={{
                    tabBarLabel: 'Rates',
                    tabBarColor: "#1E90FF",
                    tabBarIcon: ({ color }) => (
                        <Icon name="stats-chart-outline" color={color} size={26} />
                    ),
                }}
            />
            <Tab.Screen
                name="Currencies"
                component={ CurrenciesStackScreen }
                options={{
                    tabBarLabel: 'Currencies',
                    tabBarColor: "#1E90FF",
                    tabBarIcon: ({ color }) => (
                        <Icon name="search" color={color} size={26} />
                    ),
                }}
            />
        </Tab.Navigator>
    )
};

export default MainTabs;