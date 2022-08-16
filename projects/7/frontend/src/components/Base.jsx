import React from "react";
import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Footer2 } from "./footers";
import { Navbar1, Navbar2, Navbar4 } from "./navbars";
import { useNavigate } from "react-router-dom";
import * as utils from "../components/utils";

export default function Base({ children }) {
  return (
    <div className="p-0">
      <LoginComponent/>
      <main className="custom_main_1">
        <Navbar1 />
        <div className="p-0">{children}</div>
      </main>
      <Navbar1 />
    </div>
  );
}



export const CONST_USER_LOGIN = utils.ConstructorConstantRedux("CONST_USER_LOGIN");
export const getUserToken = utils.ConstructorReducerRedux(CONST_USER_LOGIN);

export function LoginComponent() {
  const navigate = useNavigate();
  const token = useSelector((state) => state.token);

  useEffect(() => {
    console.log("token", token)
  }, [token]);

  useEffect(() => {
    if (!localStorage.getItem('token')){
      navigate("/login");
    } else {
        if(navigate.path === "/login"){
          navigate("/");
        }
    }
  }, []);


  return (
    <div></div>
  );
}

export function Base1({ children }) {
  return (
    <div className="custom_body">
      <LoginComponent/>
      <main className="custom_main">
        <Navbar4 />
        {children}
      </main>
      <Footer2 />
    </div>
  );
}
