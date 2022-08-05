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
            Authorization: `Basic admin admin`,
          }
      // const response = await axios(config, headers);
      // const response = await axios.get(`/api/categories?limit=${5}&page=${1}`, headers);
      const response = await axios.get(`/api/categories?limit=${5}&page=${1}`, {
        headers : {
          Authorization: `Basic admin admin`,
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

  return (
    <base.Base1>
      <main>
        <div>
          Categories
          <button onClick={getAllCategories}></button>
        </div>
      </main>
    </base.Base1>
  );
}
