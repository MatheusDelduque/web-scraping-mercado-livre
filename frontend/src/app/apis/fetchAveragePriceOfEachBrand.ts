import { api } from "@/config/apiUrls";

export interface IAveragePriceOfEachBrand {
  brand: string;
  price: number;
}

export const fetchAveragePriceOfEachBrand = async (): Promise<IAveragePriceOfEachBrand[]> => {
  const { data } = await api.get<{ [key: string]: number }>("/average_price");

  return Object.entries(data).map(([brand, price]) => ({
    brand,
    price,
  }));
};
