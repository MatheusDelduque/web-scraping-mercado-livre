import { api } from "@/config/apiUrls";

export interface IBrandAverageRatingNumberReviews {
  brand: string;
  averageRating: number;
}

export const fetchBrandAverageRatingNumberReviews = async (): Promise<IBrandAverageRatingNumberReviews[]> => {
  const { data } = await api.get<{ [key: string]: number }>("/brand_average_rating_number_reviews");

  return Object.entries(data).map(([brand, reviews_rating_number]) => ({
    brand,
    averageRating: reviews_rating_number,
  }));
};
