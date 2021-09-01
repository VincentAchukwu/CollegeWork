// This File Is Where The Top Left Content, Inside The Drawer Is Made

import React from "react";
import { View, StyleSheet, TouchableOpacity } from "react-native";

// This Import Is For The Actual Drawer That Opens Up From The Top Left
import { DrawerContentScrollView, DrawerItem } from '@react-navigation/drawer';

// The Icons Used Are From /MaterialCommunityIcons
import Icon from "react-native-vector-icons/MaterialCommunityIcons";

// This Is Pretty Much The Tools Used Throughout The Page
import {
    Avatar,
    Title,
    Caption,
    Drawer,
} from "react-native-paper";


export function DrawerContent(props) {

    return(

        <View style= { {flex:1} }>
            <DrawerContentScrollView { ... props }>

                <View style= { {flex:1} }>

                    {/* This Contains the Users Profile Picture and Caption */}
    
                    <View style= { styles.userInfoSection }>
                        <View style= { styles.imageContent }>
                            <Avatar.Image
                                source={require("../assets/images/profile.jpg")}
                                size={60}
                            />
                            <View style= { styles.profileContent }>
                                <Title style={styles.title}> Welcome! </Title>
                                <Caption style= { styles.caption }> Mo Money Mo Problems </Caption>
                            </View>
                        </View>
                    </View>
                    
                    {/*******************************************************/}

                    {/* Setting Up The Icons and Name Tabs That Navigate You Around
                        The Screen From The Top Left Drawer.
                        The Icons Are Taken From a React-Native Library, Just
                        Have to Adjust Them to What you Prefer */}

                    <Drawer.Section title="Navigation" style= { styles.drawerContent }>
                        <DrawerItem 
                            icon= { ({ color }) => (
                                <Icon
                                    name= "home-outline"
                                    color= { color }
                                    size= { 35 }
                                />
                            )}
                            label="Home"
                            onPress={() => {props.navigation.navigate("Home")}}
                        />

                        <DrawerItem 
                            icon= { ({ color }) => (
                                <Icon
                                    name= "information-outline"
                                    color= { color }
                                    size= { 35 }
                                />
                            )}
                            label="Information"
                            onPress={() => {props.navigation.navigate("Information")}}
                        />

                        <DrawerItem 
                            icon= { ({ color }) => (
                                <Icon
                                    name= "account-multiple-plus-outline"
                                    color= { color }
                                    size= { 35 }
                                />
                            )}
                            label="About Us"
                            onPress={() => {props.navigation.navigate("AboutUs")}}
                        />

                        <DrawerItem 
                            icon= { ({ color }) => (
                                <Icon
                                    name= "account-check-outline"
                                    color= { color }
                                    size= { 35 }
                                />
                            )}
                            label="Support"
                            onPress={() => {props.navigation.navigate("Support")}}
                        />
                    </Drawer.Section>

                    {/*************************************************************/}
                </View>
            </DrawerContentScrollView>
        </View>

    );
}

const styles = StyleSheet.create({
    userInfoSection: {
      paddingLeft: 20,
    },
    imageContent: {
        flexDirection: "row",
        marginTop: "3%"
    },
    profileContent: {
        marginLeft: "3%",
        flexDirection: "column"
    },
    title: {
      fontSize: 18,
      marginTop: "2%",
      fontWeight: 'bold',
    },
    caption: {
      fontSize: 16,
      paddingTop: "3%",
      lineHeight: 14,
    },
    row: {
      marginTop: 20,
      flexDirection: 'row',
      alignItems: 'center',
    },
    section: {
      flexDirection: 'row',
      alignItems: 'center',
      marginRight: 15,
    },
    paragraph: {
      fontWeight: 'bold',
      marginRight: 3,
    },
    drawerContent: {
      marginTop: "5%",
    },
    bottomDrawerSection: {
        marginBottom: "5%",
        borderTopColor: '#f4f4f4',
        borderTopWidth: 1
    },
    preference: {
      flexDirection: 'row',
      justifyContent: 'space-between',
      paddingVertical: "5%",
      paddingHorizontal: "5%",
    },
    header: {
        backgroundColor: '#FFFFFF',
        shadowColor: '#333333',
        shadowOffset: {width: -1, height: -3},
        shadowRadius: 2,
        shadowOpacity: 0.4,
        // elevation: 5,
        paddingTop: "20%",
        borderTopLeftRadius: 20,
        borderTopRightRadius: 20,
    },
    panelHeader: {
        alignItems: 'center',
    },
    panelHandle: {
        width: "15%",
        height: 8,
        borderRadius: 4,
        backgroundColor: '#00000040',
        marginBottom: "3%",
    },
    panelTitle: {
        fontSize: 20,
        height: 25,
    },
    panelSubtitle: {
        fontSize: 14,
        color: 'gray',
        height: 20,
        marginBottom: "2%",
    },
    panelButton: {
        padding: "4%",
        borderRadius: 10,
        backgroundColor: '#FF6347',
        alignItems: 'center',
        marginVertical: "2%",
        marginRight: "8%",
        marginLeft: "8%"
    },
    panelButtonTitle: {
        fontSize: 17,
        fontWeight: 'bold',
        color: 'white',
},
});
