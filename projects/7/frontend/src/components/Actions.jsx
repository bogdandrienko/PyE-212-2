import { useNavigate } from "react-router-dom";

export function Logout() {
  //
  localStorage.removeItem("token");
  //
}
