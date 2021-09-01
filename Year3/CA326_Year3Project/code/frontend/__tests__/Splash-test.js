import "react-native";
import React from "react";
import Splash from "../screens/Splash";
import renderer from "react-test-renderer";
import {create, act} from "react-test-renderer"

const tree = create(<Splash/>);

// ********* Screen Rendering Test *********

test("Splash Snapshot", () =>{
    const snap = renderer.create(
        <Splash/>
    ).toJSON;

expect(snap).toMatchSnapshot();
});

// *****************************************

// ********* Testing Button onPress *********

test("button press", () => {
    // press button
    const button = tree.root.findByProps({ testID: "myButton"}).props;
    act(() => button.onPress());

    // express text to equal "button pressed"
    const text = tree.root.findByProps({ testID: "myText"}).props;
    expect(text.children).toEqual("button pressed")
});

// *******************************************