import React from "react";
import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Footer2 } from "./footers";
import { Navbar1, Navbar2, Navbar4 } from "./navbars";
import { Link, useLocation, useNavigate } from "react-router-dom";
import * as utils from "../components/utils";
import * as actions from "../components/actions";

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



export const CONST_USER_LOGIN = utils.ConstructorCR("CONST_USER_LOGIN");
export const getUserToken = utils.ConstructorRR(CONST_USER_LOGIN);

export function LoginComponent() {
  const navigate = useNavigate();
  const location = useLocation();
  const token = useSelector((state) => state.token);

  useEffect(() => {
    if (!token.data){
      actions.Logout();
      utils.Sleep(()=> navigate("/login"), 10);
    } else {
      if(location.pathname === "/login"){
        utils.Sleep(()=> navigate("/"), 10);
      }
    }
  }, [token.data]);

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
