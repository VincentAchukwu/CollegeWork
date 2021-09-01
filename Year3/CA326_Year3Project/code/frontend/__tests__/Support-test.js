import "react-native";
import React from "react";
import Support from "../screens/Support";
import renderer from "react-test-renderer";

test("Support Snapshot", () =>{
    const snap = renderer.create(
        <Support/>
    ).toJSON;

expect(snap).toMatchSnapshot();
})