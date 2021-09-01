import React, {Component, useState} from "react";
import { StyleSheet, ScrollView, Text, View, StatusBar, TextInput, TouchableOpacity, Dimensions, Alert } from "react-native";
import LinearGradient from "react-native-linear-gradient";
import { LineChart } from "react-native-chart-kit";

// specifying URL of Flask server
const flaskAPI = "https://currencyapp200.pythonanywhere.com/api/timeSeries?"

const Graph = (props) => {

    const [fromCurrency, setFromCurrency] = useState("");
    const [fromCurrencyError, setFromCurrencyError] = useState(null);
    const [toCurrency, setToCurrency] = useState("");
    const [toCurrencyError, setToCurrencyError] = useState(null);
    const [result, setResult] = useState([
        {
            "key":"2000-01-01",
            "code":"EUR",
            "rate":1
        },
        {
            "key":"2000-01-02",
            "code":"EUR",
            "rate":1
        },
        {
            "key":"2000-01-03",
            "code":"EUR",
            "rate":1
        },
        {
            "key":"2000-01-04",
            "code":"EUR",
            "rate":1
        },
        {
            "key":"2000-01-05",
            "code":"EUR",
            "rate":1
        },
        {
            "key":"2000-01-06",
            "code":"EUR",
            "rate":1
        }
    ]);
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

    const maximumFromData = Math.max(...result.map((e) => e.rate))
    const minimumFromData = Math.min(...result.map((e) => e.rate))

    const displayGraph = () => {
        if(fromCurrency != "field cannot be empty!" && toCurrency != "field cannot be empty!" && result[0].key != "invalid" && fromCurrency != toCurrency && result[0].rate != 1){
                if(result[0].rate > 1) {
                    return (
                        <View style={styles.container}>
                            <View style={[styles.row, {marginTop: "5%"}]}>
                                <Text style= {[styles.text, {marginRight: "40%"}]}>Lowest</Text>
                                <Text style= {styles.text}>Highest</Text>
                            </View>
                            <View style={styles.row}>
                                <Text style= {{marginRight: "40%"}}> {result[0].code} = {minimumFromData}</Text>
                                <Text>{result[0].code} = {maximumFromData}</Text>
                            </View>
                            <View style={styles.chart}>
                                <LineChart
                                    data={data}
                                    width={Dimensions.get("window").width}
                                    height={500}
                                    verticalLabelRotation={30}
                                    chartConfig={chartConfig}
                                    bezier
                                />
                            </View>
                        </View>
                    )
                } else {
                    return(<Text style={styles.errorMsg}> Please Swap Order of Currency Codes </Text>)
                }
        } else {
            return(<Text style={styles.errorMsg}> Please Enter Correct and Differing Currency Codes </Text>)
        }
    }
    
    const chartConfig = {
        backgroundColor: '#000000',
        backgroundGradientFrom: '#ffffff',
        backgroundGradientTo: '#FFF',
        decimalPlaces: 2, // optional, defaults to 2dp
        color: (opacity = 1) => `rgba(0, 206, 209, ${opacity})`,
        labelColor: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
        style: { borderRadius: 16, },
        propsForDots: { r: '6', strokeWidth: '2', stroke: '#000000', }, }

    const data = {
        labels: ["6w", "5w", "4w", "3w", "2w", "1w"],
        datasets: [
          {
            data: result.map(item => {
                return(item.rate)
            }),
            color: (opacity = 1) => `rgba(0, 0, 255, ${opacity})`, // optional
            strokeWidth: 2 // optional
          }
        ],
    };

    return (
        <View style={styles.container}>
            <ScrollView>
                <StatusBar backgroundColor="#1E90FF" barStyle="light-content"/>
                
                <View style= {[styles.row, {marginTop: "5%"}]}>
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

                    <TouchableOpacity
                        style={styles.convert}
                        disabled={!fromCurrency || !toCurrency || fromCurrency == toCurrency}
                        onPress={
                            async () => {
                            const convertEndoint = "fromCurr="+fromCurrency+"&toCurr="+toCurrency;
                            const response = await fetch(flaskAPI+convertEndoint, {
                                method: "GET",
                                mode: "CORS",
                            })
                            .then(res => res.json())
                            .then(data => {
                                setResult(data.requestedTimeSeries)
                            });
                        }}
                    >
                        <LinearGradient
                            colors={ ["#09C6F9", "#045DE9"] }
                            style={ styles.button }
                            >
                            <Text style={styles.convertText}>Show Graph</Text>
                        </LinearGradient>
                    </TouchableOpacity>
                    
                    {/* Button Testing */}
                    {/*<TouchableOpacity
                        testID="myButton"
                        onPress= {() => setStatus("button pressed")}
                    >
                        <Text testID="myText">{status}</Text>
                    </TouchableOpacity>*/}

                    {/* the key in this instance is the date */}
                    {displayGraph()}
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
    textRow: {
        flexDirection: "row",
        justifyContent: "center"
    },
    footerText: {
        fontSize: 18,
        paddingLeft: "3%"
    },
    row: {
        flexDirection: "row",
        justifyContent: "center",
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
    },
    convertText: {
        fontSize: 18,
        textAlign: "center",
        color: "white",
    },
    lineStyle:{
        borderBottomWidth: 10,
        borderRadius: 30,
        width: "100%",
        paddingTop: "5%",
        paddingBottom: "5%",
        borderBottomColor: "#1E90FF",
    },
    center: {
        justifyContent: "center",
        alignItems: "center",
        marginTop: "-5%"
    },
    text: {
        fontSize: 20,
        fontWeight: "bold",
        color: "#1E90FF"
    },
    chart: {
        marginTop: "3%"
    },
    errorMsg: {
        color: "red",
        marginTop: "5%"
    }
})

export default Graph;