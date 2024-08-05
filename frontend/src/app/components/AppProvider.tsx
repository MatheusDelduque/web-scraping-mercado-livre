"use client";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ChakraProvider } from "@chakra-ui/react";
import theme from "../theme";

export const AppProvider = ({children}: {children: React.ReactNode}) => {
    const queryClient = new QueryClient();

    return (
      <QueryClientProvider client={queryClient}>
        <ChakraProvider theme={theme}>
            {children}
        </ChakraProvider>
      </QueryClientProvider>
    );
}