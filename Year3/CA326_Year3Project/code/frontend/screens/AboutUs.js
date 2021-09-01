import React from "react";
import { StyleSheet, Text, View, StatusBar, ScrollView} from "react-native";
import Hyperlink from 'react-native-hyperlink';

const AboutUs = () => {
    return (
        <View style={styles.container}>
            <StatusBar backgroundColor="#1E90FF" barStyle="light-content"/>

            <ScrollView>
                <View style= {styles.header}>
                    <Text style= {styles.headerContent}> Who We Are ? </Text>
                </View>
                <View style= {styles.body}>
                    <Text style= {styles.bodyContent}>
                        Hello, Our names are Tinh Lien and Vincent Achukwu and we're currently
                        in our 3rd year of Computer Science in Dublin City University. This Currency
                        Conversion App is made as our 3rd year project. The goal of this application
                        is to give you the updated rates on currencies, along with the ability to view the
                        previous rates of currencies.
                    </Text>
                </View>

                <View style= {styles.header}>
                    <Text style= {styles.headerContent}> Links to Our Socials </Text>
                </View>
                <View style= {[styles.body, {marginTop: "3%"}]}>
                    <Text style= {[styles.bodyContent, {fontWeight: "bold"}]}>
                        Tinh Lien:
                    </Text>
                    <Hyperlink linkDefault={ true }>
                        <Text style= {{color: "blue", marginTop: "1%"}}> https://github.com/TinhLien </Text>
                        <Text style= {{color: "blue"}}> https://www.linkedin.com/in/tinh-lien-2bb7581b6/ </Text>
                    </Hyperlink>
                </View>
                <View style= {[styles.body, {marginTop: "4%"}]}>
                    <Text style= {[styles.bodyContent, {fontWeight: "bold"}]}>
                        Vincent Achukwu:
                    </Text>
                    <Hyperlink linkDefault={ true }>
                        <Text style= {{color: "blue", marginTop: "1%"}}> https://github.com/VincentAchukwu </Text>
                        <Text style= {{color: "blue"}}> https://www.linkedin.com/in/vincent-achukwu/ </Text>
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
        marginTop: "4%"
    },  
    body: {
        justifyContent: "center",
        alignItems: "center",
        paddingLeft:"8%",
        paddingRight: "8%"
    },
    bodyContent: {
        fontSize: 16,
    }
})

export default AboutUs;