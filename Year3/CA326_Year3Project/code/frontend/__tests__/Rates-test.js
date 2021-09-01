import "react-native";
import React from "react";
import Rates from "../screens/Rates";
import renderer from "react-test-renderer";
import {create, act} from "react-test-renderer"

const tree = create(<Rates/>);

// ********* Screen Rendering Test *********

test("Rates Snapshot", () =>{
    const snap = renderer.create(
        <Rates/>
    ).toJSON;

expect(snap).toMatchSnapshot();
});

// *****************************************

// ********* Button Testing *********

test("button press", () => {
    // press button
    const button = tree.root.findByProps({ testID: "myButton"}).props;
    act(() => button.onPress());

    // express text to equal "button pressed"
    const text = tree.root.findByProps({ testID: "myText"}).props;
    expect(text.children).toEqual("button pressed")
});

// ***********************************

// ********* Function to Find Elements in a Tree (Tree being <View/> component and everything wrapped in it) *********

const findElement = function(tree2, element) {
    let result = undefined
    for(node in tree2.children){
        if(tree2.children[node].props.testID = element) {
            result = true;
        }
    }
    return result
};

// *******************************************************************************************************************

// ********* TextInput Tests *********

it("Has Element baseCurrency", () => {
    const tree2 = renderer.create(<Rates/>).toJSON();
    expect(findElement(tree2, "baseCurrency")).toBeDefined();
});

it("Has Element date", () => {
    const tree2 = renderer.create(<Rates/>).toJSON();
    expect(findElement(tree2, "date")).toBeDefined();
});

it("Has Element currencyList", () => {
    const tree2 = renderer.create(<Rates/>).toJSON();
    expect(findElement(tree2, "currencyList")).toBeDefined();
});

// ************************************