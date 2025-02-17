"use client";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ChakraProvider } from "@chakra-ui/react";
import theme from "../theme";
import { useState } from "react";

export const AppProvider = ({children}: {children: React.ReactNode}) => {
  const [queryClient] = useState(() => new QueryClient());

    return (
      <QueryClientProvider client={queryClient}>
        <ChakraProvider theme={theme}>
            {children}
        </ChakraProvider>
      </QueryClientProvider>
    );
}