import "react-native";
import React from "react";
import Information from "../screens/Information";
import renderer from "react-test-renderer";

test("Information Snapshot", () =>{
    const snap = renderer.create(
        <Information/>
    ).toJSON;

expect(snap).toMatchSnapshot();
})