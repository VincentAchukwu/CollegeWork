import React, {Component, useState} from "react";
import { StyleSheet, FlatList, Text, View, StatusBar, TextInput, TouchableOpacity } from "react-native";
import LinearGradient from "react-native-linear-gradient";

// specifying URL of Flask server
const flaskAPI = "https://currencyapp200.pythonanywhere.com/api/conversions?"

const Home = () => {

    const [fromCurrency, setFromCurrency] = useState("");
    const [fromCurrencyError, setFromCurrencyError] = useState(null);
    const [toCurrency, setToCurrency] = useState("");
    const [toCurrencyError, setToCurrencyError] = useState(null);
    const [amount, setAmount] = useState(0);
    const [amountError, setAmountError] = useState(null);
    const [result, setResult] = useState(null);
    // For testing
    const [status, setStatus] = useState("Press");

    // checks if the "convert from" field is not empty
    const fromCurrencyValidator = () => {
        if(fromCurrency == ""){
            setFromCurrencyError("field cannot be empty!")
        }
        else{
            setFromCurrencyError("")
        }
    }

    // checks if the "convert to" field is not empty
    const toCurrencyValidator = () => {
        if(toCurrency == ""){
            setToCurrencyError("field cannot be empty!")
        }
        else{
            setToCurrencyError("")
        }
    }

    // checks if the "amount" field is not empty
    const amountValidator = () => {
        if(amount == ""){
            setAmountError("field cannot be empty!")
        }
        else{
            setAmountError("")
        }
    }

    return (
        <View style={styles.container}>
            <StatusBar backgroundColor="#1E90FF" barStyle="light-content"/>

            <View style= {[styles.row, {marginTop: "10%"}]}>
                <View style= {[styles.action, {margin: "3%"}]}>
                    <TextInput
                        testID="convertFrom"
                        style= {{flex:1}}
                        maxLength={3}
                        onBlur={()=> fromCurrencyValidator()}
                        placeholder="e.g EUR"
                        onChangeText={(text) => setFromCurrency(text)}
                    />
                </View>
                <Text style= {{fontSize: 18, marginTop: "5%", fontWeight: "bold"}}> To: </Text>
                <View style= {[styles.action, {margin: "3%"}]}>
                    <TextInput
                        testID="convertTo"
                        style= {{flex:1}}
                        maxLength={3}
                        onBlur={()=> toCurrencyValidator()}
                        placeholder="e.g GBP"
                        onChangeText={(text) => setToCurrency(text)}
                    />
                </View>
            </View>

            <View style= {styles.center}>
                <Text style={[styles.emptyError, {marginTop: "2%"}]}>{fromCurrencyError}</Text>
                <Text style={styles.emptyError}>{toCurrencyError}</Text>

                <Text style={ styles.footerText }> Amount: </Text>
                <View style= {styles.action}>
                    <TextInput
                        testID="amount"
                        style= {{flex:1}}
                        onBlur={() => amountValidator()}
                        keyboardType="numeric"
                        placeholder="e.g 25"
                        onChangeText={(text) => setAmount(text)}
                    />
                </View>
                
                <Text style={styles.emptyError}>{amountError}</Text>

                <TouchableOpacity
                    style={styles.convert}
                    disabled={!fromCurrency || !toCurrency || !amount}
                    onPress={async () => {
                        const convertEndoint = "fromCurr="+fromCurrency+"&toCurr="+toCurrency+"&amount="+amount;
                        const response = await fetch(flaskAPI+convertEndoint, {
                            method: "GET",
                            mode: "CORS",
                        })
                        .then(res => res.json())
                        .then(data => {
                            setResult(data.requestedConversion)
                        });
                    }}
                >
                    <LinearGradient
                        colors={ ["#09C6F9", "#045DE9"] }
                        style={ styles.button }
                        >
                        <Text style={styles.convertText}>Convert</Text>
                    </LinearGradient>
                </TouchableOpacity>

                <View style = {styles.lineStyle} />
                
                {/* basically the flatlist shows result of each currency rate
                unless the input was invalid, it'll display error message */}

                {/* Button Testing */}
                {/*<TouchableOpacity
                    testID="myButton"
                    onPress= {() => setStatus("button pressed")}
                >
                    <Text testID="myText">{status}</Text>
                </TouchableOpacity>*/}

                <View style={[styles.action, {marginTop: "8%"}] }>
                    <FlatList
                        data={result}
                        keyExtractor={item => item.key}
                        renderItem={({ item }) => (
                            <View>
                                {item.key != "invalid" ? <Text>{toCurrency.toUpperCase()} = {item.key}</Text> : <Text style={{color: "red"}}>Please enter valid currency codes and amount</Text> }
                            </View>
                        )}
                    />
                </View>
            </View>
        </View>
    )

}


const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "#ffffff"
    },
    footerText: {
        fontSize: 18,
        paddingLeft: "3%"
    },
    row: {
        flexDirection: "row",
        justifyContent: "center",
    },
    input: {
        borderWidth: 1,
        padding: 8,
        margin: 10,
        width: 200,
    },
    emptyError: {
        color: "red",
    },
    action: {
        flexDirection: 'row',
        alignItems: 'center',
        borderWidth: .8,
        height: 50,
        borderRadius: 30,
        paddingLeft: "4%",
        paddingRight: "4%",
        margin: "3%",
        width:"35%"
    },
    button: {
        width: '100%',
        height: 50,
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: 30
    },
    convert: {
        width: '40%',
        height: 50,
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: 30,
        marginTop: "4%"
    },
    convertText: {
        fontSize: 18,
        textAlign: "center",
        color: "white",
    },
    center: {
        justifyContent: "center",
        alignItems: "center",
        marginTop: "-5%"
    },
    lineStyle:{
        borderBottomWidth: 10,
        borderRadius: 30,
        width: "100%",
        paddingTop: "5%",
        paddingBottom: "5%",
        borderBottomColor: "#1E90FF",
    },
})

export default Home;