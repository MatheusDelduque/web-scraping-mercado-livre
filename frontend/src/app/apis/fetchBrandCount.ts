import { api } from "@/config/apiUrls";

export interface IBrandCount {
  brand: string;
  count: number;
}

export const fetchBrandCount = async (): Promise<IBrandCount[]> => {
  const { data } = await api.get<{ [key: string]: number }>("/brand_count");

  return Object.entries(data).map(([brand, count]) => ({
    brand,
    count,
  }));
};
