import React, {useState} from "react";
import { StyleSheet, Text, View, Button, StatusBar, ScrollView, TextInput } from "react-native";
import Icon from 'react-native-vector-icons/Ionicons';
import datas from "../components/CurrencyData"
import CurrenciesList from "../components/CurrenciesList";

const Currencies = () => {

    const state = {
        datas: datas,
        temp: datas
    }

    const [currencyFilter, setSearch] = useState(state.temp)

    const getFlags = () => {
        return currencyFilter.map(data => {
            return <CurrenciesList detail={data} key={data.id}/>
        })
    }

    const searchCurrencies = (searchFor) => {
        setSearch( state.datas.filter(i =>i.name.toLowerCase().includes(searchFor.toLowerCase())));
    }
    
    return (
        <View style={styles.container}>
            <StatusBar backgroundColor="#1E90FF" barStyle="light-content"/>
            <View style= {styles.action}>
                <Icon name="search" size={25}/>

                <TextInput
                    style= {{flex: 1}}
                    placeholder= "Search..."
                    underlineColorAndroid="transparent"
                    onChangeText= {text => {searchCurrencies(text)}}
                />
            </View>

            <ScrollView>
                {getFlags()}
            </ScrollView>
        </View>
        )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#ffffff"
    },
    action: {
        flexDirection: 'row',
        justifyContent: 'center',
        alignItems: 'center',
        borderWidth: 2,
        height: 50,
        borderRadius: 30,
        paddingLeft: "4%",
        paddingRight: "4%",
        margin: "3%"
      },
})

export default Currencies;