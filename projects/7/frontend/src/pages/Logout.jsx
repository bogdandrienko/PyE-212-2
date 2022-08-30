import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import Base, {Base1} from "../components/Base";
import axios from "axios";
import {useNavigate} from "react-router-dom";
import * as bases from '../components/Base'
import * as constants from "../components/Constants";
import * as actions from "../components/actions";



export function Logout() {
  const navigate = useNavigate();
  const dispatch = useDispatch();

  useEffect(() => {
    actions.Logout()
    dispatch({ type: constants.C_Token.reset });
    navigate("/login")
  }, []);

  return (
    <div></div>
  );
}
