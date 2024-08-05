"use server";
import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000", // URL do backend
});

export const TopBrandsChart = async () => {
  const response = await api.get("/produtos");
  console.log("response", response.data);
  return (
    <>
      {response.data.map((product: any) => (
        <p>{product.new_price}</p>
      ))}
    </>
  );
};
