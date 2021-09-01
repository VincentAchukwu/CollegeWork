import React, { Component, useState } from 'react';
import { View, Text, StyleSheet ,Image, TouchableOpacity } from 'react-native';
import { Caption } from "react-native-paper"

const FavouritesList = (props) => {

    return (
        <View style={ styles.container }>
            <View style={ {flex:1} }>
            
                <View style= {styles.flagInfo}>
                    <View style= {styles.imageContent}>
                        <Image
                            source={ props.detail.flag }
                            size={80}
                        />

                        <View style= {styles.currencyContent}>
                            <Text> {props.detail.abbreviation} </Text>
                            <Caption style={ styles.caption }> {props.detail.name} </Caption>
                        </View>
                        
                    </View>
                </View>
            
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
    },
    flagInfo: {
        paddingLeft: 20,
        borderWidth: 5,
        backgroundColor: "#ffffff"
    },
    imageContent: {
        flexDirection: "row",
        marginTop: "3%",
    },
    currencyContent: {
        marginLeft: "3%",
        flexDirection: "column"
    },
    caption: {
        fontSize: 16,
        paddingTop: "1%",
        lineHeight: 14,
    },
    likeButton: {
        flexDirection: "row",
        justifyContent: "flex-end",
        marginLeft: "auto"
    }
});

export default FavouritesList;