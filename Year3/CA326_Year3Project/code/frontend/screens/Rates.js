import React, {Component } from "react";
import { StyleSheet, Text, View, TouchableOpacity, StatusBar, FlatList, TextInput, ScrollView } from "react-native";
import LinearGradient from "react-native-linear-gradient";

// specifying URL of Flask server
const flaskAPI = "https://currencyapp200.pythonanywhere.com/api/rates?"

export default class Rates extends Component {
    constructor(props) {
        super(props);
        this.state = {
            base: "",
            date: "",
            rates: "",
            ratesError: null,
            result: null,
            status:"Press",
        };

    };

    // checks if the "currency" field is not empty
    ratesValidator() {
        if(this.state.rates == ""){
            this.setState({ratesError: "Field cannot be empty!"})
        }
        else{
            this.setState({ratesError: ""})
        }
    }

    // Setting up jest button testing
    setStatus() {
        this.setState({
            status: "button pressed"
        })
    }

    render() {
        return (
            <View style={styles.container}>
                <StatusBar backgroundColor="#1E90FF" barStyle="light-content"/>

                <Text style= {styles.footerText}>Base Currency (Default is EUR)</Text>
                <View style= {styles.action}>
                    <TextInput
                        testID="baseCurrency"
                        style={{flex:1}}
                        maxLength={3}
                        placeholder="e.g GBP (optional)"
                        onChangeText={(base) => { this.setState({ base }) }}
                    />
                </View>

                <Text style= {styles.footerText}>Date (Default is latest)</Text>
                <View style= {styles.action}>
                    <TextInput
                        testID="date"
                        style={{flex:1}}
                        maxLength={10}
                        keyboardType={"numeric"}
                        placeholder="YYYY-MM-DD (optional)"
                        onChangeText={(date) => { this.setState({ date }) }}
                    />
                </View>

                <Text style= {styles.footerText}>Enter one or more currencies separated by space</Text>
                <View style= {styles.action}>
                    <TextInput
                        testID="currencyList"
                        style={{flex:1}}
                        onBlur={()=>this.ratesValidator()}
                        placeholder="e.g EUR USD"
                        onChangeText={(rates) => { this.setState({ rates }) }}
                    />
                </View>

                <Text style={styles.error}>{this.state.ratesError}</Text>

                <TouchableOpacity
                    style= {styles.convert}
                    disabled={!this.state.rates}
                    onPress={async () => {
                        const ratesEndoint = "base="+this.state.base+"&date="+this.state.date+"&rates="+this.state.rates;
                        const response = await fetch(flaskAPI+ratesEndoint, {
                            method: "GET",
                            mode: "CORS",
                        })
                        .then(res => res.json())
                        .then(data => {
                            this.setState({ result: data.requestedRates })
                        });
                    }}
                >
                    <LinearGradient
                        colors={ ["#09C6F9", "#045DE9"] }
                        style={ styles.button }
                    >
                        <Text style={styles.convertText}>Get Rates</Text>
                    </LinearGradient>
                </TouchableOpacity>

                <View style = {styles.lineStyle} />

                {/* Button Testing */}
                {/*<TouchableOpacity
                    testID="myButton"
                    onPress= {() => this.setStatus()}
                >
                    <Text>Press</Text>
                </TouchableOpacity>

                <Text testID="myText">{this.state.status}</Text>*/}


                {/* basically the flatlist shows result of each currency rate
                unless the input was invalid, it'll display error message */}
                
                <View style={[styles.action, {marginTop: "1%", height: "20%"}] }>
                    <FlatList
                        data={this.state.result}
                        keyExtractor={item => item.key}
                        renderItem={({ item }) => (
                            <View>
                                {item.key != "invalid" ? <Text>{item.key} = {item.rate}</Text> : <Text style={{color: "red"}}>Please enter valid currency code(s) and date(1999 - Current Date).</Text> }
                            </View>
                        )}
                    />
                </View>
            </View>

        )
    }

}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: "center",
        backgroundColor: "#ffffff"
    },
    input: {
        borderWidth: 1,
        padding: 8,
        margin: 10,
        width: 200,
    },
    footerText: {
        fontSize: 18,
        paddingLeft: "3%"
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
        width:"50%"
    },
    convert: {
        width: '40%',
        height: 50,
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: 30,
    },
    button: {
        width: '100%',
        height: 50,
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: 30
    },
    convertText: {
        fontSize: 18,
        textAlign: "center",
        color: "white",
    },
    error: {
        color: "red",
    },
    lineStyle:{
        borderBottomWidth: 10,
        borderRadius: 30,
        width: "100%",
        paddingTop: "3%",
        paddingBottom: "3%",
        borderBottomColor: "#1E90FF",
    },
})
