import "react-native";
import React from "react";
import AboutUs from "../screens/AboutUs";
import renderer from "react-test-renderer";

test("AboutUs Snapshot", () =>{
    const snap = renderer.create(
        <AboutUs/>
    ).toJSON;

expect(snap).toMatchSnapshot();
})