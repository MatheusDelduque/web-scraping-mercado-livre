"use client";

import { Box, Flex, Grid, Heading } from "@chakra-ui/react";
import { BrandsChart } from "./components/BrandsChart";
import { AppProvider } from "./components/AppProvider";
import { fetchBrandCount, IBrandCount } from "./apis/fetchBrandCount";
import { fetchAveragePriceOfEachBrand, IAveragePriceOfEachBrand } from "./apis/fetchAveragePriceOfEachBrand";
import { fetchBrandAverageRatingNumberReviews, IBrandAverageRatingNumberReviews } from "./apis/fetchBrandAverageRatingNumberReviews";

export default function Home() {
  return (
    <AppProvider>
      <Flex p={4} color={"white"} bgGradient="linear(to-b, black, gray.700)" minH={"100vh"} flexDirection="column">
        <Heading size="2xl" mt={14} textAlign="center">
          Research about sporty shoes - Mercado Livre
        </Heading>
        <Grid p={5} templateColumns="repeat(3, 1fr)" gap={6} flexGrow={1}>
          <BrandsChart<IBrandCount> queryKey="brandCount" queryFn={fetchBrandCount} dataKeyX="brand" dataKeyY="count" />
          <BrandsChart<IAveragePriceOfEachBrand> queryKey="averagePrice" queryFn={fetchAveragePriceOfEachBrand} dataKeyX="brand" dataKeyY="price" />
          <BrandsChart<IBrandAverageRatingNumberReviews> queryKey="brandAverageRatingNumberReviews" queryFn={fetchBrandAverageRatingNumberReviews} dataKeyX="brand" dataKeyY="averageRating" />
        </Grid>
      </Flex>
    </AppProvider>
  );
}
