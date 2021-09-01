import "react-native";
import React from "react";
import Home from "../screens/Home";
import renderer from "react-test-renderer";
import {create, act} from "react-test-renderer"

const tree = create(<Home/>);

// ********* Screen Rendering Test *********

test("Home Snapshot", () =>{
    const snap = renderer.create(
        <Home/>
    ).toJSON;

expect(snap).toMatchSnapshot();
})

// *****************************************

// ********* Button Testing *********

test("button press", () => {
    // press button
    const button = tree.root.findByProps({ testID: "myButton"}).props;
    act(() => button.onPress());

    // express text to equal "button pressed"
    const text = tree.root.findByProps({ testID: "myText"}).props;
    expect(text.children).toEqual("button pressed")
})

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

it("Has Element convertFrom", () => {
    const tree2 = renderer.create(<Home/>).toJSON();
    expect(findElement(tree2, "convertFrom")).toBeDefined();
});

it("Has Element convertTo", () => {
    const tree2 = renderer.create(<Home/>).toJSON();
    expect(findElement(tree2, "convertTo")).toBeDefined();
});

it("Has Element amount", () => {
    const tree2 = renderer.create(<Home/>).toJSON();
    expect(findElement(tree2, "amount")).toBeDefined();
});

// ***********************************