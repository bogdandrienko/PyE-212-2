import React from "react";
import axios from "axios";
import * as constants from "../components/Constants";
import * as ui from "../components/ui";
import * as utils from "../components/utils";
import * as base from "../components/Base";
import { useNavigate } from "react-router-dom";

export function Categories() {
  const navigate = useNavigate();

  async function getAllCategories() {
    try {

      const token = `${"Bogdan"}:${"bogdan"}`;
      const encodedToken = btoa(token)
      console.log(token)
      console.log(encodedToken)

      const config = {
        method: "GET",
        timeout: 5000,
        timeoutErrorMessage: "timeout error",
        url: `/api/categories?limit=${5}&page=${1}`,
        data: {}
      };
      const headers = {
            Authorization: `Bearer `,
          }
      // const response = await axios(config, headers);
      // const response = await axios.get(`/api/categories?limit=${5}&page=${1}`, headers);
      const response = await axios.get(`/api/categories?limit=${5}&page=${1}`, {
        headers : {
          Authorization: `Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwMTM1MDgwLCJpYXQiOjE2NjAwNDg2ODAsImp0aSI6IjFiZjczMzM0YzRmNjQ0ZmY4MDE1MGZkZjZjMDc1ZWNlIiwidXNlcl9pZCI6MX0.g4nUUGPrRgBpiTp0doJ4JHavLTIjSRg1mpzWgSV6gMs`,
        }
      })

      // const config = {
      //   url: `/api/categories?limit=${5}&page=${1}`,
      //   method: "GET",
      //   timeout: 5000,
      //   timeoutErrorMessage: "timeout error",
      //   // headers: {
      //   //   Authorization: `Basic ${"Bogdan bogdan"}`,
      //   // },
      //   data: {},
      // };
      // const response = await axios(config);
      if (response.data) {
        console.log(response.data);
      } else {
        console.log(response);
        console.log("ошибка");
      }
    } catch (error) {
      //navigate("/login");
      console.log(typeof error);
      console.log(`ошибка: ${error}`);
    }
  }

  
  async function get_token() {
    let username = "admin"
    let password = "admin"
    const response = await axios.post(`/api/token/`, {username, password})

    localStorage.setItem("token", response.data.access)

    console.log(response.data);
  }

  async function get_data() {
    let username = "admin"
    let password = "admin1"
    let token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwMTQ3MDQzLCJpYXQiOjE2NjAwNjA2NDMsImp0aSI6Ijg0MTUwZWE5NWJlZTQ4NmFhZTNkMWE0NTA5MWExZjIwIiwidXNlcl9pZCI6MX0.vOJWIIlpZtlJ7mUBFqs5Lxa6oyNM9rZ2oWy39H3enr8";
    const response = await axios.post(`/api/get_data/`, {}, {
      headers : {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      }
      // headers : {
      //   Authorization: `Basic ${username} ${password}`,
      // }
    })
    console.log(response.data);
  }

  return (
    <base.Base1>
      <div>
        Categories
        <button onClick={getAllCategories}></button>

        <div className="m-5 p-5">
          <button onClick={get_data} className="btn btn-lg btn-outline-danger">get_data</button>
          <button onClick={get_token} className="btn btn-lg btn-outline-success">get_token</button>
        </div>
      </div>
    </base.Base1>
  );
}
