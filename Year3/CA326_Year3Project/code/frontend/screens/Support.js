import React from "react";
import { StyleSheet, Text, View, Button, StatusBar, ScrollView, Image } from "react-native";

const Support = () => {
    return (
        <View style={styles.container}>
            <StatusBar backgroundColor="#1E90FF" barStyle="light-content"/>

            <ScrollView>
                <View style= {styles.header}>
                    <Text style= {styles.headerContent}> Home Screen </Text>
                </View>
                <View style= {styles.body}>
                    <Text style= {styles.bodyContent}>
                        Here in the Home Screen, you are able to check the conversion rates 
                        of a currency of your choice by simply filling in the required fields.
                    </Text>
                    
                    <View style={styles.images}>
                    <Image
                        style= {styles.image}
                        source= {require("../assets/screen_images/HomeImage.png")}
                    />
                    </View>
                </View>

                <View style= {styles.header}>
                    <Text style= {styles.headerContent}> Graph Screen </Text>
                </View>
                <View style= {styles.body}>
                    <Text style= {styles.bodyContent}>
                        Here in the Graph Screen, you are able to view the changing rates of conversion
                        over the past 6 weeks through a graph by supplying the correct currency codes.
                        There will also be a display that shows the lowest and highest values that have occured over the 6 weeks.
                    </Text>
                    
                    <View style={styles.images}>
                        <Image
                            style= {styles.image}
                            source= {require("../assets/screen_images/GraphImage.png")}
                        />
                    </View>
                </View>
                <View style= {styles.header}>
                    <Text style= {styles.headerContent}> Rates Screen </Text>
                </View>
                <View style= {styles.body}>
                    <Text style= {styles.bodyContent}>
                        Here in the Rates Screen, you are able to check the conversion rates
                        with multiple currencies of your choice. You are also able to check what the rates of currencies were in
                        past years dating all the way back since the 1999's. The base currency is EURO and the default
                        date is the latest date. These are optional fields that dont require any input unless you are
                        specifically looking for something. You are able to view multiple currencies by listing the desired
                        currencies in the third input field.
                    </Text>
                    
                    <View style={styles.images}>
                        <Image
                            style= {styles.image}
                            source= {require("../assets/screen_images/RatesImage.png")}
                        />
                    </View>
                </View>
                <View style= {styles.header}>
                    <Text style= {styles.headerContent}> Currencies Screen </Text>
                </View>
                <View style= {styles.body}>
                    <Text style= {styles.bodyContent}>
                        Here in the Currencies Screen, if you didnt know what abbreviations of the currencies were,
                        you are able to check them here. Through the search bar, you are able to look up your desired
                        currency in plain english and it will give you the abbreviation that is associated with the wanted
                        currency.
                    </Text>
                    
                    <View style={styles.images}>
                        <Image
                            style= {styles.image}
                            source= {require("../assets/screen_images/CurrenciesImage.png")}
                        />
                    </View>
                </View>
            </ScrollView>
        
        </View>
        )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "#ffffff"
    },
    header: {
        marginTop: "6%",
        justifyContent: "center",
        alignItems: "center",
    },
    headerContent: {
        fontSize: 24,
        fontWeight: "bold",
        color: "#1E90FF",
    },
    images: {
        marginTop: "4%",
    },
    image: {
        width: 900,
        height: 900,
        resizeMode: "contain",
    },
    body: {
        justifyContent: "center",
        alignItems: "center",
        paddingLeft:"8%",
        paddingRight: "8%",
    },
    bodyContent: {
        fontSize: 16
    }
})

export default Support;