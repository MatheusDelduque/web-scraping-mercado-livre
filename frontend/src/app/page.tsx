import { Box, Heading } from "@chakra-ui/react";
import { TopBrandsChart } from "./components/TopBrandsChart";
import { AppProvider } from "./components/AppProvider";

export default function Home() {
  return (
    <AppProvider>
      <Box p={4} color={"white"} bgGradient="linear(to-b, black, gray.700)" h={"100vh"} boxShadow={"lg"}>
        <Heading size="2xl" p={5} display={"flex"} justifyContent={"center"}>
          Research about sporty shoes - Mercado Livre
        </Heading>
        <TopBrandsChart />
      </Box>
    </AppProvider>
  );
}
