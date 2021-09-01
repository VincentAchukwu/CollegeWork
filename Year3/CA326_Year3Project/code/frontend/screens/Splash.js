import React, { useState } from 'react';
import { 
    View, 
    Text, 
    TouchableOpacity, 
    Dimensions,
    StyleSheet,
    StatusBar,
    Image
} from 'react-native';
import * as Animatable from 'react-native-animatable';
import LinearGradient from 'react-native-linear-gradient';
import MaterialIcons from 'react-native-vector-icons/MaterialIcons';
import { useTheme } from '@react-navigation/native';

const Splash = ({navigation}) => {
    const { colors } = useTheme();
    // For testing
    const [status, setStatus] = useState("Press");

    return (
      <View style={styles.container}>
          <StatusBar backgroundColor='#1E90FF' barStyle="light-content"/>
        <View style={styles.header}>
            <Animatable.Image 
                animation="bounceIn"
                duraton="1500"
            source={require('../assets/images/CurrencyConverter.png')}
            style={styles.logo}
            resizeMode="stretch"
            />
        </View>
        <Animatable.View 
            style={[styles.footer, {
                backgroundColor: "#1E90FF"
            }]}
            animation="fadeInUpBig"
        >
            <Text style={[styles.title, {
                color: colors.text
            }]}>Welcome!</Text>
            <Text style={styles.text}>View The Latest Currencies Exchange Rates</Text>
            <View style={styles.button}>
            <TouchableOpacity onPress={()=>navigation.navigate("HomeDrawer")}>
                <LinearGradient
                    colors={["#09C6F9", "#045DE9"]}
                    style={styles.signIn}
                >
                    <Text style={styles.textSign}>Get Started</Text>
                    <MaterialIcons 
                        name="navigate-next"
                        color="#fff"
                        size={20}
                    />
                </LinearGradient>
            </TouchableOpacity>
            {/* Button Testing */}
            {/*<TouchableOpacity
                testID="myButton"
                onPress={() => setStatus("button pressed")}
            >
                <Text testID="myText">{status}</Text>
            </TouchableOpacity>*/}
            </View>
        </Animatable.View>
      </View>
    );
};

export default Splash;

const {height} = Dimensions.get("screen");
const height_logo = height * 0.28;

const styles = StyleSheet.create({
  container: {
    flex: 1, 
    backgroundColor: '#ffffff'
  },
  header: {
      flex: 2,
      justifyContent: 'center',
      alignItems: 'center'
  },
  footer: {
      flex: 3,
      backgroundColor: '#1E90FF',
      borderTopLeftRadius: 30,
      borderTopRightRadius: 30,
      paddingVertical: 50,
      paddingHorizontal: 30
  },
  logo: {
      width: height_logo,
      height: height_logo
  },
  title: {
      color: '#05375a',
      fontSize: 40,
      fontWeight: 'bold'
  },
  text: {
      color: 'white',
      fontSize: 20,
      marginTop:5
  },
  button: {
      alignItems: 'flex-end',
      marginTop: 30
  },
  signIn: {
      width: 150,
      height: 40,
      justifyContent: 'center',
      alignItems: 'center',
      borderRadius: 50,
      flexDirection: 'row'
  },
  textSign: {
      color: 'white',
      fontWeight: 'bold'
  }
});