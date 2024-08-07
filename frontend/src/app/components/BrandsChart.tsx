"use client";

import { Flex } from "@chakra-ui/react";
import { useQuery, QueryFunction } from "@tanstack/react-query";
import { Bar, BarChart, ResponsiveContainer, Tooltip, XAxis, YAxis, Text } from "recharts";
import { IBrandCount } from "../apis/fetchBrandCount";
import { IAveragePriceOfEachBrand } from "../apis/fetchAveragePriceOfEachBrand";
import { IBrandAverageRatingNumberReviews } from "../apis/fetchBrandAverageRatingNumberReviews";

interface BrandsChartProps<T> {
  queryKey: string;
  queryFn: QueryFunction<T[]>;
  dataKeyX: string;
  dataKeyY: string;
}

export const BrandsChart = <T extends IBrandCount | IAveragePriceOfEachBrand | IBrandAverageRatingNumberReviews>({ queryKey, queryFn, dataKeyX, dataKeyY }: BrandsChartProps<T>) => {
  const { data, error, isLoading } = useQuery<T[], Error>({
    queryKey: [queryKey],
    queryFn: queryFn,
  });

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>An error occurred: {error.message}</div>;

  const CustomTooltip = ({ active, payload }: any) => {
    if (active && payload && payload.length) {
      return (
        <div className="custom-tooltip">
          <p>{`${dataKeyX.toUpperCase()}: ${payload[0].payload.brand}`}</p>
          <p>{`${dataKeyY === "averageRating" ? "Average Rating: " : dataKeyY.toUpperCase()}: ${dataKeyY === "price" ? "$" : ""} ${payload[0].value.toFixed(2)}`}</p>
        </div>
      );
    }

    return null;
  };

  return (
    <Flex alignItems="center">
      <ResponsiveContainer width="100%" height={400}>
        <BarChart
          width={500}
          height={300}
          data={data}
          margin={{
            top: 40,
            right: 30,
            left: 20,
            bottom: 5,
          }}>
          <Text x={250} y={10} textAnchor="middle" dominantBaseline="hanging" fill="#ffffff">
            Top Brands Chart
          </Text>
          <XAxis dataKey={dataKeyX} fontSize={10} />
          <YAxis />
          <Tooltip content={<CustomTooltip />} />
          <Bar dataKey={dataKeyY} fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </Flex>
  );
};
