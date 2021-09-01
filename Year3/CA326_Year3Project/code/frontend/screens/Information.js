import React from "react";
import { StyleSheet, Text, View, StatusBar, ScrollView, Image } from "react-native";
import Hyperlink from "react-native-hyperlink";

const Information = () => {
    return (
        <View style={styles.container}>
            <StatusBar backgroundColor="#1E90FF" barStyle="light-content"/>

            <ScrollView>
                <View style= {styles.header}>
                    <Text style= {styles.headerContent}> Introduction </Text>
                </View>
                <View style= {styles.body}>
                    <Text style= {styles.bodyContent}>
                        You might be wondering where our source of data is from and can
                        it be trusted ? We get our data from a reliable source called fixer.io
                    </Text>
                </View>

                <View style= {styles.header}>
                    <Text style= {styles.headerContent}> About Fixer </Text>
                </View>
                <View style= {styles.body}>
                    <Text style= {styles.bodyContent}>
                        Fixer is a JSON API that gives information on Foreign Exchange Rates
                        and Currency Conversion. It is updated every 10 minutes and is a trusted source
                        worldwide.
                    </Text>

                    <Image
                        style= {styles.image}
                        source= {require("../assets/images/Fixer.png")}
                    />

                    <Text style= {styles.bodyContent}>
                        To Find Out More About Fixer:
                    </Text>
                    <Hyperlink linkDefault={ true }>
                        <Text style= {{color: "blue", marginTop: "1%"}}> https://fixer.io/ </Text>
                    </Hyperlink>
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
        marginTop: "1%",
    },
    image: {
        width: 450,
        height: 350,
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

export default Information;